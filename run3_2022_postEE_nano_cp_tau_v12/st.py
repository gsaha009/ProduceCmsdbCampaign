# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v12 import campaign_run3_2022_postEE_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='st_tchannel_t',
    id=22120219,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t-channel_top_4f_InclusiveDecays'],
    n_files=5,
    n_events=9368799.0,
    aux=None
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=22120220,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t-channel_antitop_4f_InclusiveDecays'],
    n_files=3,
    n_events=4794814.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_sl',
    id=22120221,
    is_data=False,
    processes=[procs.st_twchannel_t_sl],
    keys=['/ST_tW_top_LNu2Q', '/ST_tW_top_LNu2Q_ext1'],
    n_files=26,
    n_events=32511808.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_dl',
    id=22120222,
    is_data=False,
    processes=[procs.st_twchannel_t_dl],
    keys=['/ST_tW_top_2L2Nu', '/ST_tW_top_2L2Nu_ext1'],
    n_files=15,
    n_events=16575338.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_fh',
    id=22120223,
    is_data=False,
    processes=[procs.st_twchannel_t_fh],
    keys=['/ST_tW_top_4Q', '/ST_tW_top_4Q_ext1'],
    n_files=14,
    n_events=27459158.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_sl',
    id=22120224,
    is_data=False,
    processes=[procs.st_twchannel_tbar_sl],
    keys=['/ST_tW_antitop_LNu2Q', '/ST_tW_antitop_LNu2Q_ext1'],
    n_files=27,
    n_events=33757009.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_dl',
    id=22120225,
    is_data=False,
    processes=[procs.st_twchannel_tbar_dl],
    keys=['/ST_tW_antitop_2L2Nu', '/ST_tW_antitop_2L2Nu_ext1'],
    n_files=15,
    n_events=16782203.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_fh',
    id=22120226,
    is_data=False,
    processes=[procs.st_twchannel_tbar_fh],
    keys=['/ST_tW_antitop_4Q', '/ST_tW_antitop_4Q_ext1'],
    n_files=14,
    n_events=26003524.0,
    aux=None
)