#include"../interface/EventPick.h"
#include <TLorentzVector.h>
#include <iostream>
#include <iomanip>

EventPick::EventPick(std::string titleIn){
    title = titleIn;
    year = "2016";
    saveCutflows = false;

    printEvent = -1;

    loosePhotonVeto=true;

    cutFlow_ele = new TH1D("cut_flow_ele","cut flow e+jets",20,-0.5,19.5);
    cutFlow_ele->SetDirectory(0);
    set_cutflow_labels_ele(cutFlow_ele);

    cutFlow_mu = new TH1D("cut_flow_mu","cut flow mu+jets",20,-0.5,19.5);
    cutFlow_mu->SetDirectory(0);
    set_cutflow_labels_mu(cutFlow_mu);

    cutFlowWeight_ele = new TH1D("cut_flow_weight_ele","cut flow with PU weight e+jets",20,-0.5,19.5);
    cutFlowWeight_ele->SetDirectory(0);
    set_cutflow_labels_ele(cutFlowWeight_ele);

    cutFlowWeight_mu = new TH1D("cut_flow_weight_mu","cut flow with PU weight mu+jets",20,-0.5,19.5);
    cutFlowWeight_mu->SetDirectory(0);
    set_cutflow_labels_mu(cutFlowWeight_mu);


    // Cut levels
    Nmu_eq = 1;
    Nele_eq = 1;
    NlooseMuVeto_le = 0;
    NlooseEleVeto_le = 0;


    // These dR cuts are all done at selection level now
    // assign cut values
    //	veto_jet_dR = 0.1;
    // veto_lep_jet_dR = 0.4;
    // veto_pho_jet_dR = 0.7;
    // veto_pho_lep_dR = 0.7;

    MET_cut = 0.0;
    no_trigger = false;

    skimEle = false;
    skimMu = false;

    Njet_ge = 3;
    SkimNjet_ge = 2;

    NBjet_ge = 1;
    SkimNBjet_ge = 1;
    Nlep_eq = 1;

    ZeroBExclusive = false;

    QCDselect = false;

    applyMetFilter   = false;

    Npho_eq = 1;

}

EventPick::~EventPick(){
}

