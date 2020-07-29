from ROOT import TH1F, TFile, TChain, TCanvas
import sys
from sampleInformation import *
import os
from optparse import OptionParser

#-----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s", "--sample", dest="sample", default="",type='str',
                     help="Specify which sample to run on" )
parser.add_option("--level", "--level", dest="level", default="",type='str',
                     help="Specify up/down of systematic")
parser.add_option("--syst", "--systematic", dest="systematic", default="Base",type='str',
		     help="Specify which systematic to run on")
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                     help="Use 4j1t selection" )
parser.add_option("--VeryTight","--verytight", dest="isVeryTightSelection", default=False,action="store_true",
                     help="Use 4j2t selection" )
parser.add_option("--Tight0b","--tight0b", dest="isTightSelection0b", default=False,action="store_true",
                     help="Use 4j0t selection" )
parser.add_option("--LooseCR2e1","--looseCR2e1", dest="isLooseCR2e1Selection",default=False,action="store_true",
		  help="Use 2j exactly 1t control region selection" )
parser.add_option("--LooseCRe2g1","--looseCRe2g1", dest="isLooseCRe2g1Selection",default=False,action="store_true",
                  help="Use exactly 2j >= 1t control region selection" )
parser.add_option("--LooseCR3g0","--looseCR3g0", dest="isLooseCR3g0Selection",default=False,action="store_true",
		  help="Use >=3j and 0btag control region selection" )
parser.add_option("--LooseCR2g1","--looseCR2g1", dest="isLooseCR2g1Selection",default=False,action="store_true",
                  help="Use 2j at least 1t control region selection")
parser.add_option("--LooseCRe3g1","--looseCRe3g1", dest="isLooseCRe3g1Selection",default=False,action="store_true",
		  help="Use exactly 3j >= 1t control region selection" )
parser.add_option("--addPlots","--addOnly", dest="onlyAddPlots", default=False,action="store_true",
                     help="Use only if you want to add a couple of plots to the file, does not remove other plots" )
parser.add_option("--plot", dest="plotList",action="append",
                     help="Add plots" )
parser.add_option("--multiPlots", "--multiplots", dest="multiPlotList",action="append",
                     help="Add plots" )
parser.add_option("--testPlot", "--testPlot", dest="testPlot",action="store_true",default=False,
                     help="test one plot without replacing it in the original one" )
parser.add_option("--allPlots","--AllPlots", dest="makeAllPlots",action="store_true",default=False,
                     help="Make full list of plots in histogramDict" )
parser.add_option("--morePlots","--MorePlots","--makeMorePlots", dest="makeMorePlots",action="store_true",default=False,
                     help="Make larger list of plots in histogramDict (mostly object kinematics)" )
parser.add_option("--EgammaPlots","--EgammaPlots", dest="makeEGammaPlots",action="store_true",default=False,
                     help="Make only plots for e-gamma mass fits" )
parser.add_option("--dRPlots","--dRPlots", dest="makedRPlots",action="store_true",default=False,
                     help="Make only plots for dR" )
parser.add_option("--genPlots","--genPlots", dest="makegenPlots",action="store_true",default=False,
                     help="Make only plots for 2D histograms" )
parser.add_option("--jetsonly","--jetsonly", dest="makeJetsplots",action="store_true",default=False,
                     help="Extra jets" )
parser.add_option("--dilepmassPlots","--dilepmassPlots", dest="Dilepmass",action="store_true",default=False,
                     help="Make only plots for ZJetsSF fits" )
parser.add_option("--quiet", "-q", dest="quiet",default=False,action="store_true",
                     help="Quiet outputs" )
parser.add_option("--fwdjets","--fwdjets", dest="FwdJets",action="store_true",default=False,
                     help="include fwd jets" )

(options, args) = parser.parse_args()
level =options.level
Dilepmass=options.Dilepmass
year = options.year
finalState = options.channel
sample = options.sample
testPlot=options.testPlot
isVeryTightSelection=options.isVeryTightSelection
isTightSelection = options.isTightSelection
isTightSelection0b = options.isTightSelection0b
#isLooseCRe2g1Selection=options.isLooseCRe2g1Selection
isLooseCR2e1Selection = options.isLooseCR2e1Selection
isLooseCRe2g1Selection = options.isLooseCRe2g1Selection
isLooseCR3g0Selection=options.isLooseCR3g0Selection
isLooseCRe2g1Selection = options.isLooseCRe2g1Selection
isLooseCRe3g1Selection = options.isLooseCRe3g1Selection
onlyAddPlots = options.onlyAddPlots
FwdJets=options.FwdJets
makedRPlots=options.makedRPlots
makeAllPlots = options.makeAllPlots
makeMorePlots = options.makeMorePlots
makeEGammaPlots = options.makeEGammaPlots
makeJetsplots = options.makeJetsplots
makegenPlots=options.makegenPlots
runQuiet = options.quiet

#-----------------------------------------
#INPUT AnalysisNtuples Directory
#----------------------------------------
ntupleDirBase = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/%s/"%year
ntupleDirBaseDiLep = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/Dilepton/%s/"%year
ntupleDirBaseCR = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/%s/"%year
ntupleDirSyst = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/Systematics/%s/"%year
ntupleDirSystCR = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/Systematics/%s/"%year

#-----------------------------------------
#OUTPUT Histogram Directory
#----------------------------------------
#outputPath = "/home/rverma/t3store/TTGammaSemiLep13TeV/CMSSW_10_2_5/src/TTGamma/Plotting" 
outputPath = "."

#-----------------------------------------
#----------------------------------------
gROOT.SetBatch(True)
dir2=""
if FwdJets:
	dir2="_fwd"
nJets = 3
nBJets = 1
isQCD = False
dir_=""
Q2 = 1.
Pdf = 1.
Pileup ="PUweight"
MuEff = "muEffWeight"
EleEff= "eleEffWeight"
PhoEff= "phoEffWeight"
loosePhoEff= "loosePhoEffWeight"
evtWeight ="evtWeight"
btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]
ttbarDecayMode = "SemiLep"
if testPlot:
	ttbarDecayMode="Test"
