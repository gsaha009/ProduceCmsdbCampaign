# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v12 import campaign_run3_2023_preBPix_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='h_ggf_tautau',
    id=23120121,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125_amcatnloFXFX'],
    n_files=2,
    n_events=1113441.0,
    aux={'is_signal': True}
)