void EventPick::process_event(EventTree* tree, Selector* selector, double weight){

    //	clear_vectors();
    passSkim = false;
    passPresel_ele = false;
    passPresel_mu = false;
    passAll_ele = false;
    passAll_mu = false;

    if (tree->event_==printEvent){
	cout << "Found Event Number " << printEvent << endl;
    }
    bool Pass_trigger_mu  = false;
    bool Pass_trigger_ele = false;

    if (year=="2016") {
	Pass_trigger_mu = (tree->HLT_IsoMu24_ || tree->HLT_IsoTkMu24_  ) || no_trigger;
	Pass_trigger_ele = tree->HLT_Ele27_WPTight_Gsf_ || no_trigger;
    }
    if (year=="2017"){
	Pass_trigger_mu = (tree->HLT_IsoMu27_) || no_trigger;

	bool allSingleEGL1or = (tree->L1_SingleEG24_ ||
				tree->L1_SingleEG26_ ||
				tree->L1_SingleEG30_ ||
				tree->L1_SingleEG32_ ||
				tree->L1_SingleEG34_ ||
				tree->L1_SingleEG36_ ||
				tree->L1_SingleEG38_ ||
				tree->L1_SingleEG40_ ||
				tree->L1_SingleEG42_ ||
				tree->L1_SingleEG45_ ||
				tree->L1_SingleEG50_ ||
				tree->L1_SingleEG34er2p1_ ||
				tree->L1_SingleEG36er2p1_ ||
				tree->L1_SingleEG38er2p1_ ||
				tree->L1_SingleIsoEG24er2p1_ ||
				tree->L1_SingleIsoEG26er2p1_ ||
				tree->L1_SingleIsoEG28er2p1_ ||
				tree->L1_SingleIsoEG30er2p1_ ||
				tree->L1_SingleIsoEG32er2p1_ ||
				tree->L1_SingleIsoEG34er2p1_ ||
				tree->L1_SingleIsoEG36er2p1_ ||
				tree->L1_SingleIsoEG24_ ||
				tree->L1_SingleIsoEG26_ ||
				tree->L1_SingleIsoEG28_ ||
				tree->L1_SingleIsoEG30_ ||
				tree->L1_SingleIsoEG32_ ||
				tree->L1_SingleIsoEG34_ ||
				tree->L1_SingleIsoEG36_ ||
				tree->L1_SingleIsoEG38_);
	
	Pass_trigger_ele = (tree->HLT_Ele32_WPTight_Gsf_L1DoubleEG_ && allSingleEGL1or) || no_trigger;

    }
    if (year=="2018"){
	Pass_trigger_mu = (tree->HLT_IsoMu24_) || no_trigger;
	Pass_trigger_ele = tree->HLT_Ele32_WPTight_Gsf_ || no_trigger;
    }

    bool filters = (tree->Flag_goodVertices_ &&
		    tree->Flag_globalSuperTightHalo2016Filter_ &&
		    tree->Flag_HBHENoiseFilter_ &&
		    tree->Flag_HBHENoiseIsoFilter_ &&
		    tree->Flag_EcalDeadCellTriggerPrimitiveFilter_ &&
		    tree->Flag_BadPFMuonFilter_ );

    if (year=="2017" || year=="2018"){ filters = filters && tree->Flag_ecalBadCalibFilterV2_ ;}

    //comment out following two line when no filter is needed
    if(applyMetFilter){
	Pass_trigger_mu = Pass_trigger_mu && filters ;
	Pass_trigger_ele = Pass_trigger_ele && filters ;
    }

    string run_lumi_event = to_string(tree->run_)+","+to_string(tree->lumis_)+","+to_string(tree->event_)+"\n";

    if (saveCutflows) {
	cutFlow_ele->Fill(0.0); // Input events
	cutFlow_mu->Fill(0.0); // Input events
	cutFlowWeight_ele->Fill(0.0,weight);
	cutFlowWeight_mu->Fill(0.0,weight);
	// dump_input_ele << run_lumi_event;
	// dump_input_mu << run_lumi_event;
    }

    if (tree->event_==printEvent){
	cout << "TriggerMu "<< Pass_trigger_mu << endl;
	cout << "TriggerEle "<< Pass_trigger_ele << endl;
    }
    // Pass_trigger_mu = Pass_trigger_mu || Pass_trigger_ele;
    // Pass_trigger_ele = Pass_trigger_mu || Pass_trigger_ele;

    passPresel_mu  = true;
    passPresel_ele = true;

    bool isPVGood = (tree->pvNDOF_>4 &&
		     sqrt(tree->pvX_ * tree->pvX_ + tree->pvY_ * tree->pvY_)<=2. &&
		     abs(tree->pvZ_) <= 24.);

    if (tree->event_==printEvent){
    	cout << "PV "<< isPVGood << endl;
    	cout << "    ndof="<<tree->pvNDOF_ << "   (>4)" << endl;
    	cout << "    pX="<<tree->pvX_ <<  "   (<2)" << endl;
    	cout << "    pY="<<tree->pvY_ <<  "   (<2)" << endl;
    	cout << "    pZ="<<tree->pvZ_ <<  "   (<24)" << endl;
    }

    // Cut events that fail mu trigger
    if( passPresel_mu &&  (Pass_trigger_mu)) {
	if (saveCutflows) {cutFlow_mu->Fill(1); cutFlowWeight_mu->Fill(1,weight); dump_trigger_mu << run_lumi_event;}
    }
    else { passPresel_mu = false;}
    if( passPresel_mu && isPVGood) { if (saveCutflows) {cutFlow_mu->Fill(2); cutFlowWeight_mu->Fill(2,weight); } }
    else { passPresel_mu = false;}

    // Cut events that fail ele trigger
    if( passPresel_ele &&  (Pass_trigger_ele)) { if (saveCutflows) {cutFlow_ele->Fill(1); cutFlowWeight_ele->Fill(1,weight); dump_trigger_ele << run_lumi_event;}}
    else { passPresel_ele = false;}
    if( passPresel_ele && isPVGood) { if (saveCutflows) {cutFlow_ele->Fill(2); cutFlowWeight_ele->Fill(2,weight);} }
    else { passPresel_ele = false; }


    if ( passPresel_ele || passPresel_mu ) {
	selector->process_objects(tree);
    }
    else {
	return;
    }


    if (tree->event_==printEvent){
	cout << "Muons     "<< selector->Muons.size() << endl;
	cout << "  Loose   "<< selector->MuonsLoose.size() << endl;
	cout << "Electrons "<< selector->Electrons.size() << endl;
	cout << "  Loose   "<< selector->ElectronsLoose.size() << endl;
	cout << "Jets      "<< selector->Jets.size() << endl;
	cout << "BJets     "<< selector->bJets.size() << endl;
	cout << "Photons   "<< selector->Photons.size() << endl;
	cout << "  Loose   "<< selector->LoosePhotons.size() << endl;
	cout << "-------------------"<< endl;
    }

    // Cut on events with ==1 muon, no loose muons, no loose or tight electrons
    if (!QCDselect){
	if( passPresel_mu && selector->Muons.size() == Nmu_eq){
	    if (Nmu_eq==2) {
		int idx_mu1 = selector->Muons.at(0);
		int idx_mu2 = selector->Muons.at(1);
		if(tree->muCharge_[idx_mu1]*tree->muCharge_[idx_mu2] ==1){
		    passPresel_mu = false;
		}
		TLorentzVector mu1;
		TLorentzVector mu2;
		mu1.SetPtEtaPhiM(tree->muPt_[idx_mu1],
				 tree->muEta_[idx_mu1],
				 tree->muPhi_[idx_mu1],
				 tree->muMass_[idx_mu1]);
		mu2.SetPtEtaPhiM(tree->muPt_[idx_mu2],
				 tree->muEta_[idx_mu2],
				 tree->muPhi_[idx_mu2],
				 tree->muMass_[idx_mu2]);
		if (tree->event_==printEvent){
		    cout << "DilepMass:    " << (mu1 + mu2).M() << endl;
		    cout << "Lep 1 Charge: " << tree->muCharge_[idx_mu1] << endl;
		    cout << "Lep 2 Charge: " << tree->muCharge_[idx_mu2] << endl;
		    cout << "-------------------"<< endl;
		}
 
		if ( abs((mu1 + mu2).M() - 91.1876) > 10 ){
		    passPresel_mu = false;
		}
	    }
	    if (saveCutflows){cutFlow_mu->Fill(3); cutFlowWeight_mu->Fill(3,weight); }
	}
	else { passPresel_mu = false;}

	if( passPresel_mu && selector->MuonsLoose.size() <=  NlooseMuVeto_le ) { if (saveCutflows) {cutFlow_mu->Fill(4); cutFlowWeight_mu->Fill(4,weight); } }
	else { passPresel_mu = false;}
	if( passPresel_mu && (selector->ElectronsLoose.size() + selector->Electrons.size() ) <=  NlooseEleVeto_le ) {if (saveCutflows) {cutFlow_mu->Fill(5); cutFlowWeight_mu->Fill(5,weight);  dump_lepton_mu << run_lumi_event;} }
	else { passPresel_mu = false;}
    }
    else{
	if( passPresel_mu && selector->Muons.size() == 1){
            if (saveCutflows){cutFlow_mu->Fill(3); cutFlowWeight_mu->Fill(3,weight); }
        }
        else { passPresel_mu = false;}

        // if( passPresel_mu && selector->MuonsNoIso.size() == 1 ) {
	//     if (saveCutflows) {cutFlow_mu->Fill(4); cutFlowWeight_mu->Fill(4,weight); } }
        // else { passPresel_mu = false;}
        // if( passPresel_mu && (selector->ElectronsNoIso.size() ) == 0 ) {
	//     if (saveCutflows) {cutFlow_mu->Fill(5); cutFlowWeight_mu->Fill(5,weight);} }
        // else { passPresel_mu = false;}
//aloke : looselepveto in QCDCR
	if( passPresel_mu && selector->MuonsLoose.size() <=  NlooseMuVeto_le ) { if (saveCutflows) {cutFlow_mu->Fill(4); cutFlowWeight_mu->Fill(4,weight);} }
	else { passPresel_mu = false;}
	if( passPresel_mu && (selector->ElectronsLoose.size() + selector->Electrons.size() ) <=  NlooseEleVeto_le ) {if (saveCutflows) {cutFlow_mu->Fill(5); cutFlowWeight_mu->Fill(5,weight);  dump_lepton_mu << run_lumi_event;} }
	else { passPresel_mu = false;}
    }


    // Cut on events with ==1 muon, no loose muons, no loose or tight electrons
    if (!QCDselect) {
	if( passPresel_ele && selector->Electrons.size() == Nele_eq) {
	    if (Nele_eq==2) {
		int idx_ele1 = selector->Electrons.at(0);
		int idx_ele2 = selector->Electrons.at(1);
		if((tree->eleCharge_[idx_ele1])*(tree->eleCharge_[idx_ele2]) == 1){
		    passPresel_ele = false;
		}
		TLorentzVector ele1;
		TLorentzVector ele2;
		ele1.SetPtEtaPhiM(tree->elePt_[idx_ele1],
				  tree->eleEta_[idx_ele1],
				  tree->elePhi_[idx_ele1],
				  tree->eleMass_[idx_ele1]);
		ele2.SetPtEtaPhiM(tree->elePt_[idx_ele2],
				  tree->eleEta_[idx_ele2],
				  tree->elePhi_[idx_ele2],
				  tree->eleMass_[idx_ele2]);
		if (tree->event_==printEvent){
		    cout << "DilepMass:    " << (ele1 + ele2).M() << endl;
		    cout << "Lep 1 Charge: " << tree->eleCharge_[idx_ele1] << endl;
		    cout << "Lep 2 Charge: " << tree->eleCharge_[idx_ele2] << endl;
		    cout << "-------------------"<< endl;
		}
 
		if ( abs((ele1 + ele2).M() - 91.1876) > 10 ){
		    passPresel_ele = false;
		}
	    }
	    if (saveCutflows) {cutFlow_ele->Fill(3); cutFlowWeight_ele->Fill(3,weight);}
	}
	else { passPresel_ele = false;}

	if( passPresel_ele && selector->ElectronsLoose.size() <=  NlooseEleVeto_le ) { if (saveCutflows) {cutFlow_ele->Fill(4); cutFlowWeight_ele->Fill(4,weight);}}
	else { passPresel_ele = false;}

	if( passPresel_ele && (selector->MuonsLoose.size() + selector->Muons.size() ) <=  NlooseMuVeto_le ) { if (saveCutflows) {cutFlow_ele->Fill(5); cutFlowWeight_ele->Fill(5,weight);  dump_lepton_ele << run_lumi_event;}}
	else { passPresel_ele = false;}
    }
    else {
	if( passPresel_ele && selector->Electrons.size() == 1){
            if (saveCutflows){cutFlow_ele->Fill(3); cutFlowWeight_ele->Fill(3,weight); }
        }
	else { passPresel_ele = false;}

        // if( passPresel_ele && selector->ElectronsNoIso.size() == 1 ) {
	//     if (saveCutflows) {cutFlow_ele->Fill(4); cutFlowWeight_ele->Fill(4,weight); } }
        // else { passPresel_ele = false;}
        // if( passPresel_ele && (selector->MuonsNoIso.size() ) == 0 ) {
	//     if (saveCutflows) {cutFlow_ele->Fill(5); cutFlowWeight_ele->Fill(5,weight);} }
        // else { passPresel_ele = false;}
//aloke ; loose lepton veto in QCDCR too

	if( passPresel_ele && selector->ElectronsLoose.size() <=  NlooseEleVeto_le ) { if (saveCutflows) {cutFlow_ele->Fill(4); cutFlowWeight_ele->Fill(4,weight);}}
	else { passPresel_ele = false;}
	if( passPresel_ele && (selector->MuonsLoose.size() + selector->Muons.size() ) <=  NlooseMuVeto_le ) { if (saveCutflows) {cutFlow_ele->Fill(5); cutFlowWeight_ele->Fill(5,weight);  dump_lepton_ele << run_lumi_event;}}
	else { passPresel_ele = false;}
    }

    // split skim into ele and mu
    if ( (skimEle && passPresel_ele) || (skimMu && passPresel_mu) && selector->Jets.size() >= SkimNjet_ge && selector->bJets.size() >= SkimNBjet_ge ){ passSkim = true; }

    if (tree->event_==printEvent){
	cout << "PassLepMu  "<< passPresel_mu << endl;
	cout << "PassLepEle "<< passPresel_ele << endl;
    }


    // NJet cuts for electrons
    // Implemented in this way (with a loop) to check for numbers failing each level of cut < Njet cut, and filling cutflow histo
    // cutflow histo will not be filled for bins where the cut is > Njet_ge (ex, if cut is at 3, Njets>=4 bin is left empty)
    for (int ijetCut = 1; ijetCut <= Njet_ge; ijetCut++){
	if(passPresel_ele && selector->Jets.size() >= ijetCut ) {
	    if (saveCutflows) {
		cutFlow_ele->Fill(5+ijetCut);
		cutFlowWeight_ele->Fill(5+ijetCut,weight);
		if (ijetCut==1){ dump_oneJet_ele << run_lumi_event; }
		if (ijetCut==2){ dump_twoJet_ele << run_lumi_event; }
		if (ijetCut==3){ dump_threeJet_ele << run_lumi_event; }
		if (ijetCut==4){ dump_fourJet_ele << run_lumi_event; }
	    }}
	else passPresel_ele = false;
    }

    // NJet cuts for muons
    // Implemented in this way (with a loop) to check for numbers failing each level of cut < Njet cut, and filling cutflow histo
    // cutflow histo will not be filled for bins where the cut is > Njet_ge (ex, if cut is at 3, Njet>=4 bin is left empty)
    for (int ijetCut = 1; ijetCut <= Njet_ge; ijetCut++){
	if(passPresel_mu && selector->Jets.size() >= ijetCut ) {
	    if (saveCutflows) {
		cutFlow_mu->Fill(5+ijetCut); cutFlowWeight_mu->Fill(5+ijetCut,weight);
		if (ijetCut==1){ dump_oneJet_mu << run_lumi_event; }
		if (ijetCut==2){ dump_twoJet_mu << run_lumi_event; }
		if (ijetCut==3){ dump_threeJet_mu << run_lumi_event; }
		if (ijetCut==4){ dump_fourJet_mu << run_lumi_event; }
	    }
	}
	else passPresel_mu = false;
    }
    if (tree->event_==printEvent){
	cout << "PassJetMu  "<< passPresel_mu << endl;
	cout << "PassJetEle "<< passPresel_ele << endl;
    }


    // Nbtag cuts for electrons
    if (!ZeroBExclusive){
	for (int ibjetCut = 1; ibjetCut <= NBjet_ge; ibjetCut++){
            if(passPresel_ele && selector->bJets.size() >= ibjetCut ) {
		if (saveCutflows ) {
		    cutFlow_ele->Fill(9+ibjetCut);
		    cutFlowWeight_ele->Fill(9+ibjetCut,weight);
		    if (ibjetCut==1){ dump_btag_ele << run_lumi_event; }
		}
	    }
            else{
		passPresel_ele = false;
	    }
	}
    } else {
	if(passPresel_ele && selector->bJets.size() !=0) passPresel_ele = false;
    }


    // Nbtag cuts for muons
    if (!ZeroBExclusive){
	for (int ibjetCut = 1; ibjetCut <= NBjet_ge; ibjetCut++){
            if(passPresel_mu  && selector->bJets.size() >= ibjetCut ) {
		if (saveCutflows) {
		    cutFlow_mu->Fill(9+ibjetCut);
		    cutFlowWeight_mu->Fill(9+ibjetCut,weight);
		    if (ibjetCut==1){ dump_btag_mu << run_lumi_event; }
		}
	    }
            else  passPresel_mu = false;
	}
    } else {
	if(passPresel_mu && selector->bJets.size() !=0) passPresel_mu = false;
    }

    if (tree->event_==printEvent){
	cout << "PassBMu  "<< passPresel_mu << endl;
	cout << "PassBEle "<< passPresel_ele << endl;
    }

    // MET cut for electrons
    if(passPresel_ele && tree->MET_pt_ >= MET_cut) { if (saveCutflows) {cutFlow_ele->Fill(12); cutFlowWeight_ele->Fill(12,weight);}}
    else passPresel_ele = false;

    // MET cut for muons
    if(passPresel_mu && tree->MET_pt_ >= MET_cut) { if (saveCutflows) {cutFlow_mu->Fill(12); cutFlowWeight_mu->Fill(12,weight);}}
    else passPresel_mu = false;



    // Photon cut for electrons
    if(passPresel_ele  && selector->Photons.size() == Npho_eq) {  
	passAll_ele = true;
	if (saveCutflows) {cutFlow_ele->Fill(13); cutFlowWeight_ele->Fill(13,weight);  dump_photon_ele << run_lumi_event;}
    }
    else passAll_ele = false ; 


    // Photon cut for muons
    if(passPresel_mu && selector->Photons.size() == Npho_eq) { 
	passAll_mu = true;
	if (saveCutflows) {cutFlow_mu->Fill(13); cutFlowWeight_mu->Fill(13,weight); dump_photon_mu << run_lumi_event;}
    }
    else passAll_mu = false ; 
    
    if (loosePhotonVeto){
	// Loose photon cut for electrons
	if(passAll_ele && selector->LoosePhotons.size() == Npho_eq) {
	    if (saveCutflows) {cutFlow_ele->Fill(14); cutFlowWeight_ele->Fill(14,weight);  dump_loosePhoton_ele << run_lumi_event;}
	}
	else passAll_ele = false;
    
	// Loose photon cut for muons
	if(passAll_mu && selector->LoosePhotons.size() == Npho_eq) {
	    if (saveCutflows) {cutFlow_mu->Fill(14); cutFlowWeight_mu->Fill(14,weight);  dump_loosePhoton_mu << run_lumi_event;}
	}
	else passAll_mu = false;
    }    
    
}