outputHistDir = "Base"

#-----------------------------------------
#For Systematics
#----------------------------------------
syst = options.systematic
if (syst=="isr" or syst=="fsr") and sample=="TTbar":
		samples={"TTbar"     : [["TTbarPowheg_AnalysisNtuple.root"],
                          kRed+1,"t#bar{t}",isMC],
			}
if not syst=="Base":
    outputHistDir = "%s_%s"%(syst,level) 
    if syst=="PU":
    	print "is here" 
        if level=="up":
                Pileup = "PUweight_Up"
        else:
                    Pileup = "PUweight_Do"
    elif 'Q2' in syst:
        if level=="up":
                Q2="q2weight_Up"
        else:
                Q2="q2weight_Do"
    elif 'Pdf' in syst:
    	if syst=="Pdf":

    	    if level=="up":
    	    	Pdf="pdfweight_Up"
    	    else:
    	    	Pdf="pdfweight_Do"
    	else:
    	    if type(eval(syst[3:]))==type(int()):
    	    	pdfNumber = eval(syst[3:])
    	    	Pdf="pdfSystWeight[%i]/pdfWeight"%(pdfNumber-1)
    elif 'MuEff' in syst:
        if level=="up":
            MuEff = "muEffWeight_Up"
        else:
            MuEff = "muEffWeight_Do"
    elif 'EleEff' in syst:
        if level=="up":
            EleEff = "eleEffWeight_Up"
        else:
            EleEff = "eleEffWeight_Do"
    elif 'PhoEff' in syst:
       if level=="up":
           PhoEff = "phoEffWeight_Up"
           loosePhoEff = "loosePhoEffWeight_Up"
       else:
           PhoEff = "phoEffWeight_Do"
           loosePhoEff = "loosePhoEffWeight_Do"
    elif 'BTagSF' in syst:
        if level=="up":
            btagWeightCategory = ["1","(1-btagWeight_Up[0])","(btagWeight_Up[2])","(btagWeight_Up[1])"]
        else:
            btagWeightCategory = ["1","(1-btagWeight_Do[0])","(btagWeight_Do[2])","(btagWeight_Do[1])"]
    else:
    	if  level=="up":
            analysisNtupleLocation = ntupleDirSyst+"/%s_up_"%(syst)
    	if level=="down":
            analysisNtupleLocation = ntupleDirSyst+"/%s_down_"%(syst)

if finalState=="Mu":
    sampleList[-1] = "DataMu"
    sampleList[-2] = "QCDMu"
    if sample=="Data":
        sample = "DataMu"
    if sample=="QCD":
        sample = "QCDMu"
    analysisNtupleLocation = ntupleDirBase
    outputhistName = outputPath+"/Histograms/%s/%s/Mu"%(year,ttbarDecayMode)
    extraCuts            = "(passPresel_Mu && nJet>=3 && nBJet>=1)*"
    extraPhotonCuts      = "(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*"

    extraCutsTight       = "(passPresel_Mu && nJet>=4 && nBJet>=1)*"
    extraPhotonCutsTight = "(passPresel_Mu && nJet>=4 && nBJet>=1 && %s)*"
    
    extraCutsVeryTight       = "(passPresel_Mu && nJet>=4 && nBJet>=2)*"
    extraPhotonCutsVeryTight = "(passPresel_Mu && nJet>=4 && nBJet>=2 && %s)*"
    
    extraCutsTight0b       = "(passPresel_Mu && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight0b = "(passPresel_Mu && nJet>=4 && nBJet==0 && %s)*"

    extraCutsLooseCR2e1       = "(passPresel_Mu && nJet>=2 && nBJet==1)*"
    extraPhotonCutsLooseCR2e1 = "(passPresel_Mu && nJet>=2 && nBJet==1 && %s)*"

    extraCutsLooseCR2g1       = "(passPresel_Mu && nJet==2 && nBJet>=1)*"
    extraPhotonCutsLooseCR2g1 = "(passPresel_Mu && nJet==2 && nBJet>=1 && %s)*"

    extraCutsLooseCR2e0       = "(passPresel_Mu && nJet>=2)*"
    extraPhotonCutsLooseCR2e0 = "(passPresel_Mu && nJet>=2 && %s)*"

    extraCutsLooseCRe3g1       = "(passPresel_Mu && nJet==3 && nBJet>=1)*"
    extraPhotonCutsLooseCRe3g1 = "(passPresel_Mu && nJet==3 && nBJet>=1 && %s)*"


    extraCutsLooseCRe3g0       = "(passPresel_Mu && nJet>=3 && nBJet==0)*"
    extraPhotonCutsLooseCRe3g0 = "(passPresel_Mu && nJet>=3 && nBJet==0 && %s)*"

