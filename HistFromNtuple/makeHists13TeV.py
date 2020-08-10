from ROOT import TH1F, TFile, TChain, TCanvas, gDirectory 
import sys
import os
from optparse import OptionParser
from SampleInfo_cff import *
from HistsInfo_cff import *

#-----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-d", "--decay", dest="ttbarDecayMode", default="SemiLep",type='str',
                     help="Specify which decay moded of ttbar SemiLep or DiLep? default is SemiLep")
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
runQuiet = options.quiet
toPrint("Running for Year, Channel, Sample", "%s, %s, %s"%(year, channel, sample))
print parser.parse_args()

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
outFileMainDir = "./hists"

gROOT.SetBatch(True)
nJets = 3
isQCD = False
Q2 = 1.
Pdf = 1.
Pileup ="PUweight"
MuEff = "muEffWeight"
EleEff= "eleEffWeight"
PhoEff= "phoEffWeight"
loosePhoEff= "loosePhoEffWeight"
evtWeight ="evtWeight"
btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]
histDirInFile = "Base"
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
    histDirInFile = "%s%s"%(syst,level) 
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
    elif 'BTagSF_b' in syst:
        if levelUp:
            btagWeightCategory = ["1","(1-btagWeight_b_Up[0])","(btagWeight_b_Up[2])","(btagWeight_b_Up[1])"]
        else:
            btagWeightCategory = ["1","(1-btagWeight_b_Do[0])","(btagWeight_b_Do[2])","(btagWeight_b_Do[1])"]
    elif 'BTagSF_l' in syst:
        if levelUp:
            btagWeightCategory = ["1","(1-btagWeight_l_Up[0])","(btagWeight_l_Up[2])","(btagWeight_l_Up[1])"]
        else:
            btagWeightCategory = ["1","(1-btagWeight_l_Do[0])","(btagWeight_l_Do[2])","(btagWeight_l_Do[1])"]
    else:
    	if  levelUp:
            analysisNtupleLocation = ntupleDirSyst+"/%s_up_"%(syst)
    	else:
            analysisNtupleLocation = ntupleDirSyst+"/%s_down_"%(syst)
if (syst=="isr" or syst=="fsr") and sample=="TTbar":
		samples={"TTbar"     : [["TTbarPowheg_Semilept_2016_AnalysisNtuple_1of5.root", 
			"TTbarPowheg_Semilept_2016_AnalysisNtuple_2of5.root",
			"TTbarPowheg_Semilept_2016_AnalysisNtuple_3of5.root", 
			"TTbarPowheg_Semilept_2016_AnalysisNtuple_4of5.root", 
			"TTbarPowheg_Semilept_2016_AnalysisNtuple_5of5.root"],
                          kRed+1,"t#bar{t}",isMC],
			}

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
    analysisNtupleLocation = ntupleDirBase
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
    analysisNtupleLocation = ntupleDirBase 
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
    analysisNtupleLocation = ntupleDirBaseCR 
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
    analysisNtupleLocation = ntupleDirBaseCR 
    nJets, nBJets, nJetSel, nBJetSel, bothJetSel = getJetMultiCut(controlRegion, True)
    outFileFullDir = outFileMainDir+"/%s/%s/Ele"%(year,ttbarDecayMode)
    toPrint("Full Path of Hist", outFileFullDir)
    extraCuts                 = "(passPresel_Ele && elePFRelIso>0.01 && %s)*"%(bothJetSel)
    extraPhotonCuts           = "(passPresel_Ele && elePFRelIso>0.01 && %s && %s)*"%(bothJetSel, "%s")
else:
    print "Unknown final state, options are Mu and Ele"
    sys.exit()

btagWeight = btagWeightCategory[nBJets]
if "QCD" in channel:
        btagWeight="btagWeight[0]"
weights = "%s*%s*%s*%s*%s*%s*%s"%(evtWeight,Pileup,MuEff,EleEff,Q2,Pdf,btagWeight)
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
	if not runQuiet: print "Making only dR photon plots"
    elif makegenPlots:
	plotList=genPlotList
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
        print "Histogram %s is not defined in HistListDict_cff.py"%hist
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
        tree.Add("%s%s"%(analysisNtupleLocation,fileName))
    #print "Number of events:", tree.GetEntries()
    for index, hist in enumerate(histogramsToMake, start=1):
        hInfo = histogramInfo[hist]
        # skip some histograms which rely on MC truth and can't be done in data or QCD data driven templates
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
        tree.Draw("%s>>%s"%(hInfo[0],hInfo[1]),evtWeight)


