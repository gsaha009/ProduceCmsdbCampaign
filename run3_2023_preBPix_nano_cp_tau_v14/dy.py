# dy.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14 import campaign_run3_2023_preBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='dy_lep_m10to50_madgraph',
    id=2314016,
    is_data=False,
    processes=[procs.dy_m10to50],
    keys=['/DYto2L_M_10to50_madgraphMLM'],
    n_files=130,
    n_events=306998077.0, # this n_events is the gensumwt
    aux={'n_events': 306998077} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m10to50_amcatnlo',
    id=2314017,
    is_data=False,
    processes=[procs.dy_m10to50],
    keys=['/DYto2L_M_10to50_amcatnloFXFX'],
    n_files=92,
    n_events=149951901.0, # this n_events is the gensumwt
    aux={'n_events': 200673913} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_madgraph',
    id=2314018,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYto2L_M_50_madgraphMLM'],
    n_files=128,
    n_events=130559088.0, # this n_events is the gensumwt
    aux={'n_events': 130559088} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_amcatnlo',
    id=2314019,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=['/DYto2L_M_50_amcatnloFXFX'],
    n_files=165,
    n_events=103978251.0, # this n_events is the gensumwt
    aux={'n_events': 156185509} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_0j_amcatnlo',
    id=23140110,
    is_data=False,
    processes=[procs.dy_m50toinf_0j],
    keys=['/DYto2L_M_50_0J_amcatnloFXFX'],
    n_files=175,
    n_events=155735461.0, # this n_events is the gensumwt
    aux={'n_events': 195264699} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_amcatnlo',
    id=23140111,
    is_data=False,
    processes=[procs.dy_m50toinf_1j],
    keys=['/DYto2L_M_50_1J_amcatnloFXFX'],
    n_files=239,
    n_events=90103222.0, # this n_events is the gensumwt
    aux={'n_events': 192250456} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_amcatnlo',
    id=23140112,
    is_data=False,
    processes=[procs.dy_m50toinf_2j],
    keys=['/DYto2L_M_50_2J_amcatnloFXFX'],
    n_files=237,
    n_events=47134234.0, # this n_events is the gensumwt
    aux={'n_events': 154635428} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_madgraph',
    id=23140113,
    is_data=False,
    processes=[procs.dy_m50toinf_1j],
    keys=['/DYto2L_M_50_1J_madgraphMLM'],
    n_files=34,
    n_events=29110511.0, # this n_events is the gensumwt
    aux={'n_events': 29110511} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_madgraph',
    id=23140114,
    is_data=False,
    processes=[procs.dy_m50toinf_2j],
    keys=['/DYto2L_M_50_2J_madgraphMLM'],
    n_files=40,
    n_events=29201477.0, # this n_events is the gensumwt
    aux={'n_events': 29201477} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_3j_madgraph',
    id=23140115,
    is_data=False,
    processes=[procs.dy_m50toinf_3j],
    keys=['/DYto2L_M_50_3J_madgraphMLM'],
    n_files=28,
    n_events=17219638.0, # this n_events is the gensumwt
    aux={'n_events': 17219638} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_4j_madgraph',
    id=23140116,
    is_data=False,
    processes=[procs.dy_m50toinf_4j],
    keys=['/DYto2L_M_50_4J_madgraphMLM'],
    n_files=11,
    n_events=5620697.0, # this n_events is the gensumwt
    aux={'n_events': 5620697} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt40to100_amcatnlo',
    id=23140117,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    keys=['/DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX'],
    n_files=128,
    n_events=48515712.0, # this n_events is the gensumwt
    aux={'n_events': 100952990} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt100to200_amcatnlo',
    id=23140118,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    keys=['/DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX'],
    n_files=64,
    n_events=22004335.0, # this n_events is the gensumwt
    aux={'n_events': 39130201} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt200to400_amcatnlo',
    id=23140119,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    keys=['/DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX'],
    n_files=9,
    n_events=2353269.0, # this n_events is the gensumwt
    aux={'n_events': 3722389} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt400to600_amcatnlo',
    id=23140120,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    keys=['/DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX'],
    n_files=3,
    n_events=696227.0, # this n_events is the gensumwt
    aux={'n_events': 989929} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_1j_pt600toInf_amcatnlo',
    id=23140121,
    is_data=False,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    keys=['/DYto2L_M_50_PTLL_600_1J_amcatnloFXFX'],
    n_files=3,
    n_events=730095.0, # this n_events is the gensumwt
    aux={'n_events': 975787} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt40to100_amcatnlo',
    id=23140122,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    keys=['/DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX'],
    n_files=63,
    n_events=12425208.0, # this n_events is the gensumwt
    aux={'n_events': 40869178} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt100to200_amcatnlo',
    id=23140123,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    keys=['/DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX'],
    n_files=77,
    n_events=12861657.0, # this n_events is the gensumwt
    aux={'n_events': 39906573} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt200to400_amcatnlo',
    id=23140124,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    keys=['/DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX'],
    n_files=21,
    n_events=2855089.0, # this n_events is the gensumwt
    aux={'n_events': 8100581} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt400to600_amcatnlo',
    id=23140125,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    keys=['/DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX'],
    n_files=3,
    n_events=375799.0, # this n_events is the gensumwt
    aux={'n_events': 960577} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='dy_lep_m50_2j_pt600toInf_amcatnlo',
    id=23140126,
    is_data=False,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    keys=['/DYto2L_M_50_PTLL_600_2J_amcatnloFXFX'],
    n_files=3,
    n_events=422003.0, # this n_events is the gensumwt
    aux={'n_events': 1001323} # n_events in aux is the nEvents produced
)