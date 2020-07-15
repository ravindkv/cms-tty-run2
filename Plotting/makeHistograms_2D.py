from ROOT import TH1F, TH2D, TFile, TChain, TCanvas
import sys
from sampleInformation import *
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s", "--sample", dest="sample", default="",type='str',
                  help="Specify which sample to run on" )
parser.add_option("--syst", "--systematic", dest="systematic", default="nominal",type='str',
                  help="Specify up, down or nominal, default is nominal")
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                  help="Use 4j2t selection" )
parser.add_option("--Loose","--loose", dest="isLooseSelection", default=False,action="store_true",
                  help="Use 2j0t selection" )
parser.add_option("--LooseCR","--looseCR", dest="isLooseCRSelection", default=False,action="store_true",
		  help="Use 2j exactly 0t control region selection" )
parser.add_option("--addPlots","--addOnly", dest="onlyAddPlots", default=False,action="store_true",
                  help="Use only if you want to add a couple of plots to the file, does not remove other plots" )
parser.add_option("--output", dest="outputFileName", default="hists_2d",
                  help="Give the name of the directory for root fileto be saved in (default is hists_2d)" )
parser.add_option("--plot", dest="plotList",action="append",
                  help="Add plots" )
parser.add_option("--allPlots","--AllPlots", dest="makeAllPlots",action="store_true",default=False,
                     help="Make full list of plots in histogramDict" )
parser.add_option("--morePlots","--MorePlots","--makeMorePlots", dest="makeMorePlots",action="store_true",default=False,
                     help="Make larger list of plots in histogramDict (mostly object kinematics)" )
parser.add_option("--quiet", "-q", dest="quiet",default=False,action="store_true",
                     help="Quiet outputs" )

(options, args) = parser.parse_args()

level =options.systematic

gROOT.SetBatch(True)

finalState = options.channel
sample = options.sample
isTightSelection = options.isTightSelection
isLooseSelection = options.isLooseSelection
isLooseCRSelection = options.isLooseCRSelection
onlyAddPlots = options.onlyAddPlots
outputFileName = options.outputFileName

makeAllPlots = options.makeAllPlots
makeMorePlots = options.makeMorePlots

runQuiet = options.quiet

#print isTightSelection
#print isLooseSelection

nJets = 3
nBJets = 1



if finalState=="Mu":
    sampleList[-1] = "DataMu"
    sampleList[-2] = "QCDMu"

    if sample=="Data":
        sample = "DataMu"
    if sample=="QCD":
        sample = "QCDMu"

    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples/muons/V08_00_26_07/"
    outputhistName = "histograms/mu/%s"%outputFileName

    extraCuts            = "(passPresel_Mu && nJet>=3 && nBJet>=1)*"
    extraPhotonCuts      = "(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*"

    extraCutsTight       = "(passPresel_Mu && nJet>=4 && nBJet>=2)*"
    extraPhotonCutsTight = "(passPresel_Mu && nJet>=4 && nBJet>=2 && %s)*"

    extraCutsLoose       = "(passPresel_Mu && nJet==2 && nBJet==0)*"
    extraPhotonCutsLoose = "(passPresel_Mu && nJet==2 && nBJet==0 && %s)*"

    extraCutsLooseCR       = "(passPresel_Mu && nJet>=2 && nBJet>=0)*"
    extraPhotonCutsLooseCR = "(passPresel_Mu && nJet>=2 && nBJet>=0 && %s)*"

