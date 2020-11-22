from ROOT import TH1F, TFile, TChain, TCanvas, gDirectory, gROOT 
import sys
import os
from optparse import OptionParser
from SampleInfo import *
from HistInfo import *
from HistFunc import *

#-----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-d", "--decay", dest="ttbarDecayMode", default="Semilep",type='str',
                     help="Specify which decay moded of ttbar Semilep or Dilep? default is Semilep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s", "--sample", dest="sample", default="TTGamma",type='str',
                     help="Specify which sample to run on" )
parser.add_option("--level", "--level", dest="level", default="",type='str',
                     help="Specify up/down of systematic")
parser.add_option("--syst", "--systematic", dest="systematic", default="Base",type='str',
                     help="Specify which systematic to run on")
parser.add_option("--cr", "--controlRegion", dest="controlRegion", default="",type='str', 
                     help="which control selection and region such as Tight, VeryTight, Tight0b, looseCR2e1, looseCRe2g1")
parser.add_option("--addPlots","--addOnly", dest="onlyAddPlots", default=False,action="store_true",
                     help="Use only if you want to add a couple of plots to the file, does not remove other plots" )
parser.add_option("--plot", dest="plotList",action="append",
                     help="Add plots" )
parser.add_option("--multiPlots", "--multiplots", dest="multiPlotList",action="append",
                     help="Add plots" )
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
parser.add_option("--fitHist","--fitHist", dest="makeFitHist",action="store_true",default=False,
                     help="List of histograms to be used for fitting" )
parser.add_option("--jetsonly","--jetsonly", dest="makeJetsplots",action="store_true",default=False,
                     help="Extra jets" )
parser.add_option("--quiet", "-q", dest="quiet",default=False,action="store_true",
                     help="Quiet outputs" )
parser.add_option("--fwdjets","--fwdjets", dest="FwdJets",action="store_true",default=False,
                     help="include fwd jets" )

(options, args) = parser.parse_args()
level =options.level
year = options.year
channel = options.channel
ttbarDecayMode = options.ttbarDecayMode
sample = options.sample
controlRegion = options.controlRegion
onlyAddPlots = options.onlyAddPlots
FwdJets=options.FwdJets
makedRPlots=options.makedRPlots
makeAllPlots = options.makeAllPlots
makeMorePlots = options.makeMorePlots
makeEGammaPlots = options.makeEGammaPlots
makeJetsplots = options.makeJetsplots
makegenPlots=options.makegenPlots
makeFitHist = options.makeFitHist
runQuiet = options.quiet
toPrint("Running for Year, Channel, Sample", "%s, %s, %s"%(year, channel, sample))
print parser.parse_args()


#-----------------------------------------
#INPUT AnalysisNtuples Directory
#----------------------------------------
ntupleDirBase       = "%s/%s"%(dirBase,      year) 
ntupleDirBaseCR     = "%s/%s"%(dirBaseCR,    year)
ntupleDirSyst       = "%s/%s"%(dirSyst,      year)
ntupleDirSystCR     = "%s/%s"%(dirSystCR,    year)
if "Di" in ttbarDecayMode:
    ntupleDirBase  = "%s/%s"%(dirBaseDilep, year)
    ntupleDirSyst       = "%s/%s"%(dirSystDilep,year)
analysisNtupleLocation = ntupleDirBase

#-----------------------------------------
#OUTPUT Histogram Directory
#----------------------------------------
outFileMainDir = "./hists"
gROOT.SetBatch(True)
nJets = 3
isQCD = False
evtWeight ="evtWeight"
Pileup ="PUweight"
MuEff = "muEffWeight"
EleEff= "eleEffWeight"
Q2 = "q2weight_nominal"  
Pdf = 1.0
#Pdf = "pdfWeight"
prefire ="prefireSF"
isr = 1.
fsr = 1.
btagWeight="btagWeight_1a"
PhoEff= "phoEffWeight"
loosePhoEff= "loosePhoEffWeight"
histDirInFile = "%s/Base"%sample
variation = "Base"
if "Data" in sample:
    histDirInFile = "data_obs/Base"
