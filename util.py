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

    nsel_events = upfile["EventsNotSelected"]
    if isData:
        nsel_events = nsel_events.arrays()
        sumGenWt_nsel_tree = len(nsel_events)
    else:
        nsel_events = nsel_events.arrays(["genWeight"])
        genWt_nsel_tree = nsel_events["genWeight"]
        genWt_nsel_tree = ak.where(genWt_nsel_tree > 0., 1., ak.where(genWt_nsel_tree < 0., -1., genWt_nsel_tree))
        sumGenWt_nsel_tree = ak.sum(genWt_nsel_tree)

    sumWt   = sumGenWt_sel_tree + sumGenWt_nsel_tree

    return sumWt


def get_nfiles_nevents(rootfiledirs, isData: bool) -> tuple[int, float]:
    nTotalFiles = 0
    sumGenWeights = 0.0
    root_files = []
    start = time.time()
    for filedir in rootfiledirs:
        print(f"files dir: {filedir}")
        _root_files = glob.glob(f"{filedir}/*.root")
        root_files = root_files + _root_files
    sumWt_list = Parallel(n_jobs=10)(delayed(get_nfiles_nevents_per_file)(file, isData) for file in root_files)        
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
    print(f"getting sumWt in {round((end-start)/60, 3)} mins")
    print(f"nFiles: {nTotalFiles}, sumWtProduced: {sumGenWeights}")
    return nTotalFiles, sumGenWeights


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
            print(output.strip().decode("utf-8"))
    rc = process.poll()
