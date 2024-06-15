# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_v12 import campaign_run3_2023_preBPix_nano_tau_v12 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=23120113,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q'],
    n_files=143,
    n_events=151416926.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=23120114,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTTo2L2Nu'],
    n_files=0,
    n_events=0.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=23120115,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q'],
    n_files=65,
    n_events=104112654.0,
    aux=None
)