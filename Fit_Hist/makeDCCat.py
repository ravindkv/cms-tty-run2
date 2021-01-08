from ROOT import TFile, TH1F, gDirectory
import os
import sys
import json
import itertools
from optparse import OptionParser
import CombineHarvester.CombineTools.ch as ch
from FitInputs import *

#-----------------------------------------
#INPUT command-line arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specify the year of the data taking" )
parser.add_option("-d", "--decayMode", dest="decayMode", default="Semilep",type='str',
                     help="Specify which decayMode moded of ttbar Semilep or Dilep? default is Semilep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--hist", "--hist", dest="hName", default="phosel_M3",type='str', 
                     help="which histogram to be used for making datacard")
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--isQCDMC","--qcdMC",dest="isQCDMC", default=False, action="store_true",
		  help="")
parser.add_option("--isChIsoM3","--isChIsoM3",dest="isChIsoM3", default=False, action="store_true",
		  help="")
parser.add_option("--is0PhoM3","--is0PhoM3",dest="is0PhoM3", default=False, action="store_true",
		  help="")
parser.add_option("--isMassLepGamma","--isMassLepGamma",dest="isMassLepGamma", default=False, action="store_true",
		  help="")
parser.add_option("--isMassDilep","--isMassDilep",dest="isMassDilep", default=False, action="store_true",
		  help="")
parser.add_option("--isCount","--isCount",dest="isCount", default=False, action="store_true",
		  help="")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
hName           = options.hName
CR              = options.CR
isQCDMC         = options.isQCDMC
isChIsoM3       = options.isChIsoM3
is0PhoM3        = options.is0PhoM3
isMassLepGamma  = options.isMassLepGamma
isMassDilep     = options.isMassDilep
isCount         = options.isCount
print isCount

if isCount:
    shapeOrCount = "CountBased"
else:
    shapeOrCount = "ShapeBased"
#-----------------------------------------
#Path of the I/O histograms/datacards
#----------------------------------------
inFile = "%s/Hists/%s/%s/%s/Merged/%s/AllCat_%s.root"%(condorHistDir, year, decayMode, channel, shapeOrCount, hName)
print inFile
if CR=="":
    inHistDirBase   = "$PROCESS/$BIN/SR/Base"
    inHistDirSys    = "$PROCESS/$BIN/SR/$SYSTEMATIC"
    outFileDir      = "%s/Fit/%s/%s/%s/%s/%s/SR"%(condorHistDir, year, decayMode, channel, shapeOrCount, hName)
else:
    inHistDirBase   = "$PROCESS/$BIN/CR/%s/Base"%CR
    inHistDirSys    = "$PROCESS/$BIN/CR/%s/$SYSTEMATIC"%CR
    outFileDir      = "%s/Fit/%s/%s/%s/%s/%s/CR/%s"%(condorHistDir, year, decayMode, channel, shapeOrCount, hName, CR)
if not os.path.exists(outFileDir):
    os.makedirs(outFileDir)
outFilePath     = "%s/Shapes_Cat.root"%(outFileDir)
datacardPath    = "%s/Datacard_Cat.txt"%(outFileDir)
outFilePath     = "%s/Shapes_Cat.root"%(outFileDir)
datacardPath    = "%s/Datacard_Cat.txt"%(outFileDir)

