# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016_HIPM

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_preVFP_nano_cp_tau_v09 import campaign_run2_UL2016_preVFP_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='wj_lo_incl',
    id=16090126,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu'],
    n_files=14,
    n_events=5641399.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_1j',
    id=16090127,
    is_data=False,
    processes=[procs.w_lnu_lo_1j],
    keys=['/W1JetsToLNu'],
    n_files=10,
    n_events=5849005.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_2j',
    id=16090128,
    is_data=False,
    processes=[procs.w_lnu_lo_2j],
    keys=['/W2JetsToLNu'],
    n_files=7,
    n_events=5180241.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_3j',
    id=16090129,
    is_data=False,
    processes=[procs.w_lnu_lo_3j],
    keys=['/W3JetsToLNu'],
    n_files=5,
    n_events=4093378.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_4j',
    id=16090130,
    is_data=False,
    processes=[procs.w_lnu_lo_4j],
    keys=['/W4JetsToLNu'],
    n_files=2,
    n_events=1448279.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_incl',
    id=16090131,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu-amcatnloFXFX'],
    n_files=6,
    n_events=1613844.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_0j',
    id=16090132,
    is_data=False,
    processes=[procs.w_lnu_0j],
    keys=['/W0JetsToLNu-amcatnloFXFX'],
    n_files=26,
    n_events=6944450.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_1j',
    id=16090133,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/W1JetsToLNu-amcatnloFXFX'],
    n_files=41,
    n_events=13849373.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_2j',
    id=16090134,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/W2JetsToLNu-amcatnloFXFX'],
    n_files=27,
    n_events=6779563.0,
    aux=None
)