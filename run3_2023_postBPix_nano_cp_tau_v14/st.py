# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14 import campaign_run3_2023_postBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='st_tchannel_t',
    id=23140262,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t_channel_top_4f_InclusiveDecays'],
    n_files=3,
    n_events=2719204.0, # this n_events is the gensumwt
    aux={'n_events': 2954000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=23140263,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t_channel_antitop_4f_InclusiveDecays'],
    n_files=2,
    n_events=1375656.0, # this n_events is the gensumwt
    aux={'n_events': 1488000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_schannel_t',
    id=23140264,
    is_data=False,
    processes=[procs.st_schannel_t],
    keys=['/ST_s_channel_top_4f_leptonDecays'],
    n_files=2,
    n_events=793980.0, # this n_events is the gensumwt
    aux={'n_events': 1288000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_schannel_tbar',
    id=23140265,
    is_data=False,
    processes=[procs.st_schannel_tbar],
    keys=['/ST_s_channel_antitop_4f_leptonDecays'],
    n_files=1,
    n_events=483918.0, # this n_events is the gensumwt
    aux={'n_events': 784000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_t_sl',
    id=23140266,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_LNu2Q'],
    n_files=9,
    n_events=4943196.0, # this n_events is the gensumwt
    aux={'n_events': 4943378} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_t_dl',
    id=23140267,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_2L2Nu'],
    n_files=5,
    n_events=2478922.0, # this n_events is the gensumwt
    aux={'n_events': 2479000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_t_fh',
    id=23140268,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_4Q'],
    n_files=5,
    n_events=3933816.0, # this n_events is the gensumwt
    aux={'n_events': 3934000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_tb_sl',
    id=23140269,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_LNu2Q'],
    n_files=10,
    n_events=5146462.0, # this n_events is the gensumwt
    aux={'n_events': 5146630} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_tb_dl',
    id=23140270,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_2L2Nu'],
    n_files=5,
    n_events=2487898.0, # this n_events is the gensumwt
    aux={'n_events': 2488000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_tb_fh',
    id=23140271,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_4Q'],
    n_files=5,
    n_events=3975836.0, # this n_events is the gensumwt
    aux={'n_events': 3976000} # n_events in aux is the nEvents produced
)