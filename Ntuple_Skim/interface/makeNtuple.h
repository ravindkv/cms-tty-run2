//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon May  8 04:09:17 2017 by ROOT version 6.06/01
// from TTree EventTree/Event data (tag V08_00_24_00)
// found on file: skim_TTbar_100k.root
//////////////////////////////////////////////////////////

#ifndef makeNtuple_h
#define makeNtuple_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH2.h>
#include <TLorentzVector.h>
#include <iostream>
#include <algorithm>
#include <ctime>

#include "TRandom3.h"
#include "ParsePhotonID.h"
#include "PUReweight.h"

#include "EventTree.h"
#include "EventPick.h"
#include "Selector.h"

#include "JECvariation.h"

#include <iomanip>
#include <cmath>

//#include <boost/program_options.hpp>

// Standalone Btag scale factor tool from 
// https://twiki.cern.ch/twiki/bin/view/CMS/BTagCalibration
#include "BTagCalibrationStandalone.h"

// Header file for the classes stored in the TTree if any.
#include "vector"

#include "METzCalculator.h"
#include "TopEventCombinatorics.h"

// Header file that includes all of the event luminosity scaling
#include "ScaleFactorFunction.h"

#include "muSF_reader.h"
#include "eleSF_reader.h"
#include "phoSF_reader.h"

#include "PrefireWeights.h"

#include "UncertaintySourcesList.h"

#include "OverlapRemove.h"

class makeNtuple {
 public :

    makeNtuple(char* outputFileName,char** inputFileName);
    makeNtuple(int ac, char** av);

 private :

    EventTree* tree;   
    EventPick* evtPick;   
    Selector* selector;   
	
    bool isMC;

    TTree* outputTree;

    string sampleType;
    string systematicType;

    int eventNum = -1;

    bool isSystematicRun;

    bool useGenWeightScaling;

    bool getGenScaleWeights;
    bool applypdfweight;
    bool applyqsquare;

    MuonSF* muSFa;
    MuonSF* muSFb;
    ElectronSF* eleSF;
    PhotonSF* phoSF;

    PrefireWeights* l1PrefireSF;
    
    TH2D* l_eff;
    TH2D* c_eff;
    TH2D* b_eff;


    // Fixed size dimensions of array or collections stored in the TTree if any.

    // Declaration of leaf types
    Int_t           _run;
    Long64_t        _event;
    Int_t           _lumis;
    Bool_t          _isData;

    Float_t         _PUweight;
    Float_t         _PUweight_Up;
    Float_t         _PUweight_Do;
	
    Float_t         _q2weight_Up;
    Float_t         _q2weight_Do;
    Float_t         _q2weight_nominal;
    std::vector<float>   _genScaleSystWeights;
	
    Float_t          _pdfWeight;
    Float_t          _pdfuncer;
    Float_t          _pdfweight_Up;
    Float_t	         _pdfweight_Do;
    std::vector<float> _pdfSystWeight;

    Float_t         _ISRweight_Up;
    Float_t         _ISRweight_Do;

    Float_t         _FSRweight_Up;
    Float_t         _FSRweight_Do;


    float _prefireSF;
    float _prefireSF_Up;
    float _prefireSF_Do;

    float _btagWeight_1a;
    float _btagWeight_1a_b_Up;
    float _btagWeight_1a_b_Do;
    float _btagWeight_1a_l_Up;
    float _btagWeight_1a_l_Do;

    std::vector<float> _btagWeight;
    std::vector<float> _btagWeight_b_Up;
    std::vector<float> _btagWeight_b_Do;
    std::vector<float> _btagWeight_l_Up;
    std::vector<float> _btagWeight_l_Do;

    std::vector<float> _btagSF;
    std::vector<float> _btagSF_b_Up;
    std::vector<float> _btagSF_b_Do;
    std::vector<float> _btagSF_l_Up;
    std::vector<float> _btagSF_l_Do;

    Float_t         _muEffWeight;
    Float_t         _muEffWeight_Up;
    Float_t         _muEffWeight_Do;

    Float_t         _muEffWeight_IdIso;
    Float_t         _muEffWeight_IdIso_Up;
    Float_t         _muEffWeight_IdIso_Do;

    Float_t         _muEffWeight_Trig;
    Float_t         _muEffWeight_Trig_Up;
    Float_t         _muEffWeight_Trig_Do;

    Float_t         _eleEffWeight;
    Float_t         _eleEffWeight_Up;
    Float_t         _eleEffWeight_Do;

    Float_t         _eleEffWeight_IdReco;
    Float_t         _eleEffWeight_IdReco_Up;
    Float_t         _eleEffWeight_IdReco_Do;

    Float_t         _eleEffWeight_Trig;
    Float_t         _eleEffWeight_Trig_Up;
    Float_t         _eleEffWeight_Trig_Do;

    Float_t         _evtWeight;
    Float_t         _lumiWeight;
    /* Float_t         _evtWeightAlt; */
    /* Float_t         _lumiWeightAlt; */

    Int_t           _nVtx;
    Int_t           _nGoodVtx;

    Float_t         _genMET;
        
    Float_t         _pfMET;
    Float_t         _pfMETPhi;
    Float_t         _nu_pz;
    Float_t         _nu_pz_other;
    Float_t         _WtransMass;
    Float_t         _Mt_blgammaMET;
    Float_t         _Mt_lgammaMET;
    Float_t         _M_bjj;
    Float_t         _M_bjjgamma;
    Float_t         _M_jj;
    Float_t         _TopHad_pt;
    Float_t         _TopHad_eta;
    Float_t         _TopLep_pt;
    Float_t         _TopLep_eta;
    Float_t         _TopLep_charge;

    Float_t         _chi2;

    Bool_t          _MassCuts;

    //	Float_t         _HT;
    Float_t 	_DilepMass;
    Float_t 	_DiphoMass;
    Float_t         _DilepDelR;

    Int_t           _nPho;
    Int_t           _nPhoBarrel;
    Int_t           _nPhoEndcap;
    std::vector<float>   _phoEt;
    std::vector<float>   _phoEta;
    //    std::vector<float>   _phoSCEta;
    std::vector<float>   _phoPhi;

    std::vector<bool>    _phoIsBarrel;

    std::vector<float>   _phoR9;
    std::vector<float>   _phoHoverE;
    std::vector<float>   _phoSIEIE;

    std::vector<float>   _phoPFRelIso;
    std::vector<float>   _phoPFRelChIso;
    std::vector<float>   _phoPFChIso;

    std::vector<bool>    _phoTightID;
    std::vector<bool>    _phoMediumID;
    std::vector<int>     _phoGenMatchInd;

