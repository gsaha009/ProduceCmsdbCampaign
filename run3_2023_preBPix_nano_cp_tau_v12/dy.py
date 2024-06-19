# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v12 import campaign_run3_2023_preBPix_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='dy_lep_m50',
    id=2312015,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYto2L_M-50_amcatnloFXFX'],
    n_files=75,
    n_events=103978251.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_0j',
    id=2312016,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=['/DYto2L_M-50_0J_amcatnloFXFX'],
    n_files=80,
    n_events=155735461.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_1j',
    id=2312017,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DYto2L_M-50_1J_amcatnloFXFX'],
    n_files=108,
    n_events=90103222.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_2j',
    id=2312018,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DYto2L_M-50_2J_amcatnloFXFX'],
    n_files=107,
    n_events=47134234.0,
    aux=None
)