if "QCD%s"%channel in sample:
    histDirInFile = "QCD/Base"

nJets, nBJets, nJetSel, nBJetSel, bothJetSel = getJetMultiCut(controlRegion, False)

#-----------------------------------------
#For Systematics
#----------------------------------------
syst = options.systematic
levelUp = False
if level in ["up", "UP", "uP", "Up"]: 
	levelUp = True
	level= "Up"
else:
	level = "Down"
if not syst=="Base":
    histDirInFile = "%s/%s%s"%(sample,syst,level) 
    if "QCD%s"%channel in sample:
        histDirInFile = "QCD/%s%s"%(syst, level)
    variation = "%s%s"%(syst,level) 
    toPrint("Running for systematics", syst+level)
    if syst=="PU":
        if levelUp:
            Pileup = "PUweight_Up"
        else:
            Pileup = "PUweight_Do"
    elif 'Q2' in syst:
        if levelUp:
            Q2="q2weight_Up"
        else:
            Q2="q2weight_Do"
    elif 'Pdf' in syst:
    	if syst=="Pdf":
    	    if levelUp:
    	    	Pdf="pdfweight_Up"
    	    else:
    	    	Pdf="pdfweight_Do"
    	else:
    	    if type(eval(syst[3:]))==type(int()):
    	    	pdfNumber = eval(syst[3:])
    	    	Pdf="pdfSystWeight[%i]/pdfWeight"%(pdfNumber-1)
    elif 'MuEff' in syst:
        if levelUp:
            MuEff = "muEffWeight_Up"
        else:
            MuEff = "muEffWeight_Do"
    elif 'EleEff' in syst:
        if levelUp:
            EleEff = "eleEffWeight_Up"
        else:
            EleEff = "eleEffWeight_Do"
    elif 'PhoEff' in syst:
        if levelUp:
            PhoEff = "phoEffWeight_Up"
            loosePhoEff = "loosePhoEffWeight_Up"
        else:
            PhoEff = "phoEffWeight_Do"
            loosePhoEff = "loosePhoEffWeight_Do"
    elif 'fsr' in syst:
    	if levelUp:
    	    fsr = "FSRweight_Up"
    	else:
    	    fsr = "FSRweight_Do"
    elif 'isr' in syst:
    	if levelUp:
    	    isr = "ISRweight_Up"
    	else:
    	    isr = "ISRweight_Do"
    elif 'prefireEcal' in syst:
	if levelUp:
	    prefire = "prefireSF_Up"
	else:
	    prefire = "prefireSF_Do"
    elif 'BTagSF_b' in syst:
        if levelUp:
			btagWeight = "btagWeight_1a_b_Up"
        else:
			btagWeight = "btagWeight_1a_b_Do"
    elif 'BTagSF_l' in syst:
        if levelUp:
			btagWeight = "btagWeight_1a_l_Up"
        else:
			btagWeight = "btagWeight_1a_l_Do"
    else:
    	if  levelUp:
            analysisNtupleLocation = ntupleDirSyst+"/%s_up_"%(syst)
            if "Dilep" in ttbarDecayMode:
                analysisNtupleLocation = ntupleDirBase
    	else:
            analysisNtupleLocation = ntupleDirSyst+"/%s_down_"%(syst)
            if "Dilep" in ttbarDecayMode:
                analysisNtupleLocation = ntupleDirBase

#-----------------------------------------
#Select channels
#----------------------------------------
if channel=="Mu":
    if sample=="Data":
        sample = "DataMu"
    if sample=="QCD":
        sample = "QCDMu"
    sampleList[-1] = "DataMu"
    sampleList[-2] = "QCDMu"
    outFileFullDir = outFileMainDir+"/%s/%s/Mu"%(year,ttbarDecayMode)
    extraCuts            = "(passPresel_Mu && %s)*"%(bothJetSel)
    extraPhotonCuts      = "(passPresel_Mu && %s && %s)*"%(bothJetSel, "%s")

