# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14 import campaign_run3_2022_postEE_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_uncorrelated_filter',
    id=22140282,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_Filtered'],
    n_files=32,
    n_events=21340204.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 21340864} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_CPodd_Filtered_ProdAndDecay',
    id=22140283,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay'],
    n_files=42,
    n_events=21495773.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 26545013} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay',
    id=22140284,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay'],
    n_files=1,
    n_events=448150.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 560000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_MM_Filtered_ProdAndDecay',
    id=22140285,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay'],
    n_files=40,
    n_events=20689379.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 25643123} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_MM_UnFiltered_ProdAndDecay',
    id=22140286,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay'],
    n_files=1,
    n_events=441570.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 554438} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_SM_Filtered_ProdAndDecay',
    id=22140287,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay'],
    n_files=38,
    n_events=19599725.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 24356269} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_SM_UnFiltered_ProdAndDecay',
    id=22140288,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay'],
    n_files=1,
    n_events=445092.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 560000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_M125_amcatnloFXFX',
    id=22140289,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHToTauTau_M125_amcatnloFXFX'],
    n_files=5,
    n_events=1992281.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 3533459} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zh_tautau_uncorrelatedDecay_Filtered',
    id=22140290,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=4,
    n_events=1863291.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1863291} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zh_tautau_uncorrelatedDecay_UnFiltered',
    id=22140291,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=69650.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 69650} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wph_tautau_uncorrelatedDecay_Filtered',
    id=22140292,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=5,
    n_events=2025321.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 2121547} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wph_tautau_uncorrelatedDecay_UnFiltered',
    id=22140293,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WplusHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=66154.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 70000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wmh_tautau_uncorrelatedDecay_Filtered',
    id=22140294,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=4,
    n_events=1480135.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1550013} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wmh_tautau_uncorrelatedDecay_UnFiltered',
    id=22140295,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WminusHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=63910.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 67580} # n_events in aux is the nEvents produced
)