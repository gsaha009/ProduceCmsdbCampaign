# tt.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_postVFP_nano_tau_v09 import campaign_run2_UL2016_postVFP_nano_tau_v09 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=16090246,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTToSemiLeptonic'],
    n_files=86,
    n_events=73175091.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=16090247,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTTo2L2Nu'],
    n_files=32,
    n_events=34018380.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=16090248,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTToHadronic'],
    n_files=42,
    n_events=21504751.0,
    aux=None
)