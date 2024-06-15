# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_tau_v09 import campaign_run2_UL2017_nano_tau_v09 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=17090149,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTToSemiLeptonic'],
    n_files=223,
    n_events=188929771.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=17090150,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTTo2L2Nu'],
    n_files=82,
    n_events=85098463.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=17090151,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTToHadronic'],
    n_files=97,
    n_events=50275302.0,
    aux=None
)