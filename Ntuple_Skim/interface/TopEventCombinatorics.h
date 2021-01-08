#ifndef TopEventCombinatorics_h
#define TopEventCombinatorics_h


#include "TLorentzVector.h"
#include "METzCalculator.h"
#include "TMath.h"
#include <vector>

class TopEventCombinatorics{

 public:

    TopEventCombinatorics(){
	ClearVectors();
	mTop = 172.5;
	mW = 80.4;
	chi2 = 9999.;
	goodCombo = false;
	METRes = 0.2;
	leptonRes = 0.05;
	useResolutions = true;
	nBjetSize = 2;
	btagThresh = 0.;
	bhad_idx = 0;
	blep_idx = 0;
	j1_idx = 0;
	j2_idx = 0;
    }
	
    void SetMtop(double mTop_){ mTop = mTop_;}
    void SetMW(double mW_){ mW = mW_;}

    void SetJetVector(std::vector<TLorentzVector> jets_){ jets = jets_;}
    void SetJetResVector(std::vector<double> jetres_){ jetsRes = jetres_;}
    void SetBtagVector(std::vector<double> jetsTag_){ btag = jetsTag_;}

    void SetLepton(TLorentzVector lepton_){ lepton = lepton_; metZ.SetLepton(lepton_);}
    void SetMET(TLorentzVector met_){ met = met_; metZ.SetMET(met_);}

    void SetMETerror(double err){ METRes = err;}
    void SetLeperror(double err){ leptonRes = err;}

    void SetBJetsSize(int _nB){ nBjetSize = _nB;}
    void SetBtagThresh(double thresh){ btagThresh = thresh;}

    void SetUseResolutions(bool useRes_){ useResolutions = useRes_;}
		
    unsigned int getBHad(){ return bhad_idx; }
    unsigned int getBLep(){ return blep_idx; }
    unsigned int getJ1(){ return j1_idx; }
    unsigned int getJ2(){ return j2_idx; }
    double getNuPz(){ return nu_pz; }
	
    double getChi2(){ return chi2; }

    bool GoodCombination(){ return goodCombo; }

    void ClearVectors(){
	jets.clear();
    }
    int Calculate();



 private:
    double mTop;
    double mW;
    double chi2;

    double topChiSq(TLorentzVector j1, double sigma_j1,
		    TLorentzVector j2, double sigma_j2,
		    TLorentzVector bh, double sigma_bh,
		    TLorentzVector bl, double sigma_bl,
		    double nu_pz_hypo);

    std::vector<TLorentzVector> jets;
    std::vector<double> jetsRes;
    std::vector<double> btag;

    TLorentzVector lepton;
    double leptonRes;

    TLorentzVector met;
    double METRes;
 
    std::vector<int> bJetsList;
    std::vector<double> nu_pz_List;

    int nBjetSize;

    std::vector<TLorentzVector> tempJetVector;
    std::vector<double> tempJetResVector;


    TLorentzVector bhad;
    TLorentzVector blep;
    TLorentzVector j1;
    TLorentzVector j2;

    int bhad_idx;
    int blep_idx;
    int j1_idx;
    int j2_idx;
    int nu_pz;
	
    bool goodCombo;

    bool useResolutions;

    double btagThresh;

    METzCalculator metZ;

};

#endif
