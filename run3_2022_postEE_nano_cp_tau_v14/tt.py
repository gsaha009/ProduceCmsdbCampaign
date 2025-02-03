# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14 import campaign_run3_2022_postEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=22140269,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q', '/TTtoLNu2Q_ext1'],
    n_files=1081,
    n_events=537883189.0, # this n_events is the gensumwt
    aux={'n_events': 542269521} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_dl',
    id=22140270,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTto2L2Nu', '/TTto2L2Nu_ext1'],
    n_files=369,
    n_events=167682796.0, # this n_events is the gensumwt
    aux={'n_events': 169050774} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_fh',
    id=22140271,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q', '/TTto4Q_ext1'],
    n_files=484,
    n_events=363409416.0, # this n_events is the gensumwt
    aux={'n_events': 366376610} # n_events in aux is the nEvents produced
)