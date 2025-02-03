# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14 import campaign_run3_2023_preBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=23140159,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q'],
    n_files=318,
    n_events=151416926.0, # this n_events is the gensumwt
    aux={'n_events': 152653000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_dl',
    id=23140160,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTto2L2Nu'],
    n_files=111,
    n_events=47713334.0, # this n_events is the gensumwt
    aux={'n_events': 48104000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_fh',
    id=23140161,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q'],
    n_files=142,
    n_events=104112654.0, # this n_events is the gensumwt
    aux={'n_events': 104963000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttww',
    id=23140172,
    is_data=False,
    processes=[procs.ttww],
    keys=['/TTWW'],
    n_files=47,
    n_events=14598000.0, # this n_events is the gensumwt
    aux={'n_events': 14598000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttwz',
    id=23140173,
    is_data=False,
    processes=[procs.ttwz],
    keys=['/TTWZ'],
    n_files=3,
    n_events=1000000.0, # this n_events is the gensumwt
    aux={'n_events': 1000000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttzz',
    id=23140174,
    is_data=False,
    processes=[procs.ttzz],
    keys=['/TTZZ'],
    n_files=7,
    n_events=1994000.0, # this n_events is the gensumwt
    aux={'n_events': 1994000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttwh',
    id=23140175,
    is_data=False,
    processes=[procs.ttwh],
    keys=['/TTWH'],
    n_files=7,
    n_events=1981000.0, # this n_events is the gensumwt
    aux={'n_events': 1981000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttzh',
    id=23140176,
    is_data=False,
    processes=[procs.ttzh],
    keys=['/TTZH'],
    n_files=7,
    n_events=1993000.0, # this n_events is the gensumwt
    aux={'n_events': 1993000} # n_events in aux is the nEvents produced
)