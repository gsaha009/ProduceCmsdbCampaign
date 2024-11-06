# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v14 import campaign_run3_2022_preEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_uncorrelated_filter',
    id=22140180,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_Filtered'],
    n_files=12,
    n_events=8056751.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_CPodd_Filtered_ProdAndDecay',
    id=22140181,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay'],
    n_files=14,
    n_events=7185840.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay',
    id=22140182,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay'],
    n_files=1,
    n_events=159712.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_MM_Filtered_ProdAndDecay',
    id=22140183,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay'],
    n_files=13,
    n_events=6424278.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_MM_UnFiltered_ProdAndDecay',
    id=22140184,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay'],
    n_files=1,
    n_events=159083.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_SM_Filtered_ProdAndDecay',
    id=22140185,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay'],
    n_files=14,
    n_events=6703604.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_SM_UnFiltered_ProdAndDecay',
    id=22140186,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay'],
    n_files=1,
    n_events=158678.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_M125_amcatnloFXFX',
    id=22140187,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125_amcatnloFXFX'],
    n_files=2,
    n_events=585054.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_sm',
    id=22140188,
    is_data=False,
    processes=[procs.h_ggf_tautau],
    keys=['/GluGluHToTauTau_M125'],
    n_files=1,
    n_events=295692.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_uncorrelatedDecay_Filtered',
    id=22140189,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=2,
    n_events=613598.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='zh_tautau_uncorrelatedDecay_UnFiltered',
    id=22140190,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=28992.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_uncorrelatedDecay_Filtered',
    id=22140191,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=2,
    n_events=716466.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wph_tautau_uncorrelatedDecay_UnFiltered',
    id=22140192,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WplusHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=28300.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_uncorrelatedDecay_Filtered',
    id=22140193,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=1,
    n_events=431839.0,
    aux={'is_signal': True}
)

cpn.add_dataset(
    name='wmh_tautau_uncorrelatedDecay_UnFiltered',
    id=22140194,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WminusHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=27789.0,
    aux={'is_signal': True}
)