# coding: utf-8

from order import Campaign


# ----------- #
#   Campaign  #
# ----------- #
campaign_run3_2023_postBPix_nano_cp_tau_v14 = Campaign(
    name='run3_2023_postBPix_nano_cp_tau_v14',
    id=231402,
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD", 
        "year": 2023,
        "run": 3,
        "postfix": "postBPix",
        "version": 14,
        "custom": {
            "name": "run3_2023_postBPix_nano_cp_tau_v14",
            "creator": "IPHC",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix",
        },
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14.data
import cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14.dy
import cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14.signal
import cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14.st
import cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14.tt
import cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14.vv
import cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14.wj
