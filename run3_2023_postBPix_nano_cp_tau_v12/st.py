# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v12 import campaign_run3_2023_postBPix_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='st_tw_t_sl',
    id=23120217,
    is_data=False,
    processes=[procs.st_twchannel_t_sl],
    keys=['/ST_tW_top_LNu2Q'],
    n_files=4,
    n_events=4943196.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_dl',
    id=23120218,
    is_data=False,
    processes=[procs.st_twchannel_t_dl],
    keys=['/ST_tW_top_2L2Nu'],
    n_files=3,
    n_events=2478922.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t_fh',
    id=23120219,
    is_data=False,
    processes=[procs.st_twchannel_t_fh],
    keys=['/ST_tW_top_4Q'],
    n_files=2,
    n_events=3933816.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_sl',
    id=23120220,
    is_data=False,
    processes=[procs.st_twchannel_tbar_sl],
    keys=['/ST_tW_antitop_LNu2Q'],
    n_files=5,
    n_events=5146462.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_dl',
    id=23120221,
    is_data=False,
    processes=[procs.st_twchannel_tbar_dl],
    keys=['/ST_tW_antitop_2L2Nu'],
    n_files=3,
    n_events=2487898.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb_fh',
    id=23120222,
    is_data=False,
    processes=[procs.st_twchannel_tbar_fh],
    keys=['/ST_tW_antitop_4Q'],
    n_files=3,
    n_events=3975836.0,
    aux=None
)