elif finalState=="Ele":
    sampleList[-1] = "DataEle"
    sampleList[-2] = "QCDEle"

    if sample=="Data":
        sample = "DataEle"
    if sample=="QCD":
        sample = "QCDEle"

    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples/electrons/V08_00_26_07/"
    outputhistName = "histograms/ele/%s"%outputFileName

    extraCuts            = "(passPresel_Ele && nJet>=3 && nBJet>=1)*"
    extraPhotonCuts      = "(passPresel_Ele && nJet>=3 && nBJet>=1 && %s)*"

    extraCutsTight       = "(passPresel_Ele && nJet>=4 && nBJet>=2)*"
    extraPhotonCutsTight = "(passPresel_Ele && nJet>=4 && nBJet>=2 && %s)*"

    extraCutsLoose       = "(passPresel_Ele && nJet==2 && nBJet==0)*"
    extraPhotonCutsLoose = "(passPresel_Ele && nJet==2 && nBJet==0 && %s)*"

    extraCutsLooseCR       = "(passPresel_Ele && nJet>=2 && nBJet>=0)*"
    extraPhotonCutsLooseCR = "(passPresel_Ele && nJet>=2 && nBJet>=0 && %s)*"
else:
    print "Unknown final state, options are Mu and Ele"
    sys.exit()


Pileup ="PUweight"
MuEff = "muEffWeight"
btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]


if 'PU' in sys.argv:

    Pileup = "PUweight_%s"%(level)
    sys.argv.remove("PU")
    outputhistName = outputhistName.replace(".root","Pileup_%s.root"%(level))

if 'MuEff' in sys.argv:
    MuEff = "muEffWeight_%s"%(level)

    sys.argv.remove("MuEff")
    outputhistName = outputhistName.replace(".root","_MuEff_%s.root"%(level))


if 'BTagSF' in sys.argv:

    btagWeightCategory = ["1","(1-btagWeight_%s[0])"%(level),"(btagWeight_%s[2])"%(level),"(btagWeight_%s[1])"%(level)]


    sys.argv.remove("BTagSF")
    outputhistName = outputhistName.replace(".root","_BTagSF_%s.root"%(level))




weights = "evtWeight*%s*muEffWeight*eleEffWeight*%s"%(Pileup,btagWeightCategory[nBJets])

if isTightSelection:
    if not runQuiet: print "Tight Select"
    nJets = 4
    nBJets = 2
    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
    extraCuts = extraCutsTight 
    extraPhotonCuts = extraPhotonCutsTight 
    outputhistName = outputhistName.replace(".root","_tight.root")

if isLooseSelection:
    if not runQuiet: print "Loose Select"
    nJets = 2
    nBJets = 0
    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*(btagWeight[0])"
    extraCuts = extraCutsLoose
    extraPhotonCuts = extraPhotonCutsLoose
    outputhistName = outputhistName.replace(".root","_loose.root")

if isLooseCRSelection:
    if not runQuiet: print "Loose Control Region Select"
    nJets = 2
    nBJets = 0
    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*1" #*(btagWeight[2])"
    extraCuts = extraCutsLooseCR
    extraPhotonCuts = extraPhotonCutsLooseCR
    outputhistName = outputhistName.replace(".root","_looseCR.root")

from HistogramListDict import *
histogramInfo = GetHistogramInfo_2Dplot(extraCuts,extraPhotonCuts,nBJets)

#print histogramInfo

###This part will make a list of the histograms that need to be produced

plotList = options.plotList
if plotList is None:
    plotList = histogramInfo.keys()

histogramsToMake = plotList
histogramsToMake.sort()

canvas = TCanvas()
histograms=[]

