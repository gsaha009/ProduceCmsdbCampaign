# ewk.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016_HIPM

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_preVFP_nano_cp_tau_v09 import campaign_run2_UL2016_preVFP_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='ewk_wmtolnu',
    id=16090135,
    is_data=False,
    processes=[procs.ewk_wm_lnu_m50],
    keys=['/EWK_WminusToLNu'],
    n_files=1,
    n_events=699525.0,
    aux=None
)

cpn.add_dataset(
    name='ewk_wptolnu',
    id=16090136,
    is_data=False,
    processes=[procs.ewk_wp_lnu_m50],
    keys=['/EWK_WplusToLNu'],
    n_files=1,
    n_events=710320.0,
    aux=None
)

cpn.add_dataset(
    name='ewk_zll',
    id=16090137,
    is_data=False,
    processes=[procs.ewk_z_ll_m50],
    keys=['/EWK_ZTo2L'],
    n_files=1,
    n_events=307823.0,
    aux=None
)