elif finalState=="Ele":
    sampleList[-1] = "DataEle"
    sampleList[-2] = "QCDEle"
    if sample=="Data":
        sample = "DataEle"
    if sample=="QCD":
        sample = "QCDEle"
    analysisNtupleLocation = ntupleDirBase 
    outputhistName = outputPath+"/Histograms/%s/%s/Ele"%(year,ttbarDecayMode)
    extraCuts            = "(passPresel_Ele && nJet>=3 && nBJet>=1)*"
    extraPhotonCuts      = "(passPresel_Ele && nJet>=3 && nBJet>=1 && %s)*"

    extraCutsTight       = "(passPresel_Ele && nJet>=4 && nBJet>=1)*"
    extraPhotonCutsTight = "(passPresel_Ele && nJet>=4 && nBJet>=1 && %s)*"
    
    extraCutsVeryTight       = "(passPresel_Ele && nJet>=4 && nBJet>=2)*"
    extraPhotonCutsVeryTight = "(passPresel_Ele && nJet>=4 && nBJet>=2 && %s)*"

    
    extraCutsTight0b       = "(passPresel_Ele && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight0b = "(passPresel_Ele && nJet>=4 && nBJet==0 && %s)*"

    extraCutsLooseCR2e1       = "(passPresel_Ele && nJet>=2 && nBJet==1)*"
    extraPhotonCutsLooseCR2e1 = "(passPresel_Ele && nJet>=2 && nBJet==1 && %s)*"

    extraCutsLooseCR2g0       = "(passPresel_Ele && nJet==2)*"
    extraPhotonCutsLooseCR2g0 = "(passPresel_Ele && nJet==2 && %s)*"

    extraCutsLooseCR2g1       = "(passPresel_Ele && nJet==2 && nBJet>=1)*"
    extraPhotonCutsLooseCR2g1 = "(passPresel_Ele && nJet==2 && nBJet>=1 && %s)*"

    extraCutsLooseCR2e0       = "(passPresel_Ele && nJet>=2)*"
    extraPhotonCutsLooseCR2e0 = "(passPresel_Ele && nJet>=2 && %s)*"

    extraCutsLooseCRe3g1       = "(passPresel_Ele && nJet==3 && nBJet>=1)*"
    extraPhotonCutsLooseCRe3g1 = "(passPresel_Ele && nJet==3 && nBJet>=1 && %s)*"

    
    extraCutsLooseCRe3g0       = "(passPresel_Ele && nJet>=3 && nBJet==0)*"
    extraPhotonCutsLooseCRe3g0 = "(passPresel_Ele && nJet>=3 && nBJet==0 && %s)*"

elif finalState=="DiMu":
    sampleList[-1] = "DataMu"
    sampleList[-2] = "QCDMu"

    if sample=="Data":
        sample = "DataMu"
    if sample=="QCD":
        sample = "QCDMu"
    analysisNtupleLocation = ntupleDirBaseDiLep
    ttbarDecayMode = "DiLep"
    outputhistName = outputPath+"/Histograms/%s/%s/Mu"%(year,ttbarDecayMode)

    extraCuts            = "(passPresel_Mu && nJet>=3 && nBJet>=1)*"
    extraPhotonCuts      = "(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*"

    extraCutsTight       = "(passPresel_Mu && nJet>=4 && nBJet>=1)*"
    extraPhotonCutsTight = "(passPresel_Mu && nJet>=4 && nBJet>=1 && %s)*"

    extraCutsTight0b       = "(passPresel_Mu && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight0b = "(passPresel_Mu && nJet>=4 && nBJet==0 && %s)*"


    extraCutsLooseCR2e1       = "(passPresel_Mu && nJet>=2 && nBJet==1)*"
    extraPhotonCutsLooseCR2e1 = "(passPresel_Mu && nJet>=2 && nBJet==1 && %s)*"

    extraCutsLooseCR2e0       = "(passPresel_Mu && nJet==2)*"
    extraPhotonCutsLooseCR2e0 = "(passPresel_Mu && nJet==2 && %s)*"

    extraCutsLooseCR2g0       = "(passPresel_Mu && nJet>=2)*"
    extraPhotonCutsLooseCR2g0 = "(passPresel_Mu && nJet>=2 && %s)*"

    extraCutsLooseCR2g1       = "(passPresel_Mu && nJet==2 && nBJet>=1)*"
    extraPhotonCutsLooseCR2g1 = "(passPresel_Mu && nJet==2 && nBJet>=1 && %s)*"

    extraCutsLooseCR3g0       = "(passPresel_Mu && nJet>=3 && nBJet>=0)*"
    extraPhotonCutsLooseCR3g0 = "(passPresel_Mu && nJet>=3 && nBJet>=0 && %s)*"
 
    extraCutsLooseCRe3g1       = "(passPresel_Mu && nJet==3 && nBJet>=1)*"
    extraPhotonCutsLooseCRe3g1 = "(passPresel_Mu && nJet==3 && nBJet>=1 && %s)*"


    extraCutsLooseCRe3g0       = "(passPresel_Mu && nJet>=3 && nBJet==0)*"
    extraPhotonCutsLooseCRe3g0 = "(passPresel_Mu && nJet>=3 && nBJet==0 && %s)*"

elif finalState=="DiEle":
    sampleList[-1] = "DataEle"
    sampleList[-2] = "QCDEle"
    if sample=="Data":
        sample = "DataEle"
    if sample=="QCD":
        sample = "QCDEle"
    analysisNtupleLocation = ntupleDirBaseDiLep 
    outputhistName = outputPath+"/Histograms/%s/%s/Ele"%(year,ttbarDecayMode)

    extraCuts            = "(passPresel_Ele && nJet>=3 && nBJet>=1)*"
    extraPhotonCuts      = "(passPresel_Ele && nJet>=3 && nBJet>=1 && %s)*"

    extraCutsTight       = "(passPresel_Ele && nJet>=4 && nBJet>=1)*"
    extraPhotonCutsTight = "(passPresel_Ele && nJet>=4 && nBJet>=1 && %s)*"

    extraCutsTight0b       = "(passPresel_Ele && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight0b = "(passPresel_Ele && nJet>=4 && nBJet==0 && %s)*"

    extraCutsLooseCR2e1       = "(passPresel_Ele && nJet>=2 && nBJet==1)*"
    extraPhotonCutsLooseCR2e1 = "(passPresel_Ele && nJet>=2 && nBJet==1 &&%s)*"

    extraCutsLooseCR2g1       = "(passPresel_Ele && nJet==2 && nBJet>=1)*"
    extraPhotonCutsLooseCR2g1 = "(passPresel_Ele && nJet==2 && nBJet>=1 && %s)*"

    extraCutsLooseCR2g0       = "(passPresel_Ele && nJet>=2)*"
    extraPhotonCutsLooseCR2g0 = "(passPresel_Ele && nJet>=2 && %s)*"

    extraCutsLooseCRe3g1       = "(passPresel_Ele && nJet==3 && nBJet>=1)*"
    extraPhotonCutsLooseCRe3g1 = "(passPresel_Ele && nJet==3 && nBJet>=1 && %s)*"


    extraCutsLooseCRe3g0       = "(passPresel_Ele && nJet>=3 && nBJet==0)*"
    extraPhotonCutsLooseCRe3g0 = "(passPresel_Ele && nJet>=3 && nBJet==0 && %s)*"

