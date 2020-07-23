from ROOT import TH1F, TFile, TChain, TCanvas, gROOT
import sys

from sampleInformation import sampleList
import sampleInformation
import os
from optparse import OptionParser
from datetime import datetime

from subprocess import Popen, PIPE

timeString = datetime.now().strftime("%Y-%m-%d-%H:%M")

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
					 help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s", "--sample", dest="sample", default="",type='str',
					 help="Specify which sample to run on" )
parser.add_option("--lev", "--level", dest="level", default="",type='str',
					 help="Specify up/down of systematic")
parser.add_option("--syst", "--systematic", dest="systematic", default="",type='str',
					 help="Specify which systematic to run on")
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
					 help="Use 4j1t selection" )
parser.add_option("--VeryTight","--verytight", dest="isVeryTightSelection", default=False,action="store_true",
					 help="Use 4j2t selection" )
parser.add_option("--Tight0b","--tight0b", dest="isTightSelection0b", default=False,action="store_true",
					 help="Use 4j0t selection" )
##nabin

parser.add_option("--makeNabinPlots", dest="makeNabinPlots",action="store_true",default=False,
					 help="Make larger list of plots in histogramDict (mostly object kinematics)" )

parser.add_option("--LooseCRge2ge0","--looseCRge2ge0", dest="isLooseCRge2ge0Selection", default=False,action="store_true",
					 help="Use >=2 jets + >=0 bjets selection" )  

parser.add_option("--LooseCRge2e0","--looseCRge2e0", dest="isLooseCRge2e0Selection", default=False,action="store_true",
					 help="Use >=2 jets + =0 bjets selection" ) 


parser.add_option("--LooseCRe2e0","--looseCRe2e0", dest="isLooseCRe2e0Selection", default=False,action="store_true",
					 help="Use ==2 jets + ==0 bjets selection" )                     

parser.add_option("--LooseCRe2e1","--looseCRe2e1", dest="isLooseCRe2e1Selection", default=False,action="store_true",
					 help="Use ==2 jets + ==1 bjets selection" )    

parser.add_option("--LooseCRe3e0","--looseCRe3e0", dest="isLooseCRe3e0Selection", default=False,action="store_true",
					 help="Use ==3 jets + ==0 bjets selection" )   

parser.add_option("--LooseCRge4e0","--looseCRge4e0", dest="isLooseCRge4e0Selection", default=False,action="store_true",
					 help="Use >=4 jets + ==0 bjets selection" )  
parser.add_option("--LooseCRe3e1","--looseCRe3e1", dest="isLooseCRe3e1Selection", default=False,action="store_true",
					 help="Use ==3 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe2e2","--looseCRe2e2", dest="isLooseCRe2e2Selection", default=False,action="store_true",
					 help="Use ==2 jets + ==2 bjets selection" ) 

parser.add_option("--LooseCRe3ge2","--looseCRe3ge2", dest="isLooseCRe3ge2Selection", default=False,action="store_true",
					 help="Use ==3 jets + >=2 bjets selection" )  
					 
parser.add_option("--dilepmassPlots","--dilepmassPlots", dest="Dilepmass",action="store_true",default=False,
					 help="Make only plots for ZJetsSF fits" )
					 
parser.add_option("--makePlotsForSF","--makePlotsForSF", dest="makePlotsForSF",action="store_true",default=False,
					 help="misidele stuff" )
					 
parser.add_option("--makePlotsFlavour", dest="makePlotsFlavour",action="store_true",default=False,
					 help="flavour splitting " )

parser.add_option("--makePlotsMEG","--makePlotsMEG", dest="makePlotsMEG",action="store_true",default=False,
					 help="mass EG histograms" )
					 

### nabin
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
parser.add_option("--output", dest="outputFileName", default="hists",
					 help="Give the name of the root file for histograms to be saved in (default is hists.root)" )
parser.add_option("--plot", dest="plotList",action="append",
					 help="Add plots" )
parser.add_option("--multiPlots", "--multiplots", dest="multiPlotList",action="append",
					 help="Add plots" )
parser.add_option("--testone", "--testoneplot", dest="testoneplot",action="store_true",default=False,
					 help="test one plot without replacing it in the original one" )
parser.add_option("--allPlots","--AllPlots", dest="makeAllPlots",action="store_true",default=False,
					 help="Make full list of plots in histogramDict" )
parser.add_option("--makeSignalRegionPlots", dest="makeSignalRegionPlots",action="store_true",default=False,
					 help="M3 and ChIso plots" )
parser.add_option("--EgammaPlots","--EgammaPlots", dest="makeEGammaPlots",action="store_true",default=False,
					 help="Make only plots for e-gamma mass fits" )
parser.add_option("--dRPlots","--dRPlots", dest="makedRPlots",action="store_true",default=False,
					 help="Make only plots for dR" )
parser.add_option("--genPlots","--genPlots", dest="makegenPlots",action="store_true",default=False,
					 help="Make only plots for 2D histograms" )
parser.add_option("--jetsonly","--jetsonly", dest="makeJetsplots",action="store_true",default=False,
					 help="Extra jets" )

parser.add_option("--quiet", "-q", dest="quiet",default=False,action="store_true",
					 help="Quiet outputs" )
parser.add_option("--fwdjets","--fwdjets", dest="FwdJets",action="store_true",default=False,
					 help="include fwd jets" )
					 
