# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14 import campaign_run3_2023_postBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='ww',
    id=23140241,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=12,
    n_events=16545000.0, # this n_events is the gensumwt
    aux={'n_events': 16545000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_dl_powheg',
    id=23140242,
    is_data=False,
    processes=[procs.ww_dl],
    keys=['/WWto2L2Nu_powheg'],
    n_files=9,
    n_events=6361734.0, # this n_events is the gensumwt
    aux={'n_events': 6363000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_sl_powheg',
    id=23140243,
    is_data=False,
    processes=[procs.ww_sl],
    keys=['/WWtoLNu2Q_powheg'],
    n_files=30,
    n_events=26339932.0, # this n_events is the gensumwt
    aux={'n_events': 26345000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_fh_powheg',
    id=23140244,
    is_data=False,
    processes=[procs.ww_fh],
    keys=['/WWto4Q_powheg'],
    n_files=20,
    n_events=27865342.0, # this n_events is the gensumwt
    aux={'n_events': 27871000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz',
    id=23140245,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=6,
    n_events=8379000.0, # this n_events is the gensumwt
    aux={'n_events': 8379000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zll_powheg',
    id=23140246,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=['/WZto3LNu_powheg'],
    n_files=4,
    n_events=2764596.0, # this n_events is the gensumwt
    aux={'n_events': 2770000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wqq_zll_powheg',
    id=23140247,
    is_data=False,
    processes=[procs.wz_wqq_zll],
    keys=['/WZto2L2Q_powheg'],
    n_files=6,
    n_events=4262560.0, # this n_events is the gensumwt
    aux={'n_events': 4267000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zqq_powheg',
    id=23140248,
    is_data=False,
    processes=[procs.wz_wlnu_zqq],
    keys=['/WZtoLNu2Q_powheg'],
    n_files=10,
    n_events=8776368.0, # this n_events is the gensumwt
    aux={'n_events': 8780000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zll_amcatnlo',
    id=23140249,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=['/WZto3LNu_amcatnloFXFX'],
    n_files=4,
    n_events=1889691.0, # this n_events is the gensumwt
    aux={'n_events': 2985919} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz',
    id=23140250,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=1254000.0, # this n_events is the gensumwt
    aux={'n_events': 1254000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zqq_zll_powheg',
    id=23140251,
    is_data=False,
    processes=[procs.zz_zqq_zll],
    keys=['/ZZto2L2Q_powheg'],
    n_files=17,
    n_events=14827594.0, # this n_events is the gensumwt
    aux={'n_events': 14919000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zqq_zll_amcatnlo',
    id=23140252,
    is_data=False,
    processes=[procs.zz_zqq_zll],
    keys=['/ZZto2L2Q_amcatnloFXFX'],
    n_files=4,
    n_events=1347286.0, # this n_events is the gensumwt
    aux={'n_events': 2209006} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zll_zll_powheg',
    id=23140253,
    is_data=False,
    processes=[procs.zz_zll_zll],
    keys=['/ZZto4L_powheg'],
    n_files=18,
    n_events=14473446.0, # this n_events is the gensumwt
    aux={'n_events': 14625000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_znunu_zqq_powheg',
    id=23140254,
    is_data=False,
    processes=[procs.zz_znunu_zqq],
    keys=['/ZZto2Nu2Q_powheg'],
    n_files=2,
    n_events=2974354.0, # this n_events is the gensumwt
    aux={'n_events': 2979000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='www',
    id=23140255,
    is_data=False,
    processes=[procs.www],
    keys=['/WWW_4F'],
    n_files=1,
    n_events=423054.0, # this n_events is the gensumwt
    aux={'n_events': 466500} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wwz',
    id=23140256,
    is_data=False,
    processes=[procs.wwz],
    keys=['/WWZ_4F'],
    n_files=4,
    n_events=1585526.0, # this n_events is the gensumwt
    aux={'n_events': 1743000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wzz',
    id=23140257,
    is_data=False,
    processes=[procs.wzz],
    keys=['/WZZ'],
    n_files=4,
    n_events=1625116.0, # this n_events is the gensumwt
    aux={'n_events': 1788000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zzz',
    id=23140258,
    is_data=False,
    processes=[procs.zzz],
    keys=['/ZZZ'],
    n_files=3,
    n_events=1589388.0, # this n_events is the gensumwt
    aux={'n_events': 1788000} # n_events in aux is the nEvents produced
)