void EventPick::print_cutflow_mu(TH1D* _cutflow){
    std::cout << "Cut-Flow for the event selector: " << title << std::endl;
    std::cout << "Input Events :                " << _cutflow->GetBinContent(1) << std::endl;
    std::cout << "Passing Trigger               " << _cutflow->GetBinContent(2) << std::endl;
    std::cout << "Has Good Vtx               " << _cutflow->GetBinContent(3) << std::endl;
    std::cout << "Events with 1 muon     " << _cutflow->GetBinContent(4) << std::endl;
    std::cout << "Events with no loose muons " << _cutflow->GetBinContent(5) << std::endl;
    std::cout << "Events with no electrons " << _cutflow->GetBinContent(6) << std::endl;
    std::cout << "Events with >= " << 1 << " jets        " << _cutflow->GetBinContent(7) << std::endl;
    std::cout << "Events with >= " << 2 << " jets        " << _cutflow->GetBinContent(8) << std::endl;
    std::cout << "Events with >= " << 3 << " jets     " << _cutflow->GetBinContent(9) << std::endl;
    std::cout << "Events with >= " << 4 << " jets "<< _cutflow->GetBinContent(10) << std::endl;
    std::cout << "Events with >= " << 1 <<     " bjets "<< _cutflow->GetBinContent(11) << std::endl;
    std::cout << "Events with >= " << 2 << " bjets       " << _cutflow->GetBinContent(12) << std::endl;
    std::cout << "Events passing MET cut       " << _cutflow->GetBinContent(13) << std::endl;
    std::cout << "Events with >= 1 photon      " << _cutflow->GetBinContent(14) << std::endl;
    std::cout << std::endl;
}

