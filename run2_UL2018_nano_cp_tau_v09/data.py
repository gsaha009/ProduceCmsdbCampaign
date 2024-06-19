# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09 import campaign_run2_UL2018_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='data_tau_A',
    id=1809010,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2018A'],
    n_files=12,
    n_events=22241186.0,
    aux={'era': 'A'}
)

cpn.add_dataset(
    name='data_tau_B',
    id=1809011,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2018B'],
    n_files=6,
    n_events=11253001.0,
    aux={'era': 'B'}
)

cpn.add_dataset(
    name='data_tau_C',
    id=1809012,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2018C'],
    n_files=6,
    n_events=11385851.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_tau_D',
    id=1809013,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2018D'],
    n_files=29,
    n_events=59424668.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_mu_A',
    id=1809014,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2018A'],
    n_files=23,
    n_events=51709319.0,
    aux={'era': 'A'}
)

cpn.add_dataset(
    name='data_mu_B',
    id=1809015,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2018B'],
    n_files=12,
    n_events=26153206.0,
    aux={'era': 'B'}
)

cpn.add_dataset(
    name='data_mu_C',
    id=1809016,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2018C'],
    n_files=11,
    n_events=24275290.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_mu_D',
    id=1809017,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2018D'],
    n_files=48,
    n_events=109722240.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_e_A',
    id=1809018,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2018A'],
    n_files=36,
    n_events=73452711.0,
    aux={'era': 'A'}
)

cpn.add_dataset(
    name='data_e_B',
    id=1809019,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2018B'],
    n_files=17,
    n_events=34570116.0,
    aux={'era': 'B'}
)

cpn.add_dataset(
    name='data_e_C',
    id=18090110,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2018C'],
    n_files=17,
    n_events=33428809.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_e_D',
    id=18090111,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2018D'],
    n_files=77,
    n_events=163292707.0,
    aux={'era': 'D'}
)