    std::vector<float>   _phoMassLepGamma;

    std::vector<bool>  _photonIsGenuine;
    std::vector<bool>  _photonIsMisIDEle;
    std::vector<bool>  _photonIsHadronicPhoton;
    std::vector<bool>  _photonIsHadronicFake;

    std::vector<int>   _photonParentage;
    std::vector<int>   _photonParentPID;

    std::vector<float>    _phoEffWeight;
    std::vector<float>    _phoEffWeight_Up;
    std::vector<float>    _phoEffWeight_Do;

    std::vector<float>    _phoEffWeight_Id;
    std::vector<float>    _phoEffWeight_Id_Up;
    std::vector<float>    _phoEffWeight_Id_Do;

    std::vector<float>    _phoEffWeight_eVeto;
    std::vector<float>    _phoEffWeight_eVeto_Up;
    std::vector<float>    _phoEffWeight_eVeto_Do;



    std::vector<float>   _dRPhotonJet;
    std::vector<float>   _dRPhotonLepton;
    std::vector<float>   _MPhotonLepton;
    std::vector<float>   _AnglePhotonLepton;


    Int_t           _nLoosePho;
    std::vector<float>   _loosePhoEt;
    std::vector<float>   _loosePhoEta;
    //    std::vector<float>   _loosePhoSCEta;
    std::vector<float>   _loosePhoPhi;
    std::vector<bool>    _loosePhoIsBarrel;
    std::vector<float>   _loosePhoHoverE;
    std::vector<float>   _loosePhoSIEIE;
    std::vector<float>   _loosePhoPFRelIso;
    std::vector<float>   _loosePhoPFRelChIso;
    std::vector<float>   _loosePhoPFChIso;
    std::vector<bool>    _loosePhoTightID;
    std::vector<bool>    _loosePhoMediumID;
    std::vector<bool>    _loosePhoLooseID;
    std::vector<float>   _loosePhoMVAID;
    std::vector<float>   _loosePhoMVAID17v1;
    std::vector<int>     _loosePhoGenMatchInd;
    std::vector<float>   _loosePhoMassLepGamma;

    std::vector<bool>    _loosePhoMediumIDFunction; 
    std::vector<bool>    _loosePhoMediumIDPassHoverE; 
    std::vector<bool>    _loosePhoMediumIDPassSIEIE; 
    std::vector<bool>    _loosePhoMediumIDPassChIso; 
    std::vector<bool>    _loosePhoMediumIDPassNeuIso; 
    std::vector<bool>    _loosePhoMediumIDPassPhoIso; 
    std::vector<bool>    _loosePhoTightIDFunction; 
    std::vector<bool>    _loosePhoTightIDPassHoverE; 
    std::vector<bool>    _loosePhoTightIDPassSIEIE; 
    std::vector<bool>    _loosePhoTightIDPassChIso; 
    std::vector<bool>    _loosePhoTightIDPassNeuIso; 
    std::vector<bool>    _loosePhoTightIDPassPhoIso; 

    std::vector<bool>    _loosePhotonIsGenuine;
    std::vector<bool>    _loosePhotonIsMisIDEle;
    std::vector<bool>    _loosePhotonIsHadronicPhoton;
    std::vector<bool>    _loosePhotonIsHadronicFake;

    std::vector<float>    _loosePhoEffWeight;
    std::vector<float>    _loosePhoEffWeight_Up;
    std::vector<float>    _loosePhoEffWeight_Do;

    std::vector<float>    _loosePhoEffWeight_Id;
    std::vector<float>    _loosePhoEffWeight_Id_Up;
    std::vector<float>    _loosePhoEffWeight_Id_Do;

    std::vector<float>    _loosePhoEffWeight_eVeto;
    std::vector<float>    _loosePhoEffWeight_eVeto_Up;
    std::vector<float>    _loosePhoEffWeight_eVeto_Do;


    Int_t           _nPhoNoID;
    std::vector<float>   _phoNoIDEt;
    std::vector<float>   _phoNoIDEta;
    //    std::vector<float>   _phoNoIDSCEta;
    std::vector<float>   _phoNoIDPhi;
    std::vector<bool>    _phoNoIDIsBarrel;
    std::vector<float>   _phoNoIDHoverE;
    std::vector<float>   _phoNoIDSIEIE;
    std::vector<float>   _phoNoIDPFRelIso;
    std::vector<float>   _phoNoIDPFRelChIso;
    std::vector<float>   _phoNoIDPFChIso;
    std::vector<bool>    _phoNoIDTightID;
    std::vector<bool>    _phoNoIDMediumID;
    std::vector<bool>    _phoNoIDLooseID;
    std::vector<float>   _phoNoIDMVAID;
    std::vector<float>   _phoNoIDMVAID17v1;
    std::vector<int>     _phoNoIDGenMatchInd;
    std::vector<float>   _phoNoIDMassLepGamma;

    std::vector<bool>    _phoNoIDMediumIDFunction; 
    std::vector<bool>    _phoNoIDMediumIDPassHoverE; 
    std::vector<bool>    _phoNoIDMediumIDPassSIEIE; 
    std::vector<bool>    _phoNoIDMediumIDPassChIso; 
    std::vector<bool>    _phoNoIDMediumIDPassNeuIso; 
    std::vector<bool>    _phoNoIDMediumIDPassPhoIso; 
    std::vector<bool>    _phoNoIDTightIDFunction; 
    std::vector<bool>    _phoNoIDTightIDPassHoverE; 
    std::vector<bool>    _phoNoIDTightIDPassSIEIE; 
    std::vector<bool>    _phoNoIDTightIDPassChIso; 
    std::vector<bool>    _phoNoIDTightIDPassNeuIso; 
    std::vector<bool>    _phoNoIDTightIDPassPhoIso; 

    std::vector<bool>    _photonNoIDIsGenuine;
    std::vector<bool>    _photonNoIDIsMisIDEle;
    std::vector<bool>    _photonNoIDIsHadronicPhoton;
    std::vector<bool>    _photonNoIDIsHadronicFake;

    std::vector<float>    _phoNoIDEffWeight;
    std::vector<float>    _phoNoIDEffWeight_Up;
    std::vector<float>    _phoNoIDEffWeight_Do;

    std::vector<float>    _phoNoIDEffWeight_Id;
    std::vector<float>    _phoNoIDEffWeight_Id_Up;
    std::vector<float>    _phoNoIDEffWeight_Id_Do;

    std::vector<float>    _phoNoIDEffWeight_eVeto;
    std::vector<float>    _phoNoIDEffWeight_eVeto_Up;
    std::vector<float>    _phoNoIDEffWeight_eVeto_Do;



