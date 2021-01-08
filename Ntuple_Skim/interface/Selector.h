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

#include "Utils.h"

#include "../interface/JetResolution.h"
//#include "interface/JERScaleFactors.h"


#include"TRandom3.h"
#include <bitset>

#include"../interface/JetResolution.h"
#include"../interface/JetResolutionObject.h"
//#include"interface/JERScaleFactors.h"

#include <random>


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


	double jet_Pt_cut;
	double jet_Eta_cut;
	double btag_cut;
	double btag_cut_DeepCSV;
	double veto_lep_jet_dR;
	int JERsystLevel; //0= syst down, 1 = central, 2 = syst up
	int JECsystLevel;//0= syst down, 1 = central, 2 = syst up
	int elesmearLevel;
	int elescaleLevel;
	bool   smearJetPt;
	bool scaleEle;
	bool smearEle;
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
	void filter_electrons();
	void filter_muons();
	void filter_jets();

	/* double JER(int jetInd); */
	
	// effective areas, see Selector.cpp for more information
	double eleEffArea03(double SCEta);
	double muEffArea04(double muEta);

	bool passEleID(int eleInd, int cutVal, bool doRelisoCut);
	//	bool passEleVetoID(int eleInd, bool doRelisoCut);
	JME::JetResolution *jetResolution;
	JME::JetResolutionScaleFactor *jetResolutionScaleFactor;
	JME::JetParameters jetParam;

};

class Selector_gen{
public:
        Selector_gen();
        ~Selector_gen();

        void process_objects(EventTree* inp_tree);

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

        double jet_Pt_cut;
        double jet_Eta_cut;
        double btag_cut;
        double btag_cut_DeepCSV;
        bool   useDeepCSVbTag;
        double veto_lep_jet_dR;
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

	double mu_PtLoose_cut;
        double mu_RelIsoLoose_cut;
        double mu_RelIso_range[2];
        double mu_MVA_range[2];
        bool   mu_Iso_invert;

        void clear_vectors();
	EventTree* tree;
        void filter_electrons();
        void filter_muons();
        void filter_jets();
	 double eleEffArea03(double SCEta);
        double muEffArea04(double muEta);

        bool passEleTightID(int eleInd, bool doRelisoCut);
        bool passEleVetoID(int eleInd, bool doRelisoCut);
};
       
#endif