parser.add_option("-y", "--year", dest="Year", default="",type='str',
					 help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("--condor", dest="condor",default=False,action="store_true",
					 help="If running on cmslpc condor (copy files to/from eos)" )

(options, args) = parser.parse_args()

level =options.level
syst = options.systematic
if syst=="":
	runsystematic = False
else:
	runsystematic = True

gROOT.SetBatch(True)

selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()

samples = sampleInformation.main([selYear])

Dilepmass=options.Dilepmass
finalState = options.channel
sample = options.sample
isTightSelection = options.isTightSelection
makeNabinPlots = options.makeNabinPlots
isLooseCRge2ge0Selection = options.isLooseCRge2ge0Selection
isLooseCRge2e0Selection  = options.isLooseCRge2e0Selection
isLooseCRe2e0Selection   = options.isLooseCRe2e0Selection
isLooseCRe2e1Selection   = options.isLooseCRe2e1Selection
isLooseCRe3e0Selection   = options.isLooseCRe3e0Selection
isLooseCRge4e0Selection  = options.isLooseCRge4e0Selection
isLooseCRe3e1Selection   = options.isLooseCRe3e1Selection
isLooseCRe2e2Selection   = options.isLooseCRe2e2Selection
isLooseCRe3ge2Selection  = options.isLooseCRe3ge2Selection

makePlotsForSF = options.makePlotsForSF
makePlotsFlavour =options.makePlotsFlavour
makePlotsMEG = options.makePlotsMEG
## nabin
isLooseCR2e1Selection = options.isLooseCR2e1Selection
isLooseCRe2g1Selection = options.isLooseCRe2g1Selection
isLooseCR3g0Selection=options.isLooseCR3g0Selection
isLooseCRe2g1Selection = options.isLooseCRe2g1Selection
isLooseCRe3g1Selection = options.isLooseCRe3g1Selection
testoneplot=options.testoneplot
isVeryTightSelection=options.isVeryTightSelection
isTightSelection0b = options.isTightSelection0b

onlyAddPlots = options.onlyAddPlots
outputFileName = options.outputFileName
FwdJets=options.FwdJets
makedRPlots=options.makedRPlots
makeAllPlots = options.makeAllPlots
makeSignalRegionPlots = options.makeSignalRegionPlots
makeEGammaPlots = options.makeEGammaPlots
makeJetsplots = options.makeJetsplots

makegenPlots=options.makegenPlots
runQuiet = options.quiet

if not runQuiet: print runsystematic
#exit()

dir2=""
if FwdJets:
	dir2="_fwd"

nJets = 3
nBJets = 1
if testoneplot:
	outputFileName="hist_new"

isQCD = False # what is it doing now?
dir_=""
Q2 = 1.  
Pdf = 1. 
Pileup ="PUweight"
MuEff = "muEffWeight"
EleEff= "eleEffWeight"
PhoEff= "phoEffWeight"
loosePhoEff= "loosePhoEffWeight"
evtWeight ="evtWeight"
btagWeight="btagWeight_1a"

#btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]
							# >=1 b tags      exactly 2 btags == >=2    exactly 1 btags

#atleast 0, atleast 1, atleast 2, exactly 1, btagWeight[0] = exactly 0

#if (syst=="isr" or syst=="fsr") and sample=="TTbar":
#	samples={"TTbar": [["TTbarPowheg_Dilepton_%s_AnalysisNtuple.root"%selYear,
#							"TTbarPowheg_Hadronic_%s_AnalysisNtuple.root"%selYear,
#							"TTbarPowheg_Semilepton_%s_AnalysisNtuple.root"%selYear,
							#"TTbarPowheg4_AnalysisNtuple.root",
#						   ],
#						  kRed+1,
#						  "t#bar{t}",
#						  isMC
#						  ],
#			}

if finalState=="Mu":
	sampleList[-1] = "DataMu"
	sampleList[-2] = "QCDMu"
	if sample=="Data":
		sample = "DataMu"
	if sample=="QCD":
		sample = "QCDMu"

	analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/%s/"%selYear 
	outputhistName = "histograms_%s/mu/%s"%(selYear, outputFileName)
	if runsystematic:
		if syst=="PU":
			print "is here" 
			if level=="up":
				Pileup = "PUweight_Up"
			else:
				Pileup = "PUweight_Do"
			outputhistName = "histograms_%s/mu/%s_PU_%s"%(selYear,outputFileName,level)

		elif 'Q2' in syst:
			if level=="up":
				Q2="q2weight_Up"
			else:
				Q2="q2weight_Do"
			outputhistName = "histograms_%s/mu/%s_Q2_%s"%(selYear,outputFileName,level)

		elif 'Pdf' in syst:
			if syst=="Pdf":
				if level=="up":
					Pdf="pdfweight_Up"
				else:
					Pdf="pdfweight_Do"
				outputhistName = "histograms_%s/mu/%s_Pdf_%s"%(selYear,outputFileName,level)
			else:
				if type(eval(syst[3:]))==type(int()):
					pdfNumber = eval(syst[3:])
					Pdf="pdfSystWeight[%i]/pdfWeight"%(pdfNumber-1)
					outputhistName = "histograms_%s/mu/%s_Pdf/Pdf%i"%(selYear,outputFileName,pdfNumber)				

		elif 'MuEff' in syst:
			if level=="up":
				MuEff = "muEffWeight_Up"
			else:
				MuEff = "muEffWeight_Do"
			outputhistName = "histograms_%s/mu/%s_MuEff_%s"%(selYear,outputFileName,level)

		elif 'EleEff' in syst:
			if level=="up":
				EleEff = "eleEffWeight_Up"
			else:
				EleEff = "eleEffWeight_Do"
			outputhistName = "histograms_%s/mu/%s_EleEff_%s"%(selYear,outputFileName,level)
	
		elif 'PhoEff' in syst:
			if level=="up":
				PhoEff = "phoEffWeight_Up"
				loosePhoEff = "loosePhoEffWeight_Up"
			else:
				PhoEff = "phoEffWeight_Do"
				loosePhoEff = "loosePhoEffWeight_Do"
			outputhistName = "histograms_%s/mu/%s_PhoEff_%s"%(selYear,outputFileName,level)

		elif 'BTagSF_b' in syst:
			if level=="up":
				#btagWeightCategory = ["1","(1-btagWeight_Up[0])","(btagWeight_Up[2])","(btagWeight_Up[1])"]
				btagWeight = "btagWeight_1a_b_Up"
			else:
				#btagWeightCategory = ["1","(1-btagWeight_Do[0])","(btagWeight_Do[2])","(btagWeight_Do[1])"]
				btagWeight = "btagWeight_1a_b_Do"
			outputhistName = "histograms_%s/mu/%s_BTagSF_b_%s"%(selYear,outputFileName,level)

		elif 'BTagSF_l' in syst:
			if level=="up":
				#btagWeightCategory = ["1","(1-btagWeight_Up[0])","(btagWeight_Up[2])","(btagWeight_Up[1])"]
				btagWeight = "btagWeight_1a_l_Up"
			else:
				#btagWeightCategory = ["1","(1-btagWeight_Do[0])","(btagWeight_Do[2])","(btagWeight_Do[1])"]
				btagWeight = "btagWeight_1a_l_Do"
			outputhistName = "histograms_%s/mu/%s_BTagSF_l_%s"%(selYear,outputFileName,level)
		
		elif 'fsr' in syst:
			if level=="up":
				fsr = "FSRweight_Up"
			else:
				fsr = "FSRweight_Do"
			outputhistName = "histograms_%s/mu/%s_fsr_%s"%(selYear,outputFileName,level)
			
		elif 'isr' in syst:
			if level=="up":
				isr = "ISRweight_Up"
			else:
				isr = "ISRweight_Do"
			outputhistName = "histograms_%s/mu/%s_isr_%s"%(selYear,outputFileName,level)
	#	elif syst=="isr" or syst=="fsr":
	#		if level=="up":
	#			analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/%s_up_"%(syst)
		 #      outputhistName = "histograms_%s/mu/%s%s_up"%(selYear,outputFileName,syst)
	#		if level=="down":
	#			analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/%s_down_"%(syst)
		 #      outputhistName = "histograms_%s/mu/%s%s_down"%(selYear,outputFileName,syst)

		else:
			if  level=="up":
				analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_%s/13TeV_AnalysisNtuples/systematics_muons/%s_up_"%(selYear,syst) # more than one 
				outputhistName = "histograms_%s/mu/%s%s_up"%(selYear,outputFileName,syst)
			if level=="down":
				analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_%s/13TeV_AnalysisNtuples/systematics_muons/%s_down_"%(selYear,syst)
				outputhistName = "histograms_%s/mu/%s%s_down"%(selYear,outputFileName,syst)

	extraCuts                = "(passPresel_Mu && nJet>=3 && nBJet>=1)*"
	extraPhotonCuts          = "(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*"

	extraCutsTight           = "(passPresel_Mu && nJet>=4 && nBJet>=1)*"
	extraPhotonCutsTight     = "(passPresel_Mu && nJet>=4 && nBJet>=1 && %s)*"
	
	extraCutsVeryTight       = "(passPresel_Mu && nJet>=4 && nBJet>=2)*"
	extraPhotonCutsVeryTight = "(passPresel_Mu && nJet>=4 && nBJet>=2 && %s)*"
	
	extraCutsTight0b          = "(passPresel_Mu && nJet>=4 && nBJet==0)*"
	extraPhotonCutsTight0b    = "(passPresel_Mu && nJet>=4 && nBJet==0 && %s)*"
	###
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
	
	## nabin Mu
	extraCutsLooseCRge2e0        = "(passPresel_Mu && nJet>=2 && nBJet==0)*"
	extraPhotonCutsLooseCRge2e0  = "(passPresel_Mu && nJet>=2 && nBJet==0 && %s)*"
	extraCutsLooseCRge2ge0       = "(passPresel_Mu && nJet>=2 && nBJet>=0)*"
	extraPhotonCutsLooseCRge2ge0 = "(passPresel_Mu && nJet>=2 && nBJet>=0 && %s)*"
	extraCutsLooseCRe2e0         = "(passPresel_Mu && nJet==2 && nBJet==0)*"
	extraPhotonCutsLooseCRe2e0   = "(passPresel_Mu && nJet==2 && nBJet==0 && %s)*"
	extraCutsLooseCRe2e1         = "(passPresel_Mu && nJet==2 && nBJet==1)*"
	extraPhotonCutsLooseCRe2e1   = "(passPresel_Mu && nJet==2 && nBJet==1 && %s)*"
	extraCutsLooseCRe3e0         = "(passPresel_Mu && nJet==3 && nBJet==0)*"
	extraPhotonCutsLooseCRe3e0   = "(passPresel_Mu && nJet==3 && nBJet==0 && %s)*"
	extraCutsLooseCRge4e0        = "(passPresel_Mu && nJet>=4 && nBJet==0)*"
	extraPhotonCutsLooseCRge4e0  = "(passPresel_Mu && nJet>=4 && nBJet==0 && %s)*"
	extraCutsLooseCRe3e1         = "(passPresel_Mu && nJet==3 && nBJet==1)*"
	extraPhotonCutsLooseCRe3e1   = "(passPresel_Mu && nJet==3 && nBJet==1 && %s)*"
	extraCutsLooseCRe2e2         = "(passPresel_Mu && nJet==2 && nBJet==2)*"
	extraPhotonCutsLooseCRe2e2   = "(passPresel_Mu && nJet==2 && nBJet==2 && %s)*"
	extraCutsLooseCRe3ge2        = "(passPresel_Mu && nJet==3 && nBJet>=2)*"
	extraPhotonCutsLooseCRe3ge2  = "(passPresel_Mu && nJet==3 && nBJet>=2 && %s)*"

elif finalState=="Ele":
	sampleList[-1] = "DataEle"
	sampleList[-2] = "QCDEle"
	if sample=="Data":
		sample = "DataEle"
	if sample=="QCD":
		sample = "QCDEle"
	#analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples_2019/electrons/V08_00_26_07/"
	analysisNtupleLocation =  "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/%s/"%selYear
	outputhistName = "histograms_%s/ele/%s"%(selYear,outputFileName)
	if runsystematic:

		if syst=="PU":
			print "is here" 
			if level=="up":
				Pileup = "PUweight_Up"
			else:
				Pileup = "PUweight_Do"
			outputhistName = "histograms_%s/ele/%s_PU_%s"%(selYear,outputFileName,level)

		elif 'Q2' in syst:
			if level=="up":
				Q2="q2weight_Up"
			else:
				Q2="q2weight_Do"
			outputhistName = "histograms_%s/ele/%s_Q2_%s"%(selYear,outputFileName,level)

		elif 'Pdf' in syst:
			if syst=="Pdf":
				if level=="up":
					Pdf="pdfweight_Up"
				else:
					Pdf="pdfweight_Do"
				outputhistName = "histograms_%s/ele/%s_Pdf_%s"%(selYear,outputFileName,level)
			else:
				if type(eval(syst[3:]))==type(int()):
					pdfNumber = eval(syst[3:])
					Pdf="pdfSystWeight[%i]/pdfWeight"%(pdfNumber-1)
					outputhistName = "histograms_%s/ele/%s_Pdf/Pdf%i"%(selYear,outputFileName,pdfNumber)				

		elif 'MuEff' in syst:
			if level=="up":
				MuEff = "muEffWeight_Up"
			else:
				MuEff = "muEffWeight_Do"
			outputhistName = "histograms_%s/ele/%s_MuEff_%s"%(selYear,outputFileName,level)

		elif 'EleEff' in syst:
			if level=="up":
				EleEff = "eleEffWeight_Up"
			else:
				EleEff = "eleEffWeight_Do"
			outputhistName = "histograms_%s/ele/%s_EleEff_%s"%(selYear,outputFileName,level)
	
		elif 'PhoEff' in syst:
			if level=="up":
				PhoEff = "phoEffWeight_Up"
				loosePhoEff = "loosePhoEffWeight_Up"
			else:
				PhoEff = "phoEffWeight_Do"
				loosePhoEff = "loosePhoEffWeight_Do"
			outputhistName = "histograms_%s/ele/%s_PhoEff_%s"%(selYear,outputFileName,level)

		elif 'BTagSF_b' in syst:
			if level=="up":
				#btagWeightCategory = ["1","(1-btagWeight_Up[0])","(btagWeight_Up[2])","(btagWeight_Up[1])"]
				btagWeight = "btagWeight_1a_b_Up"
			else:
				#btagWeightCategory = ["1","(1-btagWeight_Do[0])","(btagWeight_Do[2])","(btagWeight_Do[1])"]
				btagWeight = "btagWeight_1a_b_Do"
			outputhistName = "histograms_%s/ele/%s_BTagSF_b_%s"%(selYear,outputFileName,level)

		elif 'BTagSF_l' in syst:
			if level=="up":
				#btagWeightCategory = ["1","(1-btagWeight_Up[0])","(btagWeight_Up[2])","(btagWeight_Up[1])"]
				btagWeight = "btagWeight_1a_l_Up"
			else:
				#btagWeightCategory = ["1","(1-btagWeight_Do[0])","(btagWeight_Do[2])","(btagWeight_Do[1])"]
				btagWeight = "btagWeight_1a_l_Do"
			outputhistName = "histograms_%s/ele/%s_BTagSF_l_%s"%(selYear,outputFileName,level)

		elif 'fsr' in syst:
			if level=="up":
				fsr = "FSRweight_Up"
			else:
				fsr = "FSRweight_Do"
			outputhistName = "histograms_%s/ele/%s_fsr_%s"%(selYear,outputFileName,level)
			
		elif 'isr' in syst:
			if level=="up":
				isr = "ISRweight_Up"
			else:
				isr = "ISRweight_Do"
			outputhistName = "histograms_%s/ele/%s_isr_%s"%(selYear,outputFileName,level)
			
	
	#	elif syst=="isr" or syst=="fsr":
	#		if level=="up":
	#			analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/%s_up_"%(syst)
		 #      outputhistName = "histograms_%s/ele/%s%s_up"%(selYear,outputFileName,syst)
	#		if level=="down":
	#			analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/%s_down_"%(syst)
		 #      outputhistName = "histograms_%s/ele/%s%s_down"%(selYear,outputFileName,syst)

		else:
			if  level=="up":
				analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_%s/13TeV_AnalysisNtuples/systematics_muons/%s_up_"%(selYear,syst) # more than one 
				outputhistName = "histograms_%s/ele/%s%s_up"%(selYear,outputFileName,syst)
			if level=="down":
				analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_%s/13TeV_AnalysisNtuples/systematics_muons/%s_down_"%(selYear,syst)
				outputhistName = "histograms_%s/ele/%s%s_down"%(selYear,outputFileName,syst)

	extraCuts                = "(passPresel_Ele && nJet>=3 && nBJet>=1)*"
	extraPhotonCuts          = "(passPresel_Ele && nJet>=3 && nBJet>=1 && %s)*"

	extraCutsTight           = "(passPresel_Ele && nJet>=4 && nBJet>=1)*"
	extraPhotonCutsTight     = "(passPresel_Ele && nJet>=4 && nBJet>=1 && %s)*"
	
	extraCutsVeryTight       = "(passPresel_Ele && nJet>=4 && nBJet>=2)*"
	extraPhotonCutsVeryTight = "(passPresel_Ele && nJet>=4 && nBJet>=2 && %s)*"

	extraCutsTight0b         = "(passPresel_Ele && nJet>=4 && nBJet==0)*"
	extraPhotonCutsTight0b   = "(passPresel_Ele && nJet>=4 && nBJet==0 && %s)*"

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
	
	## nabin Ele
	extraCutsLooseCRge2e0         = "(passPresel_Ele && nJet>=2 && nBJet==0)*"
	extraPhotonCutsLooseCRge2e0   = "(passPresel_Ele && nJet>=2 && nBJet==0 && %s)*"
	extraCutsLooseCRge2ge0        = "(passPresel_Ele && nJet>=2 && nBJet>=0)*"
	extraPhotonCutsLooseCRge2ge0  = "(passPresel_Ele && nJet>=2 && nBJet>=0 && %s)*"
	extraCutsLooseCRe2e0          = "(passPresel_Ele && nJet==2 && nBJet==0)*"
	extraPhotonCutsLooseCRe2e0    = "(passPresel_Ele && nJet==2 && nBJet==0 && %s)*"
	extraCutsLooseCRe2e1          = "(passPresel_Ele && nJet==2 && nBJet==1)*"
	extraPhotonCutsLooseCRe2e1    = "(passPresel_Ele && nJet==2 && nBJet==1 && %s)*"
	extraCutsLooseCRe3e0          = "(passPresel_Ele && nJet==3 && nBJet==0)*"
	extraPhotonCutsLooseCRe3e0    = "(passPresel_Ele && nJet==3 && nBJet==0 && %s)*"
	extraCutsLooseCRge4e0         = "(passPresel_Ele && nJet>=4 && nBJet==0)*"
	extraPhotonCutsLooseCRge4e0   = "(passPresel_Ele && nJet>=4 && nBJet==0 && %s)*"
	extraCutsLooseCRe3e1          = "(passPresel_Ele && nJet==3 && nBJet==1)*"
	extraPhotonCutsLooseCRe3e1    = "(passPresel_Ele && nJet==3 && nBJet==1 && %s)*"
	extraCutsLooseCRe2e2          = "(passPresel_Ele && nJet==2 && nBJet==2)*"
	extraPhotonCutsLooseCRe2e2    = "(passPresel_Ele && nJet==2 && nBJet==2 && %s)*"
	extraCutsLooseCRe3ge2         = "(passPresel_Ele && nJet==3 && nBJet>=2)*"
	extraPhotonCutsLooseCRe3ge2   = "(passPresel_Ele && nJet==3 && nBJet>=2 && %s)*"
	#nabin
	
elif finalState=="DiMu":
	sampleList[-1] = "DataMu"
	sampleList[-2] = "QCDMu"

	if sample=="Data":
		sample = "DataMu"
	if sample=="QCD":
		sample = "QCDMu"
	analysisNtupleLocation =  "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/Dilepton/%s/"%selYear
	outputhistName = "histograms_%s/mu/Dilep_%s"%(selYear,outputFileName)

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
	# nabin
	extraCutsLooseCRge2e0         = "(passPresel_Mu && nJet>=2 && nBJet==0)*"
	extraPhotonCutsLooseCRge2e0   = "(passPresel_Mu && nJet>=2 && nBJet==0 && %s)*"
	extraCutsLooseCRge2ge0        = "(passPresel_Mu && nJet>=2 && nBJet>=0)*"
	extraPhotonCutsLooseCRge2ge0  = "(passPresel_Mu && nJet>=2 && nBJet>=0 && %s)*"
	extraCutsLooseCRe2e0          = "(passPresel_Mu && nJet==2 && nBJet==0)*"
	extraPhotonCutsLooseCRe2e0    = "(passPresel_Mu && nJet==2 && nBJet==0 && %s)*"
	extraCutsLooseCRe2e1          = "(passPresel_Mu && nJet==2 && nBJet==1)*"
	extraPhotonCutsLooseCRe2e1    = "(passPresel_Mu && nJet==2 && nBJet==1 && %s)*"
	extraCutsLooseCRe3e0          = "(passPresel_Mu && nJet==3 && nBJet==0)*"
	extraPhotonCutsLooseCRe3e0    = "(passPresel_Mu && nJet==3 && nBJet==0 && %s)*"
	extraCutsLooseCRge4e0         = "(passPresel_Mu && nJet>=4 && nBJet==0)*"
	extraPhotonCutsLooseCRge4e0   = "(passPresel_Mu && nJet>=4 && nBJet==0 && %s)*"
	extraCutsLooseCRe3e1          = "(passPresel_Mu && nJet==3 && nBJet==1)*"
	extraPhotonCutsLooseCRe3e1    = "(passPresel_Mu && nJet==3 && nBJet==1 && %s)*"
	extraCutsLooseCRe2e2          = "(passPresel_Mu && nJet==2 && nBJet==2)*"
	extraPhotonCutsLooseCRe2e2    = "(passPresel_Mu && nJet==2 && nBJet==2 && %s)*"
	extraCutsLooseCRe3ge2         = "(passPresel_Mu && nJet==3 && nBJet>=2)*"
	extraPhotonCutsLooseCRe3ge2   = "(passPresel_Mu && nJet==3 && nBJet>=2 && %s)*"

	
elif finalState=="DiEle":
	sampleList[-1] = "DataEle"
	sampleList[-2] = "QCDEle"
	if sample=="Data":
		sample = "DataEle"
	if sample=="QCD":
		sample = "QCDEle"
	analysisNtupleLocation =  "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/Dilepton/%s/"%selYear
	outputhistName = "histograms_%s/ele/Dilep_%s"%(selYear,outputFileName)


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
	
	## nabin Ele
	extraCutsLooseCRge2e0         = "(passPresel_Ele && nJet>=2 && nBJet==0)*"
	extraPhotonCutsLooseCRge2e0   = "(passPresel_Ele && nJet>=2 && nBJet==0 && %s)*"
	extraCutsLooseCRge2ge0        = "(passPresel_Ele && nJet>=2 && nBJet>=0)*"
	extraPhotonCutsLooseCRge2ge0  = "(passPresel_Ele && nJet>=2 && nBJet>=0 && %s)*"
	extraCutsLooseCRe2e0          = "(passPresel_Ele && nJet==2 && nBJet==0)*"
	extraPhotonCutsLooseCRe2e0    = "(passPresel_Ele && nJet==2 && nBJet==0 && %s)*"
	extraCutsLooseCRe2e1          = "(passPresel_Ele && nJet==2 && nBJet==1)*"
	extraPhotonCutsLooseCRe2e1    = "(passPresel_Ele && nJet==2 && nBJet==1 && %s)*"
	extraCutsLooseCRe3e0          = "(passPresel_Ele && nJet==3 && nBJet==0)*"
	extraPhotonCutsLooseCRe3e0    = "(passPresel_Ele && nJet==3 && nBJet==0 && %s)*"
	extraCutsLooseCRge4e0         = "(passPresel_Ele && nJet>=4 && nBJet==0)*"
	extraPhotonCutsLooseCRge4e0   = "(passPresel_Ele && nJet>=4 && nBJet==0 && %s)*"
	extraCutsLooseCRe3e1          = "(passPresel_Ele && nJet==3 && nBJet==1)*"
	extraPhotonCutsLooseCRe3e1    = "(passPresel_Ele && nJet==3 && nBJet==1 && %s)*"
	extraCutsLooseCRe2e2          = "(passPresel_Ele && nJet==2 && nBJet==2)*"
	extraPhotonCutsLooseCRe2e2    = "(passPresel_Ele && nJet==2 && nBJet==2 && %s)*"
	extraCutsLooseCRe3ge2         = "(passPresel_Ele && nJet==3 && nBJet>=2)*"
	extraPhotonCutsLooseCRe3ge2   = "(passPresel_Ele && nJet==3 && nBJet>=2 && %s)*"

elif finalState=="QCDMu":
	sampleList[-1] = "DataMu"
	sampleList[-2] = "QCDMu"
	if sample=="Data":
		sample = "DataMu"
	if sample=="QCD":
		sample = "QCDMu"

	isQCD = True

	analysisNtupleLocation =  "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/%s/"%selYear
	outputhistName = "histograms_%s/mu/qcd%sCR"%(selYear,outputFileName)

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

	## nabin qcd mu
	extraCutsLooseCRge2e0         = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet==0)*"
	extraPhotonCutsLooseCRge2e0   = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet==0 && %s)*"	
	extraCutsLooseCRge2ge0        = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet>=0)*"
	extraPhotonCutsLooseCRge2ge0  = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && nBJet>=0 && %s)*"
	extraCutsLooseCRe2e0          = "(passPresel_Mu && muPFRelIso<0.3 && nJet==2 && nBJet==0)*"
	extraPhotonCutsLooseCRe2e0    = "(passPresel_Mu && muPFRelIso<0.3 && nJet==2 && nBJet==0 && %s)*"
	extraCutsLooseCRe2e1          = "(passPresel_Mu && muPFRelIso<0.3 && nJet==2 && nBJet==1)*"
	extraPhotonCutsLooseCRe2e1    = "(passPresel_Mu && muPFRelIso<0.3 && nJet==2 && nBJet==1 && %s)*"
	extraCutsLooseCRe3e0          = "(passPresel_Mu && muPFRelIso<0.3 && nJet==3 && nBJet==0)*"
	extraPhotonCutsLooseCRe3e0    = "(passPresel_Mu && muPFRelIso<0.3 && nJet==3 && nBJet==0 && %s)*"    
	extraCutsLooseCRge4e0         = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && nBJet==0)*"
	extraPhotonCutsLooseCRge4e0   = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && nBJet==0 && %s)*"  
	extraCutsLooseCRe3e1          = "(passPresel_Mu && muPFRelIso<0.3 && nJet==3 && nBJet==1)*"
	extraPhotonCutsLooseCRe3e1    = "(passPresel_Mu && muPFRelIso<0.3 && nJet==3 && nBJet==1 && %s)*"   
	extraCutsLooseCRe2e2          = "(passPresel_Mu && muPFRelIso<0.3 && nJet==2 && nBJet==2)*"
	extraPhotonCutsLooseCRe2e2    = "(passPresel_Mu && muPFRelIso<0.3 && nJet==2 && nBJet==2 && %s)*"
	extraCutsLooseCRe3ge2         = "(passPresel_Mu && muPFRelIso<0.3 && nJet==3 && nBJet>=2)*"
	extraPhotonCutsLooseCRe3ge2   = "(passPresel_Mu && muPFRelIso<0.3 && nJet==3 && nBJet>=2 && %s)*"



	#nabin
