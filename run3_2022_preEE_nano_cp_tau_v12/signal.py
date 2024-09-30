# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12 import campaign_run3_2022_preEE_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_sm',
    id=22120125,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125'],
    n_files=1,
    n_events=295692.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelated_filter',
    id=22120126,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_Filtered'],
    n_files=6,
    n_events=8056751.0,
    aux={'is_signal': True}
)