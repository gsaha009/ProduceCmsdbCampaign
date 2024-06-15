# ewk.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_postVFP_nano_tau_v09 import campaign_run2_UL2016_postVFP_nano_tau_v09 as cpn




cpn.add_dataset(
    name='ewk_wmtolnu',
    id=16090229,
    is_data=False,
    processes=[procs.ewk_wm_lnu_m50],
    keys=['/EWK_WminusToLNu'],
    n_files=1,
    n_events=669767.0,
    aux=None
)

cpn.add_dataset(
    name='ewk_wptolnu',
    id=16090230,
    is_data=False,
    processes=[procs.ewk_wp_lnu_m50],
    keys=['/EWK_WplusToLNu'],
    n_files=1,
    n_events=649055.0,
    aux=None
)

cpn.add_dataset(
    name='ewk_zll',
    id=16090231,
    is_data=False,
    processes=[procs.ewk_z_ll_m50],
    keys=['/EWK_ZTo2L'],
    n_files=1,
    n_events=278867.0,
    aux=None
)