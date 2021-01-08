#include "../interface/EventPick_Skim.h"
#include <iostream> 
#include <iomanip>


//double secondMinDr(int myInd, const EventTree* tree);

EventPick::EventPick(std::string titleIn){
    title = titleIn;
    year = "2016";
    saveCutflows = false;
    
    printEvent = -1;

    no_trigger = false;
	
    Njet_ge = 1;

}

EventPick::~EventPick(){
}

void EventPick::process_event(EventTree* tree){

    //	clear_vectors();
    passSkim = false;
    passPresel_ele = false;
    passPresel_mu = false;
    passAll_ele = false;
    passAll_mu = false;

    if (tree->event_==printEvent){
	cout << "Found Event Number " << printEvent << endl;
    }
    bool applyMetFilter   = false;
    bool Pass_trigger_mu  = false;
    bool Pass_trigger_ele = false;

    if (year=="2016") {
	Pass_trigger_mu = (tree->HLT_IsoMu24_ || tree->HLT_IsoTkMu24_);
	Pass_trigger_ele = (tree->HLT_Ele27_WPTight_Gsf_);
    }
    if (year=="2017"){
	Pass_trigger_mu = (tree->HLT_IsoMu24_ || tree->HLT_IsoMu27_);
	Pass_trigger_ele = (tree->HLT_Ele32_WPTight_Gsf_L1DoubleEG_ || tree->HLT_Ele32_WPTight_Gsf_);
    }
    if (year=="2018"){
	Pass_trigger_mu = (tree->HLT_IsoMu24_ || tree->HLT_IsoMu27_);
	Pass_trigger_ele = (tree->HLT_Ele32_WPTight_Gsf_ || tree->HLT_Ele35_WPTight_Gsf_);
    }

    bool filters = (tree->Flag_goodVertices_ &&
		    tree->Flag_globalSuperTightHalo2016Filter_ &&
		    tree->Flag_HBHENoiseFilter_ &&
		    tree->Flag_HBHENoiseIsoFilter_ && 
		    tree->Flag_EcalDeadCellTriggerPrimitiveFilter_ &&
		    tree->Flag_BadPFMuonFilter_ );

    if (year=="2017" || year=="2018"){ filters = filters && tree->Flag_ecalBadCalibFilterV2_ ;}

    //comment out following two line when no filter is needed
    if(applyMetFilter){
	Pass_trigger_mu = Pass_trigger_mu && filters ;     
	Pass_trigger_ele = Pass_trigger_ele && filters ;     
    }
    passSkim = (Pass_trigger_ele || Pass_trigger_mu) && filters;


    // if (!passSkim){
    // 	return;
    // }

    // int jetCount = 0;
    // for(int jetInd = 0; jetInd < tree->nJet_; ++jetInd){
    // 	int jetID_cutBit = 1;
    // 	if (year=="2016"){ jetID_cutBit = 0; }
	
    //     bool jetID_pass = (tree->jetID_[jetInd]>>jetID_cutBit & 1);
    // 	if (jetID_pass) {
    // 	    jetCount += 1;
    // 	}
    // }

    // if (jetCount==0){
    // 	passSkim=false;
    // }



    // // split skim into ele and mu
    // if ( (skimEle && passPresel_ele) || (skimMu && passPresel_mu) && selector->Jets.size() >= SkimNjet_ge && selector->bJets.size() >= SkimNBjet_ge ){ passSkim = true; }




    // // NJet cuts for electrons
    // // Implemented in this way (with a loop) to check for numbers failing each level of cut < Njet cut, and filling cutflow histo
    // // cutflow histo will not be filled for bins where the cut is > Njet_ge (ex, if cut is at 3, Njets>=4 bin is left empty)
    // for (int ijetCut = 1; ijetCut <= Njet_ge; ijetCut++){
    // 	if(passPresel_ele && selector->Jets.size() >= ijetCut ) { if (saveCutflows) {cutFlow_ele->Fill(5+ijetCut); cutFlowWeight_ele->Fill(5+ijetCut,weight);}}
    
}