elif channel=="Ele":
    if sample=="Data":
        sample = "DataEle"
    if sample=="QCD":
        sample = "QCDEle"
    sampleList[-1] = "DataEle"
    sampleList[-2] = "QCDEle"
    outFileFullDir = outFileMainDir+"/%s/%s/Ele"%(year,ttbarDecayMode)
    extraCuts            = "(passPresel_Ele && %s)*"%(bothJetSel)
    extraPhotonCuts      = "(passPresel_Ele && %s && %s)*"%(bothJetSel, "%s")

elif channel=="QCDMu":
    if sample=="Data":
        sample = "DataMu"
    if sample=="QCD":
        sample = "QCDMu"
    sampleList[-1] = "DataMu"
    sampleList[-2] = "QCDMu"
    outFileFullDir = outFileMainDir+"/%s/%s/Mu"%(year,ttbarDecayMode)
    nJets, nBJets, nJetSel, nBJetSel, bothJetSel = getJetMultiCut(controlRegion, True)
    extraCuts            = "(passPresel_Mu && muPFRelIso<0.3 && %s)*"%(bothJetSel)
    extraPhotonCuts      = "(passPresel_Mu && muPFRelIso<0.3 && %s && %s)*"%(bothJetSel, "%s")

elif channel=="QCDEle":
    if sample=="Data":
        sample = "DataEle"
    if sample=="QCD":
        sample = "QCDEle"
    sampleList[-1] = "DataEle"
    sampleList[-2] = "QCDEle"
    nJets, nBJets, nJetSel, nBJetSel, bothJetSel = getJetMultiCut(controlRegion, True)
    outFileFullDir = outFileMainDir+"/%s/%s/Ele"%(year,ttbarDecayMode)
    toPrint("Full Path of Hist", outFileFullDir)
    extraCuts                 = "(passPresel_Ele && elePFRelIso>0.01 && %s)*"%(bothJetSel)
    extraPhotonCuts           = "(passPresel_Ele && elePFRelIso>0.01 && %s && %s)*"%(bothJetSel, "%s")
else:
    print "Unknown final state, options are Mu and Ele"
    sys.exit()

if "JE" in syst:
    weights = "%s*%s*%s*%s*%s*%s*%s*%s*%s"%(evtWeight,prefire,Pileup,MuEff,EleEff,Pdf,isr,fsr,btagWeight)
else:
    weights = "%s*%s*%s*%s*%s*%s*%s*%s*%s*%s"%(evtWeight,prefire,Pileup,MuEff,EleEff,Q2,Pdf,isr,fsr,btagWeight)
toPrint("Extra cuts ", extraCuts)
toPrint("Extra photon cuts ", extraPhotonCuts)
toPrint("Final event weight ", weights)

#-----------------------------------------
#Get list of empty histograms
#----------------------------------------
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
        if not runQuiet: print "Making subset of kinematic plots"
        plotList = allPlotList
    elif makeEGammaPlots:
        plotList = eGammaPlotList 
        if not runQuiet: print "Making only plots for e-gamma fits"
    elif makedRPlots:
	plotList= dRPlotList
    elif makeFitHist:
	plotList= fitHistList
	if not runQuiet: print "Making only dR photon plots"
    elif makegenPlots:
	plotList=genPlotList
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
        plotList = morePlotList 
	if not runQuiet: print "Making only plots for simultaneous fits"

plotList.sort()
if not runQuiet: toPrint( "Making the following histogram(s)", "")
if not runQuiet: 
    for p in plotList: print "%s,"%p,
histogramsToMake = plotList
allHistsDefined = True
for hist in histogramsToMake:
    if not hist in histogramInfo:
        print "Histogram %s is not defined in HistInfo.py"%hist
        allHistsDefined = False
if not allHistsDefined:
    sys.exit()

