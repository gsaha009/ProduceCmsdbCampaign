# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_postVFP_nano_cp_tau_v09 import campaign_run2_UL2016_postVFP_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='wj_lo_incl',
    id=16090220,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu'],
    n_files=15,
    n_events=5875256.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_1j',
    id=16090221,
    is_data=False,
    processes=[procs.w_lnu_lo_1j],
    keys=['/W1JetsToLNu'],
    n_files=9,
    n_events=4928510.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_2j',
    id=16090222,
    is_data=False,
    processes=[procs.w_lnu_lo_2j],
    keys=['/W2JetsToLNu'],
    n_files=7,
    n_events=4584866.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_3j',
    id=16090223,
    is_data=False,
    processes=[procs.w_lnu_lo_3j],
    keys=['/W3JetsToLNu'],
    n_files=6,
    n_events=4301718.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_4j',
    id=16090224,
    is_data=False,
    processes=[procs.w_lnu_lo_4j],
    keys=['/W4JetsToLNu'],
    n_files=2,
    n_events=1489409.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_incl',
    id=16090225,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu-amcatnloFXFX'],
    n_files=6,
    n_events=1507956.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_0j',
    id=16090226,
    is_data=False,
    processes=[procs.w_lnu_0j],
    keys=['/W0JetsToLNu-amcatnloFXFX'],
    n_files=27,
    n_events=6864983.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_1j',
    id=16090227,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/W1JetsToLNu-amcatnloFXFX'],
    n_files=39,
    n_events=12917913.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_2j',
    id=16090228,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/W2JetsToLNu-amcatnloFXFX'],
    n_files=26,
    n_events=6411062.0,
    aux=None
)