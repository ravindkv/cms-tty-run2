#include"../interface/EventPick.h"
#include <iostream> 
#include <iomanip>


//double secondMinDr(int myInd, const EventTree* tree);

EventPick_gen::EventPick_gen(std::string titleIn){
	title = titleIn;
	saveCutflows = true;

	cutFlow_ele = new TH1D("cut_flow_ele","cut flow e+jets",15,-0.5,14.5);
	cutFlow_ele->SetDirectory(0);
	set_cutflow_labels_ele(cutFlow_ele); 

	cutFlow_mu = new TH1D("cut_flow_mu","cut flow mu+jets",15,-0.5,14.5);
	cutFlow_mu->SetDirectory(0);
	set_cutflow_labels_mu(cutFlow_mu); 
	
	cutFlowWeight_ele = new TH1D("cut_flow_weight_ele","cut flow with PU weight e+jets",15,-0.5,14.5);
	cutFlowWeight_ele->SetDirectory(0);
	set_cutflow_labels_ele(cutFlowWeight_ele);

	cutFlowWeight_mu = new TH1D("cut_flow_weight_mu","cut flow with PU weight mu+jets",15,-0.5,14.5);
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
	MET_cut = 0.0;
	no_trigger = false;
	
	skimEle = false;
	skimMu = false;

	Njet_ge = 4;
	SkimNjet_ge = 1;

	NBjet_ge = 1;
	SkimNBjet_ge = 1;
	Nlep_eq = 1;

	ZeroBExclusive = false;

	NlooseMuVeto_le = 0;
	NlooseEleVeto_le = 0;

}

EventPick_gen::~EventPick_gen(){
}