elif finalState=="QCDMu2":
	sampleList[-1] = "DataMu"
	sampleList[-2] = "QCDMu"
	if sample=="Data":
		sample = "DataMu"
	if sample=="QCD":
		sample = "QCDMu"

	isQCD = True

	analysisNtupleLocation =  "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/%s/"%selYear
	outputhistName = "histograms_%s/mu/qcd%sCR2"%(selYear,outputFileName)

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
	analysisNtupleLocation =  "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/%s/"%selYear
	outputhistName = "histograms_%s/ele/qcd%sCR"%(selYear,outputFileName)
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
	
	   ## nabin qcd ele
	extraCutsLooseCRge2e0         = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet==0)*"
	extraPhotonCutsLooseCRge2e0   = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet==0 && %s)*" 	
	extraCutsLooseCRge2ge0        = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet>=0)*"
	extraPhotonCutsLooseCRge2ge0  = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=2 && nBJet>=0 && %s)*" 
	extraCutsLooseCRe2e0          = "(passPresel_Ele && elePFRelIso>0.01 && nJet==2 && nBJet==0)*"
	extraPhotonCutsLooseCRe2e0    = "(passPresel_Ele && elePFRelIso>0.01 && nJet==2 && nBJet==0 && %s)*" 
	extraCutsLooseCRe2e1          = "(passPresel_Ele && elePFRelIso>0.01 && nJet==2 && nBJet==1)*"
	extraPhotonCutsLooseCRe2e1    = "(passPresel_Ele && elePFRelIso>0.01 && nJet==2 && nBJet==1 && %s)*" 
	extraCutsLooseCRe3e0          = "(passPresel_Ele && elePFRelIso>0.01 && nJet==3 && nBJet==0)*"
	extraPhotonCutsLooseCRe3e0    = "(passPresel_Ele && elePFRelIso>0.01 && nJet==3 && nBJet==0 && %s)*" 
	extraCutsLooseCRge4e0         = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=4 && nBJet==0)*"
	extraPhotonCutsLooseCRge4e0   = "(passPresel_Ele && elePFRelIso>0.01 && nJet>=4 && nBJet==0 && %s)*" 
	extraCutsLooseCRe3e1          = "(passPresel_Ele && elePFRelIso>0.01 && nJet==3 && nBJet==1)*"
	extraPhotonCutsLooseCRe3e1    = "(passPresel_Ele && elePFRelIso>0.01 && nJet==3 && nBJet==1 && %s)*" 
	extraCutsLooseCRe2e2          = "(passPresel_Ele && elePFRelIso>0.01 && nJet==2 && nBJet==2)*"
	extraPhotonCutsLooseCRe2e2    = "(passPresel_Ele && elePFRelIso>0.01 && nJet==2 && nBJet==2 && %s)*" 
	extraCutsLooseCRe3ge2         = "(passPresel_Ele && elePFRelIso>0.01 && nJet==3 && nBJet>=2)*"
	extraPhotonCutsLooseCRe3ge2   = "(passPresel_Ele && elePFRelIso>0.01 && nJet==3 && nBJet>=2 && %s)*"



