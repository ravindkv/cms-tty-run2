#include<iostream>
#include "../interface/EventTree.h"

EventTree::EventTree(int nFiles, bool xRootDAccess, string year, bool isData, char** fileNames){
    chain = new TChain("Events");

    isData_ = isData;

    //std::cout << chain->GetCacheSize() << std::endl;
    chain->SetCacheSize(100*1024*1024);
    if (xRootDAccess){
	//string dir = "root://cms-xrd-global.cern.ch/";
	string dir = "root://cmsxrootd.fnal.gov/";
	for(int fileI=0; fileI<nFiles; fileI++){
	    string fName = (string) fileNames[fileI];
	    chain->Add( (dir + fileNames[fileI]).c_str() );
	    cout << fName << "  " << chain->GetEntries() << endl;
	}
    }
    else{
	for(int fileI=0; fileI<nFiles; fileI++){
	    chain->Add(fileNames[fileI]);
	}
    }
    chain->SetBranchStatus("*",0);
	
    // keep some important branches
    chain->SetBranchStatus("PV_ndof",1);
    chain->SetBranchAddress("PV_ndof", &pvNDOF_);

    chain->SetBranchStatus("PV_x",1);
    chain->SetBranchAddress("PV_x", &pvX_);

    chain->SetBranchStatus("PV_y",1);
    chain->SetBranchAddress("PV_y", &pvY_);

    chain->SetBranchStatus("PV_z",1);
    chain->SetBranchAddress("PV_z", &pvZ_);

    chain->SetBranchStatus("PV_chi2",1);
    chain->SetBranchAddress("PV_chi2", &pvChi2_);

    if (!isData_){
	chain->SetBranchStatus("Pileup_nPU",1);
	chain->SetBranchAddress("Pileup_nPU", &nPU_);
	
	chain->SetBranchStatus("Pileup_nTrueInt",1);
	chain->SetBranchAddress("Pileup_nTrueInt", &nPUTrue_);
    }

	
    // event
	
    chain->SetBranchStatus("run",1);
    chain->SetBranchAddress("run", &run_);

    chain->SetBranchStatus("event",1);
    chain->SetBranchAddress("event", &event_);
	
    chain->SetBranchStatus("luminosityBlock",1);
    chain->SetBranchAddress("luminosityBlock", &lumis_);

    chain->SetBranchStatus("PV_npvs",1);
    chain->SetBranchAddress("PV_npvs", &nVtx_);

    chain->SetBranchStatus("PV_npvsGood",1);
    chain->SetBranchAddress("PV_npvsGood", &nGoodVtx_);


    if (!isData_){
	chain->SetBranchStatus("Generator_weight",1);
	chain->SetBranchAddress("Generator_weight", &genWeight_);

	chain->SetBranchStatus("nLHEScaleWeight",1);
	chain->SetBranchAddress("nLHEScaleWeight", &nLHEScaleWeight_);
	
	chain->SetBranchStatus("LHEScaleWeight",1);
	chain->SetBranchAddress("LHEScaleWeight", &LHEScaleWeight_);
	
	chain->SetBranchStatus("nLHEPdfWeight",1);
	chain->SetBranchAddress("nLHEPdfWeight", &nLHEPdfWeight_);
	
	chain->SetBranchStatus("LHEPdfWeight",1);
	chain->SetBranchAddress("LHEPdfWeight", &LHEPdfWeight_);
	
	chain->SetBranchStatus("PSWeight",1);
	chain->SetBranchAddress("PSWeight", &PSWeight_);
	
	chain->SetBranchStatus("nPSWeight",1);
	chain->SetBranchAddress("nPSWeight", &nPSWeight_);
	
	chain->SetBranchStatus("LHEWeight_originalXWGTUP",1);
	chain->SetBranchAddress("LHEWeight_originalXWGTUP", &LHEWeight_originalXWGTUP_);
	
    }

    // MET
    chain->SetBranchStatus("MET_pt",1);
    chain->SetBranchAddress("MET_pt", &MET_pt_);

    chain->SetBranchStatus("MET_phi",1);
    chain->SetBranchAddress("MET_phi", &MET_phi_);

    if (!isData_){
	chain->SetBranchStatus("GenMET_pt",1);
	chain->SetBranchAddress("GenMET_pt", &GenMET_pt_);
	
	chain->SetBranchStatus("GenMET_phi",1);
	chain->SetBranchAddress("GenMET_phi", &GenMET_phi_);
    }

	
    // electrons	
	
    chain->SetBranchStatus("nElectron",1);
    chain->SetBranchAddress("nElectron", &nEle_);


    chain->SetBranchStatus("Electron_charge",1);
    chain->SetBranchAddress("Electron_charge", &eleCharge_);	

    chain->SetBranchStatus("Electron_pt",1);
    chain->SetBranchAddress("Electron_pt", &elePt_);

    chain->SetBranchStatus("Electron_deltaEtaSC",1);
    chain->SetBranchAddress("Electron_deltaEtaSC", &eleDeltaEtaSC_);

    chain->SetBranchStatus("Electron_eta",1);
    chain->SetBranchAddress("Electron_eta", &eleEta_);

    chain->SetBranchStatus("Electron_phi",1);
    chain->SetBranchAddress("Electron_phi", &elePhi_);

    chain->SetBranchStatus("Electron_mass",1);
    chain->SetBranchAddress("Electron_mass", &eleMass_);

    chain->SetBranchStatus("Electron_pfRelIso03_chg",1);
    chain->SetBranchAddress("Electron_pfRelIso03_chg", &elePFRelChIso_);

    chain->SetBranchStatus("Electron_pfRelIso03_all",1);
    chain->SetBranchAddress("Electron_pfRelIso03_all", &elePFRelIso_);

    chain->SetBranchStatus("Electron_sieie",1);
    chain->SetBranchAddress("Electron_sieie", &eleSIEIE_);
	
    if (year=="2016"){
	chain->SetBranchStatus("Electron_cutBased",1); 
	chain->SetBranchAddress("Electron_cutBased", &eleIDcutbased_);

	chain->SetBranchStatus("Electron_vidNestedWPBitmap",1);
	chain->SetBranchAddress("Electron_vidNestedWPBitmap", &eleVidWPBitmap_);
    }
    if (year=="2017" || year=="2018"){
	chain->SetBranchStatus("Electron_cutBased",1);
	chain->SetBranchAddress("Electron_cutBased", &eleIDcutbased_);

	chain->SetBranchStatus("Electron_vidNestedWPBitmap",1);
	chain->SetBranchAddress("Electron_vidNestedWPBitmap", &eleVidWPBitmap_);
    }

    chain->SetBranchStatus("Electron_dxy",1);
    chain->SetBranchAddress("Electron_dxy", &eleD0_);

    chain->SetBranchStatus("Electron_dz",1);
    chain->SetBranchAddress("Electron_dz", &eleDz_);

    
    chain->SetBranchStatus("Electron_dr03EcalRecHitSumEt",1);
    chain->SetBranchAddress("Electron_dr03EcalRecHitSumEt", &eleEcalSumEtDr03_);

    chain->SetBranchStatus("Electron_dr03HcalDepth1TowerSumEt",1);
    chain->SetBranchAddress("Electron_dr03HcalDepth1TowerSumEt", &eleHcalSumEtDr03_);

    chain->SetBranchStatus("Electron_dr03TkSumPt",1);
    chain->SetBranchAddress("Electron_dr03TkSumPt", &eleTrkSumPtDr03_);

    chain->SetBranchStatus("Electron_photonIdx",1);
    chain->SetBranchAddress("Electron_photonIdx", &elePhoIdx_);




        

    // muons
    // keep some branches in the skim
	
    chain->SetBranchStatus("nMuon",1);
    chain->SetBranchAddress("nMuon", &nMuon_);

    chain->SetBranchStatus("Muon_charge",1);
    chain->SetBranchAddress("Muon_charge", &muCharge_);
	
    chain->SetBranchStatus("Muon_pt",1);
    chain->SetBranchAddress("Muon_pt", &muPt_);

    chain->SetBranchStatus("Muon_eta",1);
    chain->SetBranchAddress("Muon_eta", &muEta_);

    chain->SetBranchStatus("Muon_phi",1);
    chain->SetBranchAddress("Muon_phi", &muPhi_);

    chain->SetBranchStatus("Muon_mass",1);
    chain->SetBranchAddress("Muon_mass", &muMass_);

    chain->SetBranchStatus("Muon_pfRelIso04_all",1);
    chain->SetBranchAddress("Muon_pfRelIso04_all", &muPFRelIso_);

    chain->SetBranchStatus("Muon_tightId",1);
    chain->SetBranchAddress("Muon_tightId", &muTightId_);

    chain->SetBranchStatus("Muon_mediumId",1);
    chain->SetBranchAddress("Muon_mediumId", &muMediumId_);

    chain->SetBranchStatus("Muon_isPFcand",1);
    chain->SetBranchAddress("Muon_isPFcand", &muIsPFMuon_);

    chain->SetBranchStatus("Muon_isGlobal",1);
    chain->SetBranchAddress("Muon_isGlobal", &muIsGlobal_);

    chain->SetBranchStatus("Muon_isTracker",1);
    chain->SetBranchAddress("Muon_isTracker", &muIsTracker_);


    // jets
	
    chain->SetBranchStatus("nJet",1);
    chain->SetBranchAddress("nJet", &nJet_);
 
    chain->SetBranchStatus("Jet_pt",1);
    chain->SetBranchAddress("Jet_pt", &jetPt_);

    chain->SetBranchStatus("Jet_rawFactor",1);
    chain->SetBranchAddress("Jet_rawFactor", &jetRawFactor_);
	
    chain->SetBranchStatus("Jet_eta",1);
    chain->SetBranchAddress("Jet_eta", &jetEta_);
	
    chain->SetBranchStatus("Jet_phi",1);
    chain->SetBranchAddress("Jet_phi", &jetPhi_);

    chain->SetBranchStatus("Jet_mass",1);
    chain->SetBranchAddress("Jet_mass", &jetMass_);

    chain->SetBranchStatus("Jet_jetId",1);
    chain->SetBranchAddress("Jet_jetId", &jetID_);

    chain->SetBranchStatus("Jet_area",1);
    chain->SetBranchAddress("Jet_area", &jetArea_);

    chain->SetBranchStatus("Jet_btagCMVA",1);
    chain->SetBranchAddress("Jet_btagCMVA", &jetBtagCMVA_);

    chain->SetBranchStatus("Jet_btagCSVV2",1);
    chain->SetBranchAddress("Jet_btagCSVV2", &jetBtagCSVV2_);

    chain->SetBranchStatus("Jet_btagDeepB",1);
    chain->SetBranchAddress("Jet_btagDeepB", &jetBtagDeepB_);

    chain->SetBranchStatus("Jet_btagDeepC",1);
    chain->SetBranchAddress("Jet_btagDeepC", &jetBtagDeepC_);

    chain->SetBranchStatus("Jet_btagDeepFlavB",1);
    chain->SetBranchAddress("Jet_btagDeepFlavB", &jetBtagDeepFlavB_);

    chain->SetBranchStatus("Jet_chEmEF",1);
    chain->SetBranchAddress("Jet_chEmEF", &jetchEmEF_);

    chain->SetBranchStatus("Jet_neEmEF",1);
    chain->SetBranchAddress("Jet_neEmEF", &jetneEmEF_);

    if (!isData_){
	chain->SetBranchStatus("Jet_hadronFlavour",1);
	chain->SetBranchAddress("Jet_hadronFlavour", &jetHadFlvr_);
	
	chain->SetBranchStatus("Jet_genJetIdx",1);
	chain->SetBranchAddress("Jet_genJetIdx", &jetGenJetIdx_);
    }

    // // photons
	
    chain->SetBranchStatus("nPhoton",1);
    chain->SetBranchAddress("nPhoton", &nPho_);

    chain->SetBranchStatus("Photon_pt",1);
    chain->SetBranchAddress("Photon_pt", &phoEt_);
	
    chain->SetBranchStatus("Photon_eta",1);
    chain->SetBranchAddress("Photon_eta", &phoEta_);

    chain->SetBranchStatus("Photon_phi",1);
    chain->SetBranchAddress("Photon_phi", &phoPhi_);
	
    chain->SetBranchStatus("Photon_isScEtaEB",1);
    chain->SetBranchAddress("Photon_isScEtaEB", &phoIsEB_);

    chain->SetBranchStatus("Photon_isScEtaEE",1);
    chain->SetBranchAddress("Photon_isScEtaEE", &phoIsEE_);

    if (year=="2016"){
	chain->SetBranchStatus("Photon_cutBased",1);
	chain->SetBranchAddress("Photon_cutBased", &phoIDcutbased_);
    }
    if (year=="2017" || year=="2018"){
	chain->SetBranchStatus("Photon_cutBasedBitmap",1);
	chain->SetBranchAddress("Photon_cutBasedBitmap", &phoIDcutbased_);
    }
	

    chain->SetBranchStatus("Photon_pfRelIso03_all",1);
    chain->SetBranchAddress("Photon_pfRelIso03_all", &phoPFRelIso_);

    chain->SetBranchStatus("Photon_pfRelIso03_chg",1);
    chain->SetBranchAddress("Photon_pfRelIso03_chg", &phoPFRelChIso_);

    chain->SetBranchStatus("Photon_vidNestedWPBitmap",1);
    chain->SetBranchAddress("Photon_vidNestedWPBitmap", &phoVidWPBitmap_);

    chain->SetBranchStatus("Photon_pixelSeed",1);
    chain->SetBranchAddress("Photon_pixelSeed", &phoPixelSeed_);

    chain->SetBranchStatus("Photon_r9",1);
    chain->SetBranchAddress("Photon_r9", &phoR9_);

    chain->SetBranchStatus("Photon_sieie",1);
    chain->SetBranchAddress("Photon_sieie", &phoSIEIE_);

    chain->SetBranchStatus("Photon_hoe",1);
    chain->SetBranchAddress("Photon_hoe", &phoHoverE_);

    if (!isData_){
	chain->SetBranchStatus("Photon_genPartIdx",1);
	chain->SetBranchAddress("Photon_genPartIdx", &phoGenPartIdx_);
    }
    chain->SetBranchStatus("Photon_electronVeto",1);
    chain->SetBranchAddress("Photon_electronVeto", &phoEleVeto_);
	
    chain->SetBranchStatus("Photon_mvaID",1);
    chain->SetBranchAddress("Photon_mvaID", &phoMVAId_);

    if (year=="2016"){
	chain->SetBranchStatus("Photon_mvaID17",1);
	chain->SetBranchAddress("Photon_mvaID17", &phoMVAId17V1_);
    }
    if (year=="2017" || year=="2018"){
	chain->SetBranchStatus("Photon_mvaIDV1",1);
	chain->SetBranchAddress("Photon_mvaIDV1", &phoMVAId17V1_);
    }
    

    // Gen Partons
    if (!isData_){
	chain->SetBranchStatus("nGenPart",1);
	chain->SetBranchAddress("nGenPart", &nGenPart_);
	
	chain->SetBranchStatus("GenPart_pt",1);
	chain->SetBranchAddress("GenPart_pt", &GenPart_pt_);
	
	chain->SetBranchStatus("GenPart_eta",1);
	chain->SetBranchAddress("GenPart_eta", &GenPart_eta_);
	
	chain->SetBranchStatus("GenPart_phi",1);
	chain->SetBranchAddress("GenPart_phi", &GenPart_phi_);

	chain->SetBranchStatus("GenPart_mass",1);
	chain->SetBranchAddress("GenPart_mass", &GenPart_mass_);

	chain->SetBranchStatus("GenPart_genPartIdxMother",1);
	chain->SetBranchAddress("GenPart_genPartIdxMother", &GenPart_genPartIdxMother_);

	chain->SetBranchStatus("GenPart_pdgId",1);
	chain->SetBranchAddress("GenPart_pdgId", &GenPart_pdgId_);
	
	chain->SetBranchStatus("GenPart_status",1);
	chain->SetBranchAddress("GenPart_status", &GenPart_status_);
	
	chain->SetBranchStatus("GenPart_statusFlags",1);
	chain->SetBranchAddress("GenPart_statusFlags", &GenPart_statusFlags_);
    

	chain->SetBranchStatus("nGenJet",1);
	chain->SetBranchAddress("nGenJet", &nGenJet_);
	
	chain->SetBranchStatus("GenJet_pt",1);
	chain->SetBranchAddress("GenJet_pt", &GenJet_pt_);

	chain->SetBranchStatus("GenJet_eta",1);
	chain->SetBranchAddress("GenJet_eta", &GenJet_eta_);

	chain->SetBranchStatus("GenJet_phi",1);
	chain->SetBranchAddress("GenJet_phi", &GenJet_phi_);

	chain->SetBranchStatus("GenJet_mass",1);
	chain->SetBranchAddress("GenJet_mass", &GenJet_mass_);
    }

    //Fliters
    chain->SetBranchStatus("Flag_goodVertices",1);
    chain->SetBranchAddress("Flag_goodVertices",&Flag_goodVertices_);

    chain->SetBranchStatus("Flag_globalSuperTightHalo2016Filter",1);
    chain->SetBranchAddress("Flag_globalSuperTightHalo2016Filter", &Flag_globalSuperTightHalo2016Filter_);

    chain->SetBranchStatus("Flag_HBHENoiseFilter",1);
    chain->SetBranchAddress("Flag_HBHENoiseFilter", &Flag_HBHENoiseFilter_);

    chain->SetBranchStatus("Flag_HBHENoiseIsoFilter",1);
    chain->SetBranchAddress("Flag_HBHENoiseIsoFilter", &Flag_HBHENoiseIsoFilter_);

    chain->SetBranchStatus("Flag_EcalDeadCellTriggerPrimitiveFilter",1);
    chain->SetBranchAddress("Flag_EcalDeadCellTriggerPrimitiveFilter", &Flag_EcalDeadCellTriggerPrimitiveFilter_);

    chain->SetBranchStatus("Flag_BadPFMuonFilter",1);
    chain->SetBranchAddress("Flag_BadPFMuonFilter",&Flag_BadPFMuonFilter_);

    if(year =="2017" || year == "2018"){
	chain->SetBranchStatus("Flag_ecalBadCalibFilterV2",1);
	chain->SetBranchAddress("Flag_ecalBadCalibFilterV2",&Flag_ecalBadCalibFilterV2_);
    }

    //TRIGGERS

    if (year=="2016"){
	chain->SetBranchStatus("HLT_Ele27_WPTight_Gsf",1);
	chain->SetBranchAddress("HLT_Ele27_WPTight_Gsf",&HLT_Ele27_WPTight_Gsf_);
	
	// chain->SetBranchStatus("HLT_Ele105_CaloIdVT_GsfTrkIdT",1);
	// chain->SetBranchAddress("HLT_Ele105_CaloIdVT_GsfTrkIdT",&HLT_Ele105_CaloIdVT_GsfTrkIdT_);
	
	// chain->SetBranchStatus("HLT_Ele115_CaloIdVT_GsfTrkIdT",1);
	// chain->SetBranchAddress("HLT_Ele115_CaloIdVT_GsfTrkIdT",&HLT_Ele115_CaloIdVT_GsfTrkIdT_);
	
	// chain->SetBranchStatus("HLT_Photon175",1);
	// chain->SetBranchAddress("HLT_Photon175",&HLT_Photon175_);

	// chain->SetBranchStatus("HLT_Ele32_eta2p1_WPTight_Gsf",1);
	// chain->SetBranchAddress("HLT_Ele32_eta2p1_WPTight_Gsf",&HLT_Ele32_eta2p1_WPTight_Gsf_);

	chain->SetBranchStatus("HLT_IsoMu24",1);
	chain->SetBranchAddress("HLT_IsoMu24",&HLT_IsoMu24_);
	
	chain->SetBranchStatus("HLT_IsoTkMu24",1);
	chain->SetBranchAddress("HLT_IsoTkMu24",&HLT_IsoTkMu24_);
	
    }
    
    if (year=="2017"){
	chain->SetBranchStatus("HLT_Ele32_WPTight_Gsf_L1DoubleEG",1);
	chain->SetBranchAddress("HLT_Ele32_WPTight_Gsf_L1DoubleEG",&HLT_Ele32_WPTight_Gsf_L1DoubleEG_);
	
	// chain->SetBranchStatus("HLT_Ele32_WPTight_Gsf",1);
	// chain->SetBranchAddress("HLT_Ele32_WPTight_Gsf",&HLT_Ele32_WPTight_Gsf_);
	
	// chain->SetBranchStatus("HLT_Ele35_WPTight_Gsf",1);
	// chain->SetBranchAddress("HLT_Ele35_WPTight_Gsf",&HLT_Ele35_WPTight_Gsf_);
	
	// chain->SetBranchStatus("HLT_Ele115_CaloIdVT_GsfTrkIdT",1);
	// chain->SetBranchAddress("HLT_Ele115_CaloIdVT_GsfTrkIdT",&HLT_Ele115_CaloIdVT_GsfTrkIdT_);
	
	// chain->SetBranchStatus("HLT_Photon200",1);
	// chain->SetBranchAddress("HLT_Photon200",&HLT_Photon200_);

	chain->SetBranchStatus("HLT_IsoMu24",1);
	chain->SetBranchAddress("HLT_IsoMu24",&HLT_IsoMu24_);
	
	// chain->SetBranchStatus("HLT_IsoTkMu24",1);
	// chain->SetBranchAddress("HLT_IsoTkMu24",&HLT_IsoTkMu24_);

	// chain->SetBranchStatus("HLT_IsoMu24_eta2p1",1);
	// chain->SetBranchAddress("HLT_IsoMu24_eta2p1",&HLT_IsoMu24_eta2p1_);

	chain->SetBranchStatus("HLT_IsoMu27",1);
	chain->SetBranchAddress("HLT_IsoMu27",&HLT_IsoMu27_);

	chain->SetBranchAddress("L1_SingleEG24",&L1_SingleEG24_);
	chain->SetBranchAddress("L1_SingleEG26",&L1_SingleEG26_);
	chain->SetBranchAddress("L1_SingleEG30",&L1_SingleEG30_);
	chain->SetBranchAddress("L1_SingleEG32",&L1_SingleEG32_);
	chain->SetBranchAddress("L1_SingleEG34",&L1_SingleEG34_);
	chain->SetBranchAddress("L1_SingleEG36",&L1_SingleEG36_);
	chain->SetBranchAddress("L1_SingleEG38",&L1_SingleEG38_);
	chain->SetBranchAddress("L1_SingleEG40",&L1_SingleEG40_);
	chain->SetBranchAddress("L1_SingleEG42",&L1_SingleEG42_);
	chain->SetBranchAddress("L1_SingleEG45",&L1_SingleEG45_);
	chain->SetBranchAddress("L1_SingleEG50",&L1_SingleEG50_);
	chain->SetBranchAddress("L1_SingleEG34er2p1",&L1_SingleEG34er2p1_);
	chain->SetBranchAddress("L1_SingleEG36er2p1",&L1_SingleEG36er2p1_);
	chain->SetBranchAddress("L1_SingleEG38er2p1",&L1_SingleEG38er2p1_);
	chain->SetBranchAddress("L1_SingleIsoEG24er2p1",&L1_SingleIsoEG24er2p1_);
	chain->SetBranchAddress("L1_SingleIsoEG26er2p1",&L1_SingleIsoEG26er2p1_);
	chain->SetBranchAddress("L1_SingleIsoEG28er2p1",&L1_SingleIsoEG28er2p1_);
	chain->SetBranchAddress("L1_SingleIsoEG30er2p1",&L1_SingleIsoEG30er2p1_);
	chain->SetBranchAddress("L1_SingleIsoEG32er2p1",&L1_SingleIsoEG32er2p1_);
	chain->SetBranchAddress("L1_SingleIsoEG34er2p1",&L1_SingleIsoEG34er2p1_);
	chain->SetBranchAddress("L1_SingleIsoEG36er2p1",&L1_SingleIsoEG36er2p1_);
	chain->SetBranchAddress("L1_SingleIsoEG24",&L1_SingleIsoEG24_);
	chain->SetBranchAddress("L1_SingleIsoEG26",&L1_SingleIsoEG26_);
	chain->SetBranchAddress("L1_SingleIsoEG28",&L1_SingleIsoEG28_);
	chain->SetBranchAddress("L1_SingleIsoEG30",&L1_SingleIsoEG30_);
	chain->SetBranchAddress("L1_SingleIsoEG32",&L1_SingleIsoEG32_);
	chain->SetBranchAddress("L1_SingleIsoEG34",&L1_SingleIsoEG34_);
	chain->SetBranchAddress("L1_SingleIsoEG36",&L1_SingleIsoEG36_);
	chain->SetBranchAddress("L1_SingleIsoEG38",&L1_SingleIsoEG38_);



    }

    if (year=="2018"){
	chain->SetBranchStatus("HLT_Ele32_WPTight_Gsf",1);
	chain->SetBranchAddress("HLT_Ele32_WPTight_Gsf",&HLT_Ele32_WPTight_Gsf_);

	// chain->SetBranchStatus("HLT_Ele35_WPTight_Gsf",1);
	// chain->SetBranchAddress("HLT_Ele35_WPTight_Gsf",&HLT_Ele35_WPTight_Gsf_);

	// chain->SetBranchStatus("HLT_Ele38_WPTight_Gsf",1);
	// chain->SetBranchAddress("HLT_Ele38_WPTight_Gsf",&HLT_Ele38_WPTight_Gsf_);

	// chain->SetBranchStatus("HLT_Ele32_WPTight_Gsf_L1DoubleEG",1);
	// chain->SetBranchAddress("HLT_Ele32_WPTight_Gsf_L1DoubleEG",&HLT_Ele32_WPTight_Gsf_L1DoubleEG_);

	// chain->SetBranchStatus("HLT_Ele115_CaloIdVT_GsfTrkIdT",1);
	// chain->SetBranchAddress("HLT_Ele115_CaloIdVT_GsfTrkIdT",&HLT_Ele115_CaloIdVT_GsfTrkIdT_);
	
	// chain->SetBranchStatus("HLT_DoubleEle25_CaloIdL_MW",1);
	// chain->SetBranchAddress("HLT_DoubleEle25_CaloIdL_MW",&HLT_DoubleEle25_CaloIdL_MW_);

	// chain->SetBranchStatus("HLT_Photon200",1);
	// chain->SetBranchAddress("HLT_Photon200",&HLT_Photon200_);

	chain->SetBranchStatus("HLT_IsoMu24",1);
	chain->SetBranchAddress("HLT_IsoMu24",&HLT_IsoMu24_);

    }	

    chain->SetBranchStatus("fixedGridRhoFastjetAll",1);
    chain->SetBranchAddress("fixedGridRhoFastjetAll", &rho_);

    // chain->SetBranchStatus("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",1);
    // chain->SetBranchAddress("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",&HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_);
    
    // chain->SetBranchStatus("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",1);
    // chain->SetBranchAddress("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",&HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_);
    
    // chain->SetBranchStatus("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",1);
    // chain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",&HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_);
    
    // chain->SetBranchStatus("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",1);
    // chain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",&HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_);
    
    // chain->SetBranchStatus("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",1);
    // chain->SetBranchAddress("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",&HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_);
    
    // chain->SetBranchStatus("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",1);
    // chain->SetBranchAddress("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",&HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_);



}

EventTree::~EventTree(){
    delete chain;
    // will be some memory leak due to created vectors
}

Long64_t EventTree::GetEntries(){
    return chain->GetEntries();
}

Int_t EventTree::GetEntry(Long64_t entry){
    chain->GetEntry(entry);
    return chain->GetEntries();
}
