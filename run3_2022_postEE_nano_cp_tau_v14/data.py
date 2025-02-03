# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14 import campaign_run3_2022_postEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='data_tau_E',
    id=2214020,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022E'],
    n_files=25,
    n_events=30520481.0, # this n_events is the gensumwt
    aux={'era': 'E', 'n_events': 30520481} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_tau_F',
    id=2214021,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022F'],
    n_files=95,
    n_events=115472800.0, # this n_events is the gensumwt
    aux={'era': 'F', 'n_events': 115472800} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_tau_G',
    id=2214022,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022G'],
    n_files=15,
    n_events=17838713.0, # this n_events is the gensumwt
    aux={'era': 'G', 'n_events': 17838713} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_mu_E',
    id=2214023,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022E'],
    n_files=64,
    n_events=141480973.0, # this n_events is the gensumwt
    aux={'era': 'E', 'n_events': 141480973} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_mu_F',
    id=2214024,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022F'],
    n_files=215,
    n_events=449185088.0, # this n_events is the gensumwt
    aux={'era': 'F', 'n_events': 449185088} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_mu_G',
    id=2214025,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022G'],
    n_files=38,
    n_events=76689396.0, # this n_events is the gensumwt
    aux={'era': 'G', 'n_events': 76689396} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_muon_eg_E',
    id=2214026,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/MuonEG_Run2022E'],
    n_files=10,
    n_events=12868267.0, # this n_events is the gensumwt
    aux={'era': 'E', 'n_events': 12868267} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_muon_eg_F',
    id=2214027,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/MuonEG_Run2022F'],
    n_files=31,
    n_events=38159099.0, # this n_events is the gensumwt
    aux={'era': 'F', 'n_events': 38159099} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_muon_eg_G',
    id=2214028,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/MuonEG_Run2022G'],
    n_files=5,
    n_events=6238527.0, # this n_events is the gensumwt
    aux={'era': 'G', 'n_events': 6238527} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_e_E',
    id=2214029,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022E'],
    n_files=78,
    n_events=148661479.0, # this n_events is the gensumwt
    aux={'era': 'E', 'n_events': 148661479} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_e_F',
    id=22140210,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022F'],
    n_files=254,
    n_events=464077454.0, # this n_events is the gensumwt
    aux={'era': 'F', 'n_events': 464077454} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_e_G',
    id=22140211,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022G'],
    n_files=43,
    n_events=76724231.0, # this n_events is the gensumwt
    aux={'era': 'G', 'n_events': 76724231} # n_events in aux is the nEvents produced
)