elif finalState=="QCDMu":
    sampleList[-1] = "DataMu"
    sampleList[-2] = "QCDMu"
    if sample=="Data":
        sample = "DataMu"
    if sample=="QCD":
        sample = "QCDMu"
    isQCD = True
    analysisNtupleLocation = ntupleDirBaseCR 
    outputhistName = outputPath+"/Histograms/%s/%s/Mu/CR/"%(year,ttbarDecayMode)

    nBJets = 0
    extraCuts            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=3 && nBJet==0)*"
    extraPhotonCuts      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=3 && nBJet==0 && %s)*"

    extraCutsTight            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && nBJet==0 && %s)*"

    extraCutsVeryTight       = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && nBJet==0)*"
    extraPhotonCutsVeryTight = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && nBJet==0 && %s)*"

    extraCutsTight0b            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight0b      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && nBJet==0 && %s)*"

    extraCutsLooseCR2e1       = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet==0)*"
    extraPhotonCutsLooseCR2e1 = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet==0 && %s)*"

    extraCutsLooseCR2e0       = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet==0)*"
    extraPhotonCutsLooseCR2e0 = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet==0 && %s)*"

    extraCutsLooseCR2g0       = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet==0)*"
    extraPhotonCutsLooseCR2g0 = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet==0 && %s)*"
    
    extraCutsLooseCR2g1       = "(passPresel_Mu && muPFRelIso<0.3 && nJet==2 && nBJet==0)*"
    extraPhotonCutsLooseCR2g1 = "(passPresel_Mu && muPFRelIso<0.3 && nJet==2 && nBJet==0 && %s)*"

    extraCutsLooseCRe3g1       = "(passPresel_Mu && muPFRelIso<0.3 && nJet==3 && nBJet==0)*"
    extraPhotonCutsLooseCRe3g1 = "(passPresel_Mu && muPFRelIso<0.3 && nJet==3 && nBJet==0 && %s)*"

    extraCutsLooseCRe3g0       = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=3 && nBJet==0)*"
    extraPhotonCutsLooseCRe3g0 = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=3 && nBJet==0 && %s)*"


elif finalState=="QCDMu2":
    sampleList[-1] = "DataMu"
    sampleList[-2] = "QCDMu"
    if sample=="Data":
        sample = "DataMu"
    if sample=="QCD":
        sample = "QCDMu"
    isQCD = True
    analysisNtupleLocation = ntupleDirBaseCR
    outputhistName = outputPath+"/Histograms/%s/%s/Mu/CR2"%(year,ttbarDecayMode)

    nBJets = 0
    extraCuts            = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=3 && nBJet==0)*"
    extraPhotonCuts      = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=3 && nBJet==0 && %s)*"

    extraCutsTight            = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight      = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=4 && nBJet==0 && %s)*"

    extraCutsTight0b            = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight0b      = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=4 && nBJet==0 && %s)*"

    extraCutsLoose            = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=2 && nBJet==0)*"
    extraPhotonCutsLoose      = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=2 && nBJet==0 && %s)*"

    extraCutsLooseCR          = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=2 && nBJet==0)*"
    extraPhotonCutsLooseCR    = "(passPresel_Mu && muPFRelIso>0.3 && nJet>=2 && nBJet==0 && %s)*"

elif finalState=="QCDEle":
    sampleList[-1] = "DataEle"
    sampleList[-2] = "QCDEle"
    if sample=="Data":
        sample = "DataEle"
    if sample=="QCD":
        sample = "QCDEle"
    analysisNtupleLocation = ntupleDirBaseCR 
    outputhistName = outputPath+"/Histograms/%s/%s/Ele/CR"%(year,ttbarDecayMode)
    print outputhistName

    isQCD = True

    nBJets = 0

    extraCuts                 = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=3 && nBJet==0)*"
    extraPhotonCuts           = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=3 && nBJet==0 && %s)*"

    extraCutsTight            = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight      = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=4 && nBJet==0 && %s)*"

    extraCutsVeryTight       = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=4 && nBJet==0)*"
    extraPhotonCutsVeryTight = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=4 && nBJet==0 && %s)*"

    extraCutsTight0b            = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=4 && nBJet==0)*"
    extraPhotonCutsTight0b      = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=4 && nBJet==0 && %s)*"

    extraCutsLoose            = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet==0)*"
    extraPhotonCutsLoose      = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet==0 && %s)*"

    extraCutsLooseCR2e1       = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet==0)*"
    extraPhotonCutsLooseCR2e1 = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet==0 && %s)*"

    extraCutsLooseCR2g1       = "(passPresel_Ele && elePFRelIso>0.01 && nJet==2 && nBJet==0)*"
    extraPhotonCutsLooseCR2g1 = "(passPresel_Ele && elePFRelIso>0.01 && nJet==2 && nBJet==0 && %s)*"

    extraCutsLooseCR          = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet==0)*"
    extraPhotonCutsLooseCR    = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet==0 && %s)*"


    extraCutsLooseCRe3g1       = "(passPresel_Ele && elePFRelIso>0.01 && nJet==3 && nBJet==0)*"
    extraPhotonCutsLooseCRe3g1 = "(passPresel_Ele && elePFRelIso>0.01 && nJet==3 && nBJet==0 && %s)*"

    extraCutsLooseCRe3g0       = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=3 && nBJet==0)*"
    extraPhotonCutsLooseCRe3g0 = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=3 && nBJet==0 && %s)*"

