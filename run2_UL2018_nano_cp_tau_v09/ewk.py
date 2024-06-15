# ewk.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2018_nano_tau_v09 import campaign_run2_UL2018_nano_tau_v09 as cpn




cpn.add_dataset(
    name='ewk_wmtolnu',
    id=18090129,
    is_data=False,
    processes=[procs.ewk_wm_lnu_m50],
    keys=['/EWK_WminusToLNu'],
    n_files=2,
    n_events=1451270.0,
    aux=None
)

cpn.add_dataset(
    name='ewk_wptolnu',
    id=18090130,
    is_data=False,
    processes=[procs.ewk_wp_lnu_m50],
    keys=['/EWK_WplusToLNu'],
    n_files=2,
    n_events=1518562.0,
    aux=None
)

cpn.add_dataset(
    name='ewk_zll',
    id=18090131,
    is_data=False,
    processes=[procs.ewk_z_ll_m50],
    keys=['/EWK_ZTo2L'],
    n_files=1,
    n_events=630854.0,
    aux=None
)