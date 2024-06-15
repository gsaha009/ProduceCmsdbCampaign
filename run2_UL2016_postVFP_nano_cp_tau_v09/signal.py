# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_postVFP_nano_tau_v09 import campaign_run2_UL2016_postVFP_nano_tau_v09 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_sm',
    id=16090253,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125'],
    n_files=3,
    n_events=3228508.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_odd_flat',
    id=16090254,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_CPodd_Filtered'],
    n_files=10,
    n_events=11635033.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_flat',
    id=16090255,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_SM_Filtered'],
    n_files=10,
    n_events=11418167.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_max_mix_flat',
    id=16090256,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_UncorrelatedDecay_MM_Filtered'],
    n_files=10,
    n_events=11308222.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_vbf_tautau_sm',
    id=16090257,
    is_data=False,
    processes=[procs.h_vbf_tautau],
    keys=['/VBFHToTauTau_M125'],
    n_files=1,
    n_events=927423.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_vbf_tautau_flat',
    id=16090258,
    is_data=False,
    processes=[procs.h_vbf_tautau],
    keys=['/VBFHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=7,
    n_events=9122544.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_sm',
    id=16090259,
    is_data=False,
    processes=[procs.wph_tautau],
    keys=['/WplusHToTauTau_M125'],
    n_files=2,
    n_events=1233110.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_flat',
    id=16090260,
    is_data=False,
    processes=[procs.wph_tautau],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=2,
    n_events=1351016.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_sm',
    id=16090261,
    is_data=False,
    processes=[procs.wmh_tautau],
    keys=['/WminusHToTauTau_M125'],
    n_files=2,
    n_events=1283753.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_flat',
    id=16090262,
    is_data=False,
    processes=[procs.wmh_tautau],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=1,
    n_events=891574.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_sm',
    id=16090263,
    is_data=False,
    processes=[procs.zh_tautau],
    keys=['/ZHToTauTau_M125', '/ZHToTauTau_M125_ext1'],
    n_files=2,
    n_events=1443837.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_flat',
    id=16090264,
    is_data=False,
    processes=[procs.zh_tautau],
    keys=['/ZHToTauTau_M125', '/ZHToTauTau_M125_ext1'],
    n_files=2,
    n_events=1443837.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='tth_tautau_sm',
    id=16090265,
    is_data=False,
    processes=[procs.tth_tautau],
    keys=['/ttHToTauTau_M125'],
    n_files=12,
    n_events=9314938.0,
    aux={'is_signal': True}
)