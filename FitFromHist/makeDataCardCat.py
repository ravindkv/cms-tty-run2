from ROOT import TFile, TH1F, gDirectory
import os
import sys
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
parser.add_option("-d", "--decayMode", dest="decayMode", default="SemiLep",type='str',
                     help="Specify which decayMode moded of ttbar SemiLep or DiLep? default is SemiLep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--hist", "--hist", dest="hName", default="phosel_M3",type='str', 
                     help="which histogram to be used for making datacard")
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--isQCDMC","--qcdMC",dest="isQCDMC", default=False, action="store_true",
		  help="")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
hName           = options.hName
CR              = options.CR
isQCDMC         = options.isQCDMC

#-----------------------------------------
#Path of the I/O histograms/datacards
#----------------------------------------
inFile = "%s/Hists/%s/%s/%s/Merged/AllCat.root"%(condorHistDir, year, decayMode, channel)
if CR=="":
    inHistDirBase   = "$BIN/SR/$PROCESS/Base"
    inHistDirSys    = "$BIN/SR/$PROCESS/$SYSTEMATIC"
    outFileDir      = "%s/Fit/DataCard/Cat/%s/%s/%s/SR"%(condorHistDir, year, decayMode, channel)
else:
    inHistDirBase   = "$BIN/CR/%s/$PROCESS/Base"%CR
    inHistDirSys    = "$BIN/CR/%s/$PROCESS/$SYSTEMATIC"%CR
    outFileDir      = "%s/Fit/DataCard/Cat/%s/%s/%s/CR/%s"%(condorHistDir, year, decayMode, channel, CR)

outFilePath     = "%s/Shapes_%s.root"%(outFileDir, hName)
datacardPath    = "%s/Datacard_%s.txt"%(outFileDir, hName)
if not os.path.exists(outFileDir):
    os.makedirs(outFileDir)

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
cb = ch.CombineHarvester()
#------------------
cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
#------------------
cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],isolatedSig,[(-1, hName)], True)
cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],isolatedBkg,[(-1, hName)], False)
cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],nonPromptSig,[(-1, hName)], True)
cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],nonPromptBkg,[(-1, hName)], False)
#------------------
cb.cp().process(allMC).AddSyst(cb, "lumi_$ERA", "lnN",  ch.SystMap()(1.025))
cb.cp().process(allMC).AddSyst(cb, "BTagSF_b" , "shape",ch.SystMap()(1.0))
cb.cp().process(allMC).AddSyst(cb, "BTagSF_l" , "shape",ch.SystMap()(1.0))
cb.cp().process(allMC).AddSyst(cb, "PU"       , "shape",ch.SystMap()(1.0))
cb.cp().process(allMC).AddSyst(cb, "PhoEff"   , "shape",ch.SystMap()(1.0))
cb.cp().process(allMC).AddSyst(cb, "EleEff"   , "shape",ch.SystMap()(1.0))
cb.cp().process(allMC).AddSyst(cb, "Q2"       , "shape",ch.SystMap()(1.0))
cb.cp().process(allMC).AddSyst(cb, "isr"      , "shape",ch.SystMap()(1.0))
cb.cp().process(allMC).AddSyst(cb, "fsr"      , "shape",ch.SystMap()(1.0))
#------------------
cb.cp().process(["*TTbar"]).bin([hName]).AddSyst(cb, 'TTbarSF', 'rateParam', ch.SystMap()(1.0))
#cb.cp().GetParameter("TTbarSF").set_range(1.0, 0.05)
cb.cp().process(["*WGamma"]).bin([hName]).AddSyst(cb, 'WGSF', 'rateParam', ch.SystMap()(1.0))
#cb.cp().GetParameter("WGSF").set_range(1.0, 0.19)
cb.cp().process(["*ZGamma"]).bin([hName]).AddSyst(cb, 'ZGSF', 'rateParam', ch.SystMap()(1.0))
#cb.cp().GetParameter("ZGSF").set_range(1.0, 0.21)
cb.cp().process(["*Other"]).bin([hName]).AddSyst(cb,  'OtherSF', 'rateParam', ch.SystMap()(1.0))
#cb.cp().GetParameter("OtherSF").set_range(1.0, 0.21)
#------------------
cb.cp().backgrounds().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
cb.cp().signals().ExtractShapes(inFile, inHistDirBase, inHistDirSys)
g=TFile(outFilePath,"recreate")
g.Close()
cb.WriteDatacard(datacardPath, outFilePath) 
print cb.PrintAll()
print outFilePath
print datacardPath
