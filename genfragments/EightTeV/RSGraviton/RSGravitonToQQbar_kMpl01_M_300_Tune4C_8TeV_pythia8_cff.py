import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8GeneratorFilter",
	comEnergy = cms.double(8000.0),
        crossSection = cms.untracked.double(68.97),
	filterEfficiency = cms.untracked.double(1.0),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(0),

	PythiaParameters = cms.PSet(
		processParameters = cms.vstring(
                'Main:timesAllowErrors    = 10000',
	        'ParticleDecays:limitTau0 = on',
		'ParticleDecays:tauMax = 10',
                'ExtraDimensionsG*:ffbar2G* = on',
                '5100039:m0 = 300.',
                '5100039:onMode = off',
                '5100039:onIfAny = 1 2 3 4 5',
                'ExtraDimensionsG*:kappaMG = 0.54',
                'Tune:pp 5',
		'Tune:ee 3',
		),

		parameterSets = cms.vstring('processParameters')
	)
)