void EventPick::print_cutflow_ele(TH1D* _cutflow){
    std::cout << "Cut-Flow for the event selector: " << title << std::endl;
    std::cout << "Input Events :                " << _cutflow->GetBinContent(1) << std::endl;
    std::cout << "Passing Trigger               " << _cutflow->GetBinContent(2) << std::endl;
    std::cout << "Has Good Vtx               " << _cutflow->GetBinContent(3) << std::endl;
    std::cout << "Events with 1 electron     " << _cutflow->GetBinContent(4) << std::endl;
    std::cout << "Events with no loose electrons " << _cutflow->GetBinContent(5) << std::endl;
    std::cout << "Events with no muons " << _cutflow->GetBinContent(6) << std::endl;
    std::cout << "Events with >= " << 1 << " jets        " << _cutflow->GetBinContent(7) << std::endl;
    std::cout << "Events with >= " << 2 << " jets        " << _cutflow->GetBinContent(8) << std::endl;
    std::cout << "Events with >= " << 3 << " jets     " << _cutflow->GetBinContent(9) << std::endl;
    std::cout << "Events with >= " << 4 << " jets "<< _cutflow->GetBinContent(10) << std::endl;
    std::cout << "Events with >= " << 1 <<     " bjets "<< _cutflow->GetBinContent(11) << std::endl;
    std::cout << "Events with >= " << 2 << " bjets       " << _cutflow->GetBinContent(12) << std::endl;
    std::cout << "Events passing MET cut       " << _cutflow->GetBinContent(13) << std::endl;
    std::cout << "Events with >= 1 photon      " << _cutflow->GetBinContent(14) << std::endl;
    std::cout << std::endl;
}