else:
	print "Unknown final state, options are Mu and Ele"
	sys.exit()


#btagWeight = btagWeightCategory[s]

#btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]
							# >=1 b tags      exactly 2 btags == >=2    exactly 1 btags
#atleast 0, atleast 1, atleast 2, exactly 1, btagWeight[0] = exactly 0


if isTightSelection:
	if not runQuiet: print "Tight Select"
	nJets = 4
	nBJets = 1
	#btagWeight = btagWeightCategory[nBJets]
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsTight 
	extraPhotonCuts = extraPhotonCutsTight 
	outputhistName = outputhistName +"_tight"
	dir_="_tight"

if isVeryTightSelection:
	if not runQuiet: print "Very Tight Select"
	nJets = 4
	nBJets = 2
	#btagWeight = btagWeightCategory[nBJets]
	extraCuts = extraCutsVeryTight
	extraPhotonCuts = extraPhotonCutsVeryTight
	outputhistName = outputhistName + "_verytight"
	dir_="_verytight"

if isTightSelection0b:
	if not runQuiet: print "Tight0b Select"
	nJets = 4
	nBJets = 0
	#btagWeight = btagWeightCategory[nBJets]
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsTight0b
	extraPhotonCuts = extraPhotonCutsTight0b
	outputhistName = outputhistName + "_tight0b"
	dir_="_tight0b"

