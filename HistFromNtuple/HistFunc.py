from SampleInfo import *
from ROOT import TChain, TH1F, gROOT, gDirectory
import sys
#-----------------------------------------
# Functions for estimation of QCD from Data
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
gROOT.SetBatch(True)
def getQCDTransFact(year, channel, nBJets_, outputFile_, qcdTFDirInFile):
    ntupleDirBase       = "%s/%s"%(dirBase,      year) 
    ntupleDirBaseCR     = "%s/%s"%(dirBaseCR,    year)
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
    tree.Draw("nJet>>Njet_HighIso_0b",extraCuts+weights, "goff")
    tree.Draw("nJet>>Njet_HighIso_0b_1Photon",extraCutsPhoton+weights, "goff")
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
    tree.Draw("nJet>>Njet_LowIso_0b",extraCuts+weights,"goff")
    tree.Draw("nJet>>Njet_LowIso_0b_1Photon",extraCutsPhoton+weights,"goff")
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
    tree.Draw("nJet>>Njet_LowIso_1b",extraCuts+weights, "goff")
    tree.Draw("nJet>>Njet_LowIso_1b_1Photon",extraCutsPhoton+weights, "goff")
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
    tree.Draw("nJet>>Njet_LowIso_2b",extraCuts+weights, "goff")
    tree.Draw("nJet>>Njet_LowIso_2b_1Photon",extraCutsPhoton+weights, "goff")
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
def getShapeFromCR(year, channel, nJetSel, nBJets_, hInfo, outputFile_, qcdShapeDirInFile):
    ntupleDirBaseCR     = "%s/%s"%(dirBaseCR,    year)
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
            tree.Draw("%s>>%s_%s"%(hInfo[0],hInfo[1],sample_),evtWeight, "goff")
            hNonQCDBkgs.append(hist_)
        if "Data" in sample_:
            tree = TChain("AnalysisTree")
            fileList = samples[sampleList[-1]][0]
            evtWeight = hInfo[3]
            if evtWeight[-1]=="*":
                evtWeight= evtWeight[:-1]
            for fileName in fileList:
    	    	tree.Add("%s/QCDcr_%s"%(ntupleDirBaseCR,fileName))
            tree.Draw("%s>>%s_%s"%(hInfo[0],hInfo[1],sample_),evtWeight, "goff")
            hData.append(hist_)
        print "Integral = %s"%hist_.Integral()
    hDiffDataBkg = hData[0].Clone(hInfo[1])
    if not outputFile_.GetDirectory(qcdShapeDirInFile):
        outputFile_.mkdir(qcdShapeDirInFile)
    outputFile_.cd(qcdShapeDirInFile)
    for hNonQCDBkg in hNonQCDBkgs:
        hDiffDataBkg.Add(hNonQCDBkg, -1)
        gDirectory.Delete("%s;*"%(hNonQCDBkg.GetName()))
        hNonQCDBkg.Write()
    gDirectory.Delete("%s;*"%(hData[0].GetName()))
    hData[0].Write()
    hDiffDataBkg.Write()
    gDirectory.Delete("%s;*"%(hDiffDataBkg.GetName()))
    return hDiffDataBkg


#----------------------------------------------------------
#Get jet multiplicity cuts in a different control regions
#----------------------------------------------------------
#Jet selection naming: a3j_e2b = atleast 3 jet, out of which 2 are b jets: nJet >= 3, nBJet ==2
def getJetMultiCut(controlRegion="tight_a4j_e0b", isQCDMC=False):
    if not len(controlRegion.split("_"))==3 and not controlRegion=="":
        print "Please provide control region in NAME_ExpNumJet_ExpNumBJet formate such as tight_a4j_e0b"
        sys.exit()
    nJets, nBJets, nJetSel, nBJetSel, allJetSel = 4, 1, "nJet>=4", "nBJet>=1", "nJet>=4 && nBJet>=1"
    if isQCDMC: 
        nJets, nBJets, nJetSel, nBJetSel, allJetSel = 4, 0, "nJet>=4", "nBJet==0", "nJet>=4 && nBJet==0"
    if not controlRegion=="":
    	splitCR = controlRegion.split("_")
    	jetCut  = splitCR[1].strip()
    	bJetCut = splitCR[2].strip()
    	#For total jets 
    	operationJet, numberJet = jetCut[0].strip(), jetCut[1].strip()
    	expresssionJet = "=="
    	if operationJet=="a": 
    	    expresssionJet=">="
    	newJetCut = "nJet%s%s"%(expresssionJet, numberJet)
    	#For b jets
    	operationBJet, numberBJet = bJetCut[0].strip(), bJetCut[1].strip()
    	expresssionBJet = "=="
    	if(operationBJet=="a"): 
    	    expresssionBJet=">="
    	newBJetCut = "nBJet%s%s"%(expresssionBJet, numberBJet)
    	#Combine the two selection
        nJets_  = int(numberJet)
    	nBJets_ = int(numberBJet)
    	if isQCDMC: 
            nJets, nBJets, nJetSel, nBJetSel, allJetSel = nJets_, 0, newJetCut, "nBJet==0", "%s && nBJet==0"%newJetCut
        else:
            nJets, nBJets, nJetSel, nBJetSel, allJetSel = nJets_, nBJets_, newJetCut, newBJetCut, "%s && %s"%(newJetCut, newBJetCut)
    print "nJets: %s, nBJets: %s, nJetSel: %s, nBJetSel: %s, allJetSel: %s"%(nJets, nBJets, nJetSel, nBJetSel, allJetSel)
    return nJets, nBJets, nJetSel, nBJetSel, allJetSel

#----------------------------------------------------------
#NICE WAY TO PRINT STRINGS
#----------------------------------------------------------
def toPrint(string, value):
    length = (len(string)+len(str(value))+2)
    line = "-"*length
    print ""
    print "* "+ line +                    " *"
    print "| "+ " "*length +              " |"
    print "| "+ string+ ": "+ str(value)+ " |"
    print "| "+ " "*length +              " |"
    print "* "+ line +                    " *"
