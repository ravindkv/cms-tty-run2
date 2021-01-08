#ifndef EVENTTREE_H
#define EVENTTREE_H

#include<TFile.h>
#include<TTree.h>
#include<TChain.h>

#include<vector>

using namespace std;
const Int_t maxP = 600;

class EventTree{
 public:
    EventTree(int nFiles, bool xRootDAccess, string year, bool isData, char** fileNames);
    ~EventTree();
    Long64_t GetEntries();
    Int_t GetEntry(Long64_t entry);
    
    TChain* chain;
    
    // include all variables just in case
    UInt_t    run_;
    ULong64_t event_;
    UInt_t    lumis_;
    
    Float_t  genWeight_;
    UInt_t nLHEScaleWeight_;
    Float_t LHEScaleWeight_[200];
    
    UInt_t nLHEPdfWeight_;
    Float_t LHEPdfWeight_[200];
    
    UInt_t nPSWeight_;
    Float_t PSWeight_[200];

    Float_t LHEWeight_originalXWGTUP_;
    bool isData_;

    Int_t    nVtx_;
    Int_t    nGoodVtx_;
    

    Float_t    pvNDOF_;
    Float_t    pvX_;
    Float_t    pvY_;
    Float_t    pvZ_;
    Float_t    pvChi2_;
    

    // genParticle
    
    UInt_t    nGenPart_;
    
    Float_t   GenPart_pt_[300];
    Float_t   GenPart_eta_[300];
    Float_t   GenPart_phi_[300];
    Float_t   GenPart_mass_[300];
    Int_t     GenPart_genPartIdxMother_[300];
    Int_t     GenPart_pdgId_[300];
    Int_t     GenPart_status_[300];
    Int_t     GenPart_statusFlags_[300];
    
    
    UInt_t    nGenJet_;
    
    Float_t   GenJet_pt_[100];
    Float_t   GenJet_eta_[100];
    Float_t   GenJet_phi_[100];
    Float_t   GenJet_mass_[100];
    
    // PU
    Int_t    nPU_;  
    Float_t  nPUTrue_;  
    
    Float_t  MET_pt_;
    Float_t  MET_phi_;
    
    Float_t  GenMET_pt_;
    Float_t  GenMET_phi_;

    // Electron

    UInt_t          nEle_;
    Float_t         elePhi_[20];
    Float_t         elePt_[20];
    Float_t         eleEta_[20];
    Float_t         eleDeltaEtaSC_[20];
    Int_t           eleCharge_[20];
    Float_t         eleMass_[20];
    Float_t         elePFRelIso_[20];
    Float_t         elePFRelChIso_[20];
    Int_t           eleIDcutbased_[20];
    Float_t         eleD0_[20];
    Float_t         eleDz_[20];
    Float_t         eleSIEIE_[20];

    Int_t           eleVidWPBitmap_[20];
    Float_t         eleEcalSumEtDr03_[20];
    Float_t         eleHcalSumEtDr03_[20];
    Float_t         eleTrkSumPtDr03_[20];

    // I don't know why, but these two lines are needed to avoid possible memory issue with nMuon (segfault when it thinks there are 2**32-1 muons in an event
    // These vectors are not used
    vector<float>*  PFClustdEta_;
    vector<float>*  PFClustdPhi_;


    // Muon
    UInt_t          nMuon_;
    Float_t         muPhi_[15];
    Float_t         muPt_[15];
    Float_t         muEta_[15];
    Int_t           muCharge_[15];
    Float_t         muMass_[15];
    Float_t         muPFRelIso_[15];
    Bool_t          muMediumId_[15];
    Bool_t          muTightId_[15];
    Bool_t          muIsPFMuon_[15];
    Bool_t          muIsGlobal_[15];
    Bool_t          muIsTracker_[15];



    // Jet

