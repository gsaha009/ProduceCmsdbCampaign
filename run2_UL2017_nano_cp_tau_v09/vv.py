# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_cp_tau_v09 import campaign_run2_UL2017_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='ww_incl',
    id=17090135,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=4,
    n_events=3910456.0,
    aux=None
)

cpn.add_dataset(
    name='ww_lnulnu',
    id=17090136,
    is_data=False,
    processes=[procs.ww_lnulnu],
    keys=['/WWTo2L2Nu'],
    n_files=4,
    n_events=3911415.0,
    aux=None
)

cpn.add_dataset(
    name='ww_lnuqq',
    id=17090137,
    is_data=False,
    processes=[procs.ww_lnuqq],
    keys=['/WWTo1L1Nu2Q'],
    n_files=16,
    n_events=7686648.0,
    aux=None
)

cpn.add_dataset(
    name='ww_qqqq',
    id=17090138,
    is_data=False,
    processes=[procs.ww_qqqq],
    keys=['/WWTo4Q'],
    n_files=11,
    n_events=3002556.0,
    aux=None
)

cpn.add_dataset(
    name='wz_incl',
    id=17090139,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=2,
    n_events=1780564.0,
    aux=None
)

cpn.add_dataset(
    name='wz_qqll',
    id=17090140,
    is_data=False,
    processes=[procs.wz_qqll_m4],
    keys=['/WZTo2Q2L'],
    n_files=14,
    n_events=8174134.0,
    aux=None
)

cpn.add_dataset(
    name='wz_lllnu',
    id=17090141,
    is_data=False,
    processes=[procs.wz_lllnu_m4],
    keys=['/WZTo3LNu'],
    n_files=5,
    n_events=3119574.0,
    aux=None
)

cpn.add_dataset(
    name='wz_lnuqq',
    id=17090142,
    is_data=False,
    processes=[procs.wz_lnuqq],
    keys=['/WZTo1L1Nu2Q'],
    n_files=3,
    n_events=1467474.0,
    aux=None
)

cpn.add_dataset(
    name='zz_incl',
    id=17090143,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=598919.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llll',
    id=17090144,
    is_data=False,
    processes=[procs.zz_llll_m4],
    keys=['/ZZTo4L'],
    n_files=42,
    n_events=43557896.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llnunu',
    id=17090145,
    is_data=False,
    processes=[procs.zz_llnunu_m4],
    keys=['/ZZTo2L2Nu'],
    n_files=17,
    n_events=17693211.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llqq',
    id=17090146,
    is_data=False,
    processes=[procs.zz_qqll_m4],
    keys=['/ZZTo2Q2L'],
    n_files=15,
    n_events=9275748.0,
    aux=None
)

cpn.add_dataset(
    name='zz_qqqq',
    id=17090147,
    is_data=False,
    processes=[procs.zz_qqqq],
    keys=['/ZZTo4Q'],
    n_files=1,
    n_events=148007.0,
    aux=None
)

cpn.add_dataset(
    name='zz_qqnunu',
    id=17090148,
    is_data=False,
    processes=[procs.zz_qqnunu],
    keys=['/ZZTo2Q2Nu'],
    n_files=2,
    n_events=350260.0,
    aux=None
)