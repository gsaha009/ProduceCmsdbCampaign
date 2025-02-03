# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14 import campaign_run3_2023_preBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='st_tchannel_t',
    id=23140162,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t_channel_top_4f_InclusiveDecays'],
    n_files=6,
    n_events=5437414.0, # this n_events is the gensumwt
    aux={'n_events': 5908000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=23140163,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t_channel_antitop_4f_InclusiveDecays'],
    n_files=3,
    n_events=2662016.0, # this n_events is the gensumwt
    aux={'n_events': 2878000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_schannel_t',
    id=23140164,
    is_data=False,
    processes=[procs.st_schannel_t],
    keys=['/ST_s_channel_top_4f_leptonDecays'],
    n_files=4,
    n_events=1591938.0, # this n_events is the gensumwt
    aux={'n_events': 2588000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_schannel_tbar',
    id=23140165,
    is_data=False,
    processes=[procs.st_schannel_tbar],
    keys=['/ST_s_channel_antitop_4f_leptonDecays'],
    n_files=2,
    n_events=985718.0, # this n_events is the gensumwt
    aux={'n_events': 1600000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_t_sl',
    id=23140166,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_LNu2Q'],
    n_files=18,
    n_events=9649924.0, # this n_events is the gensumwt
    aux={'n_events': 9650268} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_t_dl',
    id=23140167,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_2L2Nu'],
    n_files=10,
    n_events=4984812.0, # this n_events is the gensumwt
    aux={'n_events': 4985000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_t_fh',
    id=23140168,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_4Q'],
    n_files=9,
    n_events=7918700.0, # this n_events is the gensumwt
    aux={'n_events': 7919000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_tb_sl',
    id=23140169,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_LNu2Q'],
    n_files=17,
    n_events=9519035.0, # this n_events is the gensumwt
    aux={'n_events': 9519385} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_tb_dl',
    id=23140170,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_2L2Nu'],
    n_files=10,
    n_events=4906798.0, # this n_events is the gensumwt
    aux={'n_events': 4907000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_tb_fh',
    id=23140171,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_4Q'],
    n_files=9,
    n_events=7969722.0, # this n_events is the gensumwt
    aux={'n_events': 7970000} # n_events in aux is the nEvents produced
)