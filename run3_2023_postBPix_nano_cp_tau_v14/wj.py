# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14 import campaign_run3_2023_postBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='wj_incl_madgraph',
    id=23140227,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM'],
    n_files=51,
    n_events=94639090.0, # this n_events is the gensumwt
    aux={'n_events': 94639090} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_madgraph',
    id=23140228,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_madgraphMLM'],
    n_files=8,
    n_events=11369658.0, # this n_events is the gensumwt
    aux={'n_events': 11369658} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_madgraph',
    id=23140229,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_madgraphMLM'],
    n_files=9,
    n_events=9459992.0, # this n_events is the gensumwt
    aux={'n_events': 9459992} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_3j_madgraph',
    id=23140230,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=['/WtoLNu_3J_madgraphMLM'],
    n_files=9,
    n_events=7718351.0, # this n_events is the gensumwt
    aux={'n_events': 7718351} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_4j_madgraph',
    id=23140231,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=['/WtoLNu_4J_madgraphMLM'],
    n_files=3,
    n_events=1436944.0, # this n_events is the gensumwt
    aux={'n_events': 1436944} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht40to100_madgraph',
    id=23140232,
    is_data=False,
    processes=[procs.w_lnu_ht40to100],
    keys=['/WtoLNu_MLNu_0to120_HT_40To100_madgraph'],
    n_files=104,
    n_events=134935396.0, # this n_events is the gensumwt
    aux={'n_events': 134935396} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht100to400_madgraph',
    id=23140233,
    is_data=False,
    processes=[procs.w_lnu_ht100to400],
    keys=['/WtoLNu_MLNu_0to120_HT_100To400_madgraph'],
    n_files=107,
    n_events=94843477.0, # this n_events is the gensumwt
    aux={'n_events': 94843477} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht400to800_madgraph',
    id=23140234,
    is_data=False,
    processes=[procs.w_lnu_ht400to800],
    keys=['/WtoLNu_MLNu_0to120_HT_400To800_madgraph'],
    n_files=28,
    n_events=13132517.0, # this n_events is the gensumwt
    aux={'n_events': 13132517} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht800to1500_madgraph',
    id=23140235,
    is_data=False,
    processes=[procs.w_lnu_ht800to1500],
    keys=['/WtoLNu_MLNu_0to120_HT_800To1500_madgraph'],
    n_files=4,
    n_events=1434836.0, # this n_events is the gensumwt
    aux={'n_events': 1434836} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_ht1500to2500_madgraph',
    id=23140236,
    is_data=False,
    processes=[procs.w_lnu_ht1500to2500],
    keys=['/WtoLNu_MLNu_0to120_HT_1500To2500_madgraph'],
    n_files=2,
    n_events=522080.0, # this n_events is the gensumwt
    aux={'n_events': 522080} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_incl_amcatnlo',
    id=23140237,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_amcatnloFXFX'],
    n_files=59,
    n_events=64991689.0, # this n_events is the gensumwt
    aux={'n_events': 95603855} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_0j_amcatnlo',
    id=23140238,
    is_data=False,
    processes=[procs.w_lnu_0j],
    keys=['/WtoLNu_0J_amcatnloFXFX'],
    n_files=99,
    n_events=158538980.0, # this n_events is the gensumwt
    aux={'n_events': 198993882} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_amcatnlo',
    id=23140239,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_amcatnloFXFX'],
    n_files=111,
    n_events=72358930.0, # this n_events is the gensumwt
    aux={'n_events': 149508424} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_amcatnlo',
    id=23140240,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_amcatnloFXFX'],
    n_files=102,
    n_events=30711458.0, # this n_events is the gensumwt
    aux={'n_events': 99673760} # n_events in aux is the nEvents produced
)