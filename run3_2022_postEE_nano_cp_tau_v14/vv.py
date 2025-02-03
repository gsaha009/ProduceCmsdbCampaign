# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14 import campaign_run3_2022_postEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='ww',
    id=22140247,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=34,
    n_events=53112080.0, # this n_events is the gensumwt
    aux={'n_events': 53112080} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_dl_powheg',
    id=22140248,
    is_data=False,
    processes=[procs.ww_dl],
    keys=['/WWto2L2Nu_powheg', '/WWto2L2Nu_powheg_ext1'],
    n_files=56,
    n_events=44754982.0, # this n_events is the gensumwt
    aux={'n_events': 44763914} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_sl_powheg',
    id=22140249,
    is_data=False,
    processes=[procs.ww_sl],
    keys=['/WWtoLNu2Q_powheg', '/WWtoLNu2Q_powheg_ext1'],
    n_files=201,
    n_events=188346496.0, # this n_events is the gensumwt
    aux={'n_events': 188383744} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_fh_powheg',
    id=22140250,
    is_data=False,
    processes=[procs.ww_fh],
    keys=['/WWto4Q_powheg', '/WWto4Q_powheg_ext1'],
    n_files=138,
    n_events=193956978.0, # this n_events is the gensumwt
    aux={'n_events': 193995550} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_sl_amcatnlo',
    id=22140251,
    is_data=False,
    processes=[procs.ww_sl],
    keys=['/WWtoLNu2Q_amcatnloFXFX'],
    n_files=85,
    n_events=45175446.0, # this n_events is the gensumwt
    aux={'n_events': 75533018} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_fh_amcatnlo',
    id=22140252,
    is_data=False,
    processes=[procs.ww_fh],
    keys=['/WWto4Q_amcatnloFXFX'],
    n_files=28,
    n_events=22853516.0, # this n_events is the gensumwt
    aux={'n_events': 37899752} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz',
    id=22140253,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=17,
    n_events=26722782.0, # this n_events is the gensumwt
    aux={'n_events': 26722782} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zll_powheg',
    id=22140254,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=['/WZto3LNu_powheg'],
    n_files=12,
    n_events=9664054.0, # this n_events is the gensumwt
    aux={'n_events': 9682904} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wqq_zll_powheg',
    id=22140255,
    is_data=False,
    processes=[procs.wz_wqq_zll],
    keys=['/WZto2L2Q_powheg', '/WZto2L2Q_powheg_ext1'],
    n_files=35,
    n_events=29890474.0, # this n_events is the gensumwt
    aux={'n_events': 29921926} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zqq_powheg',
    id=22140256,
    is_data=False,
    processes=[procs.wz_wlnu_zqq],
    keys=['/WZtoLNu2Q_powheg', '/WZtoLNu2Q_powheg_ext1'],
    n_files=62,
    n_events=60234952.0, # this n_events is the gensumwt
    aux={'n_events': 60260660} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zll_amcatnlo',
    id=22140257,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=['/WZto3LNu_amcatnloFXFX'],
    n_files=14,
    n_events=6504631.0, # this n_events is the gensumwt
    aux={'n_events': 10278601} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zqq_amcatnlo',
    id=22140258,
    is_data=False,
    processes=[procs.wz_wlnu_zqq],
    keys=['/WZtoLNu2Q_amcatnloFXFX'],
    n_files=11,
    n_events=4903875.0, # this n_events is the gensumwt
    aux={'n_events': 8556077} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz',
    id=22140259,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=3,
    n_events=4043040.0, # this n_events is the gensumwt
    aux={'n_events': 4043040} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zqq_zll_powheg',
    id=22140260,
    is_data=False,
    processes=[procs.zz_zqq_zll],
    keys=['/ZZto2L2Q_powheg', '/ZZto2L2Q_powheg_ext1'],
    n_files=107,
    n_events=99798639.0, # this n_events is the gensumwt
    aux={'n_events': 100417465} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zqq_zll_amcatnlo',
    id=22140261,
    is_data=False,
    processes=[procs.zz_zqq_zll],
    keys=['/ZZto2L2Q_amcatnloFXFX'],
    n_files=11,
    n_events=4631384.0, # this n_events is the gensumwt
    aux={'n_events': 7607188} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zll_znunu_powheg',
    id=22140262,
    is_data=False,
    processes=[procs.zz_zll_znunu],
    keys=['/ZZto2L2Nu_powheg', '/ZZto2L2Nu_powheg_ext1'],
    n_files=105,
    n_events=100090200.0, # this n_events is the gensumwt
    aux={'n_events': 100311926} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zll_zll_powheg',
    id=22140263,
    is_data=False,
    processes=[procs.zz_zll_zll],
    keys=['/ZZto4L_powheg', '/ZZto4L_powheg_ext1'],
    n_files=132,
    n_events=100584729.0, # this n_events is the gensumwt
    aux={'n_events': 101640249} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_znunu_zqq_powheg',
    id=22140264,
    is_data=False,
    processes=[procs.zz_znunu_zqq],
    keys=['/ZZto2Nu2Q_powheg', '/ZZto2Nu2Q_powheg_ext1'],
    n_files=14,
    n_events=20597604.0, # this n_events is the gensumwt
    aux={'n_events': 20630292} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='www',
    id=22140265,
    is_data=False,
    processes=[procs.www],
    keys=['/WWW_4F'],
    n_files=3,
    n_events=1345746.0, # this n_events is the gensumwt
    aux={'n_events': 1482480} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wwz',
    id=22140266,
    is_data=False,
    processes=[procs.wwz],
    keys=['/WWZ_4F'],
    n_files=10,
    n_events=5249916.0, # this n_events is the gensumwt
    aux={'n_events': 5771216} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wzz',
    id=22140267,
    is_data=False,
    processes=[procs.wzz],
    keys=['/WZZ'],
    n_files=10,
    n_events=5229208.0, # this n_events is the gensumwt
    aux={'n_events': 5751288} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zzz',
    id=22140268,
    is_data=False,
    processes=[procs.zzz],
    keys=['/ZZZ'],
    n_files=8,
    n_events=5063206.0, # this n_events is the gensumwt
    aux={'n_events': 5695440} # n_events in aux is the nEvents produced
)