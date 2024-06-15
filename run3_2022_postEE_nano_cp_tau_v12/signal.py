# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_tau_v14 import campaign_run3_2022_postEE_nano_tau_v14 as cpn




cpn.add_dataset(
    name='h_ggf_tautau',
    id=22140227,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125_amcatnloFXFX'],
    n_files=2,
    n_events=1992281.0,
    aux={'is_signal': True}
)