# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09 import campaign_run2_UL2018_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='wj_lo_incl',
    id=18090123,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu'],
    n_files=16,
    n_events=7153097.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_1j',
    id=18090124,
    is_data=False,
    processes=[procs.w_lnu_lo_1j],
    keys=['/W1JetsToLNu'],
    n_files=11,
    n_events=6454647.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_2j',
    id=18090125,
    is_data=False,
    processes=[procs.w_lnu_lo_2j],
    keys=['/W2JetsToLNu'],
    n_files=8,
    n_events=5646631.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_3j',
    id=18090126,
    is_data=False,
    processes=[procs.w_lnu_lo_3j],
    keys=['/W3JetsToLNu'],
    n_files=6,
    n_events=4778347.0,
    aux=None
)

cpn.add_dataset(
    name='wj_lo_4j',
    id=18090127,
    is_data=False,
    processes=[procs.w_lnu_lo_4j],
    keys=['/W4JetsToLNu'],
    n_files=4,
    n_events=3003361.0,
    aux=None
)

cpn.add_dataset(
    name='wj_nlo_incl',
    id=18090128,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WJetsToLNu-amcatnloFXFX'],
    n_files=7,
    n_events=1846510.0,
    aux=None
)