# vv.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016_HIPM

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_preVFP_nano_tau_v09 import campaign_run2_UL2016_preVFP_nano_tau_v09 as cpn




cpn.add_dataset(
    name='ww_incl',
    id=16090138,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=4,
    n_events=3776690.0,
    aux=None
)

cpn.add_dataset(
    name='ww_lnulnu',
    id=16090139,
    is_data=False,
    processes=[procs.ww_lnulnu],
    keys=['/WWTo2L2Nu'],
    n_files=2,
    n_events=1583155.0,
    aux=None
)

cpn.add_dataset(
    name='ww_lnuqq',
    id=16090140,
    is_data=False,
    processes=[procs.ww_lnuqq],
    keys=['/WWTo1L1Nu2Q'],
    n_files=8,
    n_events=3651801.0,
    aux=None
)

cpn.add_dataset(
    name='ww_qqqq',
    id=16090141,
    is_data=False,
    processes=[procs.ww_qqqq],
    keys=['/WWTo4Q'],
    n_files=6,
    n_events=1488134.0,
    aux=None
)

cpn.add_dataset(
    name='wz_incl',
    id=16090142,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=2,
    n_events=1709664.0,
    aux=None
)

cpn.add_dataset(
    name='wz_qqll',
    id=16090143,
    is_data=False,
    processes=[procs.wz_qqll_m4],
    keys=['/WZTo2Q2L'],
    n_files=8,
    n_events=4278966.0,
    aux=None
)

cpn.add_dataset(
    name='wz_lllnu',
    id=16090144,
    is_data=False,
    processes=[procs.wz_lllnu_m4],
    keys=['/WZTo3LNu'],
    n_files=5,
    n_events=2793736.0,
    aux=None
)

cpn.add_dataset(
    name='wz_lnuqq',
    id=16090145,
    is_data=False,
    processes=[procs.wz_lnuqq],
    keys=['/WZTo1L1Nu2Q'],
    n_files=2,
    n_events=702691.0,
    aux=None
)

cpn.add_dataset(
    name='zz_incl',
    id=16090146,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=273200.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llll',
    id=16090147,
    is_data=False,
    processes=[procs.zz_llll_m4],
    keys=['/ZZTo4L'],
    n_files=20,
    n_events=21062414.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llnunu',
    id=16090148,
    is_data=False,
    processes=[procs.zz_llnunu_m4],
    keys=['/ZZTo2L2Nu'],
    n_files=7,
    n_events=7019901.0,
    aux=None
)

cpn.add_dataset(
    name='zz_llqq',
    id=16090149,
    is_data=False,
    processes=[procs.zz_qqll_m4],
    keys=['/ZZTo2Q2L'],
    n_files=8,
    n_events=4894991.0,
    aux=None
)

cpn.add_dataset(
    name='zz_qqqq',
    id=16090150,
    is_data=False,
    processes=[procs.zz_qqqq],
    keys=['/ZZTo4Q'],
    n_files=1,
    n_events=71852.0,
    aux=None
)

cpn.add_dataset(
    name='zz_qqnunu',
    id=16090151,
    is_data=False,
    processes=[procs.zz_qqnunu],
    keys=['/ZZTo2Q2Nu'],
    n_files=1,
    n_events=163593.0,
    aux=None
)