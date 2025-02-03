# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14 import campaign_run3_2023_postBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=23140259,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q'],
    n_files=169,
    n_events=76050494.0, # this n_events is the gensumwt
    aux={'n_events': 76670000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_dl',
    id=23140260,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTto2L2Nu'],
    n_files=56,
    n_events=24357456.0, # this n_events is the gensumwt
    aux={'n_events': 24556000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_fh',
    id=23140261,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q'],
    n_files=72,
    n_events=52422350.0, # this n_events is the gensumwt
    aux={'n_events': 52849000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttww',
    id=23140272,
    is_data=False,
    processes=[procs.ttww],
    keys=['/TTWW'],
    n_files=24,
    n_events=7418000.0, # this n_events is the gensumwt
    aux={'n_events': 7418000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttwz',
    id=23140273,
    is_data=False,
    processes=[procs.ttwz],
    keys=['/TTWZ'],
    n_files=2,
    n_events=497000.0, # this n_events is the gensumwt
    aux={'n_events': 497000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttzz',
    id=23140274,
    is_data=False,
    processes=[procs.ttzz],
    keys=['/TTZZ'],
    n_files=3,
    n_events=954000.0, # this n_events is the gensumwt
    aux={'n_events': 954000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttwh',
    id=23140275,
    is_data=False,
    processes=[procs.ttwh],
    keys=['/TTWH'],
    n_files=4,
    n_events=993000.0, # this n_events is the gensumwt
    aux={'n_events': 993000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ttzh',
    id=23140276,
    is_data=False,
    processes=[procs.ttzh],
    keys=['/TTZH'],
    n_files=4,
    n_events=994000.0, # this n_events is the gensumwt
    aux={'n_events': 994000} # n_events in aux is the nEvents produced
)