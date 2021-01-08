#include "../interface/TopEventCombinatorics.h"
#include "TLorentzVector.h"
#include <iostream>

double TopEventCombinatorics::topChiSq(TLorentzVector j1, double sigma_j1,
				       TLorentzVector j2, double sigma_j2,
				       TLorentzVector bh, double sigma_bh,
				       TLorentzVector bl, double sigma_bl,
				       double nu_pz_hypo){

    met.SetPz(nu_pz_hypo);

    double sigma2_tHad = sigma_j1*sigma_j1 + sigma_j2*sigma_j2 + sigma_bh*sigma_bh;
    double sigma2_WHad = sigma_j1*sigma_j1 + sigma_j2*sigma_j2;
    double sigma2_tLep = sigma_bl*sigma_bl + pow(met.Pt()*METRes,2) + pow(lepton.Pt()*leptonRes,2);

    if (!useResolutions){
	sigma2_tHad = 1.;
	sigma2_WHad = 1.;
	sigma2_tLep = 1.;
    }
    double c = pow( (bh + j1 + j2).M() - mTop,2)/sigma2_tHad + pow( (j1 + j2).M() - mW,2)/sigma2_WHad + pow( (bl + lepton + met).M() - mTop,2)/sigma2_tLep;

}

int TopEventCombinatorics::Calculate(){

    goodCombo = false;

    if (jets.size() < 4){
	return -1;
    }

    bJetsList.clear();
    nu_pz_List.clear();

    if (nBjetSize==-1){
	for (unsigned int i =0; i < jets.size(); i++) bJetsList.push_back(i);
    } else {
	for (unsigned int i =0; i < jets.size(); i++){
	    if (btag[i] > btagThresh) bJetsList.push_back(i);
	}
	if (bJetsList.size() < nBjetSize){
	    for (unsigned int i =0; i < jets.size(); i++){
		if (std::find(bJetsList.begin(), bJetsList.end(), i) == bJetsList.end()){
		    bJetsList.push_back(i);
		}
		if (bJetsList.size()==nBjetSize) break;
	    }
	}
    }

    double _nu_pz_1 = metZ.Calculate();
    double _nu_pz_2 = metZ.getOther();

    nu_pz_List.push_back(_nu_pz_1);
    if (_nu_pz_1!=_nu_pz_2) nu_pz_List.push_back(_nu_pz_2);

    chi2 = 9.e9;
    double comboChi2 = 9.e9;

    for (const auto& i_bhad : bJetsList){
	for (const auto& i_blep : bJetsList){
	    if (i_bhad==i_blep) continue;
	    for (unsigned int i_j1=0; i_j1<jets.size(); i_j1++){
		if (i_bhad==i_j1 || i_blep==i_j1) continue; //skip if i_j1 is already used as a bjet
		for (unsigned int i_j2=i_j1+1; i_j2<jets.size(); i_j2++){
		    if (i_bhad==i_j2 || i_blep==i_j2) continue; //skip if i_j2 is already used as a bjet

		    //loop over nu_pz solutions
		    for (const auto& test_nu_pz: nu_pz_List){

			double comboChi2 = topChiSq(jets.at(i_j1), jetsRes.at(i_j1),
						    jets.at(i_j2), jetsRes.at(i_j2),
						    jets.at(i_bhad), jetsRes.at(i_bhad),
						    jets.at(i_blep), jetsRes.at(i_blep),
						    test_nu_pz);
			if (comboChi2 < chi2){
			    chi2 = comboChi2;
			    blep_idx = i_blep;
			    bhad_idx = i_bhad;
			    j1_idx = i_j1;
			    j2_idx = i_j2;
			    nu_pz = test_nu_pz;
			    goodCombo = true;
			}
		    }
		}
	    }
	}
    }

    return 0;
}

