# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_cp_tau_v09 import campaign_run2_UL2017_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='dy_lep_lo_m50',
    id=17090115,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYJetsToLL_M-50-madgraphMLM', '/DYJetsToLL_M-50-madgraphMLM_ext1'],
    n_files=69,
    n_events=89759093.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m10to50',
    id=17090116,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYJetsToLL_M-10to50-madgraphMLM'],
    n_files=11,
    n_events=3310259.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_1j',
    id=17090117,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DY1JetsToLL_M-50-madgraphMLM'],
    n_files=26,
    n_events=33095446.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_2j',
    id=17090118,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DY2JetsToLL_M-50-madgraphMLM'],
    n_files=13,
    n_events=15068869.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_3j',
    id=17090119,
    is_data=False,
    processes=[procs.dy_lep_m50_3j],
    keys=['/DY3JetsToLL_M-50-madgraphMLM'],
    n_files=11,
    n_events=11913560.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_4j',
    id=17090120,
    is_data=False,
    processes=[procs.dy_lep_m50_4j],
    keys=['/DY4JetsToLL_M-50-madgraphMLM'],
    n_files=7,
    n_events=7042058.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_m50',
    id=17090121,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYJetsToLL_M-50-amcatnloFXFX'],
    n_files=71,
    n_events=56991364.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_m10to50',
    id=17090122,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYJetsToLL_M-10to50-amcatnloFXFX'],
    n_files=17,
    n_events=3543995.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_0j',
    id=17090123,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=['/DYJetsToLL_0J-amcatnloFXFX'],
    n_files=25,
    n_events=25581936.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_1j',
    id=17090124,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DYJetsToLL_1J-amcatnloFXFX'],
    n_files=35,
    n_events=20757614.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_2j',
    id=17090125,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DYJetsToLL_2J-amcatnloFXFX'],
    n_files=24,
    n_events=8324984.0,
    aux=None
)