#-----------------------------------------
#Final output Linux and ROOT directories
#----------------------------------------
if not os.path.exists(outFileFullDir):
    os.makedirs(outFileFullDir)
outFileFullPath = "%s/%s_%s_SignalRegion.root"%(outFileFullDir, sample, histDirInFile)
if not controlRegion =="":
    outFileFullPath = "%s/%s_%s_ControlRegion_%s.root"%(outFileFullDir, sample, histDirInFile, controlRegion)
outputFile = TFile(outFileFullPath,"update")
if not controlRegion =="":
    histDirInFile  = "%s/ControlRegion/%s"%(histDirInFile,  controlRegion)
else:
    histDirInFile  = "%s/SignalRegion"%histDirInFile 
if not runQuiet: toPrint ("The histogram directory inside the root file is", histDirInFile) 


#-----------------------------------------
# Estimate QCD from Data
#----------------------------------------
#https://indico.cern.ch/event/846512/contributions/3555642/attachments/1919913/3175584/TTGamma_oct_03.pdf
#https://indico.cern.ch/event/846513/contributions/3555646/attachments/1923852/3183461/TTGamma_oct_10_v1.pdf
#https://indico.cern.ch/event/846514/contributions/3555650/attachments/1927886/3192167/QCDTFandWJetsSF.pdf
#https://indico.cern.ch/event/876401/contributions/3693185/attachments/1966719/3270985/QCD_jan9_final.pdf
'''
+ The shape of QCD in the signal region (low iso) is not 
smoooth because of large lumi event weight. 
+ Therefore, a smooth shape (substraction of other background 
from data) is taken from the control region (high iso).
+ This shape is scaled by a transfer scale factor (TF). 
+ The TF is determined from "simulated" MC QCD background. It
is the ratio of MC QCD event yields from low (SR) and 
high (CR) isolation regions.
+ The QCD estimation is performed with "additional" jet 
multiplicity cuts
+ In the CR, we always have nBJet==0. On top of this, we 
have nJet >=4, >=2, etc.
+In the SR, we have can have nBJet==0, >=1 and nJet >=4, >=2.
'''
qcdTFDirInFile = "%s/TF"%histDirInFile
def getQCDTransFact(channel, nBJets_, outputFile_):
    allHistsForTF = []
    if channel in ["Mu","mu"]:
    	sample = "QCDMu"
    	preselCut = "passPresel_Mu"
    	qcdRelIsoCut = "muPFRelIso>0.15 && muPFRelIso<0.3 "
    elif channel in ["Ele","ele","e"]:
    	sample = "QCDEle"
    	preselCut = "passPresel_Ele"
    	qcdRelIsoCut = "elePFRelIso>0.01"
    #-----------------------------------------
    #high rel iso, nJets ==2, nBJets_ = 
    #----------------------------------------
    tree = TChain("AnalysisTree")
    fileList = samples[sample][0]
    for fileName in fileList:
    	tree.Add("%s/QCDcr_%s"%(ntupleDirBaseCR,fileName))
    extraCuts       = "(%s && %s && nJet>=2 && nBJet==0)*"%(preselCut, qcdRelIsoCut)
    extraCutsPhoton = "(%s && %s && nJet>=2 && nBJet==0 && phoMediumID)*"%(preselCut, qcdRelIsoCut)
    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets_
    histCR    = TH1F("Njet_HighIso_0b","Njet_HighIso_0b",15,0,15)
    histCRPho = TH1F("Njet_HighIso_0b_1Photon","Njet_HighIso_0b_1Photon",15,0,15)
    print "Filling histograms for TF: ", histCR.GetName() 
    tree.Draw("nJet>>Njet_HighIso_0b",extraCuts+weights)
    tree.Draw("nJet>>Njet_HighIso_0b_1Photon",extraCutsPhoton+weights)
    allHistsForTF.append(histCR)
    
    #-----------------------------------------
    #low rel iso, nJets ==2, nBJets_ = 0
    #----------------------------------------
    if channel in ["Mu","mu"]:
    	qcdRelIsoCut = "muPFRelIso<0.15"
    else:
        qcdRelIsoCut = "elePFRelIso<0.01"
    tree = TChain("AnalysisTree")
    fileList = samples[sample][0]
    for fileName in fileList:
    	tree.Add("%s/%s"%(ntupleDirBase,fileName))
    fileList = samples["GJets"][0]
    for fileName in fileList:
    	tree.Add("%s/%s"%(ntupleDirBase,fileName))
    extraCuts       = "(%s && %s && nJet>=2 && nBJet==0)*"%(preselCut, qcdRelIsoCut)
    extraCutsPhoton = "(%s && %s && nJet>=2 && nBJet==0 && phoMediumID)*"%(preselCut, qcdRelIsoCut)
    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets_
    hist0 = TH1F("Njet_LowIso_0b","Njet_LowIso_0b",15,0,15)
    hist0Pho = TH1F("Njet_LowIso_0b_1Photon","Njet_LowIso_0b_1Photon",15,0,15)
    print "Filling histograms for TF: ", hist0.GetName() 
    tree.Draw("nJet>>Njet_LowIso_0b",extraCuts+weights)
    tree.Draw("nJet>>Njet_LowIso_0b_1Photon",extraCutsPhoton+weights)
    allHistsForTF.append(hist0)
    
    #-----------------------------------------
    #low rel iso, nJets ==2, nBJets_ = 1
    #----------------------------------------
    extraCuts       = "(%s && %s && nJet>=2 && nBJet==1)*"%(preselCut, qcdRelIsoCut)
    extraCutsPhoton = "(%s && %s && nJet>=2 && nBJet==1 && phoMediumID)*"%(preselCut, qcdRelIsoCut)
    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets_
    hist1 = TH1F("Njet_LowIso_1b","Njet_LowIso_1b",15,0,15)
    hist1Pho = TH1F("Njet_LowIso_1b_1Photon","Njet_LowIso_1b_1Photon",15,0,15)
    print "Filling histograms for TF: ", hist1.GetName() 
    tree.Draw("nJet>>Njet_LowIso_1b",extraCuts+weights)
    tree.Draw("nJet>>Njet_LowIso_1b_1Photon",extraCutsPhoton+weights)
    allHistsForTF.append(hist1)
    
    #-----------------------------------------
    #low rel iso, nJets ==2, nBJets_ = 2
    #----------------------------------------
    extraCuts       = "(%s && %s && nJet>=2 && nBJet>=2)*"%(preselCut, qcdRelIsoCut)
    extraCutsPhoton = "(%s && %s && nJet>=2 && nBJet>=2 && phoMediumID)*"%(preselCut, qcdRelIsoCut)
    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets_
    hist2 = TH1F("Njet_LowIso_2b","Njet_LowIso_2b",15,0,15)
    hist2Pho = TH1F("Njet_LowIso_2b_1Photon","Njet_LowIso_2b_1Photon",15,0,15)
    print "Filling histograms for TF: ", hist2.GetName() 
    tree.Draw("nJet>>Njet_LowIso_2b",extraCuts+weights)
    tree.Draw("nJet>>Njet_LowIso_2b_1Photon",extraCutsPhoton+weights)
    allHistsForTF.append(hist2)
    allHistsForTF.append(histCRPho)
    allHistsForTF.append(hist0Pho)
    allHistsForTF.append(hist1Pho)
    allHistsForTF.append(hist2Pho)
    
    #-----------------------------------------
    # Determine the TF (nb/CR) in each bin
    #----------------------------------------
    hist0_TF = hist0.Clone("TF_BinByBin_0b")
    hist0_TF.SetNameTitle("TF_BinByBin_0b","TF_BinByBin_0b")
    hist0_TF.Divide(histCR)
    hist1_TF = hist1.Clone("TF_BinByBin_1b")
    hist1_TF.SetNameTitle("TF_BinByBin_1b","TF_BinByBin_1b")
    hist1_TF.Divide(histCR)
    hist2_TF = hist2.Clone("TF_BinByBin_2b")
    hist2_TF.SetNameTitle("TF_BinByBin_2b","TF_BinByBin_2b")
    hist2_TF.Divide(histCR)
    allHistsForTF.append(hist0_TF)
    allHistsForTF.append(hist1_TF)
    allHistsForTF.append(hist2_TF)
    
    hist0Pho_TF = hist0Pho.Clone("TF_BinByBin_0b_1Photon")
    hist0Pho_TF.SetNameTitle("TF_BinByBin_0b_1Photon","TF_BinByBin_0b_1Photon")
    hist0Pho_TF.Divide(histCR)
    hist1Pho_TF = hist1Pho.Clone("TF_BinByBin_1b_1Photon")
    hist1Pho_TF.SetNameTitle("TF_BinByBin_1b_1Photon","TF_BinByBin_1b_1Photon")
    hist1Pho_TF.Divide(histCR)
    hist2Pho_TF = hist2Pho.Clone("TF_BinByBin_2b_1Photon")
    hist2Pho_TF.SetNameTitle("TF_BinByBin_2b_1Photon","TF_BinByBin_2b_1Photon")
    hist2Pho_TF.Divide(histCR)
    allHistsForTF.append(hist0Pho_TF)
    allHistsForTF.append(hist1Pho_TF)
    allHistsForTF.append(hist2Pho_TF)
    
    #-----------------------------------------
    # Determine the TF (nb/CR) in total yield
    #----------------------------------------
    hist_TF = TH1F("TF_TotalYield_012b","TF_TotalYield_012b",3,0,3)
    hist_TFCR = TH1F("TF_TotalYield_012bCR","TF_TotalYield_012bCR",3,0,3)
    histCR.Rebin(15)
    hist0.Rebin(15)
    hist1.Rebin(15)
    hist2.Rebin(15)
    hist_TF.SetBinContent(1,hist0.GetBinContent(1))
    hist_TF.SetBinError(1,hist0.GetBinError(1))
    hist_TF.SetBinContent(2,hist1.GetBinContent(1))
    hist_TF.SetBinError(2,hist1.GetBinError(1))
    hist_TF.SetBinContent(3,hist2.GetBinContent(1))
    hist_TF.SetBinError(3,hist2.GetBinError(1))
    hist_TFCR.SetBinContent(1,histCR.GetBinContent(1))
    hist_TFCR.SetBinError(1,histCR.GetBinError(1))
    hist_TFCR.SetBinContent(2,histCR.GetBinContent(1))
    hist_TFCR.SetBinError(2,histCR.GetBinError(1))
    hist_TFCR.SetBinContent(3,histCR.GetBinContent(1))
    hist_TFCR.SetBinError(3,histCR.GetBinError(1))
    hist_TF.Divide(hist_TFCR)
    allHistsForTF.append(hist_TF)
    
    hist_TFPho = TH1F("TF_TotalYield_012b_1Photon","TF_TotalYield_012b_1Photon",3,0,3)
    hist_TFCRPho = TH1F("TF_TotalYield_012bCRPho","TF_TotalYield_012bCRPho",3,0,3)
    histCRPho.Rebin(15)
    hist0Pho.Rebin(15)
    hist1Pho.Rebin(15)
    hist2Pho.Rebin(15)
    hist_TFPho.SetBinContent(1,hist0Pho.GetBinContent(1))
    hist_TFPho.SetBinError(1,hist0Pho.GetBinError(1))
    hist_TFPho.SetBinContent(2,hist1Pho.GetBinContent(1))
    hist_TFPho.SetBinError(2,hist1Pho.GetBinError(1))
    hist_TFPho.SetBinContent(3,hist2Pho.GetBinContent(1))
    hist_TFPho.SetBinError(3,hist2Pho.GetBinError(1))
    hist_TFCRPho.SetBinContent(1,histCRPho.GetBinContent(1))
    hist_TFCRPho.SetBinError(1,histCRPho.GetBinError(1))
    hist_TFCRPho.SetBinContent(2,histCRPho.GetBinContent(1))
    hist_TFCRPho.SetBinError(2,histCRPho.GetBinError(1))
    hist_TFCRPho.SetBinContent(3,histCRPho.GetBinContent(1))
    hist_TFCRPho.SetBinError(3,histCRPho.GetBinError(1))
    hist_TFPho.Divide(hist_TFCRPho)
    allHistsForTF.append(hist_TFPho)
    if nBJets_==0:
        transFact =  hist_TF.GetBinContent(1)
    if nBJets_==1:
        transFact =  hist_TF.GetBinContent(2)
    if nBJets_==2:
        transFact =  hist_TF.GetBinContent(3)
    #Write allHistsForTF in the ouput root file
    if not outputFile_.GetDirectory(qcdTFDirInFile):
        outputFile_.mkdir(qcdTFDirInFile)
    for histTF in allHistsForTF:
    	outputFile_.cd(qcdTFDirInFile)
        gDirectory.Delete("%s;*"%(histTF.GetName()))
        histTF.Write()
    return transFact

