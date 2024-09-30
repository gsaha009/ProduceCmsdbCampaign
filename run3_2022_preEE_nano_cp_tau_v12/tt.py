# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12 import campaign_run3_2022_preEE_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=22120114,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q', '/TTtoLNu2Q_ext1'],
    n_files=153,
    n_events=165110999.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=22120115,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTto2L2Nu', '/TTto2L2Nu_ext1'],
    n_files=48,
    n_events=47500385.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=22120116,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q', '/TTto4Q_ext1'],
    n_files=65,
    n_events=105189265.0,
    aux=None
)