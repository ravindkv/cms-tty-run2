from ROOT import *
import sys
from sampleInformation import *
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s", "--sample", dest="sample", default="",type='str',
                     help="Specify which sample to run on" )
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                     help="Use 4j2t selection" )
parser.add_option("--Loose","--loose", dest="isLooseSelection", default=False,action="store_true",
                     help="Use 2j0t selection" )
parser.add_option("--LooseCR","--looseCR", dest="isLooseCRSelection", default=False,action="store_true",
		  help="Use 2j exactly 0t control region selection" )
parser.add_option("--addPlots","--addOnly", dest="onlyAddPlots", default=False,action="store_true",
                     help="Use only if you want to add a couple of plots to the file, does not remove other plots" )

(options, args) = parser.parse_args()

gROOT.SetBatch(True)

finalState = options.channel
sample = options.sample
isTightSelection = options.isTightSelection
isLooseSelection = options.isLooseSelection
isLooseCRSelection = options.isLooseCRSelection

nBJets = -1

btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])","(btagWeight[0])"]

if finalState=="Mu":
    sampleList[-1] = "DataMu"
    sampleList[-2] = "QCDMu"
    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples_2019/qcdmuons/V08_00_26_07"
    outputhistName = "histograms/mu/qcdhistsCR.root"
    extraCuts            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=3)*"
    extraPhotonCuts      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=3 && %s)*"
    if isTightSelection:
        extraCuts            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4)*"
        extraPhotonCuts      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && %s)*"
        outputhistName = "histograms/mu/qcdhistsCR_Tight.root"
    if isLooseSelection or isLooseCRSelection:
        extraCuts            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2)*"
        extraPhotonCuts      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && %s)*"
        outputhistName = "histograms/mu/qcdhistsCR_Loose.root"

if finalState=="Ele":
    sampleList[-1] = "DataEle"
    sampleList[-2] = "QCDEle"
    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples_2019/qcdelectrons/V08_00_26_07"
    outputhistName = "histograms/ele/qcdhistsCR.root"
    extraCuts            = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=3)*"
    extraPhotonCuts      = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=3 && %s)*"
    if isTightSelection:
        extraCuts            = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=4)*"
        extraPhotonCuts      = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=4 && %s)*"
        outputhistName = "histograms/ele/qcdhistsCR_Tight.root"
    if isLooseSelection or isLooseCRSelection:
        extraCuts            = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=2)*"
        extraPhotonCuts      = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=2 && %s)*"
        outputhistName = "histograms/ele/qcdhistsCR_Loose.root"

# if "CR2" in sys.argv:
#     extraCuts            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2)*"
#     extraPhotonCuts      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && %s)*"
#     sys.argv.remove("CR2")
#     outputhistName = outputhistName.replace("qcdhistsCR.root","qcdhistsCR2.root")



weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*%s"%btagWeightCategory[nBJets]


if not sample in sampleList:
    print "Sample isn't in list"
    print sampleList
    sys.exit()


tree = TChain("AnalysisTree")
fileList = samples[sample][0]
for fileName in fileList:
    tree.Add("%s/QCDcr_%s"%(analysisNtupleLocation,fileName))

print sample

print "Number of events:", tree.GetEntries()


from HistogramListDict import *

histogramInfo = GetHistogramInfo(extraCuts, extraPhotonCuts, nBJets)
histogramsToMake = histogramInfo.keys()
histogramsToMake.sort()



histograms = []

for hist in histogramsToMake:
    h_Info = histogramInfo[hist]

    if not h_Info[5]: continue

    print "filling", h_Info[1], sample

    evtWeight = ""
    histograms.append(TH1F("%s_%s"%(h_Info[1],sample),"%s_%s"%(h_Info[1],sample),h_Info[2][0],h_Info[2][1],h_Info[2][2]))
    if h_Info[4]=="":
        evtWeight = "%s%s"%(h_Info[3],weights)
    else:
        evtWeight = h_Info[4]
        
    if "Data" in sample:
        evtWeight = h_Info[3]

    if evtWeight[-1]=="*":
        evtWeight= evtWeight[:-1]
    tree.Draw("%s>>%s_%s"%(h_Info[0],h_Info[1],sample),evtWeight)


outputFile = TFile(outputhistName,"update")
if sample=="QCDMu":
    outputFile.rmdir(sample+"_MC")
    outputFile.mkdir(sample+"_MC")
    outputFile.cd(sample+"_MC")
else:
    outputFile.rmdir(sample)
    outputFile.mkdir(sample)
    outputFile.cd(sample)
for h in histograms:
    h.Write()

outputFile.Close()