## start nabin
if isLooseCRge2ge0Selection:
	if not runQuiet: print " Loose CR >=2 jet and >=0 bjet"
	nJets = 2
	nBJets = 0
	#btagWeight = btagWeightCategory[nBJets]
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsLooseCRge2ge0
	extraPhotonCuts = extraPhotonCutsLooseCRge2ge0
	outputhistName = outputhistName + "_looseCRge2ge0"
	dir_="_looseCRge2ge0"

if isLooseCRge2e0Selection:
	if not runQuiet: print " Loose CR >=2 jet and =0 bjet"
	nJets = 2
	nBJets = 0
	#btagWeight = "(btagWeight[0])"
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsLooseCRge2e0
	extraPhotonCuts = extraPhotonCutsLooseCRge2e0
	outputhistName = outputhistName + "_looseCRge2e0"
	dir_="_looseCRge2e0"

if isLooseCRe2e0Selection:
	if not runQuiet: print " Loose CR ==2 jet and ==0 bjet"
	nJets = 2
	nBJets = 0
	#btagWeight = "(btagWeight[0])"
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsLooseCRe2e0
	extraPhotonCuts = extraPhotonCutsLooseCRe2e0
	outputhistName = outputhistName + "_looseCRe2e0"
	dir_="_looseCRe2e0"

