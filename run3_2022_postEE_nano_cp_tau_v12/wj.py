# wj.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_tau_v14 import campaign_run3_2022_postEE_nano_tau_v14 as cpn




cpn.add_dataset(
    name='wj_incl',
    id=22140212,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_amcatnloFXFX'],
    n_files=77,
    n_events=196137118.0,
    aux=None
)