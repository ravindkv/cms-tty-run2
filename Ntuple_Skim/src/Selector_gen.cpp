#include"../interface/Selector.h"
#include"TRandom3.h"

double dR(double eta1, double phi1, double eta2, double phi2){
	double dphi = phi2 - phi1;
	double deta = eta2 - eta1;
	static const double pi = TMath::Pi();
	dphi = TMath::Abs( TMath::Abs(dphi) - pi ) - pi;
	return TMath::Sqrt( dphi*dphi + deta*deta );
}
TRandom* generator = new TRandom3(0);
Selector_gen::Selector_gen(){
	// jets
	jet_Pt_cut = 30;
	jet_Eta_cut = 2.4;

//	looseJetID = true;
	veto_lep_jet_dR = 0.4; // remove jets with a lepton closer than this cut level
	useDeepCSVbTag = false;
	//https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
	// CSVv2M
	btag_cut = 0.8484;  
	// DeepCSV
	btag_cut_DeepCSV = 0.6324;  


	// whether to invert lepton requirements for 

	// electrons
	ele_Pt_cut = 35.0;
	ele_Eta_cut = 2.1;
	ele_PtLoose_cut = 15.0;
	ele_EtaLoose_cut = 2.5;

	// muons
	mu_Pt_cut = 30;
	mu_Eta_tight = 2.4;
	mu_RelIso_tight = 0.15;

	mu_PtLoose_cut = 15.0;
	mu_Eta_loose = 2.4;
	mu_RelIso_loose = 0.25;
	
	mu_Iso_invert = false;
	//smearJetPt = true;
}

void Selector_gen::process_objects(EventTree* inp_tree){
	tree = inp_tree;

	clear_vectors();
		//cout << "before selector muons" << endl;
	filter_muons();

		//cout << "before selector electrons" << endl;
 	filter_electrons();

		//cout << "before selector jets" << endl;
	filter_jets();
}

void Selector_gen::clear_vectors(){
	Electrons.clear();
	ElectronsLoose.clear();
	ElectronsMedium.clear();
	Muons.clear();
	MuonsLoose.clear();
	Jets.clear();
	bJets.clear();
	
	MuRelIso_corr.clear();
}

void Selector_gen::filter_electrons(){
	for(int eleInd = 0; eleInd < tree->nMC_; ++eleInd){
		if  (TMath::Abs(tree->mcPID->at(eleInd))==11){
		double eta = tree->mcEta->at(eleInd);
		double absEta = TMath::Abs(eta);
		double pt = tree->mcPt->at(eleInd);
               // double en = tree->mcE->at(eleInd);
		bool passEtaEBEEGap = (absEta < 1.4442) || (absEta > 1.566);
	   
		bool eleSel =  (passEtaEBEEGap &&
                               absEta < ele_Eta_cut &&
			       pt > ele_Pt_cut); 


		if( eleSel ){
			Electrons.push_back(eleInd);
		    }
		}
	}
}





void Selector_gen::filter_muons(){
	for(int muInd = 0; muInd < tree->nMC_; ++muInd){
		if  (TMath::Abs(tree->mcPID->at(muInd))==13){
		double eta = tree->mcEta->at(muInd);
		double pt = tree->mcPt->at(muInd);



		bool passTight = (pt > mu_Pt_cut &&
						  TMath::Abs(eta) < mu_Eta_tight);
						  


		if (passTight){
		 	Muons.push_back(muInd);
		}
	    }
	}
}


void Selector_gen::filter_jets(){
        //std::cout<<"doing gen AK4 jets:"<<tree->jetGenJetPt_->size()<<std::endl;	
	for(int jetInd = 0; jetInd < tree->jetGenJetPt_->size(); ++jetInd){
		//std::cout<<"AK4 jet:"<<jetInd<<",jet Pt:"<<tree->jetGenJetPt_->at(jetInd)<<std::endl;
		double pt = tree->jetGenJetPt_->at(jetInd);
		double eta = tree->jetGenJetEta_->at(jetInd);
		double phi = tree->jetGenJetPhi_->at(jetInd);
		bool passDR_lep_jet = true;

		//loop over selected electrons
		for(std::vector<int>::const_iterator eleInd = Electrons.begin(); eleInd != Electrons.end(); eleInd++) {
			if (dR(eta, phi, tree->mcEta->at(*eleInd), tree->mcPhi->at(*eleInd)) < veto_lep_jet_dR) passDR_lep_jet = false;
		}

		//loop over selected muons
		for(std::vector<int>::const_iterator muInd = Muons.begin(); muInd != Muons.end(); muInd++) {
			if (dR(eta, phi, tree->mcEta->at(*muInd), tree->mcPhi->at(*muInd)) < veto_lep_jet_dR) passDR_lep_jet = false;
		}

		bool jetPresel = (pt > jet_Pt_cut &&
						  TMath::Abs(eta) < jet_Eta_cut &&
						  passDR_lep_jet
						  );

		if( jetPresel){
			Jets.push_back(jetInd);
			if (!useDeepCSVbTag){
				if(tree->jetCSV2BJetTags_->at(jetInd) > btag_cut) bJets.push_back(jetInd);
			} else {
				if( (tree->jetDeepCSVTags_b_->at(jetInd) + tree->jetDeepCSVTags_bb_->at(jetInd) ) > btag_cut_DeepCSV) bJets.push_back(jetInd);
			}				
		}

	}
}

// Currently, these are the listed values for the SPRING16 MC samples, need to verify that they are what should be used from SUMMER16 as well
Selector_gen::~Selector_gen(){
}
