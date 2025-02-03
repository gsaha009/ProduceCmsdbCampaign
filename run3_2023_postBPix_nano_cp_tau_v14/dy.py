# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14 import campaign_run3_2023_postBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='dy_lep_m10to50_madgraph',
    id=2314026,
    is_data=False,
    processes=[procs.dy_m10to50],
    keys=['/DYto2L_M_10to50_madgraphMLM'],
    n_files=64,
    n_events=150291788.0, # this n_events is the gensumwt
    aux={'n_events': 150291788} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m10to50_amcatnlo',
    id=2314027,
    is_data=False,
    processes=[procs.dy_m10to50],
    keys=['/DYto2L_M_10to50_amcatnloFXFX'],
    n_files=46,
    n_events=74917918.0, # this n_events is the gensumwt
    aux={'n_events': 100269476} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_madgraph',
    id=2314028,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYto2L_M_50_madgraphMLM'],
    n_files=68,
    n_events=69398459.0, # this n_events is the gensumwt
    aux={'n_events': 69398459} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_amcatnlo',
    id=2314029,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYto2L_M_50_amcatnloFXFX'],
    n_files=102,
    n_events=63684562.0, # this n_events is the gensumwt
    aux={'n_events': 95646832} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_0j_amcatnlo',
    id=23140210,
    is_data=False,
    processes=[procs.dy_m50toinf_0j],
    keys=['/DYto2L_M_50_0J_amcatnloFXFX'],
    n_files=87,
    n_events=76989083.0, # this n_events is the gensumwt
    aux={'n_events': 96541209} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_amcatnlo',
    id=23140211,
    is_data=False,
    processes=[procs.dy_m50toinf_1j],
    keys=['/DYto2L_M_50_1J_amcatnloFXFX'],
    n_files=113,
    n_events=42819115.0, # this n_events is the gensumwt
    aux={'n_events': 91332285} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_amcatnlo',
    id=23140212,
    is_data=False,
    processes=[procs.dy_m50toinf_2j],
    keys=['/DYto2L_M_50_2J_amcatnloFXFX'],
    n_files=119,
    n_events=23588533.0, # this n_events is the gensumwt
    aux={'n_events': 77408545} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_madgraph',
    id=23140213,
    is_data=False,
    processes=[procs.dy_m50toinf_1j],
    keys=['/DYto2L_M_50_1J_madgraphMLM'],
    n_files=15,
    n_events=13040044.0, # this n_events is the gensumwt
    aux={'n_events': 13040044} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_madgraph',
    id=23140214,
    is_data=False,
    processes=[procs.dy_m50toinf_2j],
    keys=['/DYto2L_M_50_2J_madgraphMLM'],
    n_files=20,
    n_events=14194783.0, # this n_events is the gensumwt
    aux={'n_events': 14194783} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_3j_madgraph',
    id=23140215,
    is_data=False,
    processes=[procs.dy_m50toinf_3j],
    keys=['/DYto2L_M_50_3J_madgraphMLM'],
    n_files=15,
    n_events=9139978.0, # this n_events is the gensumwt
    aux={'n_events': 9139978} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_4j_madgraph',
    id=23140216,
    is_data=False,
    processes=[procs.dy_m50toinf_4j],
    keys=['/DYto2L_M_50_4J_madgraphMLM'],
    n_files=7,
    n_events=3202454.0, # this n_events is the gensumwt
    aux={'n_events': 3202454} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt40to100_amcatnlo',
    id=23140217,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    keys=['/DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX'],
    n_files=67,
    n_events=25437167.0, # this n_events is the gensumwt
    aux={'n_events': 52938287} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt100to200_amcatnlo',
    id=23140218,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    keys=['/DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX'],
    n_files=32,
    n_events=10902093.0, # this n_events is the gensumwt
    aux={'n_events': 19384285} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt200to400_amcatnlo',
    id=23140219,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    keys=['/DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX'],
    n_files=5,
    n_events=1253554.0, # this n_events is the gensumwt
    aux={'n_events': 1985212} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt400to600_amcatnlo',
    id=23140220,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    keys=['/DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX'],
    n_files=2,
    n_events=322395.0, # this n_events is the gensumwt
    aux={'n_events': 459553} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt600toInf_amcatnlo',
    id=23140221,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    keys=['/DYto2L_M_50_PTLL_600_1J_amcatnloFXFX'],
    n_files=2,
    n_events=341571.0, # this n_events is the gensumwt
    aux={'n_events': 456439} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt40to100_amcatnlo',
    id=23140222,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    keys=['/DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX'],
    n_files=32,
    n_events=6204830.0, # this n_events is the gensumwt
    aux={'n_events': 20416556} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt100to200_amcatnlo',
    id=23140223,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    keys=['/DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX'],
    n_files=39,
    n_events=6426397.0, # this n_events is the gensumwt
    aux={'n_events': 19943443} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt200to400_amcatnlo',
    id=23140224,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    keys=['/DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX'],
    n_files=10,
    n_events=1277307.0, # this n_events is the gensumwt
    aux={'n_events': 3623077} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt400to600_amcatnlo',
    id=23140225,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    keys=['/DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX'],
    n_files=2,
    n_events=193196.0, # this n_events is the gensumwt
    aux={'n_events': 493730} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt600toInf_amcatnlo',
    id=23140226,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    keys=['/DYto2L_M_50_PTLL_600_2J_amcatnloFXFX'],
    n_files=2,
    n_events=201664.0, # this n_events is the gensumwt
    aux={'n_events': 477040} # n_events in aux is the nEvents produced
)