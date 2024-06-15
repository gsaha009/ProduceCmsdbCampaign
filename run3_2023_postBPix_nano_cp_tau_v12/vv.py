# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_tau_v12 import campaign_run3_2023_postBPix_nano_tau_v12 as cpn




cpn.add_dataset(
    name='ww',
    id=23120211,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=6,
    n_events=16545000.0,
    aux=None
)

cpn.add_dataset(
    name='wz',
    id=23120212,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=3,
    n_events=8379000.0,
    aux=None
)

cpn.add_dataset(
    name='zz',
    id=23120213,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=1254000.0,
    aux=None
)