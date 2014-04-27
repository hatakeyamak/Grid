import FWCore.ParameterSet.Config as cms
process = cms.Process('Slurp')

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())
process.maxEvents = cms.untracked.PSet( input       = cms.untracked.int32(10) )
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
        '/store/mc/SAM/GenericTTbar/GEN-SIM-RECO/CMSSW_5_3_1_START53_V5-v1/0013/3E573418-4BAE-E111-B0CD-BCAEC532971D.root'
        )
                            )

process.output = cms.OutputModule("PoolOutputModule",
                                  outputCommands = cms.untracked.vstring("drop *", "keep recoTracks_*_*_*"),
                                  fileName = cms.untracked.string('outfile.root'),
                                                                    )
process.out_step = cms.EndPath(process.output)
