# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v12 import campaign_run3_2023_postBPix_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='dy_lep_m50',
    id=2312025,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYto2L_M-50_amcatnloFXFX'],
    n_files=46,
    n_events=63684562.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_m10to50',
    id=2312026,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYto2L_M-10to50_madgraphMLM'],
    n_files=30,
    n_events=150291788.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_0j',
    id=2312027,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=['/DYto2L_M-50_0J_amcatnloFXFX'],
    n_files=40,
    n_events=76989083.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_1j',
    id=2312028,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DYto2L_M-50_1J_amcatnloFXFX'],
    n_files=51,
    n_events=42819115.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_2j',
    id=2312029,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DYto2L_M-50_2J_amcatnloFXFX'],
    n_files=54,
    n_events=23588533.0,
    aux=None
)