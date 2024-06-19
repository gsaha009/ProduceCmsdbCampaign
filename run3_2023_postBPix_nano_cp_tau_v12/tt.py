# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v12 import campaign_run3_2023_postBPix_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=23120214,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q'],
    n_files=77,
    n_events=81212938.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=23120215,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTTo2L2Nu'],
    n_files=0,
    n_events=0.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=23120216,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q'],
    n_files=33,
    n_events=52422350.0,
    aux=None
)