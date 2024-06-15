# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2018_nano_tau_v09 import campaign_run2_UL2018_nano_tau_v09 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=18090146,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTToSemiLeptonic'],
    n_files=294,
    n_events=252224460.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=18090147,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTTo2L2Nu'],
    n_files=112,
    n_events=115959444.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=18090148,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTToHadronic'],
    n_files=138,
    n_events=71912107.0,
    aux=None
)