    /* std::vector<bool>    _phoMediumIDNoHoverECut;  */
    /* std::vector<bool>    _phoMediumIDNoSIEIECut;  */
    /* std::vector<bool>    _phoMediumIDNoIsoCut;  */
   
    Int_t           _nEle;
    Int_t           _nEleLoose;

    std::vector<float>   _elePt;
    std::vector<float>   _elePhi;
    std::vector<float>   _eleEta;
    std::vector<float>   _eleSCEta;
    std::vector<float>   _elePFRelIso;
    Int_t           _nMu;
    Int_t           _nMuLoose;
    std::vector<float>   _muPt;
    std::vector<float>   _muEta;
    std::vector<float>   _muPhi;
    std::vector<float>   _muPFRelIso;
	
    Int_t                _nJet;
    Int_t                _nBJet;
    std::vector<float>   _jetPt;
    std::vector<float>   _jetEta;
    std::vector<float>   _jetPhi;
    std::vector<float>   _jetMass;

    std::vector<float>   _jetCMVA;
    std::vector<float>   _jetCSVV2;
    std::vector<float>   _jetDeepB;
    std::vector<float>   _jetDeepC;

    std::vector<Int_t>   _jetGenJetIdx;

    /* std::vector<int>     _jetPartonID; */
    /* std::vector<float>   _jetGenJetPt; */
    /* std::vector<int>     _jetGenPartonID; */
    /* std::vector<float>   _jetGenPt; */
    /* std::vector<float>   _jetGenEta; */
    /* std::vector<float>   _jetGenPhi; */

    Int_t                _nGenJet;
    std::vector<float>   _genJetPt;
    std::vector<float>   _genJetEta;
    std::vector<float>   _genJetPhi;
    std::vector<float>   _genJetMass;

    Int_t                _nfwdJet;
    std::vector<float>   _fwdJetPt;
    std::vector<float>   _fwdJetEta;
    std::vector<float>   _fwdJetPhi;
    std::vector<float>   _fwdJetMass;

    Int_t                _nGenPart;
    std::vector<float>   _genPt;
    std::vector<float>   _genEta;
    std::vector<float>   _genPhi;
    std::vector<float>   _genMass;
    std::vector<int>     _genStatus;
    std::vector<int>     _genStatusFlag;
    std::vector<int>     _genPDGID;
    std::vector<int>     _genMomIdx;
    /* std::vector<int>     _genMomPID; */
    /* std::vector<int>     _genGMomPID; */


    double               _M3;
    double               _M3_gamma;
    double               _HT;
	
    bool  _passPresel_Ele;
    bool  _passPresel_Mu;
    bool  _passAll_Ele;
    bool  _passAll_Mu;
    bool  dileptonsample;

    bool  _inHEMVeto;

    METzCalculator metZ;
    TopEventCombinatorics topEvent;
    TLorentzVector jetVector;
    TLorentzVector lepVector;
    TLorentzVector lepVector2;
    TLorentzVector phoVector;
    TLorentzVector METVector;
    TLorentzVector phoVector1;
    TLorentzVector phoVector2;
    std::vector<TLorentzVector> ljetVectors;
    std::vector<TLorentzVector> bjetVectors;
    std::vector<TLorentzVector> jetVectors;

    float lepCharge;

    std::vector<double> ljetResVectors;
    std::vector<double> bjetResVectors;

    std::vector<double> jetResolutionVectors;
    std::vector<double> jetBtagVectors;

    TLorentzVector bhad;
    TLorentzVector blep;
    TLorentzVector Wj1;
    TLorentzVector Wj2;

    /* std::vector<bool> isBjet; */
    /* std::vector<int> b_ind; */
    /* std::vector<int> j_ind; */


    void InitVariables();
    void FillEvent(std::string year);
    //void FillEvent(std::string year, bool isHemVetoObj); //HEM test
    void InitBranches();

    double SFtop(double pt);
    double topPtWeight();
    void loadBtagEff(string sampleType, string year);
    float getBtagSF_1a(string sysType, BTagCalibrationReader reader, bool verbose=false);
    vector<float> getBtagSF_1c(string sysType, BTagCalibrationReader reader, vector<float> &btagSF);

    /* double getMuSF(int muInd, int systLevel); */
    /* double getEleSF(int eleInd, int systLevel); */

    void findPhotonCategory(int phoInd, EventTree* tree, bool* genuine, bool *misIDele, bool *hadronicphoton, bool* hadronicfake, bool* puPhoton, bool verbose=false);
    /* int findPhotonParentage(int phoInd, EventTree* tree); */
    int findPhotonGenMatch(int phoInd, EventTree* tree);

    vector<bool> passPhoMediumID(int phoInd);
    vector<bool> passPhoTightID(int phoInd);
    /* bool passPhoMediumID(int phoInd, bool cutHoverE, bool cutSIEIE, bool cutIso); */

    //    int minDrIndex(double myEta, double myPhi, std::vector<int> Inds, std::vector<float> *etas, std::vector<float> *phis);
    //    double minDr(double myEta, double myPhi, std::vector<int> Inds, std::vector<float> *etas, std::vector<float> *phis);

    /* bool isSignalPhoton(EventTree* tree, int mcInd, int recoPhoInd); */
    /* bool isGoodElectron(EventTree* tree, int mcInd, int recoPhoInd); */

};


