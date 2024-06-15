# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_postVFP_nano_tau_v09 import campaign_run2_UL2016_postVFP_nano_tau_v09 as cpn




cpn.add_dataset(
    name='ww_incl',
    id=16090232,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=3,
    n_events=3668765.0,
    aux=None
)

cpn.add_dataset(
    name='ww_lnulnu',
    id=16090233,
    is_data=False,
    processes=[procs.ww_lnulnu],
    keys=['/WWTo2L2Nu'],
    n_files=2,
    n_events=1526449.0,
    aux=None
)

cpn.add_dataset(
    name='ww_lnuqq',
    id=16090234,
    is_data=False,
    processes=[procs.ww_lnuqq],
    keys=['/WWTo1L1Nu2Q'],
    n_files=8,
    n_events=3558831.0,
    aux=None
)

cpn.add_dataset(
    name='ww_qqqq',
    id=16090235,
    is_data=False,
    processes=[procs.ww_qqqq],
    keys=['/WWTo4Q'],
    n_files=6,
    n_events=1389773.0,
    aux=None
)

cpn.add_dataset(
    name='wz_incl',
    id=16090236,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=2,
    n_events=1587965.0,
    aux=None
)

cpn.add_dataset(
    name='wz_qqll',
    id=16090237,
    is_data=False,
    processes=[procs.wz_qqll_m4],
    keys=['/WZTo2Q2L'],
    n_files=7,
    n_events=3675784.0,
    aux=None
)

cpn.add_dataset(
    name='wz_lllnu',
    id=16090238,
    is_data=False,
    processes=[procs.wz_lllnu_m4],
    keys=['/WZTo3LNu'],
    n_files=5,
    n_events=3033347.0,
    aux=None
)

cpn.add_dataset(
    name='wz_lnuqq',
    id=16090239,
    is_data=False,
    processes=[procs.wz_lnuqq],
    keys=['/WZTo1L1Nu2Q'],
    n_files=2,
    n_events=684957.0,
    aux=None
)

cpn.add_dataset(
    name='zz_incl',
    id=16090240,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=239286.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llll',
    id=16090241,
    is_data=False,
    processes=[procs.zz_llll_m4],
    keys=['/ZZTo4L'],
    n_files=21,
    n_events=22187918.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llnunu',
    id=16090242,
    is_data=False,
    processes=[procs.zz_llnunu_m4],
    keys=['/ZZTo2L2Nu'],
    n_files=7,
    n_events=6652986.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llqq',
    id=16090243,
    is_data=False,
    processes=[procs.zz_qqll_m4],
    keys=['/ZZTo2Q2L'],
    n_files=7,
    n_events=4174474.0,
    aux=None
)

cpn.add_dataset(
    name='zz_qqqq',
    id=16090244,
    is_data=False,
    processes=[procs.zz_qqqq],
    keys=['/ZZTo4Q'],
    n_files=1,
    n_events=68939.0,
    aux=None
)

cpn.add_dataset(
    name='zz_qqnunu',
    id=16090245,
    is_data=False,
    processes=[procs.zz_qqnunu],
    keys=['/ZZTo2Q2Nu'],
    n_files=1,
    n_events=153751.0,
    aux=None
)