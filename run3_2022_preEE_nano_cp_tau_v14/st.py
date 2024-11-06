# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v14 import campaign_run3_2022_preEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='st_tchannel_t',
    id=22140170,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t_channel_top_4f_InclusiveDecays'],
    n_files=3,
    n_events=2737505.0,
    aux=None
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=22140171,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t_channel_antitop_4f_InclusiveDecays'],
    n_files=2,
    n_events=1325389.0,
    aux=None
)

cpn.add_dataset(
    name='st_schannel_t',
    id=22140172,
    is_data=False,
    processes=[procs.st_schannel_t],
    keys=['/ST_s_channel_top_4f_leptonDecays'],
    n_files=2,
    n_events=781538.0,
    aux=None
)

cpn.add_dataset(
    name='st_schannel_tbar',
    id=22140173,
    is_data=False,
    processes=[procs.st_schannel_tbar],
    keys=['/ST_s_channel_antitop_4f_leptonDecays'],
    n_files=1,
    n_events=484738.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_sl',
    id=22140174,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_LNu2Q', '/ST_tW_top_LNu2Q_ext1'],
    n_files=18,
    n_events=9643983.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_dl',
    id=22140175,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_2L2Nu', '/ST_tW_top_2L2Nu_ext1'],
    n_files=10,
    n_events=4886868.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_fh',
    id=22140176,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_4Q', '/ST_tW_top_4Q_ext1'],
    n_files=10,
    n_events=7771275.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_sl',
    id=22140177,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_LNu2Q', '/ST_tW_antitop_LNu2Q_ext1'],
    n_files=17,
    n_events=9182711.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_dl',
    id=22140178,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_2L2Nu', '/ST_tW_antitop_2L2Nu_ext1'],
    n_files=10,
    n_events=4763261.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_fh',
    id=22140179,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_4Q', '/ST_tW_antitop_4Q_ext1'],
    n_files=10,
    n_events=7762668.0,
    aux=None
)