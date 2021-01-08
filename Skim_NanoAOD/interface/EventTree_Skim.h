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
    EventTree(int nFiles, bool xRootDAccess, string year, char** fileNames, bool isMC);
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
    
    bool isData_;

    Int_t    nPU_;  
    Float_t  nPUTrue_;  
    
    UInt_t   nJet_;  
    Int_t   jetID_[200];
    
    Bool_t  HLT_IsoMu24_;
    Bool_t  HLT_IsoTkMu24_;
    Bool_t  HLT_IsoMu24_eta2p1_;
    Bool_t  HLT_IsoMu27_;
    Bool_t  HLT_Mu45_eta2p1_;
    Bool_t  HLT_Mu50_;
    Bool_t  HLT_TkMu50_;
    Bool_t  HLT_OldMu100_;
    Bool_t  HLT_TkMu100_;

    Bool_t  HLT_Ele27_WPTight_Gsf_;
    Bool_t  HLT_Ele32_WPTight_Gsf_;
    Bool_t  HLT_Ele32_WPTight_Gsf_L1DoubleEG_;
    Bool_t  HLT_Ele35_WPTight_Gsf_;
    Bool_t  HLT_Ele38_WPTight_Gsf_;
    Bool_t  HLT_Ele105_CaloIdVT_GsfTrkIdT_;
    Bool_t  HLT_Ele115_CaloIdVT_GsfTrkIdT_;
    Bool_t  HLT_DoubleEle25_CaloIdL_MW_;
    Bool_t  HLT_Photon175_;
    Bool_t  HLT_Photon200_;

    Bool_t   HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_;
    Bool_t   HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_;
    Bool_t   HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_;
    Bool_t   HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_;
    Bool_t   HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_;
    Bool_t   HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_;
    
    Bool_t   Flag_goodVertices_ ;
    Bool_t   Flag_globalSuperTightHalo2016Filter_ ;
    Bool_t   Flag_HBHENoiseFilter_ ;
    Bool_t   Flag_HBHENoiseIsoFilter_ ;
    Bool_t   Flag_EcalDeadCellTriggerPrimitiveFilter_ ;
    Bool_t   Flag_BadPFMuonFilter_ ;
    Bool_t   Flag_ecalBadCalibFilterV2_ ;
    

};
#endif
