import os
import re
import sys
import glob
import yaml
import time
import uproot
import numpy as np
import awkward as ak
from time import sleep
from IPython import embed
from util import *
import argparse

# Define the parser
parser = argparse.ArgumentParser(description='')
parser.add_argument("-c",
                    "--config",
                    action='store', required=True, type=str,
                    help="yaml config")

parser.add_argument("-w",
                    "--workers",
                    action='store', required=False, type=int, default=1,
                    help="n threads")

parser.add_argument("-ch",
                    "--check",
                    action='store', required=False, type=int, default=0,
                    help="before the execution, it will just check if the files are there in the paths mentioned")

args = parser.parse_args()

cores = args.workers
yaml_path = args.config
config = load_config(yaml_path)
campaign_name = config.get("campaign")

if not os.path.exists(os.path.join(os.getcwd(), "logs")):
    os.mkdir(os.path.join(os.getcwd(), "logs"))

logger = setup_logger(os.path.join("logs", f"Produce_nevents_yaml_{campaign_name}.log"))
logger.info(f"PWD: {os.getcwd()}")
logger.info(f"Campaign to be produced: {campaign_name}")
logger.info(f"calculating nEntries ...")

campaign_dir  = os.path.join(os.getcwd(), campaign_name)
if os.path.exists(campaign_dir):
    logger.info(f"{campaign_dir} exists")
else:
    os.mkdir(campaign_dir)


store_path = config.get("store_path")
logger.info(f"Location of NanoAODs: {store_path}")


datasets_tobefilled = config.get("datasets_info")
nEvt_dict = {}
for dataset_key, dataset_val in datasets_tobefilled.items():
    logger.info("\n\n\n\n")
    logger.info(f"dataset name: {dataset_key}")
    #isDATA = True if 'data' in dataset_key else False
    isDATA = bool(re.match('^data_', dataset_key))
    dataset_full_paths        = [store_path+key for key in dataset_val.get("keys")]
    #nfiles, nevents           = get_nfiles_nevents(dataset_full_paths, isDATA, cores)
    if args.check == 1:
        for path in dataset_full_paths:
            root_files = glob.glob(f"{path}/*.root")
            if len(root_files) > 0:
                logger.info(f"{len(root_files)} ROOT files found in {path}")
            else:
                logger.warning(f"NO root files found in {path}")
    else:
        nfiles, sumWt, nevents    = get_nfiles_nevents(dataset_full_paths, isDATA, cores)

        #nEvt_dict[dataset_key] = {"nfiles": int(nfiles), "nevents": float(nevents) }
        nEvt_dict[dataset_key] = {"nfiles" : int(nfiles),
                                  "sumwt"  : float(sumWt),
                                  "nevents": int(nevents) }


if args.check == 1:
    logger.warning("Do not use -ch to create output")
    sys.exit()

logger.info(f"nEvt_dict: {nEvt_dict}")
# open a yaml file to write
with open(os.path.join(campaign_dir, f'nFiles_nEvents.yml'), 'w') as outfile:
    yaml.dump(nEvt_dict, outfile, default_flow_style=False, sort_keys=False)
