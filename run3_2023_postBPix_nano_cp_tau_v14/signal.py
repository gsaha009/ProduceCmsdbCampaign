# signal.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14 import campaign_run3_2023_postBPix_nano_cp_tau_v14 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_uncorrelated_filter',
    id=23140277,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_Filtered'],
    n_files=16,
    n_events=10093183.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 10093467} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_SM_Filtered_ProdAndDecay',
    id=23140278,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay'],
    n_files=18,
    n_events=8623785.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 10717909} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_CPodd_Filtered_ProdAndDecay',
    id=23140279,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay'],
    n_files=19,
    n_events=9103069.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 11235783} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_MM_Filtered_ProdAndDecay',
    id=23140280,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay'],
    n_files=19,
    n_events=9115963.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 11301507} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelated_unfilter',
    id=23140281,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=199988.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 200000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_SM_UnFiltered_ProdAndDecay',
    id=23140282,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay'],
    n_files=1,
    n_events=103106.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 130000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay',
    id=23140283,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay'],
    n_files=1,
    n_events=103696.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 130000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_MM_UnFiltered_ProdAndDecay',
    id=23140284,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay'],
    n_files=1,
    n_events=103290.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 130000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_M125_madgraph',
    id=23140285,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHToTauTau_M125'],
    n_files=5,
    n_events=3921740.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 3922000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_M125_amcatnloFXFX',
    id=23140286,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHToTauTau_M125_amcatnloFXFX'],
    n_files=5,
    n_events=1895953.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 3363741} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zh_tautau_uncorrelatedDecay_Filtered',
    id=23140287,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=3,
    n_events=1007812.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1007812} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zh_tautau_uncorrelatedDecay_UnFiltered',
    id=23140288,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=29949.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 29949} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wph_tautau_uncorrelatedDecay_Filtered',
    id=23140289,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=3,
    n_events=952493.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 998269} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wph_tautau_uncorrelatedDecay_UnFiltered',
    id=23140290,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WplusHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=28316.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 30000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wmh_tautau_uncorrelatedDecay_Filtered',
    id=23140291,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=2,
    n_events=718725.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 753115} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wmh_tautau_uncorrelatedDecay_UnFiltered',
    id=23140292,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WminusHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=28420.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 30000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_vbf_tautau_M125',
    id=23140293,
    is_data=False,
    processes=[procs.h_vbf_htt],
    keys=['/VBFHToTauTau_M125'],
    n_files=6,
    n_events=3817138.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 3822000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_vbf_tautau_uncorrelatedDecay_Filtered',
    id=23140294,
    is_data=False,
    processes=[procs.h_vbf_htt],
    keys=['/VBFHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=14,
    n_events=7048003.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 7056765} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_vbf_tautau_uncorrelatedDecay_UnFiltered',
    id=23140295,
    is_data=False,
    processes=[procs.h_vbf_htt],
    keys=['/VBFHToTauTau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=199756.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 200000} # n_events in aux is the nEvents produced
)