# data.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2016

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2016_postVFP_nano_tau_v09 import campaign_run2_UL2016_postVFP_nano_tau_v09 as cpn




cpn.add_dataset(
    name='data_tau_F',
    id=1609020,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2016F'],
    n_files=1,
    n_events=1187718.0,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name='data_tau_G',
    id=1609021,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2016G'],
    n_files=11,
    n_events=21883549.0,
    aux={'era': 'G'}
)

cpn.add_dataset(
    name='data_tau_H',
    id=1609022,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2016H'],
    n_files=13,
    n_events=25099115.0,
    aux={'era': 'H'}
)

cpn.add_dataset(
    name='data_mu_F',
    id=1609023,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2016F'],
    n_files=1,
    n_events=1537310.0,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name='data_mu_G',
    id=1609024,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2016G'],
    n_files=13,
    n_events=28922874.0,
    aux={'era': 'G'}
)

cpn.add_dataset(
    name='data_mu_H',
    id=1609025,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2016H'],
    n_files=15,
    n_events=34444121.0,
    aux={'era': 'H'}
)

cpn.add_dataset(
    name='data_e_F',
    id=1609026,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2016F'],
    n_files=1,
    n_events=1684733.0,
    aux={'era': 'F'}
)

cpn.add_dataset(
    name='data_e_G',
    id=1609027,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2016G'],
    n_files=14,
    n_events=29883091.0,
    aux={'era': 'G'}
)

cpn.add_dataset(
    name='data_e_H',
    id=1609028,
    is_data=True,
    processes=[procs.data_e],
    keys=['/SingleElectron_Run2016H'],
    n_files=13,
    n_events=28242966.0,
    aux={'era': 'H'}
)