#-----------------------------------------
# Fill histograms
#----------------------------------------
histograms=[]
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
        if "Dilep" in ttbarDecayMode:
            fileName = "Dilep_%s"%fileName
        if "JE" in syst and not "Di" in ttbarDecayMode:
            print "%s%s"%(analysisNtupleLocation,fileName)
            tree.Add("%s%s"%(analysisNtupleLocation,fileName))
        else:
            print "%s/%s"%(analysisNtupleLocation,fileName)
            tree.Add("%s/%s"%(analysisNtupleLocation,fileName))
    print "Number of events:", tree.GetEntries()
    for index, hist in enumerate(histogramsToMake, start=1):
        hInfo = histogramInfo[hist]
        if ('Data' in sample or isQCD) and not hInfo[5]: continue
        if not runQuiet: toPrint("%s/%s: Filling the histogram"%(index, len(histogramsToMake)), hInfo[1])
        evtWeight = ""
        histograms.append(TH1F("%s"%(hInfo[1]),"%s"%(hInfo[1]),hInfo[2][0],hInfo[2][1],hInfo[2][2]))
        if hInfo[4]=="":
            evtWeight = "%s%s"%(hInfo[3],weights)
        else:
            evtWeight = hInfo[4]
        if "Data" in sample:
            evtWeight = "%s%s"%(hInfo[3],weights)
        if evtWeight[-1]=="*":
            evtWeight= evtWeight[:-1]
        ### Correctly add the photon weights to the plots
        if 'phosel' in hInfo[1]:
            if hInfo[0][:8]=="loosePho":
                evtWeight = "%s*%s"%(evtWeight,loosePhoEff)
            elif hInfo[0][:3]=="pho":
                evtWeight = "%s*%s"%(evtWeight,PhoEff)
            else:
                evtWeight = "%s*%s[0]"%(evtWeight,PhoEff)
        print evtWeight
        print hInfo[0]
        print hInfo[1]
        tree.Draw("%s>>%s"%(hInfo[0],hInfo[1]),evtWeight, "goff")

#-----------------------------------------
#Final output Linux and ROOT directories
#----------------------------------------
if not os.path.exists(outFileFullDir):
    os.makedirs(outFileFullDir)
outFileFullPath = "%s/%s_%s_SR.root"%(outFileFullDir, sample, variation)
if not controlRegion =="":
    outFileFullPath = "%s/%s_%s_CR_%s.root"%(outFileFullDir, sample, variation, controlRegion)
outputFile = TFile(outFileFullPath,"update")
if not controlRegion =="":
    histDirInFile  = "%s/CR/%s"%(histDirInFile,  controlRegion)
else:
    histDirInFile  = "%s/SR"%histDirInFile 
if not runQuiet: toPrint ("The histogram directory inside the root file is", histDirInFile) 


#-----------------------------------------
# QCD in SR = TF * (data - nonQCDBkg from CR)
#----------------------------------------
qcdTFDirInFile = "%s/TF"%histDirInFile
qcdShapeDirInFile = "%s/Shape"%histDirInFile
transferFactor = 1.0
if sample =="QCD_DD" and "Semi" in ttbarDecayMode:
        toPrint("Determining QCD Transfer factor from CR", "")
	#transferFactor = getQCDTransFact(year, channel, nBJets, outputFile, qcdTFDirInFile)
	print "Transfer factor = ", transferFactor
        for hist in histogramsToMake:
            if not histogramInfo[hist][5]: continue
            toPrint("Determining QCD shape from CR", "")
	    dataMinusOtherBkg = getShapeFromCR(year, channel, nJetSel, nBJets, histogramInfo[hist], outputFile, qcdShapeDirInFile)
            histograms.append(dataMinusOtherBkg)
	    print histogramInfo[hist][1]
            histograms[-1].Scale(transferFactor)

#-----------------------------------
# Write final histograms in the file
#-----------------------------------
if not outputFile.GetDirectory(histDirInFile):
    outputFile.mkdir(histDirInFile)
outputFile.cd(histDirInFile)
for h in histograms:
    toPrint("Integral of Histogram %s = "%h.GetName(), h.Integral())
    outputFile.cd(histDirInFile)
    gDirectory.Delete("%s;*"%(h.GetName()))
    h.Write()
toPrint("Path of output root file", outFileFullPath)
outputFile.Close()
