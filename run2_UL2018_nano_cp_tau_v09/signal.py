# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09 import campaign_run2_UL2018_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_sm',
    id=18090153,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125'],
    n_files=6,
    n_events=6738204.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_odd_flat',
    id=18090154,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_CPodd_Filtered'],
    n_files=21,
    n_events=24288664.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_flat',
    id=18090155,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_SM_Filtered'],
    n_files=19,
    n_events=21311062.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_max_mix_flat',
    id=18090156,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_MM_Filtered'],
    n_files=22,
    n_events=24581037.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_vbf_tautau_sm',
    id=18090157,
    is_data=False,
    processes=[procs.h_vbf_tautau],
    keys=['/VBFHToTauTau_M125'],
    n_files=2,
    n_events=1902095.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_vbf_tautau_flat',
    id=18090158,
    is_data=False,
    processes=[procs.h_vbf_tautau],
    keys=['/VBFHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=15,
    n_events=19408772.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_sm',
    id=18090159,
    is_data=False,
    processes=[procs.wph_tautau],
    keys=['/WplusHToTauTau_M125'],
    n_files=3,
    n_events=2516243.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_flat',
    id=18090160,
    is_data=False,
    processes=[procs.wph_tautau],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=3,
    n_events=2748856.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_sm',
    id=18090161,
    is_data=False,
    processes=[procs.wmh_tautau],
    keys=['/WminusHToTauTau_M125'],
    n_files=3,
    n_events=2529616.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_flat',
    id=18090162,
    is_data=False,
    processes=[procs.wmh_tautau],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=2,
    n_events=1758954.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_sm',
    id=18090163,
    is_data=False,
    processes=[procs.zh_tautau],
    keys=['/ZHToTauTau_M125', '/ZHToTauTau_M125_ext1'],
    n_files=6,
    n_events=6106068.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_flat',
    id=18090164,
    is_data=False,
    processes=[procs.zh_tautau],
    keys=['/ZHToTauTau_M125', '/ZHToTauTau_M125_ext1'],
    n_files=6,
    n_events=6106068.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='tth_tautau_sm',
    id=18090165,
    is_data=False,
    processes=[procs.tth_tautau],
    keys=['/ttHToTauTau_M125'],
    n_files=25,
    n_events=18871485.0,
    aux={'is_signal': True}
)