void makeNtuple::InitBranches(){

    outputTree->Branch("run"                        , &_run                         );
    outputTree->Branch("event"                      , &_event                       );
    
    outputTree->Branch("lumis"                      , &_lumis                       );
    outputTree->Branch("isData"                     , &_isData                      ); 
    outputTree->Branch("PUweight"                   , &_PUweight                    );
    if (!isSystematicRun){
	outputTree->Branch("PUweight_Up"                , &_PUweight_Up                 );
	outputTree->Branch("PUweight_Do"                , &_PUweight_Do                 );
    }

    outputTree->Branch("prefireSF"                 , &_prefireSF                  );
    if (!isSystematicRun){
	outputTree->Branch("prefireSF_Up"                 , &_prefireSF_Up                  );
	outputTree->Branch("prefireSF_Do"                 , &_prefireSF_Do                  );
    }
    outputTree->Branch("btagWeight"                 , &_btagWeight                  );
    outputTree->Branch("btagWeight_1a"                 , &_btagWeight_1a                  );
    if (!isSystematicRun){
	outputTree->Branch("btagWeight_b_Up"              , &_btagWeight_b_Up               );
	outputTree->Branch("btagWeight_b_Do"              , &_btagWeight_b_Do               );
	outputTree->Branch("btagWeight_l_Up"              , &_btagWeight_l_Up               );
	outputTree->Branch("btagWeight_l_Do"              , &_btagWeight_l_Do               );
	outputTree->Branch("btagWeight_1a_b_Up"              , &_btagWeight_1a_b_Up               );
	outputTree->Branch("btagWeight_1a_b_Do"              , &_btagWeight_1a_b_Do               );
	outputTree->Branch("btagWeight_1a_l_Up"              , &_btagWeight_1a_l_Up               );
	outputTree->Branch("btagWeight_1a_l_Do"              , &_btagWeight_1a_l_Do               );
    }
    outputTree->Branch("btagSF"                     , &_btagSF                      );
    outputTree->Branch("muEffWeight"                , &_muEffWeight                 );
    outputTree->Branch("muEffWeight_IdIso"          , &_muEffWeight_IdIso           );
    outputTree->Branch("muEffWeight_Trig"           , &_muEffWeight_Trig            );
    if (!isSystematicRun){
	outputTree->Branch("muEffWeight_Up"             , &_muEffWeight_Up              );
	outputTree->Branch("muEffWeight_Do"             , &_muEffWeight_Do              );

	outputTree->Branch("muEffWeight_IdIso_Up"       , &_muEffWeight_IdIso_Up        );
	outputTree->Branch("muEffWeight_IdIso_Do"       , &_muEffWeight_IdIso_Do        );

	outputTree->Branch("muEffWeight_Trig_Up"        , &_muEffWeight_Trig_Up         );
	outputTree->Branch("muEffWeight_Trig_Do"        , &_muEffWeight_Trig_Do         );
    }
    outputTree->Branch("eleEffWeight"               , &_eleEffWeight                );
    outputTree->Branch("eleEffWeight_IdReco"        , &_eleEffWeight_IdReco         );
    outputTree->Branch("eleEffWeight_Trig"          , &_eleEffWeight_Trig           );
    if (!isSystematicRun){
	outputTree->Branch("eleEffWeight_Up"            , &_eleEffWeight_Up             );
	outputTree->Branch("eleEffWeight_Do"            , &_eleEffWeight_Do             );

	outputTree->Branch("eleEffWeight_IdReco_Up"     , &_eleEffWeight_IdReco_Up      );
	outputTree->Branch("eleEffWeight_IdReco_Do"     , &_eleEffWeight_IdReco_Do      );

	outputTree->Branch("eleEffWeight_Trig_Up"       , &_eleEffWeight_Trig_Up        );
	outputTree->Branch("eleEffWeight_Trig_Do"       , &_eleEffWeight_Trig_Do        );
    }
    outputTree->Branch("phoEffWeight"               , &_phoEffWeight                );
    outputTree->Branch("phoEffWeight_Id"            , &_phoEffWeight_Id             );
    outputTree->Branch("phoEffWeight_eVeto"         , &_phoEffWeight_eVeto          );

    outputTree->Branch("loosePhoEffWeight"          , &_loosePhoEffWeight           );
    outputTree->Branch("loosePhoEffWeight_Id"       , &_loosePhoEffWeight_Id        );
    outputTree->Branch("loosePhoEffWeight_eVeto"    , &_loosePhoEffWeight_eVeto     );

    outputTree->Branch("phoNoIDEffWeight"           , &_phoNoIDEffWeight            );
    outputTree->Branch("phoNoIDEffWeight_Id"        , &_phoNoIDEffWeight_Id         );
    outputTree->Branch("phoNoIDEffWeight_eVeto"     , &_phoNoIDEffWeight_eVeto      );

    if (!isSystematicRun){
	outputTree->Branch("phoEffWeight_Up"            , &_phoEffWeight_Up             );
	outputTree->Branch("phoEffWeight_Do"            , &_phoEffWeight_Do             );
	outputTree->Branch("phoEffWeight_Id_Up"         , &_phoEffWeight_Id_Up          );
	outputTree->Branch("phoEffWeight_Id_Do"         , &_phoEffWeight_Id_Do          );
	outputTree->Branch("phoEffWeight_eVeto_Up"      , &_phoEffWeight_eVeto_Up       );
	outputTree->Branch("phoEffWeight_eVeto_Do"      , &_phoEffWeight_eVeto_Do       );

	outputTree->Branch("loosePhoEffWeight_Up"            , &_loosePhoEffWeight_Up             );
	outputTree->Branch("loosePhoEffWeight_Do"            , &_loosePhoEffWeight_Do             );
	outputTree->Branch("loosePhoEffWeight_Id_Up"         , &_loosePhoEffWeight_Id_Up          );
	outputTree->Branch("loosePhoEffWeight_Id_Do"         , &_loosePhoEffWeight_Id_Do          );
	outputTree->Branch("loosePhoEffWeight_eVeto_Up"      , &_loosePhoEffWeight_eVeto_Up       );
	outputTree->Branch("loosePhoEffWeight_eVeto_Do"      , &_loosePhoEffWeight_eVeto_Do       );

	outputTree->Branch("phoNoIDEffWeight_Up"            , &_phoNoIDEffWeight_Up             );
	outputTree->Branch("phoNoIDEffWeight_Do"            , &_phoNoIDEffWeight_Do             );
	outputTree->Branch("phoNoIDEffWeight_Id_Up"         , &_phoNoIDEffWeight_Id_Up          );
	outputTree->Branch("phoNoIDEffWeight_Id_Do"         , &_phoNoIDEffWeight_Id_Do          );
	outputTree->Branch("phoNoIDEffWeight_eVeto_Up"      , &_phoNoIDEffWeight_eVeto_Up       );
	outputTree->Branch("phoNoIDEffWeight_eVeto_Do"      , &_phoNoIDEffWeight_eVeto_Do       );


	outputTree->Branch("q2weight_Up"               , &_q2weight_Up               );
	outputTree->Branch("q2weight_Do"               , &_q2weight_Do               );
	outputTree->Branch("q2weight_nominal"          , &_q2weight_nominal          );
	outputTree->Branch("genScaleSystWeights"       , &_genScaleSystWeights         );

	outputTree->Branch("pdfWeight"                 , &_pdfWeight                );
	outputTree->Branch("pdfuncer"                  , &_pdfuncer                 );
	outputTree->Branch("pdfweight_Up"              , &_pdfweight_Up             );
	outputTree->Branch("pdfweight_Do"              , &_pdfweight_Do             );
	outputTree->Branch("pdfSystWeight"             , &_pdfSystWeight               );

	outputTree->Branch("ISRweight_Up"               , &_ISRweight_Up               );
	outputTree->Branch("ISRweight_Do"               , &_ISRweight_Do               );

	outputTree->Branch("FSRweight_Up"               , &_FSRweight_Up               );
	outputTree->Branch("FSRweight_Do"               , &_FSRweight_Do               );
    }

    outputTree->Branch("evtWeight"                  , &_evtWeight                   );      
    //    outputTree->Branch("evtWeightAlt"               , &_evtWeightAlt                );      
    outputTree->Branch("nVtx"                       , &_nVtx                        ); 
    outputTree->Branch("nGoodVtx"                   , &_nGoodVtx                    ); 
    /* outputTree->Branch("isPVGood"                   , &_isPVGood                    );  */
    /* outputTree->Branch("rho"                        , &_rho                         );  */
    if (!isSystematicRun){
	outputTree->Branch("genMET"                     , &_genMET                      ); 
    }
    outputTree->Branch("pfMET"                      , &_pfMET                       );
    outputTree->Branch("pfMETPhi"                   , &_pfMETPhi                    ); 
    outputTree->Branch("nu_pz"                      , &_nu_pz                       );
    outputTree->Branch("nu_pz_other"                , &_nu_pz_other                 );
    outputTree->Branch("WtransMass"                 , &_WtransMass                  );

    outputTree->Branch("Mt_blgammaMET"              , &_Mt_blgammaMET               );
    outputTree->Branch("Mt_lgammaMET"               , &_Mt_lgammaMET                );
    outputTree->Branch("M_bjj"                      , &_M_bjj                       );
    outputTree->Branch("M_bjjgamma"                 , &_M_bjjgamma                  );
    outputTree->Branch("M_jj"                       , &_M_jj                        );
    outputTree->Branch("MassCuts"                   , &_MassCuts                    );
    outputTree->Branch("TopHad_pt"                  , &_TopHad_pt                   );
    outputTree->Branch("TopHad_eta"                 , &_TopHad_eta                  );
    outputTree->Branch("TopLep_pt"                  , &_TopLep_pt                   );
    outputTree->Branch("TopLep_eta"                 , &_TopLep_eta                  );
    outputTree->Branch("TopLep_charge"              , &_TopLep_charge               );

    outputTree->Branch("chi2"                       , &_chi2               );


    outputTree->Branch("DiphoMass"                  , &_DiphoMass                   ); 
    outputTree->Branch("DilepMass"                  , &_DilepMass       			);
    outputTree->Branch("DilepDelR"                  , &_DilepDelR                   );
    outputTree->Branch("nPho"                       , &_nPho                        ); 
    outputTree->Branch("nPhoBarrel"                 , &_nPhoBarrel                        );
    outputTree->Branch("nPhoEndcap"                 , &_nPhoEndcap                        );
    outputTree->Branch("phoEt"                      , &_phoEt                       );
    outputTree->Branch("phoEta"                     , &_phoEta                      );
    outputTree->Branch("phoR9"                      , &_phoR9                       ); 
    //    outputTree->Branch("phoSCEta"                   , &_phoSCEta                    ); 
    outputTree->Branch("phoPhi"                     , &_phoPhi                      ); 
    outputTree->Branch("phoIsBarrel"                , &_phoIsBarrel                 ); 
    outputTree->Branch("phoHoverE"                  , &_phoHoverE                   ); 
    outputTree->Branch("phoSIEIE"                   , &_phoSIEIE                    ); 
    outputTree->Branch("phoPFChIso"                 , &_phoPFChIso                  ); 
    /* outputTree->Branch("phoPFPhoIso"                , &_phoPFPhoIso                 );  */
    /* outputTree->Branch("phoPFNeuIso"                , &_phoPFNeuIso                 );  */
    outputTree->Branch("phoTightID"                 , &_phoTightID                  ); 
    outputTree->Branch("phoMediumID"                , &_phoMediumID                 ); 
    if (!isSystematicRun){
	outputTree->Branch("phoGenMatchInd"                , &_phoGenMatchInd                 ); 
    }
    outputTree->Branch("phoMassLepGamma"                 , &_phoMassLepGamma                  ); 

    outputTree->Branch("nLoosePho"                       , &_nLoosePho                        ); 
    outputTree->Branch("loosePhoEt"                      , &_loosePhoEt                       );
    outputTree->Branch("loosePhoEta"                     , &_loosePhoEta                      ); 
    //    outputTree->Branch("loosePhoSCEta"                   , &_loosePhoSCEta                    ); 
    outputTree->Branch("loosePhoPhi"                     , &_loosePhoPhi                      ); 
    outputTree->Branch("loosePhoIsBarrel"                , &_loosePhoIsBarrel                 ); 
    outputTree->Branch("loosePhoHoverE"                  , &_loosePhoHoverE                   ); 
    outputTree->Branch("loosePhoSIEIE"                   , &_loosePhoSIEIE                    ); 
    outputTree->Branch("loosePhoPFChIso"                 , &_loosePhoPFChIso                  ); 
    /* outputTree->Branch("loosePhoPFPhoIso"                , &_loosePhoPFPhoIso                 );  */
    /* outputTree->Branch("loosePhoPFNeuIso"                , &_loosePhoPFNeuIso                 );  */
    outputTree->Branch("loosePhoTightID"                 , &_loosePhoTightID                  ); 
    outputTree->Branch("loosePhoMediumID"                , &_loosePhoMediumID                 ); 
    outputTree->Branch("loosePhoLooseID"                 , &_loosePhoLooseID                  ); 
    outputTree->Branch("loosePhoMVAId"                 , &_loosePhoMVAID                  ); 
    outputTree->Branch("loosePhoMVAId17v1"             , &_loosePhoMVAID17v1              ); 

    if (!isSystematicRun){
	outputTree->Branch("loosePhoGenMatchInd"                 , &_loosePhoGenMatchInd                  ); 
    }
    outputTree->Branch("loosePhoMassLepGamma"                  , &_loosePhoMassLepGamma                   ); 
	
    outputTree->Branch("loosePhoMediumIDFunction"        , &_loosePhoMediumIDFunction         ); 
    outputTree->Branch("loosePhoMediumIDPassHoverE"      , &_loosePhoMediumIDPassHoverE       ); 
    outputTree->Branch("loosePhoMediumIDPassSIEIE"       , &_loosePhoMediumIDPassSIEIE        ); 
    outputTree->Branch("loosePhoMediumIDPassChIso"       , &_loosePhoMediumIDPassChIso        ); 
    outputTree->Branch("loosePhoMediumIDPassNeuIso"      , &_loosePhoMediumIDPassNeuIso       ); 
    outputTree->Branch("loosePhoMediumIDPassPhoIso"      , &_loosePhoMediumIDPassPhoIso       ); 


    outputTree->Branch("nPhoNoID"                       , &_nPhoNoID                        ); 
    outputTree->Branch("phoNoIDEt"                      , &_phoNoIDEt                       );
    outputTree->Branch("phoNoIDEta"                     , &_phoNoIDEta                      ); 
    //    outputTree->Branch("phoNoIDSCEta"                   , &_phoNoIDSCEta                    ); 
    outputTree->Branch("phoNoIDPhi"                     , &_phoNoIDPhi                      ); 
    outputTree->Branch("phoNoIDIsBarrel"                , &_phoNoIDIsBarrel                 ); 
    outputTree->Branch("phoNoIDHoverE"                  , &_phoNoIDHoverE                   ); 
    outputTree->Branch("phoNoIDSIEIE"                   , &_phoNoIDSIEIE                    ); 
    outputTree->Branch("phoNoIDPFChIso"                 , &_phoNoIDPFChIso                  ); 
    /* outputTree->Branch("phoNoIDPFPhoIso"                , &_phoNoIDPFPhoIso                 );  */
    /* outputTree->Branch("phoNoIDPFNeuIso"                , &_phoNoIDPFNeuIso                 );  */
    outputTree->Branch("phoNoIDTightID"                 , &_phoNoIDTightID                  ); 
    outputTree->Branch("phoNoIDMediumID"                , &_phoNoIDMediumID                 ); 
    outputTree->Branch("phoNoIDLooseID"                 , &_phoNoIDLooseID                  ); 
    outputTree->Branch("phoNoIDMVAId"                 , &_phoNoIDMVAID                  ); 
    outputTree->Branch("phoNoIDMVAId17v1"             , &_phoNoIDMVAID17v1              ); 

    if (!isSystematicRun){
	outputTree->Branch("phoNoIDGenMatchInd"                 , &_phoNoIDGenMatchInd                  ); 
    }
    outputTree->Branch("phoNoIDMassLepGamma"                  , &_phoNoIDMassLepGamma                   ); 
	
    outputTree->Branch("phoNoIDMediumIDFunction"        , &_phoNoIDMediumIDFunction         ); 
    outputTree->Branch("phoNoIDMediumIDPassHoverE"      , &_phoNoIDMediumIDPassHoverE       ); 
    outputTree->Branch("phoNoIDMediumIDPassSIEIE"       , &_phoNoIDMediumIDPassSIEIE        ); 
    outputTree->Branch("phoNoIDMediumIDPassChIso"       , &_phoNoIDMediumIDPassChIso        ); 
    outputTree->Branch("phoNoIDMediumIDPassNeuIso"      , &_phoNoIDMediumIDPassNeuIso       ); 
    outputTree->Branch("phoNoIDMediumIDPassPhoIso"      , &_phoNoIDMediumIDPassPhoIso       ); 


	
    outputTree->Branch("nEle"                        , &_nEle                       ); 
    outputTree->Branch("elePt"                       , &_elePt                      );
    outputTree->Branch("elePhi"                      , &_elePhi                     ); 
    outputTree->Branch("eleEta"                      , &_eleEta                     );
    outputTree->Branch("eleSCEta"                    , &_eleSCEta                   ); 
    outputTree->Branch("elePFRelIso"                 , &_elePFRelIso                ); 

    outputTree->Branch("nMu"                         , &_nMu                        ); 
    outputTree->Branch("muPt"                        , &_muPt                       ); 
    outputTree->Branch("muEta"                       , &_muEta                      );
    outputTree->Branch("muPhi"                       , &_muPhi                      );
    outputTree->Branch("muPFRelIso"                  , &_muPFRelIso                 );
    
    outputTree->Branch("nJet"                        , &_nJet                       ); 
    outputTree->Branch("nfwdJet"                        , &_nfwdJet                       );
    outputTree->Branch("nBJet"                       , &_nBJet                      ); 
    outputTree->Branch("jetPt"                       , &_jetPt                      );
    /* outputTree->Branch("jetEn"                       , &_jetEn                      ); */
    outputTree->Branch("jetEta"                      , &_jetEta                     ); 
    outputTree->Branch("jetPhi"                      , &_jetPhi                     ); 
    /* outputTree->Branch("jetRawPt"                    , &_jetRawPt                   );  */
    /* outputTree->Branch("jetArea"                     , &_jetArea                    );  */
    if (!isSystematicRun){
	/* outputTree->Branch("jetCMVA"  , &_jetCMVA ); */
	/* outputTree->Branch("jetCSVV2"  , &_jetCSVV2 ); */
	outputTree->Branch("jetDeepB"  , &_jetDeepB );
	/* outputTree->Branch("jetDeepC"  , &_jetDeepC ); */

	outputTree->Branch("jetGenJetIdx"  , &_jetGenJetIdx );
    }
	
    /* if (!tree->isData_){ */
    /* 	outputTree->Branch("jetPartonID"                 , &_jetPartonID                );  */
    /* 	outputTree->Branch("jetGenJetPt"                 , &_jetGenJetPt                );  */
    /* 	outputTree->Branch("jetGenPartonID"              , &_jetGenPartonID             );  */
    /* 	outputTree->Branch("jetGenPt"                    , &_jetGenPt                   );  */
    /* 	outputTree->Branch("jetGenEta"                   , &_jetGenEta                  ); */
    /* 	outputTree->Branch("jetGenPhi"                   , &_jetGenPhi                  ); */
    /* }		 */


    outputTree->Branch("fwdJetPt"                       , &_fwdJetPt                      );
    outputTree->Branch("fwdJetEta"                      , &_fwdJetEta                     );
    outputTree->Branch("fwdJetPhi"                      , &_fwdJetPhi                     );
    outputTree->Branch("fwdJetMass"                     , &_fwdJetMass                    );


    outputTree->Branch("dRPhotonJet"                 , &_dRPhotonJet                );
    outputTree->Branch("dRPhotonLepton"              , &_dRPhotonLepton             );
    outputTree->Branch("MPhotonLepton"               , &_MPhotonLepton             );
    outputTree->Branch("AnglePhotonLepton"           , &_AnglePhotonLepton         );

    if (!tree->isData_ && !isSystematicRun){
	outputTree->Branch("nGenPart"  	                , &_nGenPart                ); 
	outputTree->Branch("genPt"	                , &_genPt	            );
	outputTree->Branch("genEta"	                , &_genEta	            ); 
	outputTree->Branch("genPhi"	                , &_genPhi	            ); 
	outputTree->Branch("genMass"	                , &_genMass	            ); 
	outputTree->Branch("genStatus"                  , &_genStatus               );
	outputTree->Branch("genStatusFlag"              , &_genStatusFlag           );
	outputTree->Branch("genPDGID"	                , &_genPDGID	            ); 
	outputTree->Branch("genMomIdx"                  , &_genMomIdx               );
	//	outputTree->Branch("genScaleSystWeights"        , &_genScaleSystWeights     );


	outputTree->Branch("nGenJet"  	                     , &_nGenJet	         ); 
	outputTree->Branch("genJetPt"	                     , &_genJetPt	         );
	outputTree->Branch("genJetEta"	                     , &_genJetEta	         ); 
	outputTree->Branch("genJetPhi"	                     , &_genJetPhi	         ); 
	outputTree->Branch("genJetMass"	                     , &_genJetMass	         ); 

    }

    outputTree->Branch("M3"                          , &_M3                         ); 
    outputTree->Branch("M3_gamma"                    , &_M3_gamma                   );
    outputTree->Branch("HT"                          , &_HT                         ); 

    outputTree->Branch("passPresel_Ele"              , &_passPresel_Ele             ); 
    outputTree->Branch("passPresel_Mu"               , &_passPresel_Mu              );
    outputTree->Branch("passAll_Ele"                 , &_passAll_Ele                ); 
    outputTree->Branch("passAll_Mu"                  , &_passAll_Mu                 );

    outputTree->Branch("inHEMVeto"                   , &_inHEMVeto                  );

    outputTree->Branch("photonIsGenuine"             , &_photonIsGenuine            );
    outputTree->Branch("photonIsMisIDEle"            , &_photonIsMisIDEle           );
    outputTree->Branch("photonIsHadronicPhoton"      , &_photonIsHadronicPhoton     );
    outputTree->Branch("photonIsHadronicFake"        , &_photonIsHadronicFake       );
    outputTree->Branch("loosePhotonIsGenuine"             , &_loosePhotonIsGenuine            );
    outputTree->Branch("loosePhotonIsMisIDEle"            , &_loosePhotonIsMisIDEle           );
    outputTree->Branch("loosePhotonIsHadronicPhoton"      , &_loosePhotonIsHadronicPhoton     );
    outputTree->Branch("loosePhotonIsHadronicFake"        , &_loosePhotonIsHadronicFake       );
    outputTree->Branch("photonNoIDIsGenuine"             , &_photonNoIDIsGenuine            );
    outputTree->Branch("photonNoIDIsMisIDEle"            , &_photonNoIDIsMisIDEle           );
    outputTree->Branch("photonNoIDIsHadronicPhoton"      , &_photonNoIDIsHadronicPhoton     );
    outputTree->Branch("photonNoIDIsHadronicFake"        , &_photonNoIDIsHadronicFake       );

    outputTree->Branch("photonParentage"        , &_photonParentage       );
    outputTree->Branch("photonParentPID"        , &_photonParentPID       );
	
}

