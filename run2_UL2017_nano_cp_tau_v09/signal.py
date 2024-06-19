# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_cp_tau_v09 import campaign_run2_UL2017_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_sm',
    id=17090156,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125'],
    n_files=6,
    n_events=6772374.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_odd_flat',
    id=17090157,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_CPodd_Filtered'],
    n_files=20,
    n_events=22474426.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_flat',
    id=17090158,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_SM_Filtered'],
    n_files=19,
    n_events=21430105.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_max_mix_flat',
    id=17090159,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_MM_Filtered'],
    n_files=22,
    n_events=24484262.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_vbf_tautau_sm',
    id=17090160,
    is_data=False,
    processes=[procs.h_vbf_tautau],
    keys=['/VBFHToTauTau_M125'],
    n_files=2,
    n_events=1837492.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_vbf_tautau_flat',
    id=17090161,
    is_data=False,
    processes=[procs.h_vbf_tautau],
    keys=['/VBFHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=14,
    n_events=17591842.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_sm',
    id=17090162,
    is_data=False,
    processes=[procs.wph_tautau],
    keys=['/WplusHToTauTau_M125'],
    n_files=3,
    n_events=2531013.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_flat',
    id=17090163,
    is_data=False,
    processes=[procs.wph_tautau],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=3,
    n_events=2636343.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_sm',
    id=17090164,
    is_data=False,
    processes=[procs.wmh_tautau],
    keys=['/WminusHToTauTau_M125'],
    n_files=3,
    n_events=2535006.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_flat',
    id=17090165,
    is_data=False,
    processes=[procs.wmh_tautau],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=2,
    n_events=1663044.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_sm',
    id=17090166,
    is_data=False,
    processes=[procs.zh_tautau],
    keys=['/ZHToTauTau_M125', '/ZHToTauTau_M125_ext1'],
    n_files=6,
    n_events=6131522.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_flat',
    id=17090167,
    is_data=False,
    processes=[procs.zh_tautau],
    keys=['/ZHToTauTau_M125', '/ZHToTauTau_M125_ext1'],
    n_files=6,
    n_events=6131522.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='tth_tautau_sm',
    id=17090168,
    is_data=False,
    processes=[procs.tth_tautau],
    keys=['/ttHToTauTau_M125'],
    n_files=25,
    n_events=19045500.0,
    aux={'is_signal': True}
)