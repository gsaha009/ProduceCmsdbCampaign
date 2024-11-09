# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v14 import campaign_run3_2022_preEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='dy_lep_m10to50_madgraph',
    id=22140110,
    is_data=False,
    processes=[procs.dy_m10to50],
    keys=['/DYto2L_M_10to50_madgraphMLM'],
    n_files=67,
    n_events=160214290.0, # this n_events is the gensumwt
    aux={'n_events': 160214290} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m10to50_amcatnlo',
    id=22140111,
    is_data=False,
    processes=[procs.dy_m10to50],
    keys=['/DYto2L_M_10to50_amcatnloFXFX'],
    n_files=31,
    n_events=52363920.0, # this n_events is the gensumwt
    aux={'n_events': 70087610} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_madgraph',
    id=22140112,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYto2L_M_50_madgraphMLM', '/DYto2L_M_50_madgraphMLM_ext1'],
    n_files=139,
    n_events=144024010.0, # this n_events is the gensumwt
    aux={'n_events': 144024010} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_amcatnlo',
    id=22140113,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYto2L_M_50_amcatnloFXFX'],
    n_files=74,
    n_events=48541588.0, # this n_events is the gensumwt
    aux={'n_events': 72909628} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_0j_amcatnlo',
    id=22140114,
    is_data=False,
    processes=[procs.dy_m50toinf_0j],
    keys=['/DYto2L_M_50_0J_amcatnloFXFX'],
    n_files=91,
    n_events=77502776.0, # this n_events is the gensumwt
    aux={'n_events': 97176340} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_amcatnlo',
    id=22140115,
    is_data=False,
    processes=[procs.dy_m50toinf_1j],
    keys=['/DYto2L_M_50_1J_amcatnloFXFX'],
    n_files=120,
    n_events=46105807.0, # this n_events is the gensumwt
    aux={'n_events': 98369357} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_amcatnlo',
    id=22140116,
    is_data=False,
    processes=[procs.dy_m50toinf_2j],
    keys=['/DYto2L_M_50_2J_amcatnloFXFX'],
    n_files=112,
    n_events=23048154.0, # this n_events is the gensumwt
    aux={'n_events': 75615786} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_madgraph',
    id=22140117,
    is_data=False,
    processes=[procs.dy_m50toinf_1j],
    keys=['/DYto2L_M_50_1J_madgraphMLM'],
    n_files=17,
    n_events=14855860.0, # this n_events is the gensumwt
    aux={'n_events': 14855860} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_madgraph',
    id=22140118,
    is_data=False,
    processes=[procs.dy_m50toinf_2j],
    keys=['/DYto2L_M_50_2J_madgraphMLM'],
    n_files=20,
    n_events=14654880.0, # this n_events is the gensumwt
    aux={'n_events': 14654880} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_3j_madgraph',
    id=22140119,
    is_data=False,
    processes=[procs.dy_m50toinf_3j],
    keys=['/DYto2L_M_50_3J_madgraphMLM'],
    n_files=14,
    n_events=8672888.0, # this n_events is the gensumwt
    aux={'n_events': 8672888} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_4j_madgraph',
    id=22140120,
    is_data=False,
    processes=[procs.dy_m50toinf_4j],
    keys=['/DYto2L_M_50_4J_madgraphMLM'],
    n_files=7,
    n_events=3258128.0, # this n_events is the gensumwt
    aux={'n_events': 3258128} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt40to100_amcatnlo',
    id=22140121,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    keys=['/DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX'],
    n_files=61,
    n_events=24163544.0, # this n_events is the gensumwt
    aux={'n_events': 50272820} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt100to200_amcatnlo',
    id=22140122,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    keys=['/DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX'],
    n_files=29,
    n_events=10507166.0, # this n_events is the gensumwt
    aux={'n_events': 18682106} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt200to400_amcatnlo',
    id=22140123,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    keys=['/DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX'],
    n_files=5,
    n_events=1228951.0, # this n_events is the gensumwt
    aux={'n_events': 1939721} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt400to600_amcatnlo',
    id=22140124,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    keys=['/DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX'],
    n_files=2,
    n_events=353922.0, # this n_events is the gensumwt
    aux={'n_events': 503786} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt600toInf_amcatnlo',
    id=22140125,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    keys=['/DYto2L_M_50_PTLL_600_1J_amcatnloFXFX'],
    n_files=2,
    n_events=381270.0, # this n_events is the gensumwt
    aux={'n_events': 508646} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt40to100_amcatnlo',
    id=22140126,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    keys=['/DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX'],
    n_files=29,
    n_events=5875751.0, # this n_events is the gensumwt
    aux={'n_events': 19307377} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt100to200_amcatnlo',
    id=22140127,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    keys=['/DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX'],
    n_files=35,
    n_events=6166018.0, # this n_events is the gensumwt
    aux={'n_events': 19139796} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt200to400_amcatnlo',
    id=22140128,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    keys=['/DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX'],
    n_files=9,
    n_events=1285426.0, # this n_events is the gensumwt
    aux={'n_events': 3651560} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt400to600_amcatnlo',
    id=22140129,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    keys=['/DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX'],
    n_files=2,
    n_events=192545.0, # this n_events is the gensumwt
    aux={'n_events': 488707} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt600toInf_amcatnlo',
    id=22140130,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    keys=['/DYto2L_M_50_PTLL_600_2J_amcatnloFXFX'],
    n_files=2,
    n_events=200430.0, # this n_events is the gensumwt
    aux={'n_events': 474576} # n_events in aux is the nEvents produced
)