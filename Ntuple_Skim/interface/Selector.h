#ifndef SELECTOR_H
#define SELECTOR_H

#include<vector>
#include<iostream>
#include <iomanip>
#include<algorithm>
#include<TH1F.h>
#include<TMath.h>
#include<TLorentzVector.h>
#include"EventTree.h"
#include "ParsePhotonID.h"

#include "Utils.h"

#include "JetResolution.h"
//#include "JERScaleFactors.h"


#include"TRandom3.h"
#include <bitset>

#include"JetResolution.h"
#include"JetResolutionObject.h"
//#include"JERScaleFactors.h"

#include <random>


// https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedPhotonID2012
// photon ID is not going to be changed every time this code runs
// barrel/endcap, Loose/Medium/Tight
const int    photonID_IsConv[2][3]                = { {0, 0, 0} ,             {0, 0, 0}             };
const double photonID_HoverE[2][3]                = { {0.05, 0.05, 0.05} ,    {0.05, 0.05, 0.05}    };
const double photonID_SigmaIEtaIEta[2][3]         = { {0.012, 0.011, 0.011} , {0.034, 0.033, 0.031} };
const double photonID_RhoCorrR03ChHadIso[2][3]    = { {2.6, 1.5, 0.7} ,       {2.3, 1.2, 0.5}       };
const double photonID_RhoCorrR03NeuHadIso_0[2][3] = { {3.5, 1.0, 0.4} ,       {2.9, 1.5, 1.5}       };
const double photonID_RhoCorrR03NeuHadIso_1[2][3] = { {0.04, 0.04, 0.04} ,    {0.04, 0.04, 0.04}    };
const double photonID_RhoCorrR03PhoIso_0[2][3]    = { {1.3, 0.7, 0.5} ,       {999, 1.0, 1.0}       };
const double photonID_RhoCorrR03PhoIso_1[2][3]    = { {0.005, 0.005, 0.005} , {0.005, 0.005, 0.005} };

// Effective areas for photon rho correction
// First index is the egammaRegion (from above) second is whether it isChHad, NeuHad, or Pho 
///                                   chhadEA, nhadEA, photEA
///https://indico.cern.ch/event/491548/contributions/2384977/attachments/1377936/2117789/CutBasedPhotonID_25-11-2016.pdf
static const double photonEA[7][3] = {{0.0360, 0.0597, 0.1210},
									  {0.0377, 0.0807, 0.1107},
									  {0.0306, 0.0629, 0.0699},
									  {0.0283, 0.0197, 0.1056},
									  {0.0254, 0.0184, 0.1457},
									  {0.0217, 0.0284, 0.1719},
									  {0.0167, 0.0591, 0.1998}};

//https://indico.cern.ch/event/482673/contributions/2187022/attachments/1282446/1905912/talk_electron_ID_spring16.pdf
static const double electronEA[7] = {0.1703,
									 0.1715,
									 0.1213,
									 0.1230,
									 0.1635,
									 0.1937,
									 0.2393};



//double dR(double eta1, double phi1, double eta2, double phi2);

class Selector{
public:
	Selector();
	~Selector();
	
	void process_objects(EventTree* inp_tree);
	
	std::vector<int> Photons;
	std::vector<bool> PhoPassChHadIso;
	std::vector<bool> PhoPassPhoIso;
	std::vector<bool> PhoPassSih;
	std::vector<int> LoosePhotons;
	std::vector<int> PhotonsNoID;
	std::vector<int> Electrons;
	std::vector<int> ElectronsLoose;
	std::vector<int> ElectronsMedium;
	std::vector<int> ElectronsNoIso;
	std::vector<int> Muons;
	std::vector<int> MuonsLoose;
	std::vector<int> MuonsNoIso;
	std::vector<int> Jets;
	std::vector<int> bJets;
        std::vector<int> FwdJets;

	std::vector<double> jet_resolution;
	std::vector<bool>   jet_isTagged;
	
	std::vector<double> MuRelIso_corr;

	std::vector<double> PhoChHadIso_corr;
	std::vector<double> PhoNeuHadIso_corr;
	std::vector<double> PhoPhoIso_corr;
	std::vector<std::vector<float>> PhoRandConeChHadIso_corr;

	double jet_Pt_cut;
	double jet_Eta_cut;
	double btag_cut;
	double btag_cut_DeepCSV;
	double veto_lep_jet_dR;
	double veto_pho_jet_dR;
	double veto_lep_pho_dR;
	double veto_jet_pho_dR;
	int JERsystLevel; //0= syst down, 1 = central, 2 = syst up
	int JECsystLevel;//0= syst down, 1 = central, 2 = syst up
	int phosmearLevel;
	int elesmearLevel;
	int phoscaleLevel;
	int elescaleLevel;
	bool   smearJetPt;
	bool scaleEle;
	bool smearEle;
	bool scalePho;
	bool smearPho;
	bool   looseJetID;
	bool   useDeepCSVbTag;
	bool   QCDselect;

