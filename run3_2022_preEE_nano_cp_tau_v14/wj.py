# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v14 import campaign_run3_2022_preEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='wj_incl_madgraph',
    id=22140131,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM', '/WtoLNu_madgraphMLM_ext1'],
    n_files=95,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_madgraph',
    id=22140132,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_madgraphMLM'],
    n_files=8,
    n_events=11896625.0, # this n_events is the gensumwt
    aux={'n_events': 11896625} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_madgraph',
    id=22140133,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_madgraphMLM'],
    n_files=8,
    n_events=9283334.0, # this n_events is the gensumwt
    aux={'n_events': 9283334} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_3j_madgraph',
    id=22140134,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=['/WtoLNu_3J_madgraphMLM'],
    n_files=9,
    n_events=8221862.0, # this n_events is the gensumwt
    aux={'n_events': 8221862} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_4j_madgraph',
    id=22140135,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=['/WtoLNu_4J_madgraphMLM'],
    n_files=3,
    n_events=1463885.0, # this n_events is the gensumwt
    aux={'n_events': 1463885} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht40to100_madgraph',
    id=22140136,
    is_data=False,
    processes=[procs.w_lnu_ht40to100],
    keys=['/WtoLNu_MLNu_0to120_HT_40To100_madgraph'],
    n_files=110,
    n_events=147170771.0, # this n_events is the gensumwt
    aux={'n_events': 147170771} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht100to400_madgraph',
    id=22140137,
    is_data=False,
    processes=[procs.w_lnu_ht100to400],
    keys=['/WtoLNu_MLNu_0to120_HT_100To400_madgraph'],
    n_files=109,
    n_events=101108531.0, # this n_events is the gensumwt
    aux={'n_events': 101108531} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht400to800_madgraph',
    id=22140138,
    is_data=False,
    processes=[procs.w_lnu_ht400to800],
    keys=['/WtoLNu_MLNu_0to120_HT_400To800_madgraph'],
    n_files=28,
    n_events=13540857.0, # this n_events is the gensumwt
    aux={'n_events': 13540857} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht800to1500_madgraph',
    id=22140139,
    is_data=False,
    processes=[procs.w_lnu_ht800to1500],
    keys=['/WtoLNu_MLNu_0to120_HT_800To1500_madgraph'],
    n_files=4,
    n_events=1405138.0, # this n_events is the gensumwt
    aux={'n_events': 1405138} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht1500to2500_madgraph',
    id=22140140,
    is_data=False,
    processes=[procs.w_lnu_ht1500to2500],
    keys=['/WtoLNu_MLNu_0to120_HT_1500To2500_madgraph'],
    n_files=2,
    n_events=477881.0, # this n_events is the gensumwt
    aux={'n_events': 477881} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_incl_amcatnlo',
    id=22140141,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_amcatnloFXFX'],
    n_files=50,
    n_events=55638210.0, # this n_events is the gensumwt
    aux={'n_events': 81878020} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_0j_amcatnlo',
    id=22140142,
    is_data=False,
    processes=[procs.w_lnu_0j],
    keys=['/WtoLNu_0J_amcatnloFXFX'],
    n_files=92,
    n_events=152389684.0, # this n_events is the gensumwt
    aux={'n_events': 191268400} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_amcatnlo',
    id=22140143,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_amcatnloFXFX'],
    n_files=100,
    n_events=68415609.0, # this n_events is the gensumwt
    aux={'n_events': 141411157} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_amcatnlo',
    id=22140144,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_amcatnloFXFX'],
    n_files=102,
    n_events=31634488.0, # this n_events is the gensumwt
    aux={'n_events': 102668792} # n_events in aux is the nEvents produced
)