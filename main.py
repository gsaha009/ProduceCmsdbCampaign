import os
import sys
from util import *
import numpy as np
import awkward as ak
from subprocess import Popen, PIPE
from tqdm import tqdm
from IPython import embed
import argparse


# Define the parser
parser = argparse.ArgumentParser(description='')
parser.add_argument("-c",
                    "--config",
                    action='store', required=True, type=str,
                    help="yaml config")
parser.add_argument("-u",
                    "--utilconfig",
                    action='store', required=False, type=str,
                    help="config with nentries and nfiles")

args = parser.parse_args()


yaml_path = args.config
config = load_config(yaml_path)
campaign_name = config.get("campaign")

if not os.path.exists(os.path.join(os.getcwd(), "logs")):
    os.mkdir(os.path.join(os.getcwd(), "logs"))

logger = setup_logger(os.path.join("logs", f"Runlog_{campaign_name}.log"))
logger.info(f"PWD: {os.getcwd()}")
logger.info(f"Campaign to be produced: {campaign_name}")

campaign_dir  = os.path.join(os.getcwd(), campaign_name)
if os.path.exists(campaign_dir):
    logger.info(f"{campaign_dir} exists")
else:
    os.mkdir(campaign_dir)

store_path = config.get("store_path")
logger.info(f"Location of NanoAODs: {store_path}")
era = config.get("era")
logger.info(f"Era: {era}")
run = 3 if era > 2021 else 2
nanoaod_version = config.get("nanoaod")
logger.info(f"version: {nanoaod_version}")
campaign_id = config.get("campaign_id")
logger.info(f"campaign_id: {campaign_id}")
ecm = 13 if era < 2022 else 13.6
logger.info(f"ecm: {ecm}")
postfix = config.get("postfix")
logger.info(f"postfix: {postfix}")

utilconfigfile = os.path.join(campaign_dir, args.utilconfig)
fileisthere = os.path.exists(utilconfigfile)
logger.info(f"Yaml file with precalculated numbers {utilconfigfile}? : {fileisthere}")

utilconfig = load_config(utilconfigfile) if fileisthere else None

datasets_tobefilled = config.get("datasets_info")
if fileisthere:
    logger.info("checking if everything is calculated for all datasets in campaign ...")
    all_dataset_names_from_main_config = list(datasets_tobefilled.keys())
    all_dataset_names_from_util_config = list(utilconfig.keys())
    missing = np.setxor1d(all_dataset_names_from_main_config, all_dataset_names_from_util_config)
    logger.info(f"no pre-calculated numbers for : {list(missing)}")

types_of_py_files = np.unique(np.array([item.get('dest') for item in list(datasets_tobefilled.values())]))

logger.info("\n")
logger.info(types_of_py_files)
logger.info(f"creating these files inside {campaign_dir}")
for fname in types_of_py_files:
    with open(os.path.join(campaign_dir, fname), 'w') as _f:
        _f.write(f"# {fname}\n")
        _f.write(f"# Link: {store_path}\n\n")
        _f.write("import cmsdb.processes as procs\n")
        _f.write(f"from cmsdb.campaigns.{campaign_name} import campaign_{campaign_name} as cpn\n\n\n")


# preparing __init__.py
with open(os.path.join(campaign_dir, "__init__.py"), 'w') as _f:
    _f.write("# coding: utf-8"+"\n\n")
    _f.write("from order import Campaign\n\n\n")
    _f.write("# ----------- #\n")
    _f.write("#   Campaign  #\n")
    _f.write("# ----------- #\n")
    _f.write(f"campaign_{campaign_name} = Campaign("+"\n    ")
    _f.write(f"name='{campaign_name}',"+"\n    ")
    _f.write(f"id={campaign_id},"+"\n    ")
    _f.write(f"ecm={ecm},"+"\n    ")
    _f.write("bx=25,\n    ")
    _f.write("aux={\n       ")
    _f.write(f""" "tier": "NanoAOD", """+"\n       ")
    _f.write(f""" "year": {era},"""+"\n       ")
    _f.write(f""" "run": {run},"""+"\n       ")
    _f.write(f""" "postfix": "{postfix}","""+"\n       ") if postfix else _f.write(f""" "postfix": {postfix},"""+"\n       ")
    _f.write(f""" "version": {nanoaod_version},"""+"\n       ")
    _f.write(""" "custom": {"""+"\n           ")
    _f.write(f""" "name": "{campaign_name}","""+"\n           ")
    _f.write(f""" "creator": "IPHC","""+"\n           ")
    _f.write(f""" "location": "{store_path}","""+"\n        },\n    },\n)\n\n\n")

    _f.write("# trailing imports to load datasets\n")
    for fname in types_of_py_files:
        _f.write(f"import cmsdb.campaigns.{campaign_name}.{fname.split('.')[0]}\n")
    
    
        
# looping over the datasets
for idx, (dataset_key, dataset_val) in enumerate(datasets_tobefilled.items()):
    logger.info("\n\n")
    logger.info(f"dataset name: {dataset_key}")
    nfiles = None
    nevents = None
    isDATA = True if 'data' in dataset_key else False
    file_name = dataset_val.get("dest")
    #logger.info(file_name)
    dataset_full_paths        = [store_path+key for key in dataset_val.get("keys")]
    if fileisthere and dataset_key in list(utilconfig.keys()):
        logger.info(f"getting numbers from {utilconfigfile}")
        temp = utilconfig.get(dataset_key)
        nfiles  = temp["nfiles"]
        sumwt   = temp["sumwt"]
        nevents = temp["nevents"]        
    else:
        logger.info(f"calculating nevents and nfiles")
        #nfiles, nevents           = get_nfiles_nevents(dataset_full_paths, isDATA)
        nfiles, sumwt, nevents     = get_nfiles_nevents(dataset_full_paths, isDATA)
    
    logger.info(f"nFiles: {nfiles}, sumWtProduced: {sumwt}, nEventsProduced: {nevents}")

    # read existing file
    # with open(os.path.join(campaign_dir, file_name), 'r') as fname:
    #    embed()
    #    lines = fname.readlines()
    #    if f"name='{dataset_key}'"

    dataset_id = int(f"{campaign_id}{idx}")

    # -------- new -------- #
    # adding nEvents in aux
    aux = dataset_val.get("aux")
    if aux is None:
        aux = {"n_events": nevents}
    else:
        aux = dataset_val.get("aux") | {"n_events": nevents}
    
    with open(os.path.join(campaign_dir, file_name), 'a') as fname:
        fname.write("\n\n")
        fname.write("cpn.add_dataset(\n    ")
        fname.write(f"""name='{dataset_key}',"""+"\n    ")
        #fname.write(f"""id={dataset_val.get("id")},"""+"\n    ")
        fname.write(f"""id={dataset_id},"""+"\n    ")
        #fname.write(f"""is_data={dataset_val.get("is_data")},"""+"\n    ")
        fname.write(f"""is_data={isDATA},"""+"\n    ")
        #embed()
        fname.write(f"""processes=[{','.join(dataset_val.get("processes"))}],"""+"\n    ")
        fname.write(f"""keys={dataset_val.get("keys")},"""+"\n    ")
        fname.write(f"""n_files={nfiles},"""+"\n    ")
        #fname.write(f"""n_events={nevents},"""+"\n    ")
        fname.write(f"""n_events={sumwt}, # this n_events is the gensumwt"""+"\n    ")
        #fname.write(f"""aux={dataset_val.get("aux")}"""+"\n)")
        fname.write(f"""aux={aux} # n_events in aux is the nEvents produced"""+"\n)")
        
