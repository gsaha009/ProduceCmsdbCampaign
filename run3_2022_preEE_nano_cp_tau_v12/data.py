# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12 import campaign_run3_2022_preEE_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='data_tau_C',
    id=2212010,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022C'],
    n_files=10,
    n_events=25903135.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_tau_D',
    id=2212011,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022D'],
    n_files=6,
    n_events=16686692.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_single_mu_C',
    id=2212012,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2022C'],
    n_files=4,
    n_events=20162441.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_mu_C',
    id=2212013,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022C'],
    n_files=28,
    n_events=138329693.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_mu_D',
    id=2212014,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022D'],
    n_files=16,
    n_events=75440027.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_e_C',
    id=2212015,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022C'],
    n_files=46,
    n_events=263549470.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_e_D',
    id=2212016,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022D'],
    n_files=18,
    n_events=89134996.0,
    aux={'era': 'D'}
)