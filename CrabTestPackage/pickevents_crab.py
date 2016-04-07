
## Edited By Raman Khurana
##
## CRAB documentation : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrab
##
## CRAB 3 parameters : https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
##
## Once you are happy with this file, please run
## crab submit

## In CRAB3 the configuration file is in Python language. It consists of creating a Configuration object imported from the WMCore library: 

from WMCore.Configuration import Configuration
config = Configuration()

##  Once the Configuration object is created, it is possible to add new sections into it with corresponding parameters
config.section_("General")
config.General.requestName = 'pickEvents3'
config.General.workArea = 'crab_pickevents3_20160405_110758'


config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/cvmfs/cms.cern.ch/slc6_amd64_gcc491/cms/cmssw/CMSSW_7_4_1/src/PhysicsTools/Utilities/configuration/copyPickMerge_cfg.py'
config.JobType.pyCfgParams = ['eventsToProcess_load=pickevents_runEvents.txt', 'outputFile=pickevents.root']
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/JetHT/Run2015D-16Dec2015-v1/MINIAOD'

config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 3
config.Data.totalUnits = 2
#config.Data.lumiMask = 'pickevents.json'
config.Data.publication = False
#config.Data.publishDbsUrl = 'phys03'
#config.Data.publishDataName = 'CRAB3_CSA_DYJets'
#config.JobType.allowNonProductionCMSSW=True
config.Data.ignoreLocality = True

config.section_("Site")
## Change site name accordingly
config.Site.storageSite = "T3_US_Baylor"
config.Site.whitelist = ['T3_US_Baylor']

