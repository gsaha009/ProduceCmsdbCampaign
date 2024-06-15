# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_tau_v14 import campaign_run3_2022_postEE_nano_tau_v14 as cpn




cpn.add_dataset(
    name='ww',
    id=22140213,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=16,
    n_events=53112080.0,
    aux=None
)

cpn.add_dataset(
    name='wz',
    id=22140214,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=8,
    n_events=27003640.0,
    aux=None
)

cpn.add_dataset(
    name='zz',
    id=22140215,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=2,
    n_events=4043040.0,
    aux=None
)