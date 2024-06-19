# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09 import campaign_run2_UL2018_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='st_tchannel_t',
    id=18090149,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t-channel_top_4f_InclusiveDecays'],
    n_files=58,
    n_events=30774596.0,
    aux=None
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=18090150,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t-channel_antitop_4f_InclusiveDecays'],
    n_files=32,
    n_events=17335181.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t',
    id=18090151,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_5f_InclusiveDecays'],
    n_files=4,
    n_events=3017816.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb',
    id=18090152,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_5f_InclusiveDecays'],
    n_files=4,
    n_events=2940819.0,
    aux=None
)