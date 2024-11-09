import os
import sys
import glob
import yaml
import time
import uproot
import numpy as np
import awkward as ak
from time import sleep
from tqdm import tqdm
from typing import Optional
from IPython import embed
from joblib import Parallel, delayed
from subprocess import Popen, PIPE

import logging

def setup_logger(log_file):
    # Create a logger
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the file handler
    formatter = logging.Formatter('%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s','%Y-%m-%d:%H:%M:%S')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = logging.getLogger('main')

def load_config(yaml_path):
    config = None
    with open(yaml_path, 'r') as handle:
        config = yaml.safe_load(handle)
    return config


# Real time logging for shell command
def runShellCmd(cmdList):
    process = Popen(cmdList, stdout=PIPE, stderr=PIPE)
    while True:
        output = process.stdout.readline()
        if process.poll() is not None:
            break
        if output:
            logger.info(output.strip().decode("utf-8"))
    rc = process.poll()


def get_nfiles_nevents_per_file(rootfile : str, isData: bool) -> float:
    nEv_sel_tree = 0.0
    nEv_nsel_tree = 0.0
    sumGenWt_sel_tree  = 0.0
    sumGenWt_nsel_tree = 0.0

    logger.info(f"\n\nfile : {rootfile}")
    upfile = uproot.open(rootfile)

    sel_events_array = upfile["Events"]
    sel_event_column = sel_events_array.arrays(["event"])
    sel_nevents      = len(sel_event_column)
    if isData:
        sumGenWt_sel_tree = sel_nevents
        nEv_sel_tree      = sumGenWt_sel_tree
    else:
        sel_genwt_column = sel_events_array.arrays(["genWeight"])     
        genWt_sel_tree   = sel_genwt_column["genWeight"]
        genWt_sel_tree   = ak.where(genWt_sel_tree > 0.,
                                    1.,
                                    ak.where(genWt_sel_tree < 0.,
                                             -1.,
                                             genWt_sel_tree))
        sumGenWt_sel_tree = ak.sum(genWt_sel_tree)
        nEv_sel_tree = sel_nevents

    logger.info(f"sumGenWt_sel_tree : {sumGenWt_sel_tree}")
    logger.info(f"nEvents_sel_tree  : {nEv_sel_tree}")
    
    nsel_events = None

    _keys = list(upfile.keys())
    _keys = [s.split(';')[0] for s in _keys]
    logger.info(f"keys : {_keys}")

    if "EventsNotSelected" in _keys:
        nsel_events_array = upfile["EventsNotSelected"]
        
        if isData:
            nsel_run_column = nsel_events_array.arrays(["run"])
            sumGenWt_nsel_tree = len(nsel_run_column)
            nEv_nsel_tree = sumGenWt_nsel_tree
        else:
            nsel_genwt_column = nsel_events_array.arrays(["genWeight"])
            genWt_nsel_tree = nsel_genwt_column["genWeight"]
            genWt_nsel_tree = ak.where(genWt_nsel_tree > 0.,
                                       1.,
                                       ak.where(genWt_nsel_tree < 0.,
                                                -1.,
                                                genWt_nsel_tree))
            sumGenWt_nsel_tree = ak.sum(genWt_nsel_tree)
            nEv_nsel_tree = len(genWt_nsel_tree)


    logger.info(f"sumGenWt_nsel_tree : {sumGenWt_nsel_tree}")
    logger.info(f"nEvents_nsel_tree  : {nEv_nsel_tree}")
    
    sumWt   = sumGenWt_sel_tree + sumGenWt_nsel_tree
    logger.info(f"sumWt : {sumWt}")
    nEvts   = nEv_sel_tree + nEv_nsel_tree
    logger.info(f"nEvts : {nEvts}")
    
    time.sleep(0.01)

    return [sumWt, nEvts]


def get_nfiles_nevents(rootfiledirs, isData: bool, cores: Optional[int] = 1) -> tuple[int, float]:
    nTotalFiles = 0
    sumGenWeights = 0.0
    root_files = []
    start = time.time()
    for filedir in rootfiledirs:
        logger.info(f"files dir: {filedir}")
        _root_files = glob.glob(f"{filedir}/*.root")
        root_files = root_files + _root_files

    #sumWt_list = Parallel(n_jobs=cores)(delayed(get_nfiles_nevents_per_file)(root_files[i], isData) for i in tqdm(range(len(root_files))))
    sumWt_nEvt_list = Parallel(n_jobs=cores)(delayed(get_nfiles_nevents_per_file)(root_files[i], isData) for i in tqdm(range(len(root_files))))
    """
    for i in tqdm(range(len(root_files))):
        #for i, file in enumerate(root_files):
        file = root_files[i]
        nTotalFiles += 1
        wt = get_nfiles_nevents_per_file(file, isData)
        sumGenWeights += wt
        sleep(0.01)
    """
    #sumWt_array = ak.Array(sumWt_list)
    sumWt_nEvt_array = ak.to_regular(ak.Array(sumWt_nEvt_list))
    sumWt_array = sumWt_nEvt_array[:,0]
    nevts_array = sumWt_nEvt_array[:,1]
    nTotalFiles = len(sumWt_array)
    sumGenWeights = ak.sum(sumWt_array)
    sumEvts = ak.sum(nevts_array)
    end = time.time()

    logger.info(f"\n\nCombining ...")
    logger.info(f"nfiles: {nTotalFiles}")
    logger.info(f"sumGenWeights : {sumGenWeights}")
    logger.info(f"nEvents       : {sumEvts}")
    logger.info(f"getting sumWt in {round((end-start)/60, 3)} mins")

    return nTotalFiles, sumGenWeights, sumEvts
