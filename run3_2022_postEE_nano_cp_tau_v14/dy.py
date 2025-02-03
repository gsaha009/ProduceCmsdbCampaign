# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14 import campaign_run3_2022_postEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='dy_lep_m10to50_madgraph',
    id=22140212,
    is_data=False,
    processes=[procs.dy_m10to50],
    keys=['/DYto2L_M_10to50_madgraphMLM'],
    n_files=215,
    n_events=520125461.0, # this n_events is the gensumwt
    aux={'n_events': 520125461} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m10to50_amcatnlo',
    id=22140213,
    is_data=False,
    processes=[procs.dy_m10to50],
    keys=['/DYto2L_M_10to50_amcatnloFXFX'],
    n_files=98,
    n_events=168535477.0, # this n_events is the gensumwt
    aux={'n_events': 225587055} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_madgraph',
    id=22140214,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYto2L_M_50_madgraphMLM', '/DYto2L_M_50_madgraphMLM_ext1'],
    n_files=464,
    n_events=494841164.0, # this n_events is the gensumwt
    aux={'n_events': 494841164} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_amcatnlo',
    id=22140215,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYto2L_M_50_amcatnloFXFX'],
    n_files=215,
    n_events=143381876.0, # this n_events is the gensumwt
    aux={'n_events': 215402508} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_0j_amcatnlo',
    id=22140216,
    is_data=False,
    processes=[procs.dy_m50toinf_0j],
    keys=['/DYto2L_M_50_0J_amcatnloFXFX'],
    n_files=295,
    n_events=275262493.0, # this n_events is the gensumwt
    aux={'n_events': 345134359} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_amcatnlo',
    id=22140217,
    is_data=False,
    processes=[procs.dy_m50toinf_1j],
    keys=['/DYto2L_M_50_1J_amcatnloFXFX'],
    n_files=382,
    n_events=151393986.0, # this n_events is the gensumwt
    aux={'n_events': 322967488} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_amcatnlo',
    id=22140218,
    is_data=False,
    processes=[procs.dy_m50toinf_2j],
    keys=['/DYto2L_M_50_2J_amcatnloFXFX'],
    n_files=407,
    n_events=84617746.0, # this n_events is the gensumwt
    aux={'n_events': 277717852} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_madgraph',
    id=22140219,
    is_data=False,
    processes=[procs.dy_m50toinf_1j],
    keys=['/DYto2L_M_50_1J_madgraphMLM'],
    n_files=61,
    n_events=48939365.0, # this n_events is the gensumwt
    aux={'n_events': 48939365} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_madgraph',
    id=22140220,
    is_data=False,
    processes=[procs.dy_m50toinf_2j],
    keys=['/DYto2L_M_50_2J_madgraphMLM'],
    n_files=65,
    n_events=49862030.0, # this n_events is the gensumwt
    aux={'n_events': 49862030} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_3j_madgraph',
    id=22140221,
    is_data=False,
    processes=[procs.dy_m50toinf_3j],
    keys=['/DYto2L_M_50_3J_madgraphMLM'],
    n_files=44,
    n_events=28613025.0, # this n_events is the gensumwt
    aux={'n_events': 28613025} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_4j_madgraph',
    id=22140222,
    is_data=False,
    processes=[procs.dy_m50toinf_4j],
    keys=['/DYto2L_M_50_4J_madgraphMLM'],
    n_files=18,
    n_events=9376714.0, # this n_events is the gensumwt
    aux={'n_events': 9376714} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt40to100_amcatnlo',
    id=22140223,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    keys=['/DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX'],
    n_files=207,
    n_events=83342153.0, # this n_events is the gensumwt
    aux={'n_events': 173415327} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt100to200_amcatnlo',
    id=22140224,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    keys=['/DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX'],
    n_files=100,
    n_events=37150718.0, # this n_events is the gensumwt
    aux={'n_events': 66051870} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt200to400_amcatnlo',
    id=22140225,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    keys=['/DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX'],
    n_files=14,
    n_events=4216114.0, # this n_events is the gensumwt
    aux={'n_events': 6667050} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt400to600_amcatnlo',
    id=22140226,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    keys=['/DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX'],
    n_files=4,
    n_events=1212377.0, # this n_events is the gensumwt
    aux={'n_events': 1722633} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt600toInf_amcatnlo',
    id=22140227,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    keys=['/DYto2L_M_50_PTLL_600_1J_amcatnloFXFX'],
    n_files=5,
    n_events=1393865.0, # this n_events is the gensumwt
    aux={'n_events': 1861585} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt40to100_amcatnlo',
    id=22140228,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    keys=['/DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX'],
    n_files=106,
    n_events=22075566.0, # this n_events is the gensumwt
    aux={'n_events': 72553546} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt100to200_amcatnlo',
    id=22140229,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    keys=['/DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX'],
    n_files=126,
    n_events=22578364.0, # this n_events is the gensumwt
    aux={'n_events': 70064268} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt200to400_amcatnlo',
    id=22140230,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    keys=['/DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX'],
    n_files=31,
    n_events=4497493.0, # this n_events is the gensumwt
    aux={'n_events': 12755867} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt400to600_amcatnlo',
    id=22140231,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    keys=['/DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX'],
    n_files=5,
    n_events=680347.0, # this n_events is the gensumwt
    aux={'n_events': 1739647} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt600toInf_amcatnlo',
    id=22140232,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    keys=['/DYto2L_M_50_PTLL_600_2J_amcatnloFXFX'],
    n_files=5,
    n_events=710540.0, # this n_events is the gensumwt
    aux={'n_events': 1682240} # n_events in aux is the nEvents produced
)