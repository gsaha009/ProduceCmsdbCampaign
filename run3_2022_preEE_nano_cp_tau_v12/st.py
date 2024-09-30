# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12 import campaign_run3_2022_preEE_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='st_tchannel_t',
    id=22120117,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t-channel_top_4f_InclusiveDecays'],
    n_files=2,
    n_events=2737505.0,
    aux=None
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=22120118,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t-channel_antitop_4f_InclusiveDecays'],
    n_files=1,
    n_events=1325389.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_sl',
    id=22120119,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_LNu2Q', '/ST_tW_top_LNu2Q_ext1'],
    n_files=8,
    n_events=9643983.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_dl',
    id=22120120,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_2L2Nu', '/ST_tW_top_2L2Nu_ext1'],
    n_files=6,
    n_events=4886868.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_fh',
    id=22120121,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_4Q', '/ST_tW_top_4Q_ext1'],
    n_files=4,
    n_events=7771275.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_sl',
    id=22120122,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_LNu2Q', '/ST_tW_antitop_LNu2Q_ext1'],
    n_files=8,
    n_events=9224089.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_dl',
    id=22120123,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_2L2Nu', '/ST_tW_antitop_2L2Nu_ext1'],
    n_files=6,
    n_events=4901541.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_fh',
    id=22120124,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_4Q', '/ST_tW_antitop_4Q_ext1'],
    n_files=5,
    n_events=7762668.0,
    aux=None
)