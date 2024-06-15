# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016_HIPM

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_preVFP_nano_tau_v09 import campaign_run2_UL2016_preVFP_nano_tau_v09 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_sm',
    id=16090159,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125'],
    n_files=3,
    n_events=3185667.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_odd_flat',
    id=16090160,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_CPodd_Filtered'],
    n_files=10,
    n_events=10774828.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_flat',
    id=16090161,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_SM_Filtered'],
    n_files=8,
    n_events=8653419.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_max_mix_flat',
    id=16090162,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_MM_Filtered'],
    n_files=12,
    n_events=13680497.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_vbf_tautau_sm',
    id=16090163,
    is_data=False,
    processes=[procs.h_vbf_tautau],
    keys=['/VBFHToTauTau_M125'],
    n_files=1,
    n_events=856813.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_vbf_tautau_flat',
    id=16090164,
    is_data=False,
    processes=[procs.h_vbf_tautau],
    keys=['/VBFHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=7,
    n_events=8549354.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_sm',
    id=16090165,
    is_data=False,
    processes=[procs.wph_tautau],
    keys=['/WplusHToTauTau_M125'],
    n_files=2,
    n_events=1177944.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_flat',
    id=16090166,
    is_data=False,
    processes=[procs.wph_tautau],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=2,
    n_events=1408737.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_sm',
    id=16090167,
    is_data=False,
    processes=[procs.wmh_tautau],
    keys=['/WminusHToTauTau_M125'],
    n_files=2,
    n_events=1268247.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_flat',
    id=16090168,
    is_data=False,
    processes=[procs.wmh_tautau],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=1,
    n_events=1038090.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_sm',
    id=16090169,
    is_data=False,
    processes=[procs.zh_tautau],
    keys=['/ZHToTauTau_M125', '/ZHToTauTau_M125_ext1'],
    n_files=4,
    n_events=2916481.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_flat',
    id=16090170,
    is_data=False,
    processes=[procs.zh_tautau],
    keys=['/ZHToTauTau_M125', '/ZHToTauTau_M125_ext1'],
    n_files=4,
    n_events=2916481.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='tth_tautau_sm',
    id=16090171,
    is_data=False,
    processes=[procs.tth_tautau],
    keys=['/ttHToTauTau_M125'],
    n_files=12,
    n_events=9381365.0,
    aux={'is_signal': True}
)