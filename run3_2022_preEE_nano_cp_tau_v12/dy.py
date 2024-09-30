# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12 import campaign_run3_2022_preEE_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='dy_lep_m10to50_madgraph',
    id=2212017,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYto2L_M-10to50_madgraphMLM'],
    n_files=32,
    n_events=163769744.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_m50_madgraph',
    id=2212018,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYto2L_M-50_madgraphMLM', '/DYto2L_M-50_madgraphMLM_ext1'],
    n_files=63,
    n_events=145286646.0,
    aux=None
)