cb = ch.CombineHarvester()
if isChIsoM3:
    #-----------------------------------
    # Make datacard 
    #-----------------------------------
    misIdBkg        = ["MisIdTTbar", "MisIdWGamma", "MisIdZGamma", "MisIdZJets", "MisIdOther"]
    genuineBkg      = ["GenuineTTbar", "GenuineWGamma", "GenuineZGamma", "GenuineZJets", "GenuineOther"]
    nonPromptBkg    = ["NonPromptTTbar","NonPromptWGamma","NonPromptZGamma", "NonPromptZJets", "NonPromptOther"]
    misIdSig        = ["MisIdTTGamma"]
    genuineSig      = ["GenuineTTGamma"]
    nonPromptSig    = ["NonPromptTTGamma"]
    AllBkg          = misIdBkg + genuineBkg + nonPromptBkg
    AllSig          = misIdSig + genuineSig + nonPromptSig
    allMC           = AllSig + AllBkg
    #------------------
    #Add observed data
    #------------------
    cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
    #------------------
    #Add sig& bkgs
    #------------------
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],misIdSig,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],genuineSig,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],nonPromptSig,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],misIdBkg,[(-1, hName)], False)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],genuineBkg,[(-1, hName)], False)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],nonPromptBkg,[(-1, hName)], False)
    #------------------
    #Add systematics
    #------------------
    cb.cp().process(allMC).AddSyst(cb, "lumi_$ERA", "lnN",  ch.SystMap()(1.025))
    cb.cp().process(allMC).AddSyst(cb, "BTagSF_b" , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "BTagSF_l" , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "PU"       , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "PhoEff"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "EleEff"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "MuEff"   ,  "shape",ch.SystMap()(1.0))
    #cb.cp().process(allMC).AddSyst(cb, "Q2"       , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "isr"      , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "fsr"      , "shape",ch.SystMap()(1.0))
    #------------------
    #Add rateParam
    #------------------
    #misID for all
    cb.cp().process(misIdBkg).bin([hName]).AddSyst(cb, 'MisIdSF', 'rateParam', ch.SystMap()(1.0))
    #for TTbar
    cb.cp().process(["MisIdTTbar", "GenuineTTbar"]).bin([hName]).AddSyst(cb, 'IsoTTbarSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["NonPromptTTbar"]).bin([hName]).AddSyst(cb, 'NpTTbarSF', 'rateParam', ch.SystMap()(1.0))

    #for WGamma
    cb.cp().process(["MisIdWGamma", "GenuineWGamma"]).bin([hName]).AddSyst(cb, 'IsoWGammaSF','rateParam',ch.SystMap()(1.0))
    cb.cp().process(["NonPromptWGamma"]).bin([hName]).AddSyst(cb, 'NpWGammaSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["MisIdWGamma", "GenuineWGamma", "NonPromptWGamma"]).bin([hName]).AddSyst(cb,'WGammaSF','rateParam',ch.SystMap()(1.0))
    
    #for ZGamma
    cb.cp().process(["MisIdZGamma", "GenuineZGamma"]).bin([hName]).AddSyst(cb, 'IsoZGammaSF','rateParam',ch.SystMap()(1.0))
    cb.cp().process(["NonPromptZGamma"]).bin([hName]).AddSyst(cb, 'NpZGammaSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["MisIdZGamma", "GenuineZGamma", "NonPromptZGamma"]).bin([hName]).AddSyst(cb,'ZGammaSF','rateParam',ch.SystMap()(1.0))
    
    #for ZJets
    cb.cp().process(["MisIdZJets", "GenuineZJets"]).bin([hName]).AddSyst(cb, 'IsoZJetsSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["NonPromptZJets"]).bin([hName]).AddSyst(cb, 'NpZJetsSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["MisIdZJets", "GenuineZJets", "NonPromptZJets"]).bin([hName]).AddSyst(cb,'ZJetsSF','rateParam',ch.SystMap()(1.0))
    
    #for Other
    cb.cp().process(["MisIdOther", "GenuineOther"]).bin([hName]).AddSyst(cb, 'IsoOtherSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["NonPromptOther"]).bin([hName]).AddSyst(cb, 'NpOtherSF', 'rateParam', ch.SystMap()(1.0))
    #------------------
    #Add syst groups
    #------------------
    cb.SetGroup("mySyst", ["lumi_13TeV", "BTagSF_b", "BTagSF_l", "PU"])
    cb.SetGroup("otherSyst", ["TTBarSF", "WGSF", "ZGSF", "PhoEff"])
    #------------------
    #Add autoMCStat
    #------------------
    cb.SetAutoMCStats(cb, 0, True, 1)
    #------------------
    #Get shape hists
    #------------------
    cb.cp().backgrounds().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    cb.cp().signals().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    #cb.cp().AddDatacardLineAtEnd("rrr \t param \t 1.0 \t 0.05\n")
    cb.WriteDatacard(datacardPath, outFilePath) 
    #------------------
    #Add param
    #------------------
    dc = open(datacardPath, "a")
    dc.write("MisIdSF \t param \t 1.0 \t 0.05\n")
    #TTbar
    dc.write("TTbarSF \t param \t 1.0 \t 0.05\n")
    dc.write("IsoTTbarSF \t param \t 1.0 \t 0.05\n")
    dc.write("NpTTbarSF \t param \t 1.0 \t 0.05\n")
    #WGamma
    dc.write("WGammaSF    \t param \t 1.0 \t 0.19\n")
    dc.write("IsoWGammaSF    \t param \t 1.0 \t 0.19\n")
    dc.write("NpWGammaSF    \t param \t 1.0 \t 0.19\n")
    #ZGamma
    dc.write("ZGammaSF    \t param \t 1.0 \t 0.21\n")
    dc.write("IsoZGammaSF    \t param \t 1.0 \t 0.21\n")
    dc.write("NpZGammaSF    \t param \t 1.0 \t 0.21\n")
    #ZJets
    dc.write("ZJetsSF    \t param \t 1.0 \t 0.21\n")
    dc.write("IsoZJetsSF    \t param \t 1.0 \t 0.21\n")
    dc.write("NpZJetsSF    \t param \t 1.0 \t 0.21\n")
    #Other
    dc.write("IsoOtherSF \t param \t 1.0 \t 0.30\n")
    dc.write("NpOtherSF \t param \t 1.0 \t 0.30\n")
    dc.close()

if is0PhoM3:
    AllBkg = ["TTbar", "WGamma", "ZGamma", "ZJets", "Other"] 
    Signal  = ["TTGamma"]
    allMC   = Signal + AllBkg
    #------------------
    #Add observed data
    #------------------
    cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
    #------------------
    #Add sig& bkgs
    #------------------
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],Signal,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],AllBkg,[(-1, hName)], False)
    #------------------
    #Add systematics
    #------------------
    cb.cp().process(allMC).AddSyst(cb, "lumi_$ERA", "lnN"  ,ch.SystMap()(1.025))
    cb.cp().process(allMC).AddSyst(cb, "BTagSF_b" , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "BTagSF_l" , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "PU"       , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "PhoEff"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "EleEff"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "MuEff"   , "shape",ch.SystMap()(1.0))
    #cb.cp().process(["TTGamma", "TTbar"]).AddSyst(cb, "Q2" , "shape",ch.SystMap()(1.0))
    cb.cp().process(["TTGamma"]).AddSyst(cb, "isr"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(["TTGamma"]).AddSyst(cb, "fsr"   , "shape",ch.SystMap()(1.0))
    #------------------
    #Add rateParam
    #------------------
    cb.cp().process(["WGamma"]).bin([hName]).AddSyst(cb, 'WGammaSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["ZGamma"]).bin([hName]).AddSyst(cb, 'ZGammaSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["ZJets"]).bin([hName]).AddSyst(cb,  'ZJetsSF', 'rateParam', ch.SystMap()(1.0))
    #------------------
    #Add syst groups
    #------------------
    cb.SetGroup("mySyst", ["lumi_13TeV", "BTagSF_b", "BTagSF_l", "PU"])
    cb.SetGroup("otherSyst", ["TTBarSF", "WGSF", "ZGSF", "PhoEff"])
    #------------------
    #Add autoMCStat
    #------------------
    cb.SetAutoMCStats(cb, 0, True, 1)
    #------------------
    #Get shape hists
    #------------------
    cb.cp().backgrounds().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    cb.cp().signals().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    cb.WriteDatacard(datacardPath, outFilePath) 
    #------------------
    #Add param
    #------------------
    dc = open(datacardPath, "a")
    dc.write("WGammaSF    \t param \t 1.0 \t 0.19\n")
    dc.write("ZGammaSF    \t param \t 1.0 \t 0.21\n")
    dc.write("ZJetsSF    \t param \t 1.0 \t 0.21\n")
    dc.close()

if isMassLepGamma:
    AllBkg = ["OtherPhotonsZGamma","OtherPhotonsWGamma", "OtherPhotonsZJets", "OtherPhotonsOthers"]
    Signal  = ["MisIdPhotonZJets", "MisIdPhotonOther"]
    allMC   = Signal + AllBkg
    #------------------
    #Add observed data
    #------------------
    cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
    #------------------
    #Add sig& bkgs
    #------------------
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],Signal,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],AllBkg,[(-1, hName)], False)
    #------------------
    #Add systematics
    #------------------
    cb.cp().process(allMC).AddSyst(cb, "lumi_$ERA", "lnN"  ,ch.SystMap()(1.025))
    cb.cp().process(allMC).AddSyst(cb, "BTagSF_b" , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "BTagSF_l" , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "PU"       , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "PhoEff"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "EleEff"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "MuEff"   , "shape",ch.SystMap()(1.0))
    #cb.cp().process(["TTGamma", "TTbar"]).AddSyst(cb, "Q2" , "shape",ch.SystMap()(1.0))
    cb.cp().process(["TTGamma"]).AddSyst(cb, "isr"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(["TTGamma"]).AddSyst(cb, "fsr"   , "shape",ch.SystMap()(1.0))
    #------------------
    #Add rateParam
    #------------------
    cb.cp().process(["MisIdPhotonOther"]).bin([hName]).AddSyst(cb,    'MisIdSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["MisIdPhotonZJets"]).bin([hName]).AddSyst(cb,    'MisIdSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["MisIdPhotonZJets"]).bin([hName]).AddSyst(cb,    'ZJetsSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["OtherPhotonsZGamma"]).bin([hName]).AddSyst(cb, 'ZGammaSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["OtherPhotonsWGamma"]).bin([hName]).AddSyst(cb, 'WGammaSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["OtherPhotonsZJets"]).bin([hName]).AddSyst(cb, 'ZJetsSF', 'rateParam', ch.SystMap()(1.0))
    #------------------
    #Add syst groups
    #------------------
    #cb.SetGroup("mySyst", ["lumi_13TeV", "BTagSF_b", "BTagSF_l", "PU"])
    #cb.SetGroup("otherSyst", ["TTBarSF", "WGSF", "ZGSF", "PhoEff"])
    #------------------
    #Add autoMCStat
    #------------------
    cb.SetAutoMCStats(cb, 0, True, 1)
    #------------------
    #Get shape hists
    #------------------
    cb.cp().backgrounds().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    cb.cp().signals().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    cb.WriteDatacard(datacardPath, outFilePath) 
    #------------------
    #Add param
    #------------------
    dc = open(datacardPath, "a")
    dc.write("MisIdSF \t param \t 1.0 \t 0.05\n")
    dc.write("ZGammaSF    \t param \t 1.0 \t 0.21\n")
    dc.write("ZJetsSF    \t param \t 1.0 \t 0.21\n")
    dc.write("WGammaSF    \t param \t 1.0 \t 0.19\n")
    dc.close()

if isMassDilep:
    AllBkg  = ["OthersDilep"]
    Signal  = ["ZJetsDilep"]
    allMC   = Signal + AllBkg
    #------------------
    #Add observed data
    #------------------
    cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
    #------------------
    #Add sig& bkgs
    #------------------
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],Signal,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],AllBkg,[(-1, hName)], False)
    cb.SetAutoMCStats(cb, 0, True, 1)
    #------------------
    #Add systematics
    #------------------
    cb.cp().process(allMC).AddSyst(cb, "lumi_$ERA", "lnN"  ,ch.SystMap()(1.025))
    cb.cp().process(allMC).AddSyst(cb, "BTagSF_b" , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "BTagSF_l" , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "PU"       , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "PhoEff"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "EleEff"   , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "MuEff"    , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "isr"      , "shape",ch.SystMap()(1.0))
    cb.cp().process(allMC).AddSyst(cb, "fsr"      , "shape",ch.SystMap()(1.0))
    #cb.cp().process(allMC).AddSyst(cb, "Q2" , "shape",ch.SystMap()(1.0))
    #------------------
    #Add rateParam
    #------------------
    cb.cp().process(Signal).bin([hName]).AddSyst(cb, 'ZJetsSF', 'rateParam', ch.SystMap()(1.0))
    #------------------
    #Add autoMCStat
    #------------------
    cb.SetAutoMCStats(cb, 0, True, 1)
    #------------------
    #------------------
    #Get shape hists
    #------------------
    cb.cp().backgrounds().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    cb.cp().signals().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    cb.WriteDatacard(datacardPath, outFilePath) 
    #------------------
    #Add param
    #------------------
    dc = open(datacardPath, "a")
    dc.write("ZJetsSF    \t param \t 1.0 \t 0.21\n")
    dc.close()

if isChIsoM3 or is0PhoM3 or isMassLepGamma or isMassDilep:
    #------------------
    #print various info
    #------------------
    #print cb.PrintAll()
    #print cb.PrintObs();
    #print cb.PrintProcs();
    #print cb.PrintSysts();
    print cb.PrintParams();
    print outFilePath
    print datacardPath

    #------------------------
    #Save DC path in a file
    #------------------------
    if CR=="":
        name  = "DC_%s_%s_%s_%s_%s_SR"%(year, decayMode, channel, shapeOrCount, hName)
    else:
        name  = "DC_%s_%s_%s_%s_%s_CR_%s"%(year, decayMode, channel, shapeOrCount, hName, CR)
    if not os.path.exists("./DataCards.json"):
        with open("DataCards.json", "w") as f:
            data = {}
            json.dump(data, f)
    with open ('DataCards.json') as jsonFile:
        jsonData = json.load(jsonFile)
    jsonData[name] = []
    jsonData[name].append(datacardPath)
    with open ('DataCards.json', 'w') as jsonFile:
        json.dump(jsonData, jsonFile)
