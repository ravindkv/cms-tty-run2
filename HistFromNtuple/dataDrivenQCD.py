
from sampleInformation import *
#from inputOutputDir_cff import *

ntupleDirBase = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/"
ntupleDirBaseCR = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/2016/"

#-----------------------------------
'''
The QCD transfer scale factors (TF)
are determined from MC QCD background.
The TF is ratio of event yields from
high isolation and a different number
of b jet control regions.
'''
#-----------------------------------
def getQCDTransFact(channel, outputFile):
	if channel in ["Mu","mu"]:
		sample = "QCDMu"
		preselCut = "passPresel_Mu"
		qcdRelIsoCut = "muPFRelIso>0.15 && muPFRelIso<0.3 && "
	elif channel in ["Ele","ele","e"]:
		sample = "QCDEle"
		preselCut = "passPresel_Ele"
		qcdRelIsoCut = "elePFRelIso>0.01 &&"
	
	#-----------------------------------------
	#QCD histogram from: 
	#high rel iso, nJets ==2, nBJets = 0
	#----------------------------------------
	tree = TChain("AnalysisTree")
	fileList = samples[sample][0]
	for fileName in fileList:
		tree.Add("%s/QCDcr_%s"%(ntupleDirBaseCR,fileName))
	nJets  = 2
	nBJets = 0
	extraCuts       = "(%s && %s nJet>=%i && nBJet==%i)*"%(preselCut, qcdRelIsoCut, nJets, nBJets)
	extraCutsPhoton = "(%s && %s nJet>=%i && nBJet==%i && phoMediumID)*"%(preselCut, qcdRelIsoCut, nJets, nBJets)
	weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets
	histCR    = TH1F("Njet_HighIso_0b","Njet_HighIso_0b",15,0,15)
	histCRPho = TH1F("Njet_HighIso_0b_1Photon","Njet_HighIso_0b_1Photon",15,0,15)
	tree.Draw("nJet>>Njet_HighIso_0b",extraCuts+weights)
	tree.Draw("nJet>>Njet_HighIso_0b_1Photon",extraCutsPhoton+weights)
	outputFile.cd()
	histCR.Write()

	#-----------------------------------------
	#QCD histogram from: 
	#low rel iso, nJets ==2, nBJets = 0
	#----------------------------------------
	tree = TChain("AnalysisTree")
	fileList = samples[sample][0]
	for fileName in fileList:
		tree.Add("%s/%s"%(ntupleDirBase,fileName))
	fileList = samples["GJets"][0]
	for fileName in fileList:
		tree.Add("%s/%s"%(ntupleDirBase,fileName))
	nJets  = 2
	nBJets = 0
	extraCuts       = "(%s && nJet>=%i && nBJet==%i)*"%(preselCut, nJets, nBJets)
	extraCutsPhoton = "(%s && nJet>=%i && nBJet==%i && phoMediumID)*"%(preselCut, nJets, nBJets)
	weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets
	hist0 = TH1F("Njet_LowIso_0b","Njet_LowIso_0b",15,0,15)
	hist0Pho = TH1F("Njet_LowIso_0b_1Photon","Njet_LowIso_0b_1Photon",15,0,15)
	tree.Draw("nJet>>Njet_LowIso_0b",extraCuts+weights)
	tree.Draw("nJet>>Njet_LowIso_0b_1Photon",extraCutsPhoton+weights)
	outputFile.cd()
	hist0.Write()

	#-----------------------------------------
	#QCD histogram from: 
	#low rel iso, nJets ==2, nBJets = 1
	#----------------------------------------
	nJets  = 2
	nBJets = 1
	extraCuts       = "(%s && nJet>=%i && nBJet==%i)*"%(preselCut, nJets, nBJets)
	extraCutsPhoton = "(%s && nJet>=%i && nBJet==%i && phoMediumID)*"%(preselCut, nJets, nBJets)
	weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets
	hist1 = TH1F("Njet_LowIso_1b","Njet_LowIso_1b",15,0,15)
	hist1Pho = TH1F("Njet_LowIso_1b_1Photon","Njet_LowIso_1b_1Photon",15,0,15)
	tree.Draw("nJet>>Njet_LowIso_1b",extraCuts+weights)
	tree.Draw("nJet>>Njet_LowIso_1b_1Photon",extraCutsPhoton+weights)
	outputFile.cd()
	hist1.Write()

	#-----------------------------------------
	#QCD histogram from: 
	#low rel iso, nJets ==2, nBJets = 2
	#----------------------------------------
	nJets  = 2
	nBJets = 2
	extraCuts       = "(%s && nJet>=%i && nBJet>=%i)*"%(preselCut, nJets, nBJets)
	extraCutsPhoton = "(%s && nJet>=%i && nBJet>=%i && phoMediumID)*"%(preselCut, nJets, nBJets)
	weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets
	hist2 = TH1F("Njet_LowIso_2b","Njet_LowIso_2b",15,0,15)
	hist2Pho = TH1F("Njet_LowIso_2b_1Photon","Njet_LowIso_2b_1Photon",15,0,15)
	tree.Draw("nJet>>Njet_LowIso_2b",extraCuts+weights)
	tree.Draw("nJet>>Njet_LowIso_2b_1Photon",extraCutsPhoton+weights)
	outputFile.cd()
	hist2.Write()
	histCRPho.Write()
	hist0Pho.Write()
	hist1Pho.Write()
	hist2Pho.Write()

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
	hist0_TF.Write()
	hist1_TF.Write()
	hist2_TF.Write()

	hist0Pho_TF = hist0Pho.Clone("TF_BinByBin_0b_1Photon")
	hist0Pho_TF.SetNameTitle("TF_BinByBin_0b_1Photon","TF_BinByBin_0b_1Photon")
	hist0Pho_TF.Divide(histCR)
	hist1Pho_TF = hist1Pho.Clone("TF_BinByBin_1b_1Photon")
	hist1Pho_TF.SetNameTitle("TF_BinByBin_1b_1Photon","TF_BinByBin_1b_1Photon")
	hist1Pho_TF.Divide(histCR)
	hist2Pho_TF = hist2Pho.Clone("TF_BinByBin_2b_1Photon")
	hist2Pho_TF.SetNameTitle("TF_BinByBin_2b_1Photon","TF_BinByBin_2b_1Photon")
	hist2Pho_TF.Divide(histCR)
	hist0Pho_TF.Write()
	hist1Pho_TF.Write()
	hist2Pho_TF.Write()

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
	hist_TF.Write()

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
	hist_TFPho.Write()
	'''
	if nBJets==0:
		hist2.Add(hist1)
        hist2.Add(hist0)
    	transFact =  hist_TF.GetBinContent(1)
    if nBJets==1:
        hist2.Add(hist1)
        transFact = hist2.Integral(nJets+1,-1)/histCR.Integral(-1,-1)
    if nBJets==1:
    transFact = hist2.Integral(nJets+1,-1)/histCR.Integral(-1,-1)
    if isLooseCR2e1Selection:
	'''
	transFact = hist_TF.GetBinContent(2) 
	return transFact

