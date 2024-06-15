# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_v14 import campaign_run3_2022_preEE_nano_tau_v14 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=22140115,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q', '/TTtoLNu2Q_ext1'],
    n_files=153,
    n_events=165110999.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=22140116,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTTo2L2Nu', '/TTto2L2Nu_ext1'],
    n_files=24,
    n_events=23890314.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=22140117,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q', '/TTto4Q_ext1'],
    n_files=65,
    n_events=105189265.0,
    aux=None
)