void makeNtuple::InitVariables()
{

    _run             = -9999;
    _event           = -9999;
    _lumis		     = -9999;
    _isData		     = false;
    _nVtx		     = -9999;
    _nGoodVtx	     = -9999;
    /* _isPVGood	     = false; */
    /* _rho		     = -9999; */

    _genMET		     = -9999;

    _pfMET		     = -9999;
    _pfMETPhi	     = -9999;
    _nu_pz           = -9999;
    _nu_pz_other     = -9999;
    _WtransMass      = -9999;

    _Mt_blgammaMET   = -9999;
    _Mt_lgammaMET    = -9999;
    _M_bjj           = -9999;
    _M_bjjgamma      = -9999;
    _M_jj            = -9999;
    _MassCuts        = false;
    _TopHad_pt       = -9999;
    _TopHad_eta      = -9999;
    _TopLep_pt       = -9999;
    _TopLep_eta      = -9999;
    _TopLep_charge   = -9999;

    _chi2   = -9999;

    _HT		 = -9999;
    _DilepMass	 = -9999;
    _DilepDelR	 = -9999;
    _DiphoMass       = -9999;
    _nPho		 = -9999;
    //_nPhoBarrel      = -9999;
    //_nPhoEndcap      = -9999;
    _nEle		     = -9999;
    _nMu		     = -9999;
    _nMuLoose 	     = -9999;
    _nEleLoose           = -9999;
    _nJet            = -9999;  
    _nfwdJet         =-9999;  
    _nBJet           = -9999;    

    _nGenPart        = -9999;
    _nGenJet         = -9999;

    _passPresel_Ele  = false;
    _passPresel_Mu   = false;
    _passAll_Ele     = false;
    _passAll_Mu      = false;


    _pdfWeight    = 1.;
    _pdfweight_Up = 1.;
    _pdfweight_Do = 1.;
    _pdfuncer = 0.;

    _q2weight_nominal = 1.;
    _q2weight_Up = 1.;
    _q2weight_Do = 1.;

    _ISRweight_Up = 1.;
    _ISRweight_Do = 1.;

    _FSRweight_Up = 1.;
    _FSRweight_Do = 1.;

    _eleEffWeight    = 1.;
    _eleEffWeight_Do = 1.;
    _eleEffWeight_Up = 1.;

    _muEffWeight    = 1.;
    _muEffWeight_Do = 1.;
    _muEffWeight_Up = 1.;

    _phoEffWeight.clear();
    _phoEffWeight_Do.clear();
    _phoEffWeight_Up.clear();
    _phoEffWeight_Id.clear();
    _phoEffWeight_Id_Do.clear();
    _phoEffWeight_Id_Up.clear();
    _phoEffWeight_eVeto.clear();
    _phoEffWeight_eVeto_Do.clear();
    _phoEffWeight_eVeto_Up.clear();

    _loosePhoEffWeight.clear();
    _loosePhoEffWeight_Do.clear();
    _loosePhoEffWeight_Up.clear();
    _loosePhoEffWeight_Id.clear();
    _loosePhoEffWeight_Id_Do.clear();
    _loosePhoEffWeight_Id_Up.clear();
    _loosePhoEffWeight_eVeto.clear();
    _loosePhoEffWeight_eVeto_Do.clear();
    _loosePhoEffWeight_eVeto_Up.clear();

    _phoNoIDEffWeight.clear();
    _phoNoIDEffWeight_Do.clear();
    _phoNoIDEffWeight_Up.clear();
    _phoNoIDEffWeight_Id.clear();
    _phoNoIDEffWeight_Id_Do.clear();
    _phoNoIDEffWeight_Id_Up.clear();
    _phoNoIDEffWeight_eVeto.clear();
    _phoNoIDEffWeight_eVeto_Do.clear();
    _phoNoIDEffWeight_eVeto_Up.clear();

    _btagWeight.clear();
    _btagWeight_b_Up.clear();
    _btagWeight_b_Do.clear();
    _btagWeight_l_Up.clear();
    _btagWeight_l_Do.clear();

    _btagWeight_1a = 1.;
    _btagWeight_1a_b_Up = 1.;
    _btagWeight_1a_b_Do = 1.;
    _btagWeight_1a_l_Up = 1.;
    _btagWeight_1a_l_Do = 1.;

    _btagSF.clear();
    _btagSF_b_Up.clear();
    _btagSF_b_Do.clear();
    _btagSF_l_Up.clear();
    _btagSF_l_Do.clear();

    _elePt.clear();
    _elePhi.clear();
    _eleEta.clear();
    _eleSCEta.clear();
    _elePFRelIso.clear();

    _muPt.clear();
    _muEta.clear();
    _muPhi.clear();
    _muPFRelIso.clear();

    _phoEt.clear();
    _phoR9.clear();
    _phoEta.clear();
    //    _phoSCEta.clear();
    _phoPhi.clear();
    _phoIsBarrel.clear();
    _phoHoverE.clear();
    _phoSIEIE.clear();
    _phoPFChIso.clear();
    /* _phoPFPhoIso.clear(); */
    /* _phoPFNeuIso.clear(); */
    _phoTightID.clear();
    _phoMediumID.clear();
    _phoGenMatchInd.clear();
    _phoMassLepGamma.clear();

    _photonIsGenuine.clear();
    _photonIsMisIDEle.clear();
    _photonIsHadronicPhoton.clear();
    _photonIsHadronicFake.clear();

    _photonParentage.clear();
    _photonParentPID.clear();

    _loosePhoEt.clear();
    _loosePhoEta.clear();
    //    _loosePhoSCEta.clear();
    _loosePhoPhi.clear();
    _loosePhoIsBarrel.clear();
    _loosePhoHoverE.clear();
    _loosePhoSIEIE.clear();
    _loosePhoPFChIso.clear();
    /* _loosePhoPFPhoIso.clear(); */
    /* _loosePhoPFNeuIso.clear(); */
    _loosePhoTightID.clear();
    _loosePhoMediumID.clear();
    _loosePhoLooseID.clear();
    _loosePhoMVAID.clear();
    _loosePhoMVAID17v1.clear();
    _loosePhoGenMatchInd.clear();
    _loosePhoMassLepGamma.clear();
    _loosePhoMediumIDFunction.clear(); 
    _loosePhoMediumIDPassHoverE.clear(); 
    _loosePhoMediumIDPassSIEIE.clear(); 
    _loosePhoMediumIDPassChIso.clear(); 
    _loosePhoMediumIDPassNeuIso.clear(); 
    _loosePhoMediumIDPassPhoIso.clear(); 
    _loosePhoTightIDFunction.clear(); 
    _loosePhoTightIDPassHoverE.clear(); 
    _loosePhoTightIDPassSIEIE.clear(); 
    _loosePhoTightIDPassChIso.clear(); 
    _loosePhoTightIDPassNeuIso.clear(); 
    _loosePhoTightIDPassPhoIso.clear(); 
    _loosePhotonIsGenuine.clear();
    _loosePhotonIsMisIDEle.clear();
    _loosePhotonIsHadronicPhoton.clear();
    _loosePhotonIsHadronicFake.clear();

    _phoNoIDEt.clear();
    _phoNoIDEta.clear();
    //    _phoNoIDSCEta.clear();
    _phoNoIDPhi.clear();
    _phoNoIDIsBarrel.clear();
    _phoNoIDHoverE.clear();
    _phoNoIDSIEIE.clear();
    _phoNoIDPFChIso.clear();
    /* _phoNoIDPFPhoIso.clear(); */
    /* _phoNoIDPFNeuIso.clear(); */
    _phoNoIDTightID.clear();
    _phoNoIDMediumID.clear();
    _phoNoIDLooseID.clear();
    _phoNoIDMVAID.clear();
    _phoNoIDMVAID17v1.clear();
    _phoNoIDGenMatchInd.clear();
    _phoNoIDMassLepGamma.clear();
    _phoNoIDMediumIDFunction.clear(); 
    _phoNoIDMediumIDPassHoverE.clear(); 
    _phoNoIDMediumIDPassSIEIE.clear(); 
    _phoNoIDMediumIDPassChIso.clear(); 
    _phoNoIDMediumIDPassNeuIso.clear(); 
    _phoNoIDMediumIDPassPhoIso.clear(); 
    _phoNoIDTightIDFunction.clear(); 
    _phoNoIDTightIDPassHoverE.clear(); 
    _phoNoIDTightIDPassSIEIE.clear(); 
    _phoNoIDTightIDPassChIso.clear(); 
    _phoNoIDTightIDPassNeuIso.clear(); 
    _phoNoIDTightIDPassPhoIso.clear(); 
    _photonNoIDIsGenuine.clear();
    _photonNoIDIsMisIDEle.clear();
    _photonNoIDIsHadronicPhoton.clear();
    _photonNoIDIsHadronicFake.clear();

    _jetPt.clear();
    /* _jetEn.clear(); */
    _jetEta.clear();
    _jetPhi.clear();
    /* _jetRawPt.clear(); */
    /* _jetArea.clear(); */
    _jetCMVA.clear();
    _jetCSVV2.clear();
    _jetDeepB.clear();
    _jetDeepC.clear();

    _jetGenJetIdx.clear();

    _fwdJetPt.clear();
    _fwdJetEta.clear();
    _fwdJetPhi.clear();
    _fwdJetMass.clear();


    /* _jetPartonID.clear(); */
    /* _jetGenJetPt.clear(); */
    /* _jetGenPartonID.clear(); */
    /* _jetGenPt.clear(); */
    /* _jetGenEta.clear(); */
    /* _jetGenPhi.clear(); */

    _dRPhotonJet.clear();
    _dRPhotonLepton.clear();
    _MPhotonLepton.clear();
    _AnglePhotonLepton.clear();
	
    _genScaleSystWeights.clear();
    _pdfSystWeight.clear();

    _genPt.clear();
    _genPhi.clear();
    _genEta.clear();
    _genMass.clear();
    _genStatus.clear();
    _genStatusFlag.clear();
    _genPDGID.clear();
    _genMomIdx.clear();
    /* _mcMomPID.clear(); */
    /* _mcGMomPID.clear(); */
    /* _mcParentage.clear(); */

    _genJetPt.clear();
    _genJetEta.clear();
    _genJetPhi.clear();
    _genJetMass.clear();


}



#endif

