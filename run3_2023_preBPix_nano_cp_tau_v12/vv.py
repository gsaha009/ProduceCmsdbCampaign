# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_v12 import campaign_run3_2023_preBPix_nano_tau_v12 as cpn




cpn.add_dataset(
    name='ww',
    id=23120110,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=11,
    n_events=33507000.0,
    aux=None
)

cpn.add_dataset(
    name='wz',
    id=23120111,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=5,
    n_events=16770000.0,
    aux=None
)

cpn.add_dataset(
    name='zz',
    id=23120112,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=2517000.0,
    aux=None
)