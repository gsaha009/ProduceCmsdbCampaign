# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v12 import campaign_run3_2023_postBPix_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_sm',
    id=23120223,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125'],
    n_files=2,
    n_events=3921740.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_flat',
    id=23120224,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_Filtered'],
    n_files=7,
    n_events=10093183.0,
    aux={'is_signal': True}
)