else:
    print "Unknown final state, options are Mu and Ele"
    sys.exit()


btagWeight = btagWeightCategory[nBJets]
signalOrCR = "SignalRegion"
if isTightSelection:
    if not runQuiet: print "Tight Select"
    nJets = 4
    nBJets = 1
    btagWeight = btagWeightCategory[nBJets]
    # weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
    extraCuts = extraCutsTight 
    extraPhotonCuts = extraPhotonCutsTight 
    signalOrCR = "ControlRegion/Tight"
    dir_="_tight"

if isVeryTightSelection:
    if not runQuiet: print "Very Tight Select"
    nJets = 4
    nBJets = 2
    btagWeight = btagWeightCategory[nBJets]
   
    extraCuts = extraCutsVeryTight
    extraPhotonCuts = extraPhotonCutsVeryTight
    signalOrCR = "ControlRegion/VerytTight"
    dir_=""



if isTightSelection0b:
    if not runQuiet: print "Tight Select"
    nJets = 4
    nBJets = 0
    btagWeight = btagWeightCategory[nBJets]
    # weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
    extraCuts = extraCutsTight0b
    extraPhotonCuts = extraPhotonCutsTight0b
    signalOrCR = "ControlRegion/Tight0b"
    dir_="_tight0b"


if isLooseCR2e1Selection:
    if not runQuiet: print "Loose Control Region Select"
    nJets = 2
    nBJets = 1
    btagWeight = "(btagWeight[1])"
    #    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[1]"
    extraCuts = extraCutsLooseCR2e1
    extraPhotonCuts = extraPhotonCutsLooseCR2e1
    signalOrCR = "ControlRegion/LooseCR2e1"
    dir_="_looseCR2e1"

if isLooseCRe2g1Selection:
    if not runQuiet: print "Loose Control Region1 Select"
    nJets = 2
    nBJets = 1
    btagWeight = btagWeightCategory[nBJets]
    if 'QCD' in finalState:
        btagWeight="1"
    # weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*(1-btagWeight[0])"
    # if 'QCD' in finalState:
    #     weights = "evtWeight*PUweight*muEffWeight*eleEffWeight"
    extraCuts = extraCutsLooseCR2g1
    extraPhotonCuts = extraPhotonCutsLooseCR2g1    
    signalOrCR = "ControlRegion/LooseCR2g1"
    dir_="_looseCRe2g1"

if isLooseCR3g0Selection:
    if not runQuiet: print "Loose Control Region for EGamma"
    nJets = 3
    nBJets = 0
    btagWeight = "btagWeight[0]" 
    if 'QCD' in finalState:
       	btagWeight="1"
    extraCuts = extraCutsLooseCRe3g0
    extraPhotonCuts = extraPhotonCutsLooseCRe3g0
    signalOrCR = "ControlRegion/LooseCRe3g0"
    dir_="_looseCRe3g0"




if isLooseCRe3g1Selection:
    if not runQuiet: print "Loose Control Region Select"
    nJets = 3
    nBJets = 1
    btagWeight = btagWeightCategory[nBJets]
    #weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*(btagWeight[0])"
    extraCuts = extraCutsLooseCRe3g1
    extraPhotonCuts = extraPhotonCutsLooseCRe3g1
    signalOrCR = "ControlRegion/LooseCRe3g1"
    dir_="_looseCRe3g1"

histDestination = "%s/%s"%(signalOrCR, outputHistDir)
if "QCD" in finalState:
	nBJets = 0
        btagWeight="btagWeight[0]"
weights = "%s*%s*%s*%s*%s*%s*%s"%(evtWeight,Pileup,MuEff,EleEff,Q2,Pdf,btagWeight)
print extraCuts
print extraPhotonCuts
print "using weights", weights
if not runQuiet: print " the output folder is:", outputhistName


from HistogramListDict import *
histogramInfo = GetHistogramInfo(extraCuts,extraPhotonCuts,nBJets)


multiPlotList = options.multiPlotList