    UInt_t          nJet_;
    Float_t         jetPt_[200];
    Float_t         jetEta_[200];
    Float_t         jetPhi_[200];
    Float_t         jetMass_[200];
    Float_t         jetRawFactor_[200];
    Int_t           jetID_[200];
    Float_t         jetArea_[200];
    Float_t         jetBtagCMVA_[200];
    Float_t         jetBtagCSVV2_[200];
    Float_t         jetBtagDeepB_[200];
    Float_t         jetBtagDeepC_[200];
    Float_t         jetBtagDeepFlavB_[200];
    Float_t         jetchEmEF_[200];
    Float_t         jetneEmEF_[200];
    Int_t           jetHadFlvr_[200];
    Int_t           jetGenJetIdx_[200];

    Float_t  rho_;


    Bool_t   HLT_Ele32_eta2p1_WPTight_Gsf_;
    Bool_t   HLT_IsoMu24_;
    Bool_t   HLT_IsoTkMu24_;
    Bool_t   HLT_Ele32_WPTight_Gsf_L1DoubleEG_;
    Bool_t   HLT_IsoMu24_eta2p1_;
    Bool_t   HLT_IsoMu27_;

    Bool_t   HLT_Ele105_CaloIdVT_GsfTrkIdT_;
    Bool_t   HLT_Ele115_CaloIdVT_GsfTrkIdT_;
    Bool_t   HLT_DoubleEle25_CaloIdL_MW_;

    Bool_t   HLT_Ele27_WPTight_Gsf_;
    Bool_t   HLT_Ele32_WPTight_Gsf_;
    Bool_t   HLT_Ele35_WPTight_Gsf_;
    Bool_t   HLT_Ele38_WPTight_Gsf_;

    Bool_t   HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_;
    Bool_t   HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_;
    Bool_t   HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_;
    Bool_t   HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_;
    Bool_t   HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_;
    Bool_t   HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_;

    Bool_t   L1_SingleEG24_;
    Bool_t   L1_SingleEG26_;
    Bool_t   L1_SingleEG30_;
    Bool_t   L1_SingleEG32_;
    Bool_t   L1_SingleEG34_;
    Bool_t   L1_SingleEG36_;
    Bool_t   L1_SingleEG38_;
    Bool_t   L1_SingleEG40_;
    Bool_t   L1_SingleEG42_;
    Bool_t   L1_SingleEG45_;
    Bool_t   L1_SingleEG50_;
    Bool_t   L1_SingleEG34er2p1_;
    Bool_t   L1_SingleEG36er2p1_;
    Bool_t   L1_SingleEG38er2p1_;
    Bool_t   L1_SingleIsoEG24er2p1_;
    Bool_t   L1_SingleIsoEG26er2p1_;
    Bool_t   L1_SingleIsoEG28er2p1_;
    Bool_t   L1_SingleIsoEG30er2p1_;
    Bool_t   L1_SingleIsoEG32er2p1_;
    Bool_t   L1_SingleIsoEG34er2p1_;
    Bool_t   L1_SingleIsoEG36er2p1_;
    Bool_t   L1_SingleIsoEG24_;
    Bool_t   L1_SingleIsoEG26_;
    Bool_t   L1_SingleIsoEG28_;
    Bool_t   L1_SingleIsoEG30_;
    Bool_t   L1_SingleIsoEG32_;
    Bool_t   L1_SingleIsoEG34_;
    Bool_t   L1_SingleIsoEG36_;
    Bool_t   L1_SingleIsoEG38_;


    
    Bool_t   Flag_goodVertices_ ;
    Bool_t   Flag_globalSuperTightHalo2016Filter_ ;
    Bool_t   Flag_HBHENoiseFilter_ ;
    Bool_t   Flag_HBHENoiseIsoFilter_ ;
    Bool_t   Flag_EcalDeadCellTriggerPrimitiveFilter_ ;
    Bool_t   Flag_BadPFMuonFilter_ ;
    Bool_t   Flag_ecalBadCalibFilterV2_ ;
    

};
#endif
