# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v12 import campaign_run3_2023_preBPix_nano_cp_tau_v12 as cpn




cpn.add_dataset(
    name='wj_incl',
    id=2312019,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM'],
    n_files=48,
    n_events=191075090.0,
    aux=None
)