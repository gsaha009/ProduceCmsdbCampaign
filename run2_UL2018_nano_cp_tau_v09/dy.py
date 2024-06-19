# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09 import campaign_run2_UL2018_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='dy_lep_lo_m50',
    id=18090112,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYJetsToLL_M-50-madgraphMLM', '/DYJetsToLL_M-50-madgraphMLM_ext1'],
    n_files=65,
    n_events=86005241.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m10to50',
    id=18090113,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYJetsToLL_M-10to50-madgraphMLM'],
    n_files=16,
    n_events=4673892.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_1j',
    id=18090114,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DY1JetsToLL_M-50-madgraphMLM'],
    n_files=23,
    n_events=30090188.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_2j',
    id=18090115,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DY2JetsToLL_M-50-madgraphMLM'],
    n_files=13,
    n_events=15217673.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_3j',
    id=18090116,
    is_data=False,
    processes=[procs.dy_lep_m50_3j],
    keys=['/DY3JetsToLL_M-50-madgraphMLM'],
    n_files=11,
    n_events=12036413.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_4j',
    id=18090117,
    is_data=False,
    processes=[procs.dy_lep_m50_4j],
    keys=['/DY4JetsToLL_M-50-madgraphMLM'],
    n_files=6,
    n_events=5503099.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_m50',
    id=18090118,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYJetsToLL_M-50-amcatnloFXFX'],
    n_files=70,
    n_events=56769592.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_m10to50',
    id=18090119,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYJetsToLL_M-10to50-amcatnloFXFX'],
    n_files=17,
    n_events=3564672.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_0j',
    id=18090120,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=['/DYJetsToLL_0J-amcatnloFXFX'],
    n_files=27,
    n_events=27988906.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_1j',
    id=18090121,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DYJetsToLL_1J-amcatnloFXFX'],
    n_files=38,
    n_events=22598935.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_2j',
    id=18090122,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DYJetsToLL_2J-amcatnloFXFX'],
    n_files=22,
    n_events=7879288.0,
    aux=None
)