if sample =="QCD_DD":
    if finalState=="Mu":
        if isTightSelection:
            qcd_File    = TFile("histograms/mu/qcdhistsCR_Tight.root","read")
        elif isLooseSelection:
            qcd_File    = TFile("histograms/mu/qcdhistsCR_Loose.root","read")
        else:
            qcd_File    = TFile("histograms/mu/qcdhistsCR.root","read")
        qcd_TF_File = TFile("histograms/mu/qcdTransferFactors.root","read")
        dirName = "QCDMu"
    if finalState=="Ele":
        if isTightSelection:
            qcd_File    = TFile("histograms/ele/qcdhistsCR_Tight.root","read")
        elif isLooseSelection:
            qcd_File    = TFile("histograms/ele/qcdhistsCR_Loose.root","read")
        else:
            qcd_File    = TFile("histograms/ele/qcdhistsCR.root","read")
        qcd_TF_File = TFile("histograms/ele/qcdTransferFactors.root","read")
        dirName = "QCDEle"


    #Calculate the transfer Factor for the QCD events from the QCDcr to the signal region being used, based on jet/bjet multiplicities
    transferFactor = 1.
    histNjet_QCDcr = qcd_TF_File.Get("histNjet_QCDcr")
    histNjet_0b = qcd_TF_File.Get("histNjet_0b")
    histNjet_1b = qcd_TF_File.Get("histNjet_1b")
    histNjet_2b = qcd_TF_File.Get("histNjet_2b")
    if nBJets==0:
        histNjet_2b.Add(histNjet_1b)
        histNjet_2b.Add(histNjet_0b)
    if nBJets==1:
        histNjet_2b.Add(histNjet_1b)
#    transferFactor = histNjet_2b.Integral(nJets+1,-1)/histNjet_QCDcr.Integral(-1,-1)
    transferFactor = histNjet_2b.Integral(nJets+1,-1)/histNjet_QCDcr.Integral(nJets+1,-1)
#    print transferFactor

    for hist in histogramsToMake:
        h_Info = histogramInfo[hist]
        if not h_Info[7]: continue
        if not runQuiet: print "filling", h_Info[0], sample

        histograms.append(qcd_File.Get("QCD_DD/%s_QCD_DD"%(h_Info[1])))
        histograms[-1].Scale(transferFactor)

if not "QCD_DD" in sample:
    if not sample in sampleList:
        print "Sample isn't in list"
        print sampleList
        sys.exit()

    tree = TChain("AnalysisTree")
    fileList = samples[sample][0]
    for fileName in fileList:
        tree.Add("%s/%s"%(analysisNtupleLocation,fileName))

    if not runQuiet: print "Number of events:", tree.GetEntries()

    for hist in histogramsToMake:
        h_Info = histogramInfo[hist]
        if not runQuiet: print "filling", h_Info[2], sample
        evtWeight = ""

        histograms.append(TH2D("%s_%s"%(h_Info[2],sample),"%s_%s"%(h_Info[2],sample),h_Info[3][0],h_Info[3][1],h_Info[3][2],h_Info[4][0],h_Info[4][1],h_Info[4][2]))
        if h_Info[6]=="":
            evtWeight = "%s%s"%(h_Info[5],weights)
        else:
            evtWeight = h_Info[6]

        if "Data" in sample:
            evtWeight = "%s%s"%(h_Info[3],weights)
        # if "Data" in sample:
        #     evtWeight = h_Info[6]

        if evtWeight[-1]=="*":
            evtWeight= evtWeight[:-1]
#	print h_Info[0],h_Info[1],h_Info[2]
       # tree.Draw("%s>>%s_%s"%(h_Info[0],h_Info[1],sample),evtWeight)
        tree.Draw("%s:%s>>%s_%s"%(h_Info[0],h_Info[1],h_Info[2],sample),evtWeight,"colz")


#outputFile = TFile(outputhistName,"update")

# if not onlyAddPlots:
#     outputFile.rmdir(sample)
#     outputFile.mkdir(sample)
# outputFile.cd(sample)
# for h in histograms:
#     if onlyAddPlots:
#         gDirectory.Delete("%s;*"%(h.GetName()))
#     h.Write()

# outputFile.Close()

if not os.path.exists(outputhistName):
    os.makedirs(outputhistName)

outputFile = TFile("%s/%s.root"%(outputhistName,sample),"update")

for h in histograms:
    outputFile.Delete("%s;*"%h.GetName())
    if onlyAddPlots:
        gDirectory.Delete("%s;*"%(h.GetName()))
    h.Write()

outputFile.Close()
