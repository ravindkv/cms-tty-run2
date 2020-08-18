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
parser.add_option("--hist", "--hist", dest="hName", default="presel_Njet",type='str', 
                     help="which histogram to be used for making datacard")
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--isQCDMC","--qcdMC",dest="isQCDMC", default=False, action="store_true",
		  help="")
(options, args) = parser.parse_args()
year            = options.year
decayMode  = options.decayMode
channel         = options.channel
hName        = options.hName
CR   = options.CR
isQCDMC        = options.isQCDMC

#-----------------------------------------
#Path of the I/O histograms/datacards
#----------------------------------------
inFileSubDir = "./Merged"
#inFileSubDir = "Hists/%s/%s/%s/Merged"%(year, decayMode, channel)
inFileFullDir = "%s/%s"%(condorHistDir, inFileSubDir)
if CR=="":
    outFileSubDir   = "Fit/%s/%s/%s/SR"%(year, decayMode, channel)
    outFileFullDir  = "%s/%s"%(condorHistDir, outFileSubDir)
    outFileFullPath = "%s/Shapes_%s_%s_%s_%s_SR.root"%(outFileFullDir, year, decayMode, channel, hName)
    datacardPath    = "%s/datacard_%s_%s_%s_%s_SR.txt"%(outFileFullDir, year, decayMode, channel, hName)
else:
    outFileSubDir   = "Fit/%s/%s/%s/CR/%s"%(year, decayMode, channel, CR)
    outFileFullDir  = "%s/%s"%(condorHistDir, outFileSubDir)
    outFileFullPath = "%s/Shapes_%s_%s_%s_%s_CR_%s.root"%(outFileFullDir, year, decayMode, channel, hName, CR)
    datacardPath    = "%s/datacard_%s_%s_%s_%s_CR_%s.txt"%(outFileFullDir, year, decayMode, channel, hName, CR)
if not os.path.exists(outFileFullDir):
    os.makedirs(outFileFullDir)

#-----------------------------------
# Write final histograms in the file
#-----------------------------------
outputFile = TFile(outFileFullPath,"update")
#For nominal histograms
for sample in SamplesBase:
    if CR=="":
        inHistDir  = "Base/SignalRegion/%s"%hName
    else:
        inHistDir  = "Base/ControlRegion/%s/%s"%(CR, hName)
    rootFile = TFile("%s/%s.root"%(inFileFullDir,sample), "read")
    h = rootFile.Get(inHistDir).Clone("nominal")
    if sample=="Data":
        outHistDir = "%s/data_obs"%hName
    else:
        outHistDir = "%s/%s"%(hName,sample)
    if not outputFile.GetDirectory(outHistDir):
        outputFile.mkdir(outHistDir)
    outputFile.cd(outHistDir)
    gDirectory.Delete("%s;*"%(h.GetName()))
    print "%s, \t%s, \t%s, \t%s"%(hName, sample, h.GetName(), h.Integral())
    h.Write()

#For syst up/down histograms
print "\n --------- For Sys -------------"
for sample, syst, level in itertools.product(SamplesSyst, Systematics, SystLevel):
    if CR=="":
        inHistDir  = "%s%s/SignalRegion/%s"%(syst, level, hName)
    else:
        inHistDir  = "%s%s/ControlRegion/%s/%s"%(syst, level, CR, hName)
    rootFile = TFile("%s/%s.root"%(inFileFullDir,sample), "read")
    hSys = rootFile.Get(inHistDir).Clone("%s%s"%(syst, level))
    print "%s, \t%s, \t%s, \t%s"%(hName, sample, hSys.GetName(), hSys.Integral())
    outHistDir = "%s/%s"%(hName,sample)
    if not outputFile.GetDirectory(outHistDir):
        outputFile.mkdir(outHistDir)
    outputFile.cd(outHistDir)
    gDirectory.Delete("%s;*"%(hSys.GetName()))
    hSys.Write()
outputFile.Close()
#-----------------------------------
# Make datacard 
#-----------------------------------
AllBkgs = ["TTbar", "TGJets", "WGamma", "ZGamma"] 
#AllBkgs = ["TTbar", "TGJets", "WJets", "ZJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","GJets", "QCD"]
Signal  = ["TTGamma"]
cb = ch.CombineHarvester()
#------------------
cb.AddObservations(["*"],["ttgamma"],["13TeV"],[channel],[(-1, hName)])
#------------------
cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],Signal,[(-1, hName)], True)
cb.AddProcesses(["*"],["ttgamma"],["13TeV"],[channel],AllBkgs,[(-1, hName)], False)
#------------------
cb.cp().process(Signal+AllBkgs).AddSyst(cb, "lumi_$ERA", "lnN",ch.SystMap("era") (["13TeV"], 1.025))
cb.cp().process(Signal+AllBkgs).AddSyst(cb, "BTagSF_b" , "shape",ch.SystMap("era") (["13TeV"], 1.0))
cb.cp().process(Signal+AllBkgs).AddSyst(cb, "BTagSF_l" , "shape",ch.SystMap("era") (["13TeV"], 1.0))
cb.cp().process(Signal+AllBkgs).AddSyst(cb, "PU"       , "shape",ch.SystMap("era") (["13TeV"], 1.0))
cb.cp().process(Signal+AllBkgs).AddSyst(cb, "PhoEff"   , "shape",ch.SystMap("era") (["13TeV"], 1.0))
cb.cp().process(Signal+AllBkgs).AddSyst(cb, "EleEff"   , "shape",ch.SystMap("era") (["13TeV"], 1.0))
cb.cp().process(["TTGamma", "TTbar"]).AddSyst(cb, "Q2" , "shape",ch.SystMap("era") (["13TeV"], 1.0))
cb.cp().process(["TTGamma"]).AddSyst(cb, "isr"   , "shape",ch.SystMap("era") (["13TeV"], 1.0))
cb.cp().process(["TTGamma"]).AddSyst(cb, "fsr"   , "shape",ch.SystMap("era") (["13TeV"], 1.0))
#------------------
cb.cp().process(["TTbar"]).bin([hName]).AddSyst(cb, 'SFTTbar', 'rateParam', ch.SystMap()(1.0))
cb.cp().GetParameter("SFTTbar").set_range(1.0, 0.05)
cb.cp().process(["WGamma"]).bin([hName]).AddSyst(cb, 'SFWG', 'rateParam', ch.SystMap()(1.0))
cb.cp().GetParameter("SFWG").set_range(1.0, 0.19)
cb.cp().process(["ZGamma"]).bin([hName]).AddSyst(cb, 'SFZG', 'rateParam', ch.SystMap()(1.0))
cb.cp().GetParameter("SFZG").set_range(1.0, 0.21)
#------------------
fileName = "Fit/2016/SemiLep/Mu/SR/Shapes_2016_SemiLep_Mu_presel_Njet_SR.root" 
cb.cp().backgrounds().ExtractShapes(fileName,"$BIN/$PROCESS/nominal","$BIN/$PROCESS/$SYSTEMATIC")
cb.cp().signals().ExtractShapes(fileName,"$BIN/$PROCESS/nominal","$BIN/$PROCESS/$SYSTEMATIC")
g=TFile("ttgamma_mu.input.root","recreate")
g.Close()
cb.WriteDatacard("card.txt", "ttgamma_mu.input.root")
print cb.PrintAll()