#-----------------------------------------
# Determine data - nonQCDBkg from CR
#----------------------------------------
qcdCRDirInFile = "%s/CR"%histDirInFile
def getShapeFromCR(channel, nJetSel, nBJets_, hInfo, outputFile_):
    btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])","(btagWeight[0])"]
    if channel=="Mu":
    	sampleList[-1] = "DataMu"
    	sampleList[-2] = "QCDMu"
    	extraCuts            = "(passPresel_Mu && muPFRelIso>0.15 && %s)*"%nJetSel
    	extraPhotonCuts      = "(passPresel_Mu && muPFRelIso>0.15 && %s && %s)*"%(nJetSel, "%s")
    if channel=="Ele":
    	sampleList[-1] = "DataEle"
    	sampleList[-2] = "QCDEle"
    	extraCuts            = "(passPresel_Ele && elePFRelIso>0.01 && %s)*"%nJetSel
    	extraPhotonCuts      = "(passPresel_Ele && elePFRelIso>0.01 && %s && %s)*"%(nJetSel, "%s")
    weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*%s"%btagWeightCategory[nBJets_]
    #if not hInfo[5]: continue
    print "filling", hInfo[1], sample
    evtWeight = ""
    if hInfo[4]=="":
        evtWeight = "%s%s"%(hInfo[3],weights)
    else:
        evtWeight = hInfo[4]
    hNonQCDBkgs = []
    hData = []
    for sample_ in sampleList:
        hist_ = TH1F("%s_%s"%(hInfo[1], sample_),"%s_%s"%(hInfo[1],sample_),hInfo[2][0],hInfo[2][1],hInfo[2][2])
        print "Filling histograms for QCD Shape: ", hist_.GetName() 
	if sample_ not in ["QCDMu", "QCDEle","DataMu","DataEle", "TTGJets"]:
            tree = TChain("AnalysisTree")
            fileList = samples[sample_][0]
            for fileName in fileList:
    	        tree.Add("%s/QCDcr_%s"%(ntupleDirBaseCR,fileName))
            tree.Draw("%s>>%s_%s"%(hInfo[0],hInfo[1],sample_),evtWeight)
            hNonQCDBkgs.append(hist_)
        if "Data" in sample_:
            tree = TChain("AnalysisTree")
            fileList = samples[sampleList[-1]][0]
            evtWeight = hInfo[3]
            if evtWeight[-1]=="*":
                evtWeight= evtWeight[:-1]
            for fileName in fileList:
    	    	tree.Add("%s/QCDcr_%s"%(ntupleDirBaseCR,fileName))
            tree.Draw("%s>>%s_%s"%(hInfo[0],hInfo[1],sample_),evtWeight)
            hData.append(hist_)
        print "Integral = %s"%hist_.Integral()
    hDiffDataBkg = hData[0].Clone(hInfo[1])
    if not outputFile_.GetDirectory(qcdCRDirInFile):
        outputFile_.mkdir(qcdCRDirInFile)
    outputFile_.cd(qcdCRDirInFile)
    for hNonQCDBkg in hNonQCDBkgs:
        hDiffDataBkg.Add(hNonQCDBkg, -1)
        gDirectory.Delete("%s;*"%(hNonQCDBkg.GetName()))
        hNonQCDBkg.Write()
    gDirectory.Delete("%s;*"%(hData[0].GetName()))
    hData[0].Write()
    hDiffDataBkg.Write()
    gDirectory.Delete("%s;*"%(hDiffDataBkg.GetName()))
    return hDiffDataBkg

#-----------------------------------------
# QCD in SR = TF * (data - nonQCDBkg from CR)
#----------------------------------------
transferFactor = 1.0
canvas = TCanvas()
if sample =="QCD_DD":
        toPrint("Determining QCD Transfer factor from CR", "")
	#transferFactor = getQCDTransFact(channel, nBJets, outputFile)
	print "Transfer factor = ", transferFactor
        for hist in histogramsToMake:
            if not histogramInfo[hist][5]: continue
            toPrint("Determining QCD shape from CR", "")
	    dataMinusOtherBkg = getShapeFromCR(channel, nJetSel, nBJets, histogramInfo[hist], outputFile)
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
