# ewk.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_cp_tau_v09 import campaign_run2_UL2017_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='ewk_wmtolnu',
    id=17090132,
    is_data=False,
    processes=[procs.ewk_wm_lnu_m50],
    keys=['/EWK_WminusToLNu'],
    n_files=2,
    n_events=1338756.0,
    aux=None
)

cpn.add_dataset(
    name='ewk_wptolnu',
    id=17090133,
    is_data=False,
    processes=[procs.ewk_wp_lnu_m50],
    keys=['/EWK_WplusToLNu'],
    n_files=2,
    n_events=1233864.0,
    aux=None
)

cpn.add_dataset(
    name='ewk_zll',
    id=17090134,
    is_data=False,
    processes=[procs.ewk_z_ll_m50],
    keys=['/EWK_ZTo2L'],
    n_files=1,
    n_events=367507.0,
    aux=None
)