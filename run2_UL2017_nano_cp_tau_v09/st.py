# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_tau_v09 import campaign_run2_UL2017_nano_tau_v09 as cpn




cpn.add_dataset(
    name='st_tchannel_t',
    id=17090152,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t-channel_top_4f_InclusiveDecays'],
    n_files=42,
    n_events=22809034.0,
    aux=None
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=17090153,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t-channel_antitop_4f_InclusiveDecays'],
    n_files=24,
    n_events=12877381.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t',
    id=17090154,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_5f_InclusiveDecays'],
    n_files=3,
    n_events=2163654.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb',
    id=17090155,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_5f_InclusiveDecays'],
    n_files=3,
    n_events=2173605.0,
    aux=None
)