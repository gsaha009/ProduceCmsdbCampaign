# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12 import campaign_run3_2022_preEE_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='wj_incl_madgraph',
    id=2212019,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM', '/WtoLNu_madgraphMLM_ext1'],
    n_files=45,
    n_events=184695989.0,
    aux=None
)

cpn.add_dataset(
    name='wj_incl_amcatnlo',
    id=22120110,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_amcatnloFXFX'],
    n_files=24,
    n_events=59463375.0,
    aux=None
)