void EventPick_gen::process_event(EventTree* tree, Selector_gen* selector_gen, double weight){

	//	clear_vectors();
	passSkim = false;
	passPresel_ele = false;
	passPresel_mu = false;
	passAll_ele = false;
	passAll_mu = false;


	bool Pass_trigger_mu  = ( tree->HLTEleMuX >> 19 & 1 || tree->HLTEleMuX >> 20 & 1) || no_trigger;
	bool Pass_trigger_ele = ( tree->HLTEleMuX >> 3 & 1) || no_trigger;

	if (saveCutflows) {
		cutFlow_ele->Fill(0.0); // Input events
		cutFlow_mu->Fill(0.0); // Input events
		cutFlowWeight_ele->Fill(0.0,weight);
		cutFlowWeight_mu->Fill(0.0,weight);
	}


	passPresel_mu  = true;
	passPresel_ele = true;
	//	cout << "-------" << endl;
	// Cut events that fail ele trigger
//	if( passPresel_mu &&  Pass_trigger_mu) { if (saveCutflows) {cutFlow_mu->Fill(1); cutFlowWeight_mu->Fill(1,weight); } }
//	else { passPresel_mu = false;}
//	if( passPresel_mu && tree->isPVGood_) { if (saveCutflows) {cutFlow_mu->Fill(2); cutFlowWeight_mu->Fill(2,weight); } }
//	else { passPresel_mu = false;}

	// Cut events that fail ele trigger
//	if( passPresel_ele &&  Pass_trigger_ele) { if (saveCutflows) {cutFlow_ele->Fill(1); cutFlowWeight_ele->Fill(1,weight);}}
//	else { passPresel_ele = false;}
//	if( passPresel_ele && tree->isPVGood_) { if (saveCutflows) {cutFlow_ele->Fill(2); cutFlowWeight_ele->Fill(2,weight);} }
//	else { passPresel_ele = false; }


	if ( passPresel_ele || passPresel_mu ) {
        selector_gen->process_objects(tree);
	}
	else {
		return;
	}


	// Cut on events with ==1 muon, no loose muons, no loose or tight electrons
	if( passPresel_mu && selector_gen->Muons.size() == Nmu_eq){
		if (Nmu_eq==2) { 
			int mu1 = selector_gen->Muons.at(0); 
			int mu2 = selector_gen->Muons.at(1);
			if(tree->muCharge_->at(mu1)*tree->muCharge_->at(mu2) ==1){
				passPresel_mu = false;
			}
		}
		if (saveCutflows){cutFlow_mu->Fill(3); cutFlowWeight_mu->Fill(3,weight); } 
	}
	else { passPresel_mu = false;}

	if( passPresel_mu && selector_gen->MuonsLoose.size() <=  NlooseMuVeto_le ) { if (saveCutflows) {cutFlow_mu->Fill(4); cutFlowWeight_mu->Fill(4,weight); } }
	else { passPresel_mu = false;}
	if( passPresel_mu && (selector_gen->ElectronsLoose.size() + selector_gen->Electrons.size() ) <=  NlooseEleVeto_le ) {if (saveCutflows) {cutFlow_mu->Fill(5); cutFlowWeight_mu->Fill(5,weight);} }
	else { passPresel_mu = false;}


	// Cut on events with ==1 muon, no loose muons, no loose or tight electrons
	if( passPresel_ele && selector_gen->Electrons.size() == Nele_eq) { 
		if (Nele_eq==2) {
                        int ele1 = selector_gen->Electrons.at(0);
                        int ele2 = selector_gen->Electrons.at(1);
                        if((tree->eleCharge_->at(ele1))*(tree->eleCharge_->at(ele2)) == 1){
                                passPresel_ele = false;
                        }
                }
		
		if (saveCutflows) {cutFlow_ele->Fill(3); cutFlowWeight_ele->Fill(3,weight);}
	}
	else { passPresel_ele = false;}
	if( passPresel_ele && selector_gen->ElectronsLoose.size() <=  NlooseEleVeto_le ) { if (saveCutflows) {cutFlow_ele->Fill(4); cutFlowWeight_ele->Fill(4,weight);}}
	else { passPresel_ele = false;}
	if( passPresel_ele && (selector_gen->MuonsLoose.size() + selector_gen->Muons.size() ) <=  NlooseMuVeto_le ) { if (saveCutflows) {cutFlow_ele->Fill(5); cutFlowWeight_ele->Fill(5,weight);}}
	else { passPresel_ele = false;}

	// split skim into ele and mu
	if ( (skimEle && passPresel_ele) || (skimMu && passPresel_mu) && selector_gen->Jets.size() >= SkimNjet_ge && selector_gen->bJets.size() >= SkimNBjet_ge ){ passSkim = true; }

	// NJet cuts for electrons
	// Implemented in this way (with a loop) to check for numbers failing each level of cut < Njet cut, and filling cutflow histo
	// cutflow histo will not be filled for bins where the cut is > Njet_ge (ex, if cut is at 3, Njets>=4 bin is left empty)
	for (int ijetCut = 1; ijetCut <= Njet_ge; ijetCut++){
		if(passPresel_ele && selector_gen->Jets.size() >= ijetCut ) { if (saveCutflows) {cutFlow_ele->Fill(5+ijetCut); cutFlowWeight_ele->Fill(5+ijetCut,weight);}}
		else passPresel_ele = false;
	}

	// Nbtag cuts for electrons
	if (!ZeroBExclusive){
		for (int ibjetCut = 1; ibjetCut <= NBjet_ge; ibjetCut++){
			if(passPresel_ele && selector_gen->bJets.size() >= ibjetCut ) { if (saveCutflows) {cutFlow_ele->Fill(9+ibjetCut); cutFlowWeight_ele->Fill(9+ibjetCut,weight);}}
			else passPresel_ele = false;
		}
	} else {
		if(passPresel_ele && selector_gen->bJets.size() !=0) passPresel_ele = false;
	}



	// MET cut for electrons
//	if(passPresel_ele && tree->pfMET_ >= MET_cut) { if (saveCutflows) {cutFlow_ele->Fill(13); cutFlowWeight_ele->Fill(13,weight);}}
//	else passPresel_ele = false;

	// NJet cuts for muons
	// Implemented in this way (with a loop) to check for numbers failing each level of cut < Njet cut, and filling cutflow histo
	// cutflow histo will not be filled for bins where the cut is > Njet_ge (ex, if cut is at 3, Njet>=4 bin is left empty)
	for (int ijetCut = 1; ijetCut <= Njet_ge; ijetCut++){
		if(passPresel_mu && selector_gen->Jets.size() >= ijetCut ) { if (saveCutflows) {cutFlow_mu->Fill(5+ijetCut); cutFlowWeight_mu->Fill(5+ijetCut,weight);}}
		else passPresel_mu = false;
	}

	// Nbtag cuts for muons
	if (!ZeroBExclusive){
		for (int ibjetCut = 1; ibjetCut <= NBjet_ge; ibjetCut++){
			if(passPresel_mu && selector_gen->bJets.size() >= ibjetCut ) { if (saveCutflows) {cutFlow_mu->Fill(9+ibjetCut); cutFlowWeight_mu->Fill(9+ibjetCut,weight);}}
			else passPresel_mu = false;
		}
	} else {
		if(passPresel_mu && selector_gen->bJets.size() !=0) passPresel_mu = false;
	}


	// MET cut for muons
//	if(passPresel_mu && tree->pfMET_ >= MET_cut) { if (saveCutflows) {cutFlow_mu->Fill(13); cutFlowWeight_mu->Fill(13,weight);}}
//	else passPresel_mu = false;

}

