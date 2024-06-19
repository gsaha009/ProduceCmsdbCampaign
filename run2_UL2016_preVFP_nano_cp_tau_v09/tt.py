# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016_HIPM

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_preVFP_nano_cp_tau_v09 import campaign_run2_UL2016_preVFP_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=16090152,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTToSemiLeptonic'],
    n_files=79,
    n_events=67797898.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=16090153,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTTo2L2Nu'],
    n_files=28,
    n_events=29183604.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=16090154,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTToHadronic'],
    n_files=39,
    n_events=20556738.0,
    aux=None
)