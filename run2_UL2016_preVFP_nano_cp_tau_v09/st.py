# st.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016_HIPM

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_preVFP_nano_tau_v09 import campaign_run2_UL2016_preVFP_nano_tau_v09 as cpn




cpn.add_dataset(
    name='st_tchannel_t',
    id=16090155,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t-channel_top_4f_InclusiveDecays'],
    n_files=18,
    n_events=9273634.0,
    aux=None
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=16090156,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t-channel_antitop_4f_InclusiveDecays'],
    n_files=10,
    n_events=5430866.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_t',
    id=16090157,
    is_data=False,
    processes=[procs.st_twchannel_t],
    keys=['/ST_tW_top_5f_InclusiveDecays'],
    n_files=2,
    n_events=854247.0,
    aux=None
)

cpn.add_dataset(
    name='st_tw_tb',
    id=16090158,
    is_data=False,
    processes=[procs.st_twchannel_tbar],
    keys=['/ST_tW_antitop_5f_InclusiveDecays'],
    n_files=2,
    n_events=854509.0,
    aux=None
)