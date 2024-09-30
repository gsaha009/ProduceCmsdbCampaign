import os
import sys
import glob
import uproot
import awkward as ak
import numpy as np
from time import sleep
import argparse
import tqdm
from prettytable import PrettyTable
from util import setup_logger

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


if not os.path.exists(os.path.join(os.getcwd(), "logs")):
    os.mkdir(os.path.join(os.getcwd(), "logs"))

logger = setup_logger(os.path.join("logs", f"HLTlog_{args.era}{args.postfix}.log"))
logger.info(f"PWD: {os.getcwd()}")


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
        "targets_data": ["/Tau_Run2018A", "/Tau_Run2018B", "/Tau_Run2018C", "/Tau_Run2018D",
                         "/SingleMuon_Run2018A", "/SingleMuon_Run2018B", "/SingleMuon_Run2018C", "/SingleMuon_Run2018D",
                         "/EGamma_Run2018A", "/EGamma_Run2018B", "/EGamma_Run2018C", "/EGamma_Run2018D"],
        "paths" : ["HLT_Ele35_WPTight_Gsf",
                   "HLT_Ele32_WPTight_Gsf",
                   "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
                   "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1",
                   "HLT_IsoMu24",
                   "HLT_IsoMu27",
                   "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
                   "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1",
                   "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1",
                   "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
                   "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
                   "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
                   #"HLT_DoubleTightChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
                   "HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg"],
    },
    2022: {
        "PreEE": {
            "source": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022",
            "targets_mc": ["/WtoLNu_amcatnloFXFX"],
            "targets_data": ["/Tau_Run2022C", "/Tau_Run2022D",
                             "/SingleMuon_Run2022C",
                             "/Muon_Run2022C", "/Muon_Run2022D",
                             "/EGamma_Run2022C", "/EGamma_Run2022D"],
            "paths" : ["HLT_Ele32_WPTight_Gsf",
                       "HLT_Ele27_WPTight_Gsf",
                       "HLT_IsoMu27",
                       "HLT_IsoMu24",
                       "HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
                       "HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
                       "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1",
                       "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1",
                       "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1"],
        },
        "PostEE": {
            "source": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022EE",
            "targets_mc": ["/WtoLNu_amcatnloFXFX"],
            "targets_data": ["/Tau_Run2022E", "/Tau_Run2022F", "/Tau_Run2022G",
                             "/Muon_Run2022E", "/Muon_Run2022F", "/Muon_Run2022G",
                             "/EGamma_Run2022E", "/EGamma_Run2022F", "/EGamma_Run2022G",
                             ],
            "paths" : ["HLT_Ele32_WPTight_Gsf",
                       "HLT_Ele27_WPTight_Gsf",
                       "HLT_IsoMu27",
                       "HLT_IsoMu24",
                       "HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
                       "HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
                       "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1",
                       "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1",
                       "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1"],
        },
    },
    2023: {
        "PreBPix": {
            "source": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023",
            "targets_mc": ["/WtoLNu_madgraphMLM"],
            "targets_data": ["/Tau_Run2023C_v1"],
            "paths" : ["HLT_Ele32_WPTight_Gsf",
                       "HLT_Ele30_WPTight_Gsf",
                       "HLT_IsoMu27",
                       "HLT_IsoMu24",
                       "HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
                       "HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
                       "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1"],
        },
        "PostBPix": {
            "source": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023BPix",
            "targets_mc": ["/WtoLNu_madgraphMLM"],
            "targets_data": ["/Tau_Run2023D_v1",
                             "/Tau_Run2023D_v2"],
            "paths" : ["HLT_Ele32_WPTight_Gsf",
                       "HLT_Ele30_WPTight_Gsf",
                       "HLT_IsoMu27",
                       "HLT_IsoMu24",
                       "HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
                       "HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
                       "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1"],
        },
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
        #logger.info(rootf)
        urootf = uproot.open(rootf)
        events = urootf["Events"]
        fields = [item for item in events.keys() if item.startswith("HLT_")]
        if HLT in fields:
            Out.append('√')
        else:
            Out.append('X')
    return Out, runs


logger.info(f"Era: {args.era}")
logger.info(f"Postfix: {args.postfix}")

trig_details = triggers[args.era]
if args.postfix:
    trig_details = triggers[args.era][args.postfix] 

logger.info(f"Trigger details: {trig_details}")

mcToCheck = [trig_details["source"]+item for item in trig_details["targets_mc"]]
logger.info(f"MC targets: {mcToCheck}")
dataToCheck = [trig_details["source"]+item for item in trig_details["targets_data"]]
logger.info(f"DATA targets: {dataToCheck}")

# check trigger
x = PrettyTable()
x.field_names = ["HLT"] + ["MC"]# + trig_details["targets_data"]

for i in tqdm.tqdm(range(len(trig_details["paths"]))):
    HLT = trig_details["paths"][i]
    inMC, runs_MC = isThereTheTrigger(HLT, mcToCheck)
    #inData, runs_Data = isThereTheTrigger(HLT, dataToCheck, checkrun=False)

    values = [HLT] + inMC# + inData
    x.add_row(values)

#x.add_row(["run nos"] + runs_MC + runs_Data)
x = str(x)
logger.info(f"\n{x}")

HLTs = trig_details["paths"]
HLTidxs = []
logger.info("encode HLTs")
for i in range(len(HLTs)):
    HLTidxs.append(f"HLT_{i}")
    logger.info(f"{i} : {HLTs[i]}")

    
# dig deeper into data
for datadir in dataToCheck:
    logger.info(f"===> Dataset : {datadir}")       
    files = glob.glob(f"{datadir}/*.root")

    y = PrettyTable()
    y.field_names = ["File", "from run", "to run", "nEvents"] + HLTidxs #list(range(trig_details["paths"]))
    y.title = f"{os.path.basename(datadir)} : {len(files)} files [HLT present? : nSelectedEvents]"
    
    allRuns = np.array([], dtype=np.int32)
    for ifile in tqdm.tqdm(range(len(files))):
        file = files[ifile]
        #logger.info(file)
        file_basename = os.path.basename(file)
        opfile = uproot.open(file)
        events = opfile["Events"]
        nEvents = int(ak.count(events["event"].array()))
        #logger.info(f"nEvents : {nEvents}")
        runs   = events["run"].array(library="np")
        allRuns = np.concatenate([allRuns, runs])
        min_run = np.min(runs)
        max_run = np.max(runs)
        #logger.info(f"     {min_run} - {max_run}")
        hlts = [item for item in events.keys() if item.startswith("HLT_")]
        hltdict = {}
        for ipath in range(len(HLTs)):
            path = HLTs[ipath]
            #logger.info(f"{ipath} : {path}")
            if path in hlts:
                hlt_array = events[path].array()
                nEvPassed = int(ak.sum(hlt_array))
                #logger.info(f"selecetd : {nEvPassed}")
                hltdict[f"HLT_{ipath}"] = f'√ : {nEvPassed}'
            else:
                hltdict[f"HLT_{ipath}"] = f'X'

        row = [file_basename, min_run, max_run, nEvents] + list(hltdict.values())
        sleep(0.1)
        y.add_row(row)

    allRuns = np.sort(np.unique(allRuns))
    y = str(y)
    logger.info(f"\n{y}\n")
    logger.info(f"Runs: {allRuns.tolist()}")
