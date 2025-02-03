# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14 import campaign_run3_2023_preBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='ww',
    id=23140141,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=24,
    n_events=33507000.0, # this n_events is the gensumwt
    aux={'n_events': 33507000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_dl_powheg',
    id=23140142,
    is_data=False,
    processes=[procs.ww_dl],
    keys=['/WWto2L2Nu_powheg'],
    n_files=18,
    n_events=12948460.0, # this n_events is the gensumwt
    aux={'n_events': 12951000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_sl_powheg',
    id=23140143,
    is_data=False,
    processes=[procs.ww_sl],
    keys=['/WWtoLNu2Q_powheg'],
    n_files=60,
    n_events=53684756.0, # this n_events is the gensumwt
    aux={'n_events': 53695000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_fh_powheg',
    id=23140144,
    is_data=False,
    processes=[procs.ww_fh],
    keys=['/WWto4Q_powheg'],
    n_files=41,
    n_events=55502862.0, # this n_events is the gensumwt
    aux={'n_events': 55514000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz',
    id=23140145,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=12,
    n_events=16770000.0, # this n_events is the gensumwt
    aux={'n_events': 16770000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zll_powheg',
    id=23140146,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=['/WZto3LNu_powheg'],
    n_files=7,
    n_events=5507998.0, # this n_events is the gensumwt
    aux={'n_events': 5519000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wqq_zll_powheg',
    id=23140147,
    is_data=False,
    processes=[procs.wz_wqq_zll],
    keys=['/WZto2L2Q_powheg'],
    n_files=10,
    n_events=8357166.0, # this n_events is the gensumwt
    aux={'n_events': 8366000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zqq_powheg',
    id=23140148,
    is_data=False,
    processes=[procs.wz_wlnu_zqq],
    keys=['/WZtoLNu2Q_powheg'],
    n_files=19,
    n_events=17789344.0, # this n_events is the gensumwt
    aux={'n_events': 17797000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zll_amcatnlo',
    id=23140149,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=['/WZto3LNu_amcatnloFXFX'],
    n_files=9,
    n_events=3832981.0, # this n_events is the gensumwt
    aux={'n_events': 6051187} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz',
    id=23140150,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=2,
    n_events=2517000.0, # this n_events is the gensumwt
    aux={'n_events': 2517000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zqq_zll_powheg',
    id=23140151,
    is_data=False,
    processes=[procs.zz_zqq_zll],
    keys=['/ZZto2L2Q_powheg'],
    n_files=33,
    n_events=29573916.0, # this n_events is the gensumwt
    aux={'n_events': 29757000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zqq_zll_amcatnlo',
    id=23140152,
    is_data=False,
    processes=[procs.zz_zqq_zll],
    keys=['/ZZto2L2Q_amcatnloFXFX'],
    n_files=7,
    n_events=2622239.0, # this n_events is the gensumwt
    aux={'n_events': 4301883} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zll_zll_powheg',
    id=23140153,
    is_data=False,
    processes=[procs.zz_zll_zll],
    keys=['/ZZto4L_powheg'],
    n_files=36,
    n_events=29522954.0, # this n_events is the gensumwt
    aux={'n_events': 29832000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_znunu_zqq_powheg',
    id=23140154,
    is_data=False,
    processes=[procs.zz_znunu_zqq],
    keys=['/ZZto2Nu2Q_powheg'],
    n_files=4,
    n_events=5945796.0, # this n_events is the gensumwt
    aux={'n_events': 5955000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='www',
    id=23140155,
    is_data=False,
    processes=[procs.www],
    keys=['/WWW_4F'],
    n_files=2,
    n_events=849916.0, # this n_events is the gensumwt
    aux={'n_events': 936000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wwz',
    id=23140156,
    is_data=False,
    processes=[procs.wwz],
    keys=['/WWZ_4F'],
    n_files=7,
    n_events=3275962.0, # this n_events is the gensumwt
    aux={'n_events': 3600000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wzz',
    id=23140157,
    is_data=False,
    processes=[procs.wzz],
    keys=['/WZZ'],
    n_files=7,
    n_events=3251476.0, # this n_events is the gensumwt
    aux={'n_events': 3576000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zzz',
    id=23140158,
    is_data=False,
    processes=[procs.zzz],
    keys=['/ZZZ'],
    n_files=5,
    n_events=3201470.0, # this n_events is the gensumwt
    aux={'n_events': 3600000} # n_events in aux is the nEvents produced
)