# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_tau_v09 import campaign_run2_UL2017_nano_tau_v09 as cpn




cpn.add_dataset(
    name='data_tau_B',
    id=1709010,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2017B'],
    n_files=6,
    n_events=11646232.0,
    aux={'era': 'B'}
)

cpn.add_dataset(
    name='data_tau_C',
    id=1709011,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2017C'],
    n_files=9,
    n_events=18525566.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_tau_D',
    id=1709012,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2017D'],
    n_files=4,
    n_events=7388733.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_tau_E',
    id=1709013,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2017E'],
    n_files=9,
    n_events=15967428.0,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name='data_tau_F',
    id=1709014,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2017F'],
    n_files=15,
    n_events=27278347.0,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name='data_mu_B',
    id=1709015,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2017B'],
    n_files=9,
    n_events=21572907.0,
    aux={'era': 'B'}
)

cpn.add_dataset(
    name='data_mu_C',
    id=1709016,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2017C'],
    n_files=14,
    n_events=32021527.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_mu_D',
    id=1709017,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2017D'],
    n_files=6,
    n_events=13405476.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_mu_E',
    id=1709018,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2017E'],
    n_files=15,
    n_events=33008071.0,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name='data_mu_F',
    id=1709019,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2017F'],
    n_files=26,
    n_events=54333809.0,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name='data_e_B',
    id=17090110,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2017B'],
    n_files=6,
    n_events=14808355.0,
    aux={'era': 'B'}
)

cpn.add_dataset(
    name='data_e_C',
    id=17090111,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2017C'],
    n_files=14,
    n_events=32631295.0,
    aux={'era': 'C'}
)

cpn.add_dataset(
    name='data_e_D',
    id=17090112,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2017D'],
    n_files=6,
    n_events=12563381.0,
    aux={'era': 'D'}
)

cpn.add_dataset(
    name='data_e_E',
    id=17090113,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2017E'],
    n_files=13,
    n_events=27869639.0,
    aux={'era': 'E'}
)

cpn.add_dataset(
    name='data_e_F',
    id=17090114,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2017F'],
    n_files=17,
    n_events=37181406.0,
    aux={'era': 'F'}
)