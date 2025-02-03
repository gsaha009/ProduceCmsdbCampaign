# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14 import campaign_run3_2023_postBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='data_tau_D',
    id=2314020,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023D_v1', '/Tau_Run2023D_v2'],
    n_files=38,
    n_events=39338861.0, # this n_events is the gensumwt
    aux={'era': 'D', 'n_events': 39338861} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_mu0_D',
    id=2314021,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023D_v1', '/Muon0_Run2023D_v2'],
    n_files=65,
    n_events=121674449.0, # this n_events is the gensumwt
    aux={'era': 'D', 'n_events': 121674449} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_mu1_D',
    id=2314022,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon1_Run2023D_v1', '/Muon1_Run2023D_v2'],
    n_files=65,
    n_events=121745621.0, # this n_events is the gensumwt
    aux={'era': 'D', 'n_events': 121745621} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_muon_eg_D',
    id=2314023,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/MuonEG_Run2023D_v1', '/MuonEG_Run2023D_v2'],
    n_files=20,
    n_events=21282118.0, # this n_events is the gensumwt
    aux={'era': 'D', 'n_events': 21282118} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_e0_D',
    id=2314024,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma0_Run2023D_v1', '/EGamma0_Run2023D_v2'],
    n_files=78,
    n_events=128549857.0, # this n_events is the gensumwt
    aux={'era': 'D', 'n_events': 128549857} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_e1_D',
    id=2314025,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma1_Run2023D_v1', '/EGamma1_Run2023D_v2'],
    n_files=78,
    n_events=128503830.0, # this n_events is the gensumwt
    aux={'era': 'D', 'n_events': 128503830} # n_events in aux is the nEvents produced
)