void EventPick::set_cutflow_labels_mu(TH1D* hist){
    hist->GetXaxis()->SetBinLabel(1,"Input");
    hist->GetXaxis()->SetBinLabel(2,"Trigger");
    hist->GetXaxis()->SetBinLabel(3,"Good Vtx");
    hist->GetXaxis()->SetBinLabel(4,"1 Muons");
    hist->GetXaxis()->SetBinLabel(5,"No Loose Muons");
    hist->GetXaxis()->SetBinLabel(6,"Veto Electrons");
    hist->GetXaxis()->SetBinLabel(7,">=1 jet");
    hist->GetXaxis()->SetBinLabel(8,">=2 jets");
    hist->GetXaxis()->SetBinLabel(9,">=3 jets");
    hist->GetXaxis()->SetBinLabel(10,">=4 jets");
    hist->GetXaxis()->SetBinLabel(11,">=1 b-tags");
    hist->GetXaxis()->SetBinLabel(12,">=2 b-tags");
    hist->GetXaxis()->SetBinLabel(13,"MET Cut");
    hist->GetXaxis()->SetBinLabel(14,"Photon");
    hist->GetXaxis()->SetBinLabel(15,"Loose Photon Veto");
    hist->GetXaxis()->SetBinLabel(16,"Genuine");
    hist->GetXaxis()->SetBinLabel(17,"MisIDEle");
    hist->GetXaxis()->SetBinLabel(18,"HadronicPho");
    hist->GetXaxis()->SetBinLabel(19,"HadronicFake");
}

