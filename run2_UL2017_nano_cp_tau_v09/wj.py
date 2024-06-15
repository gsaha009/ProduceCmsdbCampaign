# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_tau_v09 import campaign_run2_UL2017_nano_tau_v09 as cpn




cpn.add_dataset(
    name='wj_lo_incl',
    id=17090126,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu'],
    n_files=15,
    n_events=7148834.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_1j',
    id=17090127,
    is_data=False,
    processes=[procs.w_lnu_lo_1j],
    keys=['/W1JetsToLNu'],
    n_files=11,
    n_events=6516920.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_2j',
    id=17090128,
    is_data=False,
    processes=[procs.w_lnu_lo_2j],
    keys=['/W2JetsToLNu'],
    n_files=8,
    n_events=5657208.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_3j',
    id=17090129,
    is_data=False,
    processes=[procs.w_lnu_lo_3j],
    keys=['/W3JetsToLNu'],
    n_files=6,
    n_events=4790499.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_4j',
    id=17090130,
    is_data=False,
    processes=[procs.w_lnu_lo_4j],
    keys=['/W4JetsToLNu'],
    n_files=4,
    n_events=3205459.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_incl',
    id=17090131,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu-amcatnloFXFX'],
    n_files=6,
    n_events=1770884.0,
    aux=None
)