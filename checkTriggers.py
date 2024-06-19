import os
import sys
import glob
import uproot
import awkward as ak
import numpy as np
import argparse
import tqdm
from prettytable import PrettyTable

# Define the parser
parser = argparse.ArgumentParser(description='')
parser.add_argument("-e",
                    "--era",
                    action='store', required=True, type=int,
                    help="era")
parser.add_argument("-p",
                    "--postfix",
                    action='store', required=False, type=str,
                    help="config with nentries and nfiles")

args = parser.parse_args()


triggers = {
    2016: {
        "PreVFP": {
            "source": "/eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016_HIPM",
            "targets_mc": ["/TTTo2L2Nu"],
            "targets_data": ["/Tau_Run2016B",
                             "/Tau_Run2016C",
                             "/Tau_Run2016D",
                             "/Tau_Run2016E",
                             "/Tau_Run2016F"],
            "paths" : ["HLT_Ele25_eta2p1_WPTight_Gsf",
                       "HLT_IsoMu22",
                       "HLT_IsoTkMu22",
                       "HLT_IsoTkMu22_eta2p1",
                       "HLT_IsoMu19_eta2p1_LooseIsoPFTau20",
                       "HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1",
                       "HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg",
                       "HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg"],
        },
        "PostVFP": {
            "source": "/eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016",
            "targets_mc": ["/TTTo2L2Nu"],
            "targets_data": ["/Tau_Run2016F",
                             "/Tau_Run2016G",
                             "/Tau_Run2016H"],
            "paths": ["HLT_Ele25_eta2p1_WPTight_Gsf",
                      "HLT_IsoMu22",
                      "HLT_IsoTkMu22",
                      "HLT_IsoTkMu22_eta2p1",
                      "HLT_IsoMu19_eta2p1_LooseIsoPFTau20",
                      "HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1",
                      "HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg",
                      "HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg"],
        },
    },
    2017: {
        "source": "/eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017",
        "targets_mc": ["/TTToSemiLeptonic"],
        "targets_data": ["/Tau_Run2017B",
                         "/Tau_Run2017C",
                         "/Tau_Run2017D",
                         "/Tau_Run2017E",
                         "/Tau_Run2017F"],
        "paths": ["HLT_Ele27_WPTight_Gsf",
                  "HLT_Ele32_WPTight_Gsf",
                  "HLT_IsoMu24",
                  "HLT_IsoMu27",
                  "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
                  "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
                  "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
                  "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
                  "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg"],
    },
    2018: {
        "source": "/eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018",
        "targets_mc": ["/TTToSemiLeptonic"],
        "targets_data": ["/Tau_Run2018A",
                         "/Tau_Run2018B",
                         "/Tau_Run2018C",
                         "/Tau_Run2018D"],
        "paths" : ["HLT_Ele35_WPTight_Gsf",
                   "HLT_Ele32_WPTight_Gsf",
                   "HLT_IsoMu24",
                   "HLT_IsoMu27",
                   "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
                   "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1",
                   "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
                   "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1",
                   "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_TightID_CrossL1",
                   "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
                   "HLT_DoubleTightChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
                   "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
                   "HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg"],
    },
}

def docheckrun(files):
    runs = []
    for i in tqdm.tqdm(range(len(files))):
        file = files[i]
        opfile = uproot.open(file)
        tree = opfile["Events"]
        _runs = np.unique(ak.to_numpy(tree.arrays(["run"])))
        runs = runs + _runs.tolist()
    return runs
        
def isThereTheTrigger(HLT, mcToCheck, checkrun=False):
    Out = []
    runs = []
    for i, mc in enumerate(mcToCheck):
        roots = glob.glob(f"{mc}/*.root")
        if checkrun:
            _runs = docheckrun(roots)
            runs.append(_runs)
        rootf = roots[0]
        #print(rootf)
        urootf = uproot.open(rootf)
        events = urootf["Events"]
        fields = [item for item in events.keys() if item.startswith("HLT_")]
        if HLT in fields:
            Out.append('√')
        else:
            Out.append('X')
    return Out, runs


print(f"Era: {args.era}")
print(f"Postfix: {args.postfix}")

trig_details = triggers[args.era]
if args.postfix:
    trig_details = triggers[args.era][args.postfix] 

print(f"Trigger details: {trig_details}")

mcToCheck = [trig_details["source"]+item for item in trig_details["targets_mc"]]
print(f"MC targets: {mcToCheck}")
dataToCheck = [trig_details["source"]+item for item in trig_details["targets_data"]]
print(f"DATA targets: {dataToCheck}")

# check trigger
x = PrettyTable()
x.field_names = ["HLT"] + ["MC"] + trig_details["targets_data"]

for i in tqdm.tqdm(range(len(trig_details["paths"]))):
    HLT = trig_details["paths"][i]
    inMC, runs_MC = isThereTheTrigger(HLT, mcToCheck)
    inData, runs_Data = isThereTheTrigger(HLT, dataToCheck, checkrun=False)

    values = [HLT] + inMC + inData
    x.add_row(values)

#x.add_row(["run nos"] + runs_MC + runs_Data)
x = str(x)
print(x)