if isLooseCRe2e1Selection:
	if not runQuiet: print " Loose CR ==2 jet and ==1 bjet"
	nJets = 2
	nBJets = 1
	#btagWeight = "(btagWeight[1])"
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsLooseCRe2e1
	extraPhotonCuts = extraPhotonCutsLooseCRe2e1
	outputhistName = outputhistName + "_looseCRe2e1"
	dir_="_looseCRe2e1"

if isLooseCRe3e0Selection:
	if not runQuiet: print " Loose CR ==3 jet and ==0 bjet"
	nJets = 3
	nBJets = 0
	#btagWeight = "(btagWeight[0])"
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsLooseCRe3e0
	extraPhotonCuts = extraPhotonCutsLooseCRe3e0
	outputhistName = outputhistName + "_looseCRe3e0"
	dir_="_looseCRe3e0"

if isLooseCRge4e0Selection:
	if not runQuiet: print " Loose CR >=4 jet and ==0 bjet"
	nJets = 4
	nBJets = 0
	#btagWeight = "(btagWeight[0])"
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsLooseCRge4e0
	extraPhotonCuts = extraPhotonCutsLooseCRge4e0
	outputhistName = outputhistName + "_looseCRge4e0"
	dir_="_looseCRge4e0"
## 3 more
if isLooseCRe3e1Selection:
	if not runQuiet: print " Loose CR ==3 jet and ==1 bjet"
	nJets = 3
	nBJets = 1
	#btagWeight = "(btagWeight[1])"
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsLooseCRe3e1
	extraPhotonCuts = extraPhotonCutsLooseCRe3e1
	outputhistName = outputhistName + "_looseCRe3e1"
	dir_="_looseCRe3e1"

if isLooseCRe2e2Selection:
	if not runQuiet: print " Loose CR ==2 jet and ==2 bjet"
	nJets = 2
	nBJets = 2
	#btagWeight = "(btagWeight[2])"
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsLooseCRe2e2
	extraPhotonCuts = extraPhotonCutsLooseCRe2e2
	outputhistName = outputhistName + "_looseCRe2e2"
	dir_="_looseCRe2e2"

if isLooseCRe3ge2Selection:
	if not runQuiet: print " Loose CR >=3 jet and >=2 bjet"
	nJets = 3
	nBJets = 2
	#btagWeight = btagWeightCategory[nBJets]
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"
	extraCuts = extraCutsLooseCRe3ge2
	extraPhotonCuts = extraPhotonCutsLooseCRe3ge2
	outputhistName = outputhistName + "_looseCRe3ge2"
	dir_="_looseCRe3ge2"
## end nabin 

if isLooseCR2e1Selection:
	if not runQuiet: print "Loose Control Region Select"
	nJets = 2
	nBJets = 1
	#btagWeight = "(btagWeight[1])"
	#    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[1]"
	extraCuts = extraCutsLooseCR2e1
	extraPhotonCuts = extraPhotonCutsLooseCR2e1
	outputhistName = outputhistName + "_looseCR2e1"
	dir_="_looseCR2e1"

if isLooseCRe2g1Selection:
	if not runQuiet: print "Loose Control Region1 Select"
	nJets = 2
	nBJets = 1
	#btagWeight = btagWeightCategory[nBJets]
	if 'QCD' in finalState:
		btagWeight="1"
	# weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*(1-btagWeight[0])"
	# if 'QCD' in finalState:
	#     weights = "evtWeight*PUweight*muEffWeight*eleEffWeight"
	extraCuts = extraCutsLooseCR2g1
	extraPhotonCuts = extraPhotonCutsLooseCR2g1    
	outputhistName = outputhistName + "_looseCRe2g1"
	dir_="_looseCRe2g1"

if isLooseCR3g0Selection:
	if not runQuiet: print "Loose Control Region for EGamma"
	nJets = 3
	nBJets = 0
	#btagWeight = "btagWeight[0]" 
	extraCuts = extraCutsLooseCRe3g0
	extraPhotonCuts = extraPhotonCutsLooseCRe3g0
	outputhistName = outputhistName + "_looseCRe3g0"
	dir_="_looseCRe3g0"

