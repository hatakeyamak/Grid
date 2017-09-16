from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = ''

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'slurp.py'
#config.JobType.allowNonProductionCMSSW = False 
config.JobType.allowUndistributedCMSSW = False # Parameter JobType.allowNonProductionCMSSW has been renamed to JobType.allowUndistributedCMSSW

config.section_("Data")
config.Data.inputDataset = '/TestEnablesEcalHcal/Run2017C-v1/RAW'
#config.Data.inputDataset = '/GenericTTbar/HC-CMSSW_7_0_4_START70_V7-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/SingleMuon/Run2015B-17Jul2015-v1/MINIAOD'
#config.Data.inputDataset = '/HTMHT/Run2015B-PromptReco-v1/MINIAOD'
#config.Data.inputDataset = '/HTMHT/Run2015B-17Jul2015-v1/MINIAOD'

config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'  # Parameter Data.dbsUrl has been renamed to Data.inputDBS
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
#NJOBS = 30
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.inputDBS = 'global'
#config.Data.inputDBS = 'global'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY_Run2015B.txt'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-251252_13TeV_PromptReco_Collisions15_JSON.txt'
#config.Data.lumiMask = './json_Run2015_DCSOnly_251244to251721_17July2015.txt'
#config.Data.runRange = '251244-251721'
#config.Data.lumiMask = './json_DCSONLY_Run2015B_ammended_720.txt'
#config.Data.runRange = '251244-251883'
#config.Data.lumiMask = './Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt'
#config.Data.runRange = '251563-251883'
#config.Data.publication = True
#config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/' # Parameter Data.publishDbsUrl has been renamed to Data.publishDBS
#config.Data.publishDataName = 'Run2017C_v1_TestEnablesEcalHcal_RAW'
#config.Data.outputDatasetTag = 'Run2017C_v1_TestEnablesEcalHcal_RAW'

config.Data.outLFNDirBase = '/store/user/hatake/crab_test'  # Data.outLFN has been renamed to Data.outLFNDirBase
#config.Data.outputPrimaryDataset = 'slurp'
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T3_US_Baylor'
#KH (this whitelisting below is not really necessary. we can use any T2/T3 for running jobs. we can still send output to Baylor)
#config.Site.whitelist = ['T3_US_Baylor']
config.Site.whitelist = ['T3_US*']
config.Site.blacklist = ['T3_US_UCR','T3_US_UMiss']

config.General.transferLogs=True 

