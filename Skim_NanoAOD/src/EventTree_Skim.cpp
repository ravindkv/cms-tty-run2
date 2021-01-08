#include<iostream>
#include "../interface/EventTree_Skim.h"

EventTree::EventTree(int nFiles, bool xRootDAccess, string year, char** fileNames, bool isMC){
    chain = new TChain("Events");

    std::cout << "Start EventTree" << std::endl;
    chain->SetCacheSize(100*1024*1024);
    if (xRootDAccess){
	//string dir = "root://cms-xrd-global.cern.ch/";
	string dir = "root://cmsxrootd.fnal.gov/";
	for(int fileI=0; fileI<nFiles; fileI++){
	    string fName = (string) fileNames[fileI];
	    chain->Add( (dir + fileNames[fileI]).c_str() );
	    //cout << dir+fName << "  " << chain->GetEntries() << endl;
	    cout << (dir + fileNames[fileI]).c_str() << "  " << chain->GetEntries() << endl;
	}
    }
    else{
	for(int fileI=0; fileI<nFiles; fileI++){
	    chain->Add(fileNames[fileI]);
	    cout <<fileNames[fileI]<<endl;
	}
    }
    std::cout << "Begin" << std::endl;
    chain->SetBranchStatus("*",0);
	
    // keep some important branches
    chain->SetBranchStatus("PV_ndof",1);
    chain->SetBranchStatus("PV_x",1);
    chain->SetBranchStatus("PV_y",1);
    chain->SetBranchStatus("PV_z",1);
    chain->SetBranchStatus("PV_chi2",1);

    if (isMC){
	chain->SetBranchStatus("Pileup_nPU",1);
	chain->SetBranchAddress("Pileup_nPU", &nPU_);
	
	chain->SetBranchStatus("Pileup_nTrueInt",1);
	chain->SetBranchAddress("Pileup_nTrueInt", &nPUTrue_);
    }

	
    // event
	
    chain->SetBranchStatus("run",1);
    chain->SetBranchStatus("event",1);
    chain->SetBranchStatus("luminosityBlock",1);

    if (isMC){
	chain->SetBranchStatus("Generator_weight",1);
	chain->SetBranchAddress("Generator_weight", &genWeight_);
    }

    chain->SetBranchStatus("PV_npvs",1);

    chain->SetBranchStatus("PV_npvsGood",1);

    // MET
    chain->SetBranchStatus("MET_pt",1);
    chain->SetBranchStatus("MET_phi",1);

    if (isMC){
	chain->SetBranchStatus("GenMET_pt",1);
	chain->SetBranchStatus("GenMET_phi",1);
    }

	
    // electrons	
	
    chain->SetBranchStatus("nElectron",1);
    chain->SetBranchStatus("Electron_*",1);
    // muons
    // keep some branches in the skim
	
    chain->SetBranchStatus("nMuon",1);
    chain->SetBranchStatus("Muon_*",1);

    // jets
	
    chain->SetBranchStatus("nJet",1);
    chain->SetBranchStatus("Jet_*",1);

    chain->SetBranchAddress("nJet", &nJet_);
    chain->SetBranchAddress("Jet_jetId", &jetID_);


    // // photons
	
    chain->SetBranchStatus("nPhoton",1);

    chain->SetBranchStatus("Photon_*",1);
	
    // Gen Partons
    if (isMC){
	chain->SetBranchStatus("nGenPart",1);
	
	chain->SetBranchStatus("GenPart_*",1);

	chain->SetBranchStatus("nLHEPart",1);

	chain->SetBranchStatus("LHEPart_*",1);

	// chain->SetBranchAddress("GenPart_pt", &GenPart_pt_);
	
	// chain->SetBranchStatus("GenPart_eta",1);
	// chain->SetBranchAddress("GenPart_eta", &GenPart_eta_);
	
	// chain->SetBranchStatus("GenPart_phi",1);
	// chain->SetBranchAddress("GenPart_phi", &GenPart_phi_);

	// chain->SetBranchStatus("GenPart_mass",1);
	// chain->SetBranchAddress("GenPart_mass", &GenPart_mass_);

	// chain->SetBranchStatus("GenPart_genPartIdxMother",1);
	// chain->SetBranchAddress("GenPart_genPartIdxMother", &GenPart_genPartIdxMother_);

	// chain->SetBranchStatus("GenPart_pdgId",1);
	// chain->SetBranchAddress("GenPart_pdgId", &GenPart_pdgId_);
	
	// chain->SetBranchStatus("GenPart_status",1);
	// chain->SetBranchAddress("GenPart_status", &GenPart_status_);
	
	// chain->SetBranchStatus("GenPart_statusFlags",1);
	// chain->SetBranchAddress("GenPart_statusFlags", &GenPart_statusFlags_);
    

	chain->SetBranchStatus("nGenJet",1);
	
	chain->SetBranchStatus("GenJet_*",1);
	// chain->SetBranchAddress("GenJet_pt", &GenJet_pt_);

	// chain->SetBranchStatus("GenJet_eta",1);
	// chain->SetBranchAddress("GenJet_eta", &GenJet_eta_);

	// chain->SetBranchStatus("GenJet_phi",1);
	// chain->SetBranchAddress("GenJet_phi", &GenJet_phi_);

	// chain->SetBranchStatus("GenJet_mass",1);
	// chain->SetBranchAddress("GenJet_mass", &GenJet_mass_);

        chain->SetBranchStatus("nPSWeight",1);
        chain->SetBranchStatus("PSWeight",1);

        chain->SetBranchStatus("nLHEPdfWeight",1);
        chain->SetBranchStatus("LHEPdfWeight",1);

        chain->SetBranchStatus("nLHEScaleWeight",1);
        chain->SetBranchStatus("LHEScaleWeight",1);

	chain->SetBranchStatus("LHEWeight_originalXWGTUP",1);
    }

    if (year=="2016" || year=="2017"){
	chain->SetBranchStatus("L1PreFiringWeight*",1);
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
    std::cout << "Triggers" << std::endl;
    chain->SetBranchStatus("L1*",1);
    chain->SetBranchStatus("HLT_Ele*",1);
    chain->SetBranchStatus("HLT_Mu*",1);
    chain->SetBranchStatus("HLT_IsoMu*",1);
    chain->SetBranchStatus("HLT_TkMu*",1);
    chain->SetBranchStatus("HLT_Photon*",1);

    std::cout << "Triggers" << std::endl;
    
    if (year=="2016"){
	chain->SetBranchAddress("HLT_Ele27_WPTight_Gsf",&HLT_Ele27_WPTight_Gsf_);
	chain->SetBranchAddress("HLT_Ele105_CaloIdVT_GsfTrkIdT",&HLT_Ele105_CaloIdVT_GsfTrkIdT_);
	chain->SetBranchAddress("HLT_Ele115_CaloIdVT_GsfTrkIdT",&HLT_Ele115_CaloIdVT_GsfTrkIdT_);
	chain->SetBranchAddress("HLT_Photon175",&HLT_Photon175_);

	chain->SetBranchAddress("HLT_IsoMu24",&HLT_IsoMu24_);
        chain->SetBranchStatus("HLT_IsoTkMu*",1);
	chain->SetBranchAddress("HLT_IsoTkMu24",&HLT_IsoTkMu24_);
	chain->SetBranchAddress("HLT_Mu50",&HLT_Mu50_);
	chain->SetBranchAddress("HLT_TkMu50",&HLT_TkMu50_);
	chain->SetBranchAddress("HLT_Mu45_eta2p1",&HLT_Mu45_eta2p1_);
    }
    
    if (year=="2017"){
	chain->SetBranchAddress("HLT_Ele32_WPTight_Gsf_L1DoubleEG",&HLT_Ele32_WPTight_Gsf_L1DoubleEG_);
	chain->SetBranchAddress("HLT_Ele32_WPTight_Gsf",&HLT_Ele32_WPTight_Gsf_);
	chain->SetBranchAddress("HLT_Ele35_WPTight_Gsf",&HLT_Ele35_WPTight_Gsf_);
	chain->SetBranchAddress("HLT_Ele115_CaloIdVT_GsfTrkIdT",&HLT_Ele115_CaloIdVT_GsfTrkIdT_);
	chain->SetBranchAddress("HLT_Photon200",&HLT_Photon200_);

	
	chain->SetBranchAddress("HLT_IsoMu24",&HLT_IsoMu24_);
	chain->SetBranchAddress("HLT_IsoMu24_eta2p1",&HLT_IsoMu24_eta2p1_);
	chain->SetBranchAddress("HLT_IsoMu27",&HLT_IsoMu27_);
	chain->SetBranchAddress("HLT_Mu50",&HLT_Mu50_);
	chain->SetBranchStatus("HLT_OldMu*",1);
	chain->SetBranchAddress("HLT_OldMu100",&HLT_OldMu100_);
	chain->SetBranchAddress("HLT_TkMu100",&HLT_TkMu100_);

    }

    if (year=="2018"){
	chain->SetBranchAddress("HLT_Ele32_WPTight_Gsf",&HLT_Ele32_WPTight_Gsf_);
	chain->SetBranchAddress("HLT_Ele35_WPTight_Gsf",&HLT_Ele35_WPTight_Gsf_);
	chain->SetBranchAddress("HLT_Ele38_WPTight_Gsf",&HLT_Ele38_WPTight_Gsf_);
	chain->SetBranchAddress("HLT_Ele32_WPTight_Gsf_L1DoubleEG",&HLT_Ele32_WPTight_Gsf_L1DoubleEG_);
	chain->SetBranchAddress("HLT_Ele115_CaloIdVT_GsfTrkIdT",&HLT_Ele115_CaloIdVT_GsfTrkIdT_);
	chain->SetBranchStatus("HLT_DoubleEle*",1);
	chain->SetBranchAddress("HLT_DoubleEle25_CaloIdL_MW",&HLT_DoubleEle25_CaloIdL_MW_);
	chain->SetBranchAddress("HLT_Photon200",&HLT_Photon200_);

	chain->SetBranchAddress("HLT_IsoMu24",&HLT_IsoMu24_);
	chain->SetBranchAddress("HLT_IsoMu27",&HLT_IsoMu27_);
	chain->SetBranchAddress("HLT_Mu50",&HLT_Mu50_);
	chain->SetBranchStatus("HLT_OldMu*",1);
	chain->SetBranchAddress("HLT_OldMu100",&HLT_OldMu100_);
	chain->SetBranchAddress("HLT_TkMu100",&HLT_TkMu100_);

    }	

    chain->SetBranchStatus("fixedGridRhoFastjetAll",1);
    //    chain->SetBranchAddress("fixedGridRhoFastjetAll", &rho_);

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
