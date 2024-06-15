# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_v12 import campaign_run3_2023_preBPix_nano_tau_v12 as cpn




cpn.add_dataset(
    name='st_tw_t_sl',
    id=23120116,
    is_data=False,
    processes=[procs.st_twchannel_t_sl],
    keys=['/ST_tW_top_LNu2Q'],
    n_files=8,
    n_events=9649924.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_dl',
    id=23120117,
    is_data=False,
    processes=[procs.st_twchannel_t_dl],
    keys=['/ST_tW_top_2L2Nu'],
    n_files=5,
    n_events=4984812.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_fh',
    id=23120118,
    is_data=False,
    processes=[procs.st_twchannel_t_fh],
    keys=['/ST_tW_top_4Q'],
    n_files=4,
    n_events=7918700.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_dl',
    id=23120119,
    is_data=False,
    processes=[procs.st_twchannel_tbar_dl],
    keys=['/ST_tW_antitop_2L2Nu'],
    n_files=5,
    n_events=4906798.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_fh',
    id=23120120,
    is_data=False,
    processes=[procs.st_twchannel_tbar_fh],
    keys=['/ST_tW_antitop_4Q'],
    n_files=5,
    n_events=7969722.0,
    aux=None
)