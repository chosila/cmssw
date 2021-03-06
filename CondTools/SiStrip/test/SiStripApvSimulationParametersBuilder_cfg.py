import FWCore.ParameterSet.Config as cms

process = cms.Process("ICALIB")
process.source = cms.Source("EmptySource",
    numberEventsInRun = cms.untracked.uint32(1),
    firstRun = cms.untracked.uint32(1)
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(2),
        authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
    ),
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:dbfile.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('SiStripApvSimulationParametersRcd'),
        tag = cms.string('SiStripApvSimulationParameters_2016preVFP_v1')
    ))
)

process.apvSimParam = cms.ESSource("SiStripApvSimulationParametersESSource",
    apvBaselines_nBinsPerBaseline=cms.uint32(82),
    apvBaselines_minBaseline=cms.double(0.),
    apvBaselines_maxBaseline=cms.double(738.),
    apvBaselines_puBinEdges=cms.vdouble(0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20., 22., 24., 26., 28., 30., 32., 34., 36., 38., 40., 42., 44., 46., 48., 50.),
    apvBaselines_zBinEdges=cms.vdouble(0., 25., 50., 75.),
    apvBaselines_rBinEdges_TID = cms.untracked.vdouble(),
    apvBaselines_rBinEdges_TEC = cms.untracked.vdouble(),
    apvBaselinesFile_tib1=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB1_11us.txt"),
    apvBaselinesFile_tib2=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB2_14us.txt"),
    apvBaselinesFile_tib3=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB3_15us.txt"),
    apvBaselinesFile_tib4=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB4_17us.txt"),
    apvBaselinesFile_tob1=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB1_9us.txt"),
    apvBaselinesFile_tob2=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB2_11us.txt"),
    apvBaselinesFile_tob3=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB3_14us.txt"),
    apvBaselinesFile_tob4=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB4_17us.txt"),
    apvBaselinesFile_tob5=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB5_21us.txt"),
    apvBaselinesFile_tob6=cms.untracked.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB6_21us.txt")
    )
process.prod = cms.EDAnalyzer("SiStripApvSimulationParametersBuilder")

process.p = cms.Path(process.prod)
