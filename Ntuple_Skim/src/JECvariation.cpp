#include"../interface/JetCorrectorParameters.h"
#include"../interface/FactorizedJetCorrector.h"
#include"../interface/JetCorrectionUncertainty.h"
#include"../interface/JECvariation.h"
#include<iostream>


JECvariation::JECvariation(std::string inputPrefix, bool isMC, string systematicLevel){
	if( isMC ){
		std::cout << inputPrefix+"_MC_Uncertainty_AK4PFchs.txt" << std::endl;
		jecUnc = new JetCorrectionUncertainty(*(new JetCorrectorParameters((inputPrefix+"_MC_UncertaintySources_AK4PFchs.txt").c_str(),systematicLevel)));
		ResJetPar = new JetCorrectorParameters((inputPrefix+"_MC_L2L3Residual_AK4PFchs.txt").c_str());
		L3JetPar  = new JetCorrectorParameters((inputPrefix+"_MC_L3Absolute_AK4PFchs.txt").c_str());
		L2JetPar  = new JetCorrectorParameters((inputPrefix+"_MC_L2Relative_AK4PFchs.txt").c_str());
		L1JetPar  = new JetCorrectorParameters((inputPrefix+"_MC_L1FastJet_AK4PFchs.txt").c_str());
	}
	else{
		jecUnc = new JetCorrectionUncertainty((inputPrefix+"_DATA_Uncertainty_AK4PFchs.txt").c_str());
		ResJetPar = new JetCorrectorParameters((inputPrefix+"_DATA_L2L3Residual_AK4PFchs.txt").c_str());
		L3JetPar  = new JetCorrectorParameters((inputPrefix+"_DATA_L3Absolute_AK4PFchs.txt").c_str());
		L2JetPar  = new JetCorrectorParameters((inputPrefix+"_DATA_L2Relative_AK4PFchs.txt").c_str());
		L1JetPar  = new JetCorrectorParameters((inputPrefix+"_DATA_L1FastJet_AK4PFchs.txt").c_str());
	}
	std::vector<JetCorrectorParameters> vPar;
	vPar.push_back(*L1JetPar);
	vPar.push_back(*L2JetPar);
	vPar.push_back(*L3JetPar);
	if (!isMC) vPar.push_back(*ResJetPar);
	JetCorrector = new FactorizedJetCorrector(vPar);
}

JECvariation::~JECvariation(){

}


void JECvariation::applyJEC(EventTree* tree, int scaleDownNormUp012){
	//	if(scaleDownNormUp012 == 1) return;
	//bool JECapplied false; 

	TLorentzVector tMET;
	tMET.SetPtEtaPhiM(tree->MET_pt_,0.0,tree->MET_phi_,0.0);

	//	double before = tree->jetPt_->at(0);

	for(int jetInd = 0; jetInd < tree->nJet_ ; ++jetInd){
		if(tree->jetPt_[jetInd] < 10) continue;
		if(fabs(tree->jetEta_[jetInd]) > 5.2) continue;
		JetCorrector->setJetEta(tree->jetEta_[jetInd]);
		JetCorrector->setJetPt(tree->jetPt_[jetInd] / tree->jetRawFactor_[jetInd]);
		JetCorrector->setJetA(tree->jetArea_[jetInd]);
		JetCorrector->setRho(tree->rho_);
		
		double correction = JetCorrector->getCorrection();
		// std::cout << scaleDownNormUp012 << std::endl;
		// std::cout << tree->jetPt_[jetInd] << "  " << tree->jetRawPt_[jetInd] << "  " << tree->jetPt_[jetInd]/tree->jetRawPt_[jetInd] << "  " << correction << std::endl;
		// assume jets are corrected, no need to change unless we want Up Down variation
		//tree->jetPt_[jetInd] = tree->jetRawPt_[jetInd] * correction;
		//tree->jetEn_[jetInd] = tree->jetRawEn_[jetInd] * correction;


		TLorentzVector tjet;
		tjet.SetPtEtaPhiM(tree->jetPt_[jetInd], tree->jetEta_[jetInd], tree->jetPhi_[jetInd], 0.0);
		tMET+=tjet;

		
		jecUnc->setJetEta(tree->jetEta_[jetInd]);
		jecUnc->setJetPt(tree->jetPt_[jetInd]); // here you must use the CORRECTED jet pt

		//		std::cout << jetInd << "  " << tree->jetPt_[jetInd] << "  " << tree->jetEta_[jetInd] << std::endl;
		double unc = jecUnc->getUncertainty(true);
		//std::cout << "unc " << unc << std::endl;
		if(scaleDownNormUp012==0) correction-=unc;
		//		if(scaleDownNormUp012==1) continue;
		if(scaleDownNormUp012==2) correction+=unc;
		
		tree->jetPt_[jetInd] = tree->jetPt_[jetInd] / tree->jetRawFactor_[jetInd] * correction;
		//tree->jetEn_[jetInd] = tree->jetRawEn_[jetInd] * correction;
		
		tjet.SetPtEtaPhiM(tree->jetPt_[jetInd], tree->jetEta_[jetInd], tree->jetPhi_[jetInd], 0.0);		       
		tMET-=tjet;
		
	}
	tree->MET_pt_ = tMET.Pt();
	tree->MET_phi_ = tMET.Phi();

	// double after = tree->jetPt_->at(0);
	// std::cout << before << " " << after << std::endl;
}

