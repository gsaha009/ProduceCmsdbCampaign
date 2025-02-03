# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14 import campaign_run3_2022_postEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='st_tchannel_t',
    id=22140272,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t_channel_top_4f_InclusiveDecays'],
    n_files=10,
    n_events=9368799.0, # this n_events is the gensumwt
    aux={'n_events': 10178237} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=22140273,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t_channel_antitop_4f_InclusiveDecays'],
    n_files=5,
    n_events=4794814.0, # this n_events is the gensumwt
    aux={'n_events': 5185208} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_schannel_t',
    id=22140274,
    is_data=False,
    processes=[procs.st_schannel_t],
    keys=['/ST_s_channel_top_4f_leptonDecays'],
    n_files=5,
    n_events=2685976.0, # this n_events is the gensumwt
    aux={'n_events': 4363850} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_schannel_tbar',
    id=22140275,
    is_data=False,
    processes=[procs.st_schannel_tbar],
    keys=['/ST_s_channel_antitop_4f_leptonDecays'],
    n_files=4,
    n_events=1700756.0, # this n_events is the gensumwt
    aux={'n_events': 2762668} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_t_sl',
    id=22140276,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_LNu2Q', '/ST_tW_top_LNu2Q_ext1'],
    n_files=57,
    n_events=32511808.0, # this n_events is the gensumwt
    aux={'n_events': 32513048} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_t_dl',
    id=22140277,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_2L2Nu', '/ST_tW_top_2L2Nu_ext1'],
    n_files=31,
    n_events=16575338.0, # this n_events is the gensumwt
    aux={'n_events': 16575934} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_t_fh',
    id=22140278,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_4Q', '/ST_tW_top_4Q_ext1'],
    n_files=31,
    n_events=27459158.0, # this n_events is the gensumwt
    aux={'n_events': 27460118} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_tb_sl',
    id=22140279,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_LNu2Q', '/ST_tW_antitop_LNu2Q_ext1'],
    n_files=59,
    n_events=33757009.0, # this n_events is the gensumwt
    aux={'n_events': 33758259} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_tb_dl',
    id=22140280,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_2L2Nu', '/ST_tW_antitop_2L2Nu_ext1'],
    n_files=32,
    n_events=16782203.0, # this n_events is the gensumwt
    aux={'n_events': 16782809} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='st_tw_tb_fh',
    id=22140281,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_4Q', '/ST_tW_antitop_4Q_ext1'],
    n_files=29,
    n_events=25974756.0, # this n_events is the gensumwt
    aux={'n_events': 25975708} # n_events in aux is the nEvents produced
)