# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_v14 import campaign_run3_2022_preEE_nano_tau_v14 as cpn




cpn.add_dataset(
    name='dy_lep_m50',
    id=2214016,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYto2L_M-50_madgraphMLM', '/DYto2L_M-50_madgraphMLM_ext1'],
    n_files=63,
    n_events=145286646.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_m10to50',
    id=2214017,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYto2L_M-10to50_amcatnloFXFX'],
    n_files=15,
    n_events=52629903.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_0j',
    id=2214018,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=['/DYto2L_M-50_0J_amcatnloFXFX'],
    n_files=42,
    n_events=83840818.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_1j',
    id=2214019,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DYto2L_M-50_1J_amcatnloFXFX'],
    n_files=54,
    n_events=46809421.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_2j',
    id=22140110,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DYto2L_M-50_2J_amcatnloFXFX'],
    n_files=51,
    n_events=23075468.0,
    aux=None
)