void EventPick::set_cutflow_labels_ele(TH1D* hist){
    hist->GetXaxis()->SetBinLabel(1,"Input");
    hist->GetXaxis()->SetBinLabel(2,"Trigger");
    hist->GetXaxis()->SetBinLabel(3,"Good Vtx");
    hist->GetXaxis()->SetBinLabel(4,"1 Electrons");
    hist->GetXaxis()->SetBinLabel(5,"No Loose Electrons");
    hist->GetXaxis()->SetBinLabel(6,"Veto Muons");
    hist->GetXaxis()->SetBinLabel(7,">=1 jet");
    hist->GetXaxis()->SetBinLabel(8,">=2 jets");
    hist->GetXaxis()->SetBinLabel(9,">=3 jets");
    hist->GetXaxis()->SetBinLabel(10,">=4 jets");
    hist->GetXaxis()->SetBinLabel(11,">=1 b-tags");
    hist->GetXaxis()->SetBinLabel(12,">=2 b-tags");
    hist->GetXaxis()->SetBinLabel(13,"MET Cut");
    hist->GetXaxis()->SetBinLabel(14,"Photon");
    hist->GetXaxis()->SetBinLabel(15,"Lose Photon Veto");
    hist->GetXaxis()->SetBinLabel(16,"Genuine");
    hist->GetXaxis()->SetBinLabel(17,"MisIDEle");
    hist->GetXaxis()->SetBinLabel(18,"HadronicPho");
    hist->GetXaxis()->SetBinLabel(19,"HadronicFake");
}

