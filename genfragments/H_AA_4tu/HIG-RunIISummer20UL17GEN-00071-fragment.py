import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
                                 comEnergy = cms.double(13000.0),
                                 crossSection = cms.untracked.double(1),
                                 filterEfficiency = cms.untracked.double(1.0),
                                 maxEventsToPrint = cms.untracked.int32(0),
                                 pythiaPylistVerbosity = cms.untracked.int32(0),
                                 pythiaHepMCVerbosity = cms.untracked.bool(False),
                                 PythiaParameters = cms.PSet(

    pythia8CommonSettingsBlock,
    pythia8CP5SettingsBlock,
    pythia8PSweightsSettingsBlock,
    processParameters = cms.vstring('Higgs:useBSM = on',
      'HiggsBSM:gg2H2 = on',
      '35:m0 = 125.',
      '35:onMode = off',
      '35:onIfMatch = 25 25',
      '25:mMin = 3',
      '25:m0 = 10.',
      '25:onMode = off',
      '25:onIfMatch = 15 -15'
      ),

    parameterSets = cms.vstring(
      'pythia8CommonSettings',
      'pythia8CP5Settings',
      'pythia8PSweightsSettings',
      'processParameters'
      )
    )
)

ProductionFilterSequence = cms.Sequence(generator)