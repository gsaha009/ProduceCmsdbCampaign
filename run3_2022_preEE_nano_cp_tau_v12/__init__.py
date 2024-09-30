# coding: utf-8

from order import Campaign


# ----------- #
#   Campaign  #
# ----------- #
campaign_run3_2022_preEE_nano_cp_tau_v12 = Campaign(
    name='run3_2022_preEE_nano_cp_tau_v12',
    id=221201,
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD", 
        "year": 2022,
        "run": 3,
        "postfix": "preEE",
        "version": 12,
        "custom": {
            "name": "run3_2022_preEE_nano_cp_tau_v12",
            "creator": "IPHC",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022",
        },
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12.data
import cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12.dy
import cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12.signal
import cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12.st
import cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12.tt
import cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12.vv
import cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v12.wj
