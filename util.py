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
    sumGenWt_sel_tree  = 0.0
    sumGenWt_nsel_tree = 0.0

    upfile = uproot.open(rootfile)

    sel_events = upfile["Events"]
    if isData:
        sel_events = sel_events.arrays(["event"]) 
        sumGenWt_sel_tree = len(sel_events)
    else:
        sel_events = sel_events.arrays(["genWeight"])     
        genWt_sel_tree = sel_events["genWeight"]
        genWt_sel_tree = ak.where(genWt_sel_tree > 0., 1., ak.where(genWt_sel_tree < 0., -1., genWt_sel_tree))
        sumGenWt_sel_tree = ak.sum(genWt_sel_tree)

    nsel_events = None

    if "EventsNotSelected" in list(upfile.keys()):
        nsel_events = upfile["EventsNotSelected"]
        if isData and "":
            nsel_events = nsel_events.arrays()
            sumGenWt_nsel_tree = len(nsel_events)
        else:
            nsel_events = nsel_events.arrays(["genWeight"])
            genWt_nsel_tree = nsel_events["genWeight"]
            genWt_nsel_tree = ak.where(genWt_nsel_tree > 0., 1., ak.where(genWt_nsel_tree < 0., -1., genWt_nsel_tree))
            sumGenWt_nsel_tree = ak.sum(genWt_nsel_tree)
        
    sumWt   = sumGenWt_sel_tree + sumGenWt_nsel_tree

    time.sleep(0.01)

    return sumWt


def get_nfiles_nevents(rootfiledirs, isData: bool) -> tuple[int, float]:
    nTotalFiles = 0
    sumGenWeights = 0.0
    root_files = []
    start = time.time()
    for filedir in rootfiledirs:
        logger.info(f"files dir: {filedir}")
        _root_files = glob.glob(f"{filedir}/*.root")
        root_files = root_files + _root_files
    sumWt_list = Parallel(n_jobs=3)(delayed(get_nfiles_nevents_per_file)(root_files[i], isData) for i in tqdm(range(len(root_files))))
    """
    for i in tqdm(range(len(root_files))):
        #for i, file in enumerate(root_files):
        file = root_files[i]
        nTotalFiles += 1
        wt = get_nfiles_nevents_per_file(file, isData)
        sumGenWeights += wt
        sleep(0.01)
    """
    sumWt_array = ak.Array(sumWt_list)
    nTotalFiles = len(sumWt_array)
    sumGenWeights = ak.sum(sumWt_array)
    end = time.time()
    logger.info(f"getting sumWt in {round((end-start)/60, 3)} mins")

    return nTotalFiles, sumGenWeights
