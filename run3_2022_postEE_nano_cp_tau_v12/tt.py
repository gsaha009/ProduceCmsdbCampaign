# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_tau_v14 import campaign_run3_2022_postEE_nano_tau_v14 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=22140216,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q', '/TTtoLNu2Q_ext1'],
    n_files=488,
    n_events=539114618.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=22140217,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTTo2L2Nu', '/TTto2L2Nu_ext1'],
    n_files=83,
    n_events=84236946.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=22140218,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q', '/TTto4Q_ext1'],
    n_files=219,
    n_events=364238114.0,
    aux=None
)