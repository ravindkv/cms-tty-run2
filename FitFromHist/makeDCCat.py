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
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
hName           = options.hName
CR              = options.CR
isQCDMC         = options.isQCDMC
isChIsoM3         = options.isChIsoM3
is0PhoM3          = options.is0PhoM3
isMassLepGamma      = options.isMassLepGamma
isMassDilep         = options.isMassDilep

#-----------------------------------------
#Path of the I/O histograms/datacards
#----------------------------------------
inFile = "%s/Hists/%s/%s/%s/Merged/AllCat_%s.root"%(condorHistDir, year, decayMode, channel,hName)
print inFile
if CR=="":
    inHistDirBase   = "$PROCESS/$BIN/SR/Base"
    inHistDirSys    = "$PROCESS/$BIN/SR/$SYSTEMATIC"
    outFileDir      = "%s/Fit/%s/%s/%s/DataCard/SR"%(condorHistDir, year, decayMode, channel)
else:
    inHistDirBase   = "$PROCESS/$BIN/CR/%s/Base"%CR
    inHistDirSys    = "$PROCESS/$BIN/CR/%s/$SYSTEMATIC"%CR
    outFileDir      = "%s/Fit/%s/%s/%s/DataCard/CR/%s"%(condorHistDir, year, decayMode, channel, CR)
outFilePath     = "%s/Shapes_Cat_%s.root"%(outFileDir, hName)
datacardPath    = "%s/Datacard_Cat_%s.txt"%(outFileDir, hName)

if not os.path.exists(outFileDir):
    os.makedirs(outFileDir)

cb = ch.CombineHarvester()
if isChIsoM3:
    #-----------------------------------
    # Make datacard 
    #-----------------------------------
    isolatedBkg    = ["isolatedTTbar", "isolatedWGamma", "isolatedZGamma", "isolatedOther"]
    nonPromptBkg   = ["nonPromptTTbar","nonPromptWGamma","nonPromptZGamma","nonPromptOther"]
    isolatedSig    = ["isolatedTTGamma"]
    nonPromptSig   = ["nonPromptTTGamma"]
    AllBkgs        = isolatedBkg +  nonPromptBkg
    allSig         = isolatedSig +  nonPromptSig
    allMC          = allSig + AllBkgs
    #------------------
    #Add observed data
    #------------------
    cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
    #------------------
    #Add sig& bkgs
    #------------------
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],isolatedSig,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],isolatedBkg,[(-1, hName)], False)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],nonPromptSig,[(-1, hName)], True)
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
    cb.cp().process(["isolatedTTbar", "nonPromptTTbar"]).bin([hName]).AddSyst(cb, 'TTbarSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["isolatedWGamma", "nonPromptWGamma"]).bin([hName]).AddSyst(cb, 'WGSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["isolatedZGamma", "nonPromptZGamma"]).bin([hName]).AddSyst(cb, 'ZGSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["isolatedOther", "nonPromptOther"]).bin([hName]).AddSyst(cb,  'OtherSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(nonPromptBkg).bin([hName]).AddSyst(cb, 'nonPromptSF', 'rateParam', ch.SystMap()(1.0))
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
    dc.write("TTbarSF \t param \t 1.0 \t 0.05\n")
    dc.write("WGSF    \t param \t 1.0 \t 0.10\n")
    dc.write("ZGSF    \t param \t 1.0 \t 0.10\n")
    dc.write("OtherSF \t param \t 1.0 \t 0.30\n")
    dc.close()

if is0PhoM3:
    AllBkgs = ["TTbar", "WGamma", "ZGamma", "Other"] 
    Signal  = ["TTGamma"]
    allMC   = Signal + AllBkgs
    #------------------
    #Add observed data
    #------------------
    cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
    #------------------
    #Add sig& bkgs
    #------------------
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],Signal,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],AllBkgs,[(-1, hName)], False)
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
    cb.cp().process(["TTbar"]).bin([hName]).AddSyst(cb, 'TTbarSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["WGamma"]).bin([hName]).AddSyst(cb, 'WGSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["ZGamma"]).bin([hName]).AddSyst(cb, 'ZGSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["Other"]).bin([hName]).AddSyst(cb,  'OtherSF', 'rateParam', ch.SystMap()(1.0))
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
    dc.write("TTbarSF \t param \t 1.0 \t 0.05\n")
    dc.write("WGSF    \t param \t 1.0 \t 0.19\n")
    dc.write("ZGSF    \t param \t 1.0 \t 0.21\n")
    dc.write("OtherSF \t param \t 1.0 \t 0.30\n")
    dc.close()

if isMassLepGamma:
    AllBkgs = ["OtherPhotonsZGamma","OtherPhotonsWGamma","OtherPhotonsOthers"]
    Signal  = ["MisIDPhotonAll"]
    allMC   = Signal + AllBkgs
    #------------------
    #Add observed data
    #------------------
    cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
    #------------------
    #Add sig& bkgs
    #------------------
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],Signal,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],AllBkgs,[(-1, hName)], False)
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
    cb.cp().process(["OtherPhotonsZGamma"]).bin([hName]).AddSyst(cb, 'OtherPhotonsZGammaSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["OtherPhotonsWGamma"]).bin([hName]).AddSyst(cb, 'OtherPhotonsWGammaSF', 'rateParam', ch.SystMap()(1.0))
    cb.cp().process(["OtherPhotonsOthers"]).bin([hName]).AddSyst(cb,  'OtherPhotonsOthersSF', 'rateParam', ch.SystMap()(1.0))
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
    dc.write("OtherPhotonsOthersSF \t param \t 1.0 \t 0.10\n")
    dc.close()

if isMassDilep:
    AllBkgs = ["Others"]
    Signal  = ["ZJets"]
    allMC   = Signal + AllBkgs
    #------------------
    #Add observed data
    #------------------
    cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
    #------------------
    #Add sig& bkgs
    #------------------
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],Signal,[(-1, hName)], True)
    cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],AllBkgs,[(-1, hName)], False)
    cb.SetAutoMCStats(cb, 0, True, 1)
    #------------------
    #Get shape hists
    #------------------
    cb.cp().backgrounds().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    cb.cp().signals().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
    cb.WriteDatacard(datacardPath, outFilePath) 

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
        name  = "DC_%s_%s_%s_SR_%s"%(year, decayMode, channel, hName)
    else:
        name  = "DC_%s_%s_%s_CR_%s_%s"%(year, decayMode, channel, CR, hName)
    with open ('DataCards.json') as jsonFile:
        jsonData = json.load(jsonFile)
    jsonData[name] = []
    jsonData[name].append(datacardPath)
    with open ('DataCards.json', 'w') as jsonFile:
        json.dump(jsonData, jsonFile)