plotList = options.plotList
if plotList is None:
    if makeAllPlots:
        plotList = histogramInfo.keys()
        if not runQuiet: print "Making full list of plots"
    elif makeJetsplots:
	plotList = ["presel_jet2Pt","presel_jet3Pt", "presel_jet4Pt"]
    elif makeMorePlots:
        plotList = ["presel_Njet","phosel_SIEIE_barrel","phosel_SIEIE_GenuinePhoton_barrel","phosel_SIEIE_MisIDEle_barrel","phosel_SIEIE_NonPrompt_barrel","phosel_R9_barrel","phosel_elePt_barrel","phosel_elePt_GenuinePhoton_barrel","phosel_elePt_MisIDEle_barrel","phosel_elePt_NonPrompt_barrel","presel_elePt","phosel_muPt_barrel","phosel_muPt_GenuinePhoton_barrel","phosel_muPt_MisIDEle_barrel","phosel_muPt_NonPrompt_barrel","presel_muPt","phosel_eleSCEta_barrel","phosel_eleSCEta_GenuinePhoton_barrel","phosel_eleSCEta_MisIDEle_barrel","phosel_eleSCEta_NonPrompt_barrel","presel_eleSCEta","phosel_muEta_barrel","phosel_muEta_GenuinePhoton_barrel","phosel_muEta_MisIDEle_barrel","phosel_muEta_NonPrompt_barrel","presel_muEta","phosel_PhotonCategory_barrel","phosel_Njet_barrel","phosel_Njet_GenuinePhoton_barrel","phosel_Njet_MisIDEle_barrel","phosel_Njet_NonPrompt_barrel","presel_jet1Pt","phosel_jet1Pt_barrel","phosel_jet1Pt_GenuinePhoton_barrel","phosel_jet1Pt_MisIDEle_barrel","phosel_jet1Pt_NonPrompt_barrel","phosel_LeadingPhotonEt_barrel","phosel_LeadingPhotonEt_GenuinePhoton_barrel","phosel_LeadingPhotonEt_MisIDEle_barrel","phosel_LeadingPhotonEt_NonPrompt_barrel","phosel_LeadingPhotonEta_barrel","presel_M3_control","phosel_noCut_ChIso_barrel","phosel_noCut_SIEIE_barrel","phosel_noCut_SIEIE_GenuinePhoton_barrel","phosel_noCut_SIEIE_MisIDEle_barrel","phosel_noCut_SIEIE_NonPrompt_barrel","presel_nVtx","phosel_nVtx_barrel","presel_nVtxdo","presel_nVtxup","phosel_nVtxdo_barrel","phosel_nVtxup_barrel","presel_nVtxNoPU","phosel_nVtxNoPU_barrel","phosel_ChIso_barrel","phosel_ChIso_GenuinePhoton_barrel","phosel_ChIso_MisIDEle_barrel","phosel_ChIso_NonPrompt_barrel","phosel_NeuIso_barrel","phosel_NeuIso_GenuinePhoton_barrel","phosel_NeuIso_MisIDEle_barrel","phosel_NeuIso_NonPrompt_barrel","phosel_PhoIso_barrel","phosel_PhoIso_GenuinePhoton_barrel","phosel_PhoIso_MisIDEle_barrel","phosel_PhoIso_NonPrompt_barrel","phosel_HoverE_barrel","phosel_Nphotons_barrel","phosel_Nphotons_GenuinePhoton_barrel","phosel_Nphotons_MisIDEle_barrel","phosel_Nphotons_NonPrompt_barrel","phosel_LeadingPhotonSCEta_barrel", "phosel_LeadingPhotonSCEta_GenuinePhoton_barrel","phosel_LeadingPhotonSCEta_MisIDEle_barrel","phosel_LeadingPhotonSCEta_NonPrompt_barrel","phosel_noCut_SIEIE_noChIso_barrel","phosel_noCut_SIEIE_noChIso_GenuinePhoton_barrel","phosel_noCut_SIEIE_noChIso_MisIDEle_barrel","phosel_noCut_SIEIE_noChIso_NonPrompt_barrel","presel_HT","phosel_HT_barrel","phosel_HT_GenuinePhoton_barrel","phosel_HT_MisIDEle_barrel","phosel_HT_NonPrompt_barrel","presel_M3","phosel_noCut_ChIso_GenuinePhoton_barrel","phosel_noCut_ChIso_MisIDEle_barrel","phosel_noCut_ChIso_HadronicPhoton_barrel","phosel_noCut_ChIso_HadronicFake_barrel","phosel_M3","phosel_M3_barrel","phosel_M3_GenuinePhoton_barrel","phosel_M3_MisIDEle_barrel","phosel_M3_HadronicPhoton_barrel","phosel_M3_HadronicFake_barrel","phosel_M3_NonPrompt_barrel","phosel_AntiSIEIE_ChIso",
			"phosel_AntiSIEIE_ChIso_barrel","phosel_AntiSIEIE_ChIso_GenuinePhoton_barrel","phosel_AntiSIEIE_ChIso_HadronicPhoton_barrel","phosel_AntiSIEIE_ChIso_HadronicFake_barrel","phosel_AntiSIEIE_ChIso_MisIDEle_barrel","phosel_MassEGamma","phosel_MassEGammaMisIDEle","phosel_MassEGammaOthers","phosel_MassEGamma_barrel","phosel_MassEGamma_NonPrompt_barrel","phosel_MassEGamma_GenuinePhoton_barrel","phosel_MassEGamma_MisIDEle_barrel","phosel_MassEGammaOthers_barrel", "phosel_LeadingPhotonabsSCEta_barrel", "phosel_LeadingPhotonabsSCEta_GenuinePhoton_barrel","phosel_LeadingPhotonabsSCEta_MisIDEle_barrel","phosel_LeadingPhotonabsSCEta_NonPrompt_barrel", "phosel_dRLeadingPhotonLepton_GenuinePhoton_barrel", "phosel_dRLeadingPhotonLepton_MisIDEle_barrel", "phosel_dRLeadingPhotonLepton_NonPrompt_barrel", "phosel_dRLeadingPhotonLepton_barrel","phosel_dRLeadingPhotonJet_GenuinePhoton_barrel", "phosel_dRLeadingPhotonJet_MisIDEle_barrel", "phosel_dRLeadingPhotonJet_NonPrompt_barrel", "phosel_dRLeadingPhotonJet_barrel"]
        if not runQuiet: print "Making subset of kinematic plots"
    elif makeEGammaPlots:
        plotList = ["phosel_MassEGamma","phosel_MassEGammaMisIDEle","phosel_MassEGammaOthers","phosel_MassEGamma_barrel","phosel_MassEGamma_MisIDEle_barrel","phosel_MassEGammaOthers_barrel"]
        if not runQuiet: print "Making only plots for e-gamma fits"
    elif makedRPlots:
	 plotList=["phosel_dRLeadingPhotonLepton_GenuinePhoton_barrel", "phosel_dRLeadingPhotonLepton_MisIDEle_barrel", "phosel_dRLeadingPhotonLepton_NonPrompt_barrel", "phosel_dRLeadingPhotonLepton_barrel","phosel_dRLeadingPhotonJet_GenuinePhoton_barrel", "phosel_dRLeadingPhotonJet_MisIDEle_barrel", "phosel_dRLeadingPhotonJet_NonPrompt_barrel", "phosel_dRLeadingPhotonJet_barrel"]
    
	 if not runQuiet: print "Making only dR photon plots"
    elif makegenPlots:
	 plotList=["phosel_LeadingPhotonabsSCEta_barrel", "phosel_LeadingPhotonabsSCEta_GenuinePhoton_barrel","phosel_LeadingPhotonabsSCEta_MisIDEle_barrel","phosel_LeadingPhotonabsSCEta_NonPrompt_barrel","phosel_LeadingPhotonEt_barrel","phosel_LeadingPhotonEt_GenuinePhoton_barrel","phosel_LeadingPhotonEt_MisIDEle_barrel","phosel_LeadingPhotonEt_NonPrompt_barrel", "phosel_GenPhoPt","phosel_GenPhoEta"]
         if not runQuiet: print "Making only 2D photon plots"
    elif Dilepmass:
	plotList = ["presel_DilepMass"]
        if not runQuiet: print "Making only plots for ZJetsSF fits"
    elif not multiPlotList is None:
        plotList = []
        for plotNameTemplate in multiPlotList:
            thisPlotList = []
            for plotName in histogramInfo.keys():
                if plotNameTemplate in plotName:
                    thisPlotList.append(plotName)
            thisPlotList.sort()
            if not runQuiet: 
                print '---'
                print '  Found the following plots matching the name key %s'%plotNameTemplate
                print '    ',thisPlotList
            plotList += thisPlotList

        #take the set to avoid duplicates (if multiple plot name templates are used, and match the same plot)
        plotList = list(set(plotList))


    else:
        # plotList = ["presel_M3_control","phosel_noCut_ChIso","phosel_noCut_ChIso_GenuinePhoton","phosel_noCut_ChIso_MisIDEle","phosel_noCut_ChIso_HadronicPhoton","phosel_noCut_ChIso_HadronicFake","phosel_M3","phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake","phosel_AntiSIEIE_ChIso","phosel_AntiSIEIE_ChIso_barrel","phosel_AntiSIEIE_ChIso_endcap","phosel_PhotonCategory"]
        plotList = ["presel_M3_control","presel_M3","phosel_noCut_ChIso","phosel_noCut_ChIso_barrel","phosel_noCut_ChIso_endcap","phosel_noCut_ChIso_GenuinePhoton","phosel_noCut_ChIso_MisIDEle","phosel_noCut_ChIso_HadronicPhoton","phosel_noCut_ChIso_HadronicFake","phosel_noCut_ChIso_GenuinePhoton_barrel","phosel_noCut_ChIso_GenuinePhoton_endcap","phosel_noCut_ChIso_MisIDEle_barrel","phosel_noCut_ChIso_MisIDEle_endcap","phosel_noCut_ChIso_HadronicPhoton_barrel","phosel_noCut_ChIso_HadronicPhoton_endcap","phosel_noCut_ChIso_HadronicFake_barrel","phosel_noCut_ChIso_HadronicFake_endcap","phosel_M3","phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake","phosel_M3_barrel","phosel_M3_endcap","phosel_M3_GenuinePhoton_barrel","phosel_M3_GenuinePhoton_endcap","phosel_M3_MisIDEle_barrel","phosel_M3_MisIDEle_endcap","phosel_M3_HadronicPhoton_barrel","phosel_M3_HadronicPhoton_endcap","phosel_M3_HadronicFake_barrel","phosel_M3_HadronicFake_endcap","phosel_AntiSIEIE_ChIso","phosel_AntiSIEIE_ChIso_barrel","phosel_AntiSIEIE_ChIso_endcap","phosel_AntiSIEIE_ChIso_GenuinePhoton_barrel","phosel_AntiSIEIE_ChIso_GenuinePhoton_endcap","phosel_AntiSIEIE_ChIso_HadronicPhoton_barrel","phosel_AntiSIEIE_ChIso_HadronicPhoton_endcap","phosel_AntiSIEIE_ChIso_HadronicFake_barrel","phosel_AntiSIEIE_ChIso_HadronicFake_endcap","phosel_AntiSIEIE_ChIso_MisIDEle_barrel","phosel_AntiSIEIE_ChIso_MisIDEle_endcap","phosel_MassEGamma","phosel_MassEGammaMisIDEle","phosel_MassEGammaOthers","phosel_MassEGamma_barrel","phosel_MassEGamma_MisIDEle_barrel","phosel_MassEGammaOthers_barrel","phosel_MassEGamma_endcap","phosel_MassEGammaMisIDEle_endcap","phosel_MassEGammaOthers_endcap"]
	'''
        if isLooseCR2g1Selection or isLooseCR2e1Selection:
		plotList.append("presel_WtransMass")
		plotList.append("phosel_WtransMass_barrel")
		plotList.append("phosel_WtransMass_GenuinePhoton_barrel")
		plotList.append("phosel_WtransMass_HadronicPhoton_barrel")
		plotList.append("phosel_WtransMass_MisIDEle_barrel")
		plotList.append("phosel_WtransMass_HadronicFake_barrel")
	elif isTightSelection0b:
		plotList=["phosel_Njet", "phosel_Njet_barrel","phosel_Njet_GenuinePhoton_barrel", "phosel_Njet_MisIDEle_barrel","phosel_Njet_HadronicPhoton_barrel","phosel_Njet_HadronicFake_barrel"]
	'''
	if not runQuiet: print "Making only plots for simultaneous fits"

