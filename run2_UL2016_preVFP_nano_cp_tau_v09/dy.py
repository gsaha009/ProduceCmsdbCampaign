# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016_HIPM

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_preVFP_nano_tau_v09 import campaign_run2_UL2016_preVFP_nano_tau_v09 as cpn




cpn.add_dataset(
    name='dy_lep_lo_m50',
    id=16090115,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYJetsToLL_M-50-madgraphMLM'],
    n_files=30,
    n_events=39816526.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m10to50',
    id=16090116,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYJetsToLL_M-10to50-madgraphMLM'],
    n_files=4,
    n_events=1141136.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_1j',
    id=16090117,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DY1JetsToLL_M-50-madgraphMLM'],
    n_files=12,
    n_events=15382205.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_2j',
    id=16090118,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DY2JetsToLL_M-50-madgraphMLM'],
    n_files=6,
    n_events=6824062.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_3j',
    id=16090119,
    is_data=False,
    processes=[procs.dy_lep_m50_3j],
    keys=['/DY3JetsToLL_M-50-madgraphMLM'],
    n_files=6,
    n_events=5894240.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_4j',
    id=16090120,
    is_data=False,
    processes=[procs.dy_lep_m50_4j],
    keys=['/DY4JetsToLL_M-50-madgraphMLM'],
    n_files=3,
    n_events=2818631.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_m50',
    id=16090121,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYJetsToLL_M-50-amcatnloFXFX'],
    n_files=31,
    n_events=25252938.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_m10to50',
    id=16090122,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYJetsToLL_M-10to50-amcatnloFXFX'],
    n_files=9,
    n_events=1676175.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_0j',
    id=16090123,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=['/DYJetsToLL_0J-amcatnloFXFX'],
    n_files=24,
    n_events=24708588.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_1j',
    id=16090124,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DYJetsToLL_1J-amcatnloFXFX'],
    n_files=35,
    n_events=20952336.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_2j',
    id=16090125,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DYJetsToLL_2J-amcatnloFXFX'],
    n_files=21,
    n_events=7373841.0,
    aux=None
)