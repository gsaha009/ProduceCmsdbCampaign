# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v12 import campaign_run3_2022_postEE_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='data_tau_E',
    id=2212020,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022E'],
    n_files=11,
    n_events=30520481.0,
    aux={'era': 'E', 'require_triggers': ['DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1', 'DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1']}
)

cpn.add_dataset(
    name='data_tau_F',
    id=2212021,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022F'],
    n_files=43,
    n_events=115472800.0,
    aux={'era': 'F', 'require_triggers': ['DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1', 'DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1']}
)

cpn.add_dataset(
    name='data_tau_G',
    id=2212022,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022G'],
    n_files=7,
    n_events=17838713.0,
    aux={'era': 'G', 'require_triggers': ['DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1', 'DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1']}
)

cpn.add_dataset(
    name='data_mu_E',
    id=2212023,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022E'],
    n_files=29,
    n_events=141480973.0,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name='data_mu_G',
    id=2212024,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022G'],
    n_files=18,
    n_events=76689396.0,
    aux={'era': 'G'}
)

cpn.add_dataset(
    name='data_e_E',
    id=2212025,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022E'],
    n_files=31,
    n_events=148661479.0,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name='data_e_G',
    id=2212026,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022G'],
    n_files=18,
    n_events=76724231.0,
    aux={'era': 'G'}
)