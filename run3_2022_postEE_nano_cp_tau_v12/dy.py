# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v12 import campaign_run3_2022_postEE_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='dy_lep_m50',
    id=2212027,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYto2L_M-50_amcatnloFXFX'],
    n_files=99,
    n_events=143544567.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_m10to50',
    id=2212028,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYto2L_M-10to50_amcatnloFXFX'],
    n_files=47,
    n_events=168896855.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_0j',
    id=2212029,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=['/DYto2L_M-50_0J_amcatnloFXFX'],
    n_files=134,
    n_events=276057135.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_1j',
    id=22120210,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DYto2L_M-50_1J_amcatnloFXFX'],
    n_files=172,
    n_events=151462400.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_2j',
    id=22120211,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DYto2L_M-50_2J_amcatnloFXFX'],
    n_files=184,
    n_events=84648120.0,
    aux=None
)