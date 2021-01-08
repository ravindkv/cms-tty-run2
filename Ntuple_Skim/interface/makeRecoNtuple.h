//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon May  8 04:09:17 2017 by ROOT version 6.06/01
// from TTree EventTree/Event data (tag V08_00_24_00)
// found on file: skim_TTbar_100k.root
//////////////////////////////////////////////////////////

#ifndef makeRecoNtuple_h
#define makeRecoNtuple_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH2.h>
#include <TLorentzVector.h>
#include <iostream>
#include <algorithm>
#include <ctime>

#include "TRandom3.h"
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
#include "UncertaintySourcesList.h"


class makeRecoNtuple {
 public :

    makeRecoNtuple(char* outputFileName,char** inputFileName);
    makeRecoNtuple(int ac, char** av);

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
    Float_t         _M_bjj;
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
    Float_t         _DilepDelR;

    Int_t           _nEle;
    Int_t           _nEleLoose;

    std::vector<float>   _elePt;
    std::vector<float>   _elePhi;
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
    double               _HT;
	
    bool  _passPresel_Ele;
    bool  _passPresel_Mu;
    bool  _passAll_Ele;
    bool  _passAll_Mu;
    bool  dileptonsample;

    METzCalculator metZ;
    TopEventCombinatorics topEvent;
    TLorentzVector jetVector;
    TLorentzVector lepVector;
    TLorentzVector lepVector2;
    TLorentzVector METVector;
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
    //void FillEvent(std::string year);
    void FillEvent(std::string year, bool isHemVetoObj);
    void InitBranches();

    double SFtop(double pt);
    double topPtWeight();
    void loadBtagEff(string sampleType, string year);
    float getBtagSF_1a(string sysType, BTagCalibrationReader reader, bool verbose=false);
    vector<float> getBtagSF_1c(string sysType, BTagCalibrationReader reader, vector<float> &btagSF);

    /* double getMuSF(int muInd, int systLevel); */
    /* double getEleSF(int eleInd, int systLevel); */
};


void makeRecoNtuple::InitBranches(){

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
    if (!isSystematicRun){
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

    outputTree->Branch("M_bjj"                      , &_M_bjj                       );
    outputTree->Branch("M_jj"                       , &_M_jj                        );
    outputTree->Branch("MassCuts"                   , &_MassCuts                    );
    outputTree->Branch("TopHad_pt"                  , &_TopHad_pt                   );
    outputTree->Branch("TopHad_eta"                 , &_TopHad_eta                  );
    outputTree->Branch("TopLep_pt"                  , &_TopLep_pt                   );
    outputTree->Branch("TopLep_eta"                 , &_TopLep_eta                  );
    outputTree->Branch("TopLep_charge"              , &_TopLep_charge               );

    outputTree->Branch("chi2"                       , &_chi2               );


    outputTree->Branch("DilepMass"                  , &_DilepMass       			);
    outputTree->Branch("DilepDelR"                  , &_DilepDelR                   );
    outputTree->Branch("nEle"                        , &_nEle                       ); 
    outputTree->Branch("elePt"                       , &_elePt                      );
    outputTree->Branch("elePhi"                      , &_elePhi                     ); 
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
    outputTree->Branch("HT"                          , &_HT                         ); 

    outputTree->Branch("passPresel_Ele"              , &_passPresel_Ele             ); 
    outputTree->Branch("passPresel_Mu"               , &_passPresel_Mu              );
    outputTree->Branch("passAll_Ele"                 , &_passAll_Ele                ); 
    outputTree->Branch("passAll_Mu"                  , &_passAll_Mu                 );
}

void makeRecoNtuple::InitVariables()
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

    _M_bjj           = -9999;
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
    _eleSCEta.clear();
    _elePFRelIso.clear();

    _muPt.clear();
    _muEta.clear();
    _muPhi.clear();
    _muPFRelIso.clear();

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

