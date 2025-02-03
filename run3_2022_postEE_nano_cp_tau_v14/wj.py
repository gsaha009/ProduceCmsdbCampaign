# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14 import campaign_run3_2022_postEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='wj_incl_madgraph',
    id=22140233,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM', '/WtoLNu_madgraphMLM_ext1'],
    n_files=344,
    n_events=683448011.0, # this n_events is the gensumwt
    aux={'n_events': 683448011} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_madgraph',
    id=22140234,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_madgraphMLM'],
    n_files=25,
    n_events=42695566.0, # this n_events is the gensumwt
    aux={'n_events': 42695566} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_madgraph',
    id=22140235,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_madgraphMLM'],
    n_files=29,
    n_events=36349344.0, # this n_events is the gensumwt
    aux={'n_events': 36349344} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_3j_madgraph',
    id=22140236,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=['/WtoLNu_3J_madgraphMLM'],
    n_files=28,
    n_events=27828446.0, # this n_events is the gensumwt
    aux={'n_events': 27828446} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_4j_madgraph',
    id=22140237,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=['/WtoLNu_4J_madgraphMLM'],
    n_files=7,
    n_events=4906634.0, # this n_events is the gensumwt
    aux={'n_events': 4906634} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht40to100_madgraph',
    id=22140238,
    is_data=False,
    processes=[procs.w_lnu_ht40to100],
    keys=['/WtoLNu_MLNu_0to120_HT_40To100_madgraph'],
    n_files=336,
    n_events=463219744.0, # this n_events is the gensumwt
    aux={'n_events': 463219744} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht100to400_madgraph',
    id=22140239,
    is_data=False,
    processes=[procs.w_lnu_ht100to400],
    keys=['/WtoLNu_MLNu_0to120_HT_100To400_madgraph'],
    n_files=395,
    n_events=371652113.0, # this n_events is the gensumwt
    aux={'n_events': 371652113} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht400to800_madgraph',
    id=22140240,
    is_data=False,
    processes=[procs.w_lnu_ht400to800],
    keys=['/WtoLNu_MLNu_0to120_HT_400To800_madgraph'],
    n_files=99,
    n_events=48339233.0, # this n_events is the gensumwt
    aux={'n_events': 48339233} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht800to1500_madgraph',
    id=22140241,
    is_data=False,
    processes=[procs.w_lnu_ht800to1500],
    keys=['/WtoLNu_MLNu_0to120_HT_800To1500_madgraph'],
    n_files=14,
    n_events=5234836.0, # this n_events is the gensumwt
    aux={'n_events': 5234836} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht1500to2500_madgraph',
    id=22140242,
    is_data=False,
    processes=[procs.w_lnu_ht1500to2500],
    keys=['/WtoLNu_MLNu_0to120_HT_1500To2500_madgraph'],
    n_files=5,
    n_events=1711928.0, # this n_events is the gensumwt
    aux={'n_events': 1711928} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_incl_amcatnlo',
    id=22140243,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_amcatnloFXFX'],
    n_files=162,
    n_events=195475598.0, # this n_events is the gensumwt
    aux={'n_events': 287618486} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_0j_amcatnlo',
    id=22140244,
    is_data=False,
    processes=[procs.w_lnu_0j],
    keys=['/WtoLNu_0J_amcatnloFXFX'],
    n_files=320,
    n_events=543560166.0, # this n_events is the gensumwt
    aux={'n_events': 682250482} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_amcatnlo',
    id=22140245,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_amcatnloFXFX'],
    n_files=363,
    n_events=252954566.0, # this n_events is the gensumwt
    aux={'n_events': 522743298} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_amcatnlo',
    id=22140246,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_amcatnloFXFX'],
    n_files=337,
    n_events=106873894.0, # this n_events is the gensumwt
    aux={'n_events': 346779790} # n_events in aux is the nEvents produced
)