if isLooseCRe3g1Selection:
	if not runQuiet: print "Loose Control Region Select"
	nJets = 3
	nBJets = 1
	#btagWeight = btagWeightCategory[nBJets]
	#weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*(btagWeight[0])"
	extraCuts = extraCutsLooseCRe3g1
	extraPhotonCuts = extraPhotonCutsLooseCRe3g1
	outputhistName = outputhistName + "_looseCRe3g1"
	dir_="_looseCRe3g1"

if "QCD" in finalState:
	nBJets = 0
	#btagWeight="btagWeight[0]"

weights = "%s*%s*%s*%s*%s*%s*%s"%(evtWeight,Pileup,MuEff,EleEff,Q2,Pdf,btagWeight)
#weights = "%s*%s*%s*%s*%s*%s*%s"%(evtWeight,Pileup,1,1,Q2,Pdf,btagWeight)
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
	elif makePlotsFlavour:
		plotList =["phosel_MassEGamma_LightTag","phosel_MassEGamma_CTag","phosel_MassEGamma_BTag"] 
	elif makePlotsMEG:
		plotList =["phosel_MassEGamma", "phosel_MassEGamma_GenuinePhoton", "phosel_MassEGamma_MisIDEle", "phosel_MassEGamma_HadronicPhoton", "phosel_MassEGamma_HadronicFake"] 	
	elif makePlotsForSF:
		plotList =["presel_Njet","presel_WtransMass", "phosel_MassEGamma", "phosel_MassEGamma_GenuinePhoton",  
	   "phosel_MassEGamma_MisIDEle", "phosel_MassEGamma_HadronicPhoton", "phosel_MassEGamma_HadronicFake",
	   "phosel_Njet","phosel_WtransMass","presel_jet1Pt","phosel_jet1Pt",
	   "phosel_WtransMass_GenuinePhoton","phosel_WtransMass_MisIDEle","phosel_WtransMass_HadronicPhoton",
	   "phosel_WtransMass_HadronicFake","phosel_jet1Pt_GenuinePhoton",
	   "phosel_jet1Pt_MisIDEle","phosel_jet1Pt_HadronicPhoton","phosel_jet1Pt_HadronicFake",
	   "presel_M3", "phosel_M3", "phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake",
	   "phosel_mediumID_ChIso", "phosel_mediumID_ChIso_GenuinePhoton", "phosel_mediumID_ChIso_MisIDEle","phosel_mediumID_ChIso_HadronicPhoton","phosel_mediumID_ChIso_HadronicFake",
	   "phosel_noCut_SIEIE", "phosel_noCut_SIEIE_GenuinePhoton", "phosel_noCut_SIEIE_MisIDEle","phosel_noCut_SIEIE_HadronicPhoton", "phosel_noCut_SIEIE_HadronicFake","presel_MET","phosel_MET"]
	elif makeSignalRegionPlots:
		plotList =["presel_M3", "phosel_M3", "phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake",
				   "phosel_mediumID_ChIso", "phosel_mediumID_ChIso_GenuinePhoton", "phosel_mediumID_ChIso_MisIDEle","phosel_mediumID_ChIso_HadronicPhoton","phosel_mediumID_ChIso_HadronicFake"]
		if not runQuiet: print "Making subset of kinematic plots"
	elif makeNabinPlots and finalState == 'Mu':
		plotList = ["presel_muEta",	"phosel_muEta","presel_muPhi","phosel_LeadingPhotonEta","phosel_LeadingPhotonEt", "phosel_LeadingPhotonEt_GenuinePhoton","phosel_LeadingPhotonEt_MisIDEle","phosel_LeadingPhotonEt_HadronicPhoton", "phosel_LeadingPhotonEt_HadronicFake", "presel_jet1Pt", "presel_jet2Pt","presel_Njet", "presel_muPt",  "presel_M3", "presel_WtransMass", "phosel_Njet", "phosel_muPt",  "phosel_M3", "phosel_WtransMass", "phosel_MassEGammaMisIDEle", "phosel_MassEGammaOthers","phosel_noCut_SIEIE", "phosel_noCut_SIEIE_GenuinePhoton", "phosel_noCut_SIEIE_MisIDEle","phosel_noCut_SIEIE_HadronicPhoton", "phosel_noCut_SIEIE_HadronicFake","presel_MET","phosel_MET","phosel_MassEGamma", "phosel_MassEGamma_GenuinePhoton", "phosel_MassEGamma_MisIDEle", "phosel_MassEGamma_HadronicPhoton","phosel_MassEGamma_HadronicFake"	]
	elif makeNabinPlots and finalState == 'Ele':
		plotList = ["presel_eleSCEta","phosel_eleSCEta","presel_elePhi","phosel_LeadingPhotonEta","phosel_LeadingPhotonEt", "phosel_LeadingPhotonEt_GenuinePhoton","phosel_LeadingPhotonEt_MisIDEle","phosel_LeadingPhotonEt_HadronicPhoton", "phosel_LeadingPhotonEt_HadronicFake", "presel_jet1Pt", "presel_jet2Pt","presel_Njet", "presel_elePt",  "presel_M3", "presel_WtransMass", "phosel_Njet", "phosel_elePt",  "phosel_M3", "phosel_WtransMass", "phosel_MassEGammaMisIDEle", "phosel_MassEGammaOthers","phosel_noCut_SIEIE",                   "phosel_noCut_SIEIE_GenuinePhoton",      "phosel_noCut_SIEIE_MisIDEle",           "phosel_noCut_SIEIE_HadronicPhoton",     "phosel_noCut_SIEIE_HadronicFake","presel_MET","phosel_MET","phosel_MassEGamma",               "phosel_MassEGamma_GenuinePhoton", "phosel_MassEGamma_MisIDEle",      "phosel_MassEGamma_HadronicPhoton","phosel_MassEGamma_HadronicFake"]
		if not runQuiet: print "Making subset of kinematic plots"
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
		plotList = ["presel_M3_control","presel_M3","phosel_noCut_ChIso","phosel_noCut_ChIso_barrel","phosel_noCut_ChIso_endcap","phosel_noCut_ChIso_GenuinePhoton","phosel_noCut_ChIso_MisIDEle","phosel_noCut_ChIso_HadronicPhoton","phosel_noCut_ChIso_HadronicFake","phosel_noCut_ChIso_GenuinePhoton_barrel","phosel_noCut_ChIso_GenuinePhoton_endcap","phosel_noCut_ChIso_MisIDEle_barrel","phosel_noCut_ChIso_MisIDEle_endcap","phosel_noCut_ChIso_HadronicPhoton_barrel","phosel_noCut_ChIso_HadronicPhoton_endcap","phosel_noCut_ChIso_HadronicFake_barrel","phosel_noCut_ChIso_HadronicFake_endcap","phosel_M3","phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake","phosel_M3_barrel","phosel_M3_endcap","phosel_M3_GenuinePhoton_barrel","phosel_M3_GenuinePhoton_endcap","phosel_M3_MisIDEle_barrel","phosel_M3_MisIDEle_endcap","phosel_M3_HadronicPhoton_barrel","phosel_M3_HadronicPhoton_endcap","phosel_M3_HadronicFake_barrel","phosel_M3_HadronicFake_endcap","phosel_AntiSIEIE_ChIso","phosel_AntiSIEIE_ChIso_barrel","phosel_AntiSIEIE_ChIso_endcap","phosel_AntiSIEIE_ChIso_GenuinePhoton_barrel","phosel_AntiSIEIE_ChIso_GenuinePhoton_endcap","phosel_AntiSIEIE_ChIso_HadronicPhoton_barrel","phosel_AntiSIEIE_ChIso_HadronicPhoton_endcap","phosel_AntiSIEIE_ChIso_HadronicFake_barrel","phosel_AntiSIEIE_ChIso_HadronicFake_endcap","phosel_AntiSIEIE_ChIso_MisIDEle_barrel","phosel_AntiSIEIE_ChIso_MisIDEle_endcap","phosel_MassEGamma","phosel_MassEGammaMisIDEle","phosel_MassEGammaOthers","phosel_MassEGamma_barrel","phosel_MassEGamma_MisIDEle_barrel","phosel_MassEGammaOthers_barrel","phosel_MassEGamma_endcap","phosel_MassEGammaMisIDEle_endcap","phosel_MassEGammaOthers_endcap"]
		if not runQuiet: print "Making only plots for simultaneous fits"

