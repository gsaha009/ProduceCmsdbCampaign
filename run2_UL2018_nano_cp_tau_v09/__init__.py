# coding: utf-8

from order import Campaign


# ----------- #
#   Campaign  #
# ----------- #
campaign_run2_UL2018_nano_cp_tau_v09 = Campaign(
    name='run2_UL2018_nano_cp_tau_v09',
    id=180901,
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD", 
        "year": 2018,
        "postfix": None,
        "version": 9,
        "custom": {
            "name": "run2_UL2018_nano_cp_tau_v09",
            "creator": "IPHC",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2018",
        },
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09.data
import cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09.dy
import cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09.ewk
import cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09.signal
import cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09.st
import cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09.tt
import cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09.vv
import cmsdb.campaigns.run2_UL2018_nano_cp_tau_v09.wj
