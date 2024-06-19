# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016_HIPM

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_preVFP_nano_cp_tau_v09 import campaign_run2_UL2016_preVFP_nano_cp_tau_v09 as cpn




cpn.add_dataset(
    name='data_tau_B',
    id=1609010,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2016B'],
    n_files=10,
    n_events=19202880.0,
    aux={'era': 'B'}
)

cpn.add_dataset(
    name='data_tau_C',
    id=1609011,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2016C'],
    n_files=6,
    n_events=10163592.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_tau_D',
    id=1609012,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2016D'],
    n_files=8,
    n_events=15591454.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_tau_E',
    id=1609013,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2016E'],
    n_files=9,
    n_events=16862919.0,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name='data_tau_F',
    id=1609014,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2016F'],
    n_files=6,
    n_events=10382762.0,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name='data_mu_B',
    id=1609015,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2016B'],
    n_files=12,
    n_events=27322389.0,
    aux={'era': 'B'}
)

cpn.add_dataset(
    name='data_mu_C',
    id=1609016,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2016C'],
    n_files=6,
    n_events=12866495.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_mu_D',
    id=1609017,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2016D'],
    n_files=8,
    n_events=18670547.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_mu_E',
    id=1609018,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2016E'],
    n_files=9,
    n_events=19119988.0,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name='data_mu_F',
    id=1609019,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2016F'],
    n_files=6,
    n_events=12237840.0,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name='data_e_B',
    id=16090110,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2016B'],
    n_files=18,
    n_events=38714038.0,
    aux={'era': 'B'}
)

cpn.add_dataset(
    name='data_e_C',
    id=16090111,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2016C'],
    n_files=8,
    n_events=16894559.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_e_D',
    id=16090112,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2016D'],
    n_files=12,
    n_events=25317735.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_e_E',
    id=16090113,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2016E'],
    n_files=11,
    n_events=22984217.0,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name='data_e_F',
    id=16090114,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2016F'],
    n_files=6,
    n_events=13043827.0,
    aux={'era': 'F'}
)