plotList.sort()
if not runQuiet: print '-----'
if not runQuiet: print "Making the following plots:"
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
		
		qcd_File    = TFile("histograms_%s/mu/qcd%sCR%s/QCD_DD.root"%(selYear,outputFileName,dir_),"read")
		qcd_TF_File = TFile("histograms_%s/mu/qcdTransferFactors.root"%selYear,"read")

	if finalState=="Ele":
		
		qcd_File    = TFile("histograms_%s/ele/qcd%sCR%s/QCD_DD.root"%(selYear,outputFileName,dir_),"read")
		print  qcd_File

		qcd_TF_File = TFile("histograms_%s/ele/qcdTransferFactors.root"%selYear,"read")

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
	if finalState=="DiMu" or finalState=="DiEle":
		fileListTemp = samples[sample][0]
		fileList1 = ["{}{}".format("Dilep_",i) for i in fileListTemp]
	else:
		fileList1 = samples[sample][0]
	elementsToRemove = ["Dilep_Data_SingleEle_a_2016_AnalysisNtuple.root", 
						"Dilep_Data_SingleMu_a_2016_AnalysisNtuple.root", 
						"Dilep_Data_SingleEle_a_2017_AnalysisNtuple.root", 
						"Dilep_Data_SingleEle_h_2017_AnalysisNtuple.root" ,
						"Dilep_Data_SingleEle_g_2017_AnalysisNtuple.root", 
						"Dilep_Data_SingleMu_a_2017_AnalysisNtuple.root", 
						"Dilep_Data_SingleMu_h_2017_AnalysisNtuple.root" ,
						"Dilep_Data_SingleMu_g_2017_AnalysisNtuple.root",
						"Dilep_Data_SingleEle_e_2018_AnalysisNtuple.root",
						"Dilep_Data_SingleEle_f_2018_AnalysisNtuple.root" ,
						"Dilep_Data_SingleEle_g_2018_AnalysisNtuple.root", 
						"Dilep_Data_SingleEle_h_2018_AnalysisNtuple.root",
						"Dilep_Data_SingleMu_e_2018_AnalysisNtuple.root",
						"Dilep_Data_SingleMu_f_2018_AnalysisNtuple.root"  ,
						"Dilep_Data_SingleMu_g_2018_AnalysisNtuple.root",
						"Dilep_Data_SingleMu_h_2018_AnalysisNtuple.root", 
						"Data_SingleEle_a_2016_AnalysisNtuple.root", 
						"Data_SingleMu_a_2016_AnalysisNtuple.root",
						"Data_SingleEle_a_2017_AnalysisNtuple.root",
						"Data_SingleEle_h_2017_AnalysisNtuple.root" ,
						"Data_SingleEle_g_2017_AnalysisNtuple.root",
						"Data_SingleMu_a_2017_AnalysisNtuple.root", 
						"Data_SingleMu_h_2017_AnalysisNtuple.root" ,
						"Data_SingleMu_g_2017_AnalysisNtuple.root",
						"Data_SingleEle_e_2018_AnalysisNtuple.root",
						"Data_SingleEle_f_2018_AnalysisNtuple.root",
						"Data_SingleEle_g_2018_AnalysisNtuple.root", 
						"Data_SingleEle_h_2018_AnalysisNtuple.root",
						"Data_SingleMu_e_2018_AnalysisNtuple.root", 
						"Data_SingleMu_f_2018_AnalysisNtuple.root",
						"Data_SingleMu_g_2018_AnalysisNtuple.root", 
						"Data_SingleMu_h_2018_AnalysisNtuple.root",
						"QCD_Pt170to300_Ele_2017_AnalysisNtuple.root"]

	fileList = [x for x in fileList1 if not any(y in x for y in elementsToRemove)] 
	
	for fileName in fileList:
		#print "==> ",fileName
		tree.Add("%s%s"%(analysisNtupleLocation,fileName))

	for hist in histogramsToMake:
		h_Info = histogramInfo[hist]
		# skip some histograms which rely on MC truth and can't be done in data or QCD data driven templates
		if ('Data' in sample or isQCD) and not h_Info[5]: continue
		if not runQuiet: print "filling", h_Info[1], sample
		evtWeight = ""
		histograms.append(TH1F("%s_%s"%(h_Info[1],sample),"%s_%s_%s"%(h_Info[1],sample,timeString),h_Info[2][0],h_Info[2][1],h_Info[2][2]))
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
				evtWeight = "%s*%s"%(evtWeight,PhoEff)
			else:
				evtWeight = "%s*%s[0]"%(evtWeight,PhoEff)
		tree.Draw("%s>>%s_%s"%(h_Info[0],h_Info[1],sample),evtWeight)



## histogramtodraw, cuts(passPresel_Mu && nJet>=4 && nBJet>=1 && nPho==1) weight*evtWeight*PUweight*muEffWeight*eleEffWeight*1.0*1.0*btagWeight_1a

if not os.path.exists(outputhistName):
	os.makedirs(outputhistName)

eosdir = "root://cmseos.fnal.gov//store/user/npoudyal/"
localdir = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/TTGammaSemiLep_13TeV/Plotting_Nabin/Plotting/"
#if options.condor:
#	stdout, stderr = subprocess.Popen("BASH COMMAND", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate() # copy from eos to local dir
	#command = ["xrdcp","-f",eosdir+outputhistName+"/"+sample+".root", localdir+outputhistName+"/"]
	#Popen(command)
	

outputFile = TFile("%s/%s.root"%(outputhistName,sample),"update")

#print "%s/%s.root"%(outputhistName,sample)

for h in histograms:
	outputFile.Delete("%s;*"%h.GetName())
	if onlyAddPlots:
		gDirectory.Delete("%s;*"%(h.GetName()))
	h.Write()

if options.condor:
	command = ["xrdcp","-f",localdir+outputhistName+"/"+sample+".root", eosdir+outputhistName+"/"] #copy from local to eos
	Popen(command)
	
outputFile.Close()	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