void EventPick::init_cutflow_files(string fileName){
    fileName.replace(fileName.find(".root"),5,"");

    //    dump_input_ele.open(fileName+"_input_ele.csv");  
    dump_trigger_ele.open(fileName+"_trigger_ele.csv");  
    dump_lepton_ele.open(fileName+"_lepton_ele.csv");   
    dump_oneJet_ele.open(fileName+"_oneJet_ele.csv");   
    dump_twoJet_ele.open(fileName+"_twoJet_ele.csv");   
    dump_threeJet_ele.open(fileName+"_threeJet_ele.csv");
    dump_fourJet_ele.open(fileName+"_fourJet_ele.csv");  
    dump_btag_ele.open(fileName+"_btag_ele.csv");     
    dump_photon_ele.open(fileName+"_photon_ele.csv");   
    dump_loosePhoton_ele.open(fileName+"_loosePhoton_ele.csv");   
    dump_photon_GenPho_ele.open(fileName+"_photon_GenPho_ele.csv");   
    dump_photon_MisIDEle_ele.open(fileName+"_photon_MisIDEle_ele.csv");   
    dump_photon_HadPho_ele.open(fileName+"_photon_HadPho_ele.csv");   
    dump_photon_HadFake_ele.open(fileName+"_photon_HadFake_ele.csv");   
    dump_photon_PU_ele.open(fileName+"_photon_PU_ele.csv");   

    //    dump_input_mu.open(fileName+"_input_mu.csv");  
    dump_trigger_mu.open(fileName+"_trigger_mu.csv");  
    dump_lepton_mu.open(fileName+"_lepton_mu.csv");   
    dump_oneJet_mu.open(fileName+"_oneJet_mu.csv");   
    dump_twoJet_mu.open(fileName+"_twoJet_mu.csv");   
    dump_threeJet_mu.open(fileName+"_threeJet_mu.csv");
    dump_fourJet_mu.open(fileName+"_fourJet_mu.csv");  
    dump_btag_mu.open(fileName+"_btag_mu.csv");     
    dump_photon_mu.open(fileName+"_photon_mu.csv");   
    dump_loosePhoton_mu.open(fileName+"_loosePhoton_mu.csv");   
    dump_photon_GenPho_mu.open(fileName+"_photon_GenPho_mu.csv");   
    dump_photon_MisIDEle_mu.open(fileName+"_photon_MisIDEle_mu.csv");   
    dump_photon_HadPho_mu.open(fileName+"_photon_HadPho_mu.csv");   
    dump_photon_HadFake_mu.open(fileName+"_photon_HadFake_mu.csv");   
    dump_photon_PU_mu.open(fileName+"_photon_PU_mu.csv");   
    
}