	// electrons
	double ele_Pt_cut;
	double ele_PtLoose_cut;
	double ele_Eta_cut;
	double ele_EtaLoose_cut;
	double mu_Eta_loose;
	double mu_Eta_tight;
	double mu_Pt_cut;
	double mu_RelIso_tight;
	double mu_RelIso_loose;
	double ele_Ptmedium_cut;
	double ele_RelIso_range[2];
	double ele_RelIsoLoose_cut;
	double ele_MVA_range[2];
	double ele_cutbased_range[2];
	double ele_MVALoose_cut;
	double ele_Dxy_cut;
	int    ele_MissInnHit_cut;
	bool   ele_Iso_MVA_invert;
	
	// photons
	double pho_Et_cut;
	double pho_Eta_cut;
	int    pho_ID_ind; // 0 - Loose, 1 - Medium, 2 - Tight
	bool   pho_noPixelSeed_cut;
	bool   pho_noEleVeto_cut;
	bool   pho_applyPhoID;

	// muons
	double mu_PtLoose_cut;
	double mu_RelIsoLoose_cut;
	double mu_RelIso_range[2];
 	double mu_MVA_range[2];
	bool   mu_Iso_invert;

	std::string year;

	int printEvent;

	void clear_vectors();
	
	void init_JER(std::string inputPrefix);


private:
	EventTree* tree;
	void filter_photons();
	void filter_electrons();
	void filter_muons();
	void filter_jets();
	void filter_photons_jetsDR();

	/* double JER(int jetInd); */
	
	// effective areas, see Selector.cpp for more information
	double eleEffArea03(double SCEta);
	double muEffArea04(double muEta);
	double phoEffArea03ChHad(double phoSCEta);
	double phoEffArea03NeuHad(double phoSCEta);
	double phoEffArea03Pho(double phoSCEta);
	int egammaRegion(double absEta);

	bool passEleID(int eleInd, int cutVal, bool doRelisoCut);
	//	bool passEleVetoID(int eleInd, bool doRelisoCut);
	//	bool passPhoMediumID(int phoInd);
	bool passPhoMediumID(int phoInd, bool cutHoverE, bool cutSIEIE, bool cutIso);

	JME::JetResolution *jetResolution;
	JME::JetResolutionScaleFactor *jetResolutionScaleFactor;
	JME::JetParameters jetParam;

};

class Selector_gen{
public:
        Selector_gen();
        ~Selector_gen();

        void process_objects(EventTree* inp_tree);

        std::vector<int> Photons;
        std::vector<bool> PhoPassChHadIso;
        std::vector<bool> PhoPassPhoIso;
        std::vector<bool> PhoPassSih;
        std::vector<int> LoosePhotons;
        std::vector<int> PhotonsNoID;
        std::vector<int> Electrons;
        std::vector<int> ElectronsLoose;
        std::vector<int> ElectronsMedium;
        std::vector<int> ElectronsNoIso;
        std::vector<int> Muons;
        std::vector<int> MuonsLoose;
        std::vector<int> MuonsNoIso;
        std::vector<int> Jets;
        std::vector<int> bJets;
        std::vector<int> FwdJets;

        std::vector<double> MuRelIso_corr;

        std::vector<double> PhoChHadIso_corr;
        std::vector<double> PhoNeuHadIso_corr;
        std::vector<double> PhoPhoIso_corr;
        std::vector<std::vector<float>> PhoRandConeChHadIso_corr;

        double jet_Pt_cut;
        double jet_Eta_cut;
        double btag_cut;
        double btag_cut_DeepCSV;
        bool   useDeepCSVbTag;
        double veto_lep_jet_dR;
        double veto_pho_jet_dR;
        double veto_lep_pho_dR;
        double veto_jet_pho_dR;
	double ele_Pt_cut;
        double ele_PtLoose_cut;
        double ele_Eta_cut;
        double ele_EtaLoose_cut;
        double mu_Eta_loose;
        double mu_Eta_tight;
        double mu_Pt_cut;
        double mu_RelIso_tight;
        double mu_RelIso_loose;
        double ele_Ptmedium_cut;
        double ele_RelIso_range[2];
        double ele_RelIsoLoose_cut;
        double ele_MVA_range[2];
        double ele_cutbased_range[2];
        double ele_MVALoose_cut;
        double ele_Dxy_cut;
        int    ele_MissInnHit_cut;
        bool   ele_Iso_MVA_invert;

	double pho_Et_cut;
        double pho_Eta_cut;
	double mu_PtLoose_cut;
        double mu_RelIsoLoose_cut;
        double mu_RelIso_range[2];
        double mu_MVA_range[2];
        bool   mu_Iso_invert;

        void clear_vectors();
	EventTree* tree;
        void filter_photons();
        void filter_electrons();
        void filter_muons();
        void filter_jets();
        void filter_photons_jetsDR();
	 double eleEffArea03(double SCEta);
        double muEffArea04(double muEta);
        double phoEffArea03ChHad(double phoSCEta);
        double phoEffArea03NeuHad(double phoSCEta);
        double phoEffArea03Pho(double phoSCEta);
        int egammaRegion(double absEta);

        bool passEleTightID(int eleInd, bool doRelisoCut);
        bool passEleVetoID(int eleInd, bool doRelisoCut);
        bool passPhoMediumID(int phoInd);
        bool passPhoMediumID(int phoInd, bool cutHoverE, bool cutSIEIE, bool cutIso);
};
       
#endif