'''
def getShapeFromCR(h_Info):
	nBJets = -1
	btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])","(btagWeight[0])"]
	if finalState=="Mu":
		sampleList[-1] = "DataMu"
		sampleList[-2] = "QCDMu"
		extraCuts            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=3)*"
		extraPhotonCuts      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=3 && %s)*"
		if isTightSelection:
			extraCuts            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4)*"
			extraPhotonCuts      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=4 && %s)*"
		if isLooseSelection or isLooseCRSelection:
			extraCuts            = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2)*"
			extraPhotonCuts      = "(passPresel_Mu && muPFRelIso<0.3 && nJet>=2 && %s)*"

	if finalState=="Ele":
		sampleList[-1] = "DataEle"
		sampleList[-2] = "QCDEle"
		extraCuts            = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=3)*"
		extraPhotonCuts      = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=3 && %s)*"
		if isTightSelection:
			extraCuts            = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=4)*"
			extraPhotonCuts      = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=4 && %s)*"
		if isLooseSelection or isLooseCRSelection:
			extraCuts            = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=2)*"
			extraPhotonCuts      = "(passPresel_Ele && muPFRelIso<0.3 && nJet>=2 && %s)*"

	weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*%s"%btagWeightCategory[nBJets]
	tree = TChain("AnalysisTree")
	fileList = samples[sample][0]
	for fileName in fileList:
		tree.Add("%s/QCDcr_%s"%(ntupleDirBase,fileName))

	if not h_Info[5]: continue
	print "filling", h_Info[1], sample
	evtWeight = ""
	if h_Info[4]=="":
		evtWeight = "%s%s"%(h_Info[3],weights)
	else:
		evtWeight = h_Info[4]
	if "Data" in sample:
		evtWeight = h_Info[3]
	if evtWeight[-1]=="*":
		evtWeight= evtWeight[:-1]
	tree.Draw("%s>>%s_%s"%(h_Info[0],h_Info[1],sample),evtWeight)


#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
	keylist = _file["Data%s"%finalState].GetListOfKeys()
	histoList = {}
	print stackList
	for key in keylist:
		name = key.GetName()
		print name
		split = name.split('_')
		nameKey = split[0]
		if "Dilep" in nameKey:continue
		for n in split[1:-1]: nameKey += "_%s"%n
		hName = "%s_QCD_DD"%(nameKey)
		histoList[nameKey]= _file["Data%s"%finalState].Get("%s_%s"%(nameKey,"Data%s"%finalState))
		histoList[nameKey].SetNameTitle(hName,hName)
		for sample in stackList:
			tempHist = _file[sample].Get("%s_%s"%(nameKey,sample))
		print _file[sample], "%s_%s"%(nameKey,sample)
		if nameKey=="presel_DilepMass":continue
		if "endcap" in nameKey:continue
			histoList[nameKey].Add(tempHist,-1)
	for h in histoList:
		histoList[h].Write()
	outputFile.Close()

'''
if __name__=="__main__":
		output = TFile("aa.root", "recreate")
		getQCDTransFact("Mu")

