# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2018_nano_tau_v09 import campaign_run2_UL2018_nano_tau_v09 as cpn




cpn.add_dataset(
    name='ww_incl',
    id=18090132,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=4,
    n_events=3869972.0,
    aux=None
)

cpn.add_dataset(
    name='ww_lnulnu',
    id=18090133,
    is_data=False,
    processes=[procs.ww_lnulnu],
    keys=['/WWTo2L2Nu'],
    n_files=5,
    n_events=5468722.0,
    aux=None
)

cpn.add_dataset(
    name='ww_lnuqq',
    id=18090134,
    is_data=False,
    processes=[procs.ww_lnuqq],
    keys=['/WWTo1L1Nu2Q'],
    n_files=16,
    n_events=7653289.0,
    aux=None
)

cpn.add_dataset(
    name='ww_qqqq',
    id=18090135,
    is_data=False,
    processes=[procs.ww_qqqq],
    keys=['/WWTo4Q'],
    n_files=11,
    n_events=2970855.0,
    aux=None
)

cpn.add_dataset(
    name='wz_incl',
    id=18090136,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=2,
    n_events=1768369.0,
    aux=None
)

cpn.add_dataset(
    name='wz_qqll',
    id=18090137,
    is_data=False,
    processes=[procs.wz_qqll_m4],
    keys=['/WZTo2Q2L'],
    n_files=14,
    n_events=7983585.0,
    aux=None
)

cpn.add_dataset(
    name='wz_lllnu',
    id=18090138,
    is_data=False,
    processes=[procs.wz_lllnu_m4],
    keys=['/WZTo3LNu'],
    n_files=5,
    n_events=2940955.0,
    aux=None
)

cpn.add_dataset(
    name='wz_lnuqq',
    id=18090139,
    is_data=False,
    processes=[procs.wz_lnuqq],
    keys=['/WZTo1L1Nu2Q'],
    n_files=3,
    n_events=1461494.0,
    aux=None
)

cpn.add_dataset(
    name='zz_incl',
    id=18090140,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=770416.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llll',
    id=18090141,
    is_data=False,
    processes=[procs.zz_llll_m4],
    keys=['/ZZTo4L'],
    n_files=41,
    n_events=43315632.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llnunu',
    id=18090142,
    is_data=False,
    processes=[procs.zz_llnunu_m4],
    keys=['/ZZTo2L2Nu'],
    n_files=23,
    n_events=24514879.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llqq',
    id=18090143,
    is_data=False,
    processes=[procs.zz_qqll_m4],
    keys=['/ZZTo2Q2L'],
    n_files=15,
    n_events=9169061.0,
    aux=None
)

cpn.add_dataset(
    name='zz_qqqq',
    id=18090144,
    is_data=False,
    processes=[procs.zz_qqqq],
    keys=['/ZZTo4Q'],
    n_files=1,
    n_events=146331.0,
    aux=None
)

cpn.add_dataset(
    name='zz_qqnunu',
    id=18090145,
    is_data=False,
    processes=[procs.zz_qqnunu],
    keys=['/ZZTo2Q2Nu'],
    n_files=6,
    n_events=1478157.0,
    aux=None
)