# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v12 import campaign_run3_2023_postBPix_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='data_tau_D',
    id=2312020,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023D_v1', '/Tau_Run2023D_v2'],
    n_files=17,
    n_events=39338861.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_mu0_D',
    id=2312021,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023D_v1'],
    n_files=22,
    n_events=100211533.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_mu1_D',
    id=2312022,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon1_Run2023D_v1'],
    n_files=22,
    n_events=100281976.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_e0_D',
    id=2312023,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma0_Run2023D_v1', '/EGamma0_Run2023D_v2'],
    n_files=30,
    n_events=128549857.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_e1_D',
    id=2312024,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma1_Run2023D_v1', '/EGamma1_Run2023D_v2'],
    n_files=30,
    n_events=128503830.0,
    aux={'era': 'D'}
)