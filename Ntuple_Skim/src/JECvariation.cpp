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

	TLorentzVector tMET;
	tMET.SetPtEtaPhiM(tree->MET_pt_,0.0,tree->MET_phi_,0.0);

	for(int jetInd = 0; jetInd < tree->nJet_ ; ++jetInd){
		if(tree->jetPt_[jetInd] < 10) continue;
		if(fabs(tree->jetEta_[jetInd]) > 5.2) continue;
		JetCorrector->setJetEta(tree->jetEta_[jetInd]);
		JetCorrector->setJetPt(tree->jetPt_[jetInd] * (1.-tree->jetRawFactor_[jetInd]));
		JetCorrector->setJetA(tree->jetArea_[jetInd]);
		JetCorrector->setRho(tree->rho_);
		
		double correction = JetCorrector->getCorrection();

		TLorentzVector tjet;
		tjet.SetPtEtaPhiM(tree->jetPt_[jetInd], tree->jetEta_[jetInd], tree->jetPhi_[jetInd], 0.0);
		tMET+=tjet;

		
		jecUnc->setJetEta(tree->jetEta_[jetInd]);
		jecUnc->setJetPt(tree->jetPt_[jetInd]); // here you must use the CORRECTED jet pt

		double unc = jecUnc->getUncertainty(true);
		if(scaleDownNormUp012==0) correction-=unc;
		if(scaleDownNormUp012==2) correction+=unc;
		
		tree->jetPt_[jetInd] = tree->jetPt_[jetInd] * (1.-tree->jetRawFactor_[jetInd]) * correction;
		//tree->jetEn_[jetInd] = tree->jetRawEn_[jetInd] * correction;
		
		tjet.SetPtEtaPhiM(tree->jetPt_[jetInd], tree->jetEta_[jetInd], tree->jetPhi_[jetInd], 0.0);		       
		tMET-=tjet;
		
	}
	tree->MET_pt_ = tMET.Pt();
	tree->MET_phi_ = tMET.Phi();

}