void EventPick::close_cutflow_files(){

    //    dump_input_ele.close();
    dump_trigger_ele.close();
    dump_lepton_ele.close();
    dump_oneJet_ele.close();
    dump_twoJet_ele.close();
    dump_threeJet_ele.close();
    dump_fourJet_ele.close();
    dump_btag_ele.close();
    dump_photon_ele.close();
    dump_loosePhoton_ele.close();
    dump_photon_GenPho_ele.close();
    dump_photon_MisIDEle_ele.close();
    dump_photon_HadPho_ele.close();
    dump_photon_HadFake_ele.close();
    dump_photon_PU_ele.close();

    //    dump_input_mu.close();
    dump_trigger_mu.close();
    dump_lepton_mu.close();
    dump_oneJet_mu.close();
    dump_twoJet_mu.close();
    dump_threeJet_mu.close();
    dump_fourJet_mu.close();
    dump_btag_mu.close();
    dump_photon_mu.close();
    dump_loosePhoton_mu.close();
    dump_photon_GenPho_mu.close();
    dump_photon_MisIDEle_mu.close();
    dump_photon_HadPho_mu.close();
    dump_photon_HadFake_mu.close();
    dump_photon_PU_mu.close();
    
}











// void EventPick::clear_vectors(){
// 	Electrons.clear();
// 	ElectronsLoose.clear();
// 	ElectronsMedium.clear();
// 	Muons.clear();
// 	MuonsLoose.clear();
// 	Jets.clear();
// 	bJets.clear();
// 	Photons.clear();
// 	LoosePhotons.clear();
// 	PhotonsPresel.clear();
// 	PhoPassChHadIso.clear();
// 	PhoPassPhoIso.clear();
// 	PhoPassSih.clear();
// }

// double EventPick::dR_jet_ele(int jetInd, int eleInd){
// 	return dR(tree->jetEta_->at(jetInd), tree->jetPhi_->at(jetInd), tree->eleSCEta_->at(eleInd), tree->elePhi_->at(eleInd));
// }
// double EventPick::dR_jet_mu(int jetInd, int muInd){
// 	return dR(tree->jetEta_->at(jetInd), tree->jetPhi_->at(jetInd), tree->muEta_->at(muInd), tree->muPhi_->at(muInd));
// }
// double EventPick::dR_jet_pho(int jetInd, int phoInd){
// 	return dR(tree->jetEta_->at(jetInd), tree->jetPhi_->at(jetInd), tree->phoSCEta_->at(phoInd), tree->phoPhi_->at(phoInd));
// }
// double EventPick::dR_ele_pho(int eleInd, int phoInd){
// 	return dR(tree->eleSCEta_->at(eleInd), tree->elePhi_->at(eleInd), tree->phoSCEta_->at(phoInd), tree->phoPhi_->at(phoInd));
// }
// double EventPick::dR_mu_pho(int muInd, int phoInd){
// 	return dR(tree->muEta_->at(muInd), tree->muPhi_->at(muInd), tree->phoSCEta_->at(phoInd), tree->phoPhi_->at(phoInd));
// }

