import os
import sys
from util import *
import numpy as np
import awkward as ak
from subprocess import Popen, PIPE
from tqdm import tqdm
import argparse


# Define the parser
parser = argparse.ArgumentParser(description='')
parser.add_argument("-c",
                    "--config",
                    action='store', required=True, type=str,
                    help="yaml config")

args = parser.parse_args()

yaml_path = args.config


config = load_config(yaml_path)

campaign_name = config.get("campaign")
campaign_dir  = os.path.join(os.getcwd(), campaign_name)
if os.path.exists(campaign_dir):
    print(f"{campaign_dir} exists")
else:
    runShellCmd(['mkdir', campaign_dir])

store_path = config.get("store_path")
era = config.get("era")
nanoaod_version = config.get("nanoaod")
campaign_id = config.get("campaign_id")
ecm = 13 if era < 2022 else 13.6

datasets_tobefilled = config.get("datasets_info")

print(campaign_name, datasets_tobefilled)

types_of_py_files = np.unique(np.array([item.get('dest') for item in list(datasets_tobefilled.values())]))

    
print("\n")
print(types_of_py_files)
print(f"creating these files inside {campaign_dir}")
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
    _f.write(f""" "version": {nanoaod_version},"""+"\n       ")
    _f.write(""" "custom": {"""+"\n           ")
    _f.write(f""" "name": "{campaign_name}","""+"\n           ")
    _f.write(f""" "creator": "IPHC","""+"\n           ")
    _f.write(f""" "location": "{store_path}","""+"\n        },\n    },\n)\n\n\n")

    _f.write("# trailing imports to load datasets\n")
    for fname in types_of_py_files:
        _f.write(f"import cmsdb.campaigns.{campaign_name}.{fname.split('.')[0]}\n")
    
    
        
# looping over the datasets
for dataset_key, dataset_val in datasets_tobefilled.items():
    print(f"\ndataset name: {dataset_key}")
    file_name = dataset_val.get("dest")
    #print(file_name)
    dataset_full_paths        = [store_path+key for key in dataset_val.get("keys")]
    nfiles, nevents           = get_nfiles_nevents(dataset_full_paths, dataset_val.get("is_data"))

    #print(nfiles, nevents)

    with open(os.path.join(campaign_dir, file_name), 'a') as fname:
        fname.write("\n\n")
        fname.write("cpn.add_dataset(\n    ")
        fname.write(f"""name='{dataset_key}', """+"\n    ")
        fname.write(f"""id={dataset_val.get("id")},"""+"\n    ")
        fname.write(f"""is_data={dataset_val.get("is_data")},"""+"\n    ")
        fname.write(f"""processes={dataset_val.get("processes")},"""+"\n    ")
        fname.write(f"""keys={dataset_val.get("keys")},"""+"\n    ")
        fname.write(f"""n_files={nfiles},"""+"\n    ")
        fname.write(f"""n_events={nevents},"""+"\n    ")
        fname.write(f"""aux={dataset_val.get("aux")}"""+"\n)")
        