plotList.sort()
if not runQuiet: print '-----'
if not runQuiet: print "The histogram directory inside the root file is:"
if not runQuiet: print histDestination
if not runQuiet: print "Making the following histogram:"
if not runQuiet: 
    for p in plotList: print "%s,"%p,
if not runQuiet: print
if not runQuiet: print '-----'

histogramsToMake = plotList

allHistsDefined = True
for hist in histogramsToMake:
    if not hist in histogramInfo:
        print "Histogram %s is not defined in HistogramListDict.py"%hist
        allHistsDefined = False
if not allHistsDefined:
    sys.exit()

transferFactor = 1.

histograms=[]
canvas = TCanvas()
#sample = sys.argv[-1]
if sample =="QCD_DD":
    if finalState=="Mu":
        
        qcd_File    = TFile("Histograms/%s/%s/Mu/CR/QCD_DD.root"%(year, ttbarDecayMode,dir_),"read")
        qcd_TF_File = TFile("Histograms/%s/%s/Mu/qcdTransferFactors.root","read")%year
    if finalState=="Ele":
        qcd_File    = TFile("Histograms/%s/%s/Ele/CR/QCD_DD.root"%(year, ttbarDecayMode,dir_),"read")
        qcd_TF_File = TFile("Histograms/%s/%s/Ele/qcdTransferFactors.root","read")%year
    print  qcd_File

    #Calculate the transfer Factor for the QCD events from the QCDcr to the signal region being used, based on jet/bjet multiplicities
    histNjet_QCDcr = qcd_TF_File.Get("histNjet_QCDcr")
    histNjet_0b = qcd_TF_File.Get("histNjet_0b")
    histNjet_1b = qcd_TF_File.Get("histNjet_1b")
    histNjet_2b = qcd_TF_File.Get("histNjet_2b")
   
    print "doing QCD using :", nBJets

    if nBJets==0:
        histNjet_2b.Add(histNjet_1b)
        histNjet_2b.Add(histNjet_0b)
    #    transferFactor_old = histNjet_0b.Integral(nJets+1,-1)/histNjet_QCDcr.Integral(nJets+1,-1)
