# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14 import campaign_run3_2023_preBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='data_tau_C',
    id=2314010,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023C_v1', '/Tau_Run2023C_v2', '/Tau_Run2023C_v3', '/Tau_Run2023C_v4'],
    n_files=72,
    n_events=71310533.0, # this n_events is the gensumwt
    aux={'era': 'C', 'n_events': 71310533} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_mu0_C',
    id=2314011,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023C_v1', '/Muon0_Run2023C_v2', '/Muon0_Run2023C_v3', '/Muon0_Run2023C_v4'],
    n_files=122,
    n_events=230738507.0, # this n_events is the gensumwt
    aux={'era': 'C', 'n_events': 230738507} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_mu1_C',
    id=2314012,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon1_Run2023C_v1', '/Muon1_Run2023C_v2', '/Muon1_Run2023C_v3', '/Muon1_Run2023C_v4'],
    n_files=122,
    n_events=230526490.0, # this n_events is the gensumwt
    aux={'era': 'C', 'n_events': 230526490} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_muon_eg_C',
    id=2314013,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/MuonEG_Run2023C_v1', '/MuonEG_Run2023C_v2', '/MuonEG_Run2023C_v3', '/MuonEG_Run2023C_v4'],
    n_files=36,
    n_events=40215913.0, # this n_events is the gensumwt
    aux={'era': 'C', 'n_events': 40215913} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_e0_C',
    id=2314014,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma0_Run2023C_v1', '/EGamma0_Run2023C_v2', '/EGamma0_Run2023C_v3', '/EGamma0_Run2023C_v4'],
    n_files=156,
    n_events=266932555.0, # this n_events is the gensumwt
    aux={'era': 'C', 'n_events': 266932555} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_e1_C',
    id=2314015,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma1_Run2023C_v1', '/EGamma1_Run2023C_v2', '/EGamma1_Run2023C_v3', '/EGamma1_Run2023C_v4'],
    n_files=156,
    n_events=266745855.0, # this n_events is the gensumwt
    aux={'era': 'C', 'n_events': 266745855} # n_events in aux is the nEvents produced
)