void EventPick_gen::print_cutflow_mu(TH1D* _cutflow){
	std::cout << "Cut-Flow for the event selector_gen: " << title << std::endl;
	std::cout << "Input Events :                " << _cutflow->GetBinContent(1) << std::endl;
//	std::cout << "Passing Trigger               " << _cutflow->GetBinContent(2) << std::endl;
//	std::cout << "Has Good Vtx               " << _cutflow->GetBinContent(3) << std::endl;
	std::cout << "Events with 1 muon     " << _cutflow->GetBinContent(4) << std::endl;
	std::cout << "Events with no loose muons " << _cutflow->GetBinContent(5) << std::endl;
	std::cout << "Events with no electrons " << _cutflow->GetBinContent(6) << std::endl;
	std::cout << "Events with >= " << 1 << " jets        " << _cutflow->GetBinContent(7) << std::endl;
	std::cout << "Events with >= " << 2 << " jets        " << _cutflow->GetBinContent(8) << std::endl;
 	std::cout << "Events with >= " << 3 << " jets     " << _cutflow->GetBinContent(9) << std::endl;
	std::cout << "Events with >= " << 4 << " jets "<< _cutflow->GetBinContent(10) << std::endl;
	std::cout << "Events with >= " << 1 <<     " bjets "<< _cutflow->GetBinContent(11) << std::endl;
//	std::cout << "Events with >= " << 2 << " bjets       " << _cutflow->GetBinContent(12) << std::endl;
//	std::cout << "Events passing MET cut       " << _cutflow->GetBinContent(1) << std::endl;
	std::cout << std::endl;
}

void EventPick_gen::print_cutflow_ele(TH1D* _cutflow){
	std::cout << "Cut-Flow for the event selector_gen: " << title << std::endl;
//	std::cout << "Input Events :                " << _cutflow->GetBinContent(1) << std::endl;
//	std::cout << "Passing Trigger               " << _cutflow->GetBinContent(2) << std::endl;
	std::cout << "Has Good Vtx               " << _cutflow->GetBinContent(3) << std::endl;
	std::cout << "Events with 1 electron     " << _cutflow->GetBinContent(4) << std::endl;
	std::cout << "Events with no loose electrons " << _cutflow->GetBinContent(5) << std::endl;
	std::cout << "Events with no muons " << _cutflow->GetBinContent(6) << std::endl;
	std::cout << "Events with >= " << 1 << " jets        " << _cutflow->GetBinContent(7) << std::endl;
	std::cout << "Events with >= " << 2 << " jets        " << _cutflow->GetBinContent(8) << std::endl;
 	std::cout << "Events with >= " << 3 << " jets     " << _cutflow->GetBinContent(9) << std::endl;
	std::cout << "Events with >= " << 4 << " jets "<< _cutflow->GetBinContent(10) << std::endl;
	std::cout << "Events with >= " << 1 <<     " bjets "<< _cutflow->GetBinContent(11) << std::endl;
//	std::cout << "Events with >= " << 2 << " bjets       " << _cutflow->GetBinContent(12) << std::endl;
//	std::cout << "Events passing MET cut       " << _cutflow->GetBinContent(14) << std::endl;
	std::cout << std::endl;
}

void EventPick_gen::set_cutflow_labels_mu(TH1D* hist){
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
//	hist->GetXaxis()->SetBinLabel(12,">=2 b-tags");
//	hist->GetXaxis()->SetBinLabel(13,"MET Cut");
}

void EventPick_gen::set_cutflow_labels_ele(TH1D* hist){
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
//	hist->GetXaxis()->SetBinLabel(12,">=2 b-tags");
//	hist->GetXaxis()->SetBinLabel(13,"MET Cut");
}