#	print histNjet_0b.Integral(nJets+1,-1), histNjet_QCDcr.Integral(nJets+1,-1)
	transferFactor =  qcd_TF_File.Get("TransferFactors").GetBinContent(1)
	
    if nBJets==1:
	#print "doing bjets:",nBJets
        histNjet_2b.Add(histNjet_1b)
        transferFactor = histNjet_2b.Integral(nJets+1,-1)/histNjet_QCDcr.Integral(-1,-1)

    #	transferFactor = histNjet_2b.Integral(nJets+1,-1)/histNjet_QCDcr.Integral(nJets+1,-1)
# 	transferFactor =  qcd_TF_File.Get("TransferFactors").GetBinContent(2)
    if nBJets==1:
	#print "doing bjets
	transferFactor = histNjet_2b.Integral(nJets+1,-1)/histNjet_QCDcr.Integral(-1,-1)
    if isLooseCR2e1Selection:
	transferFactor = qcd_TF_File.Get("TransferFactors").GetBinContent(2) 
	print transferFactor, histNjet_1b.Integral(nJets+1,-1), histNjet_QCDcr.Integral(-1,-1)
    for hist in histogramsToMake:

        if not histogramInfo[hist][5]: continue
        if not runQuiet: print "filling", histogramInfo[hist][1], sample

        histograms.append(qcd_File.Get("%s_QCD_DD"%(histogramInfo[hist][1])))
	#print "old value:", transferFactor_old
	print transferFactor, qcd_File, histogramInfo[hist][1]
        #if "Photon" in histogramInfo[hist][1]:continue
	#if "MisIDEle" in histogramInfo[hist][1]:continue
	#if "Fake" in histogramInfo[hist][1]:continue
#	if "Wtrans" in histogramInfo[hist][1]:continue	
        histograms[-1].Scale(transferFactor)

if not "QCD_DD" in sample:
    if not sample in samples:
        print "Sample isn't in list"
        print samples.keys()
        sys.exit()

    tree = TChain("AnalysisTree")
    fileList = samples[sample][0]
    for fileName in fileList:
 	if year=="2017":
		fileName = fileName.replace("2016", "2017")
 	if year=="2018":
		fileName = fileName.replace("2016", "2018")
        tree.Add("%s%s"%(analysisNtupleLocation,fileName))
 #   	print "%s%s"%(analysisNtupleLocation,fileName)
    #print sample

    #print "Number of events:", tree.GetEntries()
    
    for hist in histogramsToMake:
        h_Info = histogramInfo[hist]
#	print hist
        # skip some histograms which rely on MC truth and can't be done in data or QCD data driven templates
        if ('Data' in sample or isQCD) and not h_Info[5]: continue

        if not runQuiet: print "filling", h_Info[1], sample
        evtWeight = ""
#	print TH1F("%s_%s"%(h_Info[1],sample),"%s_%s"%(h_Info[1],sample),h_Info[2][0],h_Info[2][1],h_Info[2][2])
        histograms.append(TH1F("%s_%s"%(h_Info[1],sample),"%s_%s"%(h_Info[1],sample),h_Info[2][0],h_Info[2][1],h_Info[2][2]))
        if h_Info[4]=="":
            evtWeight = "%s%s"%(h_Info[3],weights)
        else:
            evtWeight = h_Info[4]

        if "Data" in sample:
            evtWeight = "%s%s"%(h_Info[3],weights)

        if evtWeight[-1]=="*":
            evtWeight= evtWeight[:-1]


        ### Correctly add the photon weights to the plots
        if 'phosel' in h_Info[1]:
	    	    
            if h_Info[0][:8]=="loosePho":
                evtWeight = "%s*%s"%(evtWeight,loosePhoEff)
            elif h_Info[0][:3]=="pho":
#		print h_Info[0][:3], "%s*%s"%(evtWeight,PhoEff)
                evtWeight = "%s*%s"%(evtWeight,PhoEff)
            else:
#		print h_Info[0], "%s*%s[0]"%(evtWeight,PhoEff)
                evtWeight = "%s*%s[0]"%(evtWeight,PhoEff)
	#print "%s>>%s_%s"%(h_Info[0],h_Info[1],sample),evtWeight
     #   print "evtweight is:", evtWeight	
        tree.Draw("%s>>%s_%s"%(h_Info[0],h_Info[1],sample),evtWeight)

if not os.path.exists(outputhistName):
    os.makedirs(outputhistName)

outputFile = TFile("%s/%s.root"%(outputhistName,sample),"update")
print "%s/%s.root"%(outputhistName,sample)

if not outputFile.GetDirectory(histDestination):
    outputFile.mkdir(histDestination)
outputFile.cd(histDestination)

for h in histograms:
    outputFile.Delete("%s;*"%h.GetName())
    if onlyAddPlots:
        gDirectory.Delete("%s;*"%(h.GetName()))
    h.Write()

outputFile.Close()
