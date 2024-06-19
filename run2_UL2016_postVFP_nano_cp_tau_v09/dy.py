# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_postVFP_nano_cp_tau_v09 import campaign_run2_UL2016_postVFP_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='dy_lep_lo_m50',
    id=1609029,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYJetsToLL_M-50-madgraphMLM'],
    n_files=26,
    n_events=34529675.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m10to50',
    id=16090210,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYJetsToLL_M-10to50-madgraphMLM'],
    n_files=4,
    n_events=1035962.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_1j',
    id=16090211,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DY1JetsToLL_M-50-madgraphMLM'],
    n_files=12,
    n_events=15250208.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_2j',
    id=16090212,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DY2JetsToLL_M-50-madgraphMLM'],
    n_files=7,
    n_events=7837961.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_3j',
    id=16090213,
    is_data=False,
    processes=[procs.dy_lep_m50_3j],
    keys=['/DY3JetsToLL_M-50-madgraphMLM'],
    n_files=5,
    n_events=5473160.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_lo_m50_4j',
    id=16090214,
    is_data=False,
    processes=[procs.dy_lep_m50_4j],
    keys=['/DY4JetsToLL_M-50-madgraphMLM'],
    n_files=3,
    n_events=2687941.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_m50',
    id=16090215,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=['/DYJetsToLL_M-50-amcatnloFXFX'],
    n_files=25,
    n_events=20588425.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_m10to50',
    id=16090216,
    is_data=False,
    processes=[procs.dy_lep_m10to50],
    keys=['/DYJetsToLL_M-10to50-amcatnloFXFX'],
    n_files=9,
    n_events=1645781.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_0j',
    id=16090217,
    is_data=False,
    processes=[procs.dy_lep_m50_0j],
    keys=['/DYJetsToLL_0J-amcatnloFXFX'],
    n_files=23,
    n_events=23797082.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_1j',
    id=16090218,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=['/DYJetsToLL_1J-amcatnloFXFX'],
    n_files=32,
    n_events=19529939.0,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_nlo_2j',
    id=16090219,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=['/DYJetsToLL_2J-amcatnloFXFX'],
    n_files=20,
    n_events=7188583.0,
    aux=None
)