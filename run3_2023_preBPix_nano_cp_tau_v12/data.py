# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_v12 import campaign_run3_2023_preBPix_nano_tau_v12 as cpn




cpn.add_dataset(
    name='data_tau_C',
    id=2312010,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023C_v1'],
    n_files=7,
    n_events=14484171.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_mu0_C',
    id=2312011,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023C_v1', '/Muon0_Run2023C_v2', '/Muon0_Run2023C_v3'],
    n_files=21,
    n_events=91794724.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_mu1_C',
    id=2312012,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon1_Run2023C_v1', '/Muon1_Run2023C_v2', '/Muon1_Run2023C_v3'],
    n_files=21,
    n_events=91692246.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_e0_C',
    id=2312013,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma0_Run2023C_v1', '/EGamma0_Run2023C_v2', '/EGamma0_Run2023C_v3'],
    n_files=23,
    n_events=106824436.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_e1_C',
    id=2312014,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma1_Run2023C_v1', '/EGamma1_Run2023C_v2', '/EGamma1_Run2023C_v3'],
    n_files=23,
    n_events=106748681.0,
    aux={'era': 'C'}
)