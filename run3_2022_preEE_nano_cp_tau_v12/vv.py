# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_v14 import campaign_run3_2022_preEE_nano_tau_v14 as cpn




cpn.add_dataset(
    name='ww',
    id=22140112,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=5,
    n_events=15405496.0,
    aux=None
)

cpn.add_dataset(
    name='wz',
    id=22140113,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=3,
    n_events=7527043.0,
    aux=None
)

cpn.add_dataset(
    name='zz',
    id=22140114,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=1181750.0,
    aux=None
)