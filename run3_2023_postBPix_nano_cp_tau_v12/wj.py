# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_tau_v12 import campaign_run3_2023_postBPix_nano_tau_v12 as cpn




cpn.add_dataset(
    name='wj_incl',
    id=23120210,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM'],
    n_files=24,
    n_events=94639090.0,
    aux=None
)