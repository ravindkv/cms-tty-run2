#include<iostream>
#include<string>
#include"EventTree.h"
#include"Selector.h"
#include"EventPick.h"
#include<TFile.h>
#include<TTree.h>
#include<TDirectory.h>
#include<TObject.h>
#include<TH1F.h>
#include<TCanvas.h>

std::string PUfilename = "Data_2017BCDEF.root";
//std::string PUfilename = "Data_2016BCDGH_Pileup.root";
std::string PUfilename_up = "Data_2016BCDGH_Pileup_scaledUp.root";
std::string PUfilename_down = "Data_2016BCDGH_Pileup_scaledDown.root";

#include"PUReweight.h"
#include "BTagCalibrationStandalone.h"
#include "ScaleFactors.h"
#include "elemuSF.h"

bool overlapRemovalTT(EventTree* tree);
double getBtagSF(EventTree *tree, Selector *selector,  string sysType, BTagCalibrationReader reader, int NBjet_ge);

int main(int ac, char** av){
	if(ac < 4){
		std::cout << "usage: ./makeCutflows sampleType outputFile inputFile[s]" << std::endl;
		return -1;
	}

	string sampleType = av[1];
	string systematicType = "";
	cout << sampleType << endl;

	size_t pos = sampleType.find("__");
	if (pos != std::string::npos){
		systematicType = sampleType.substr(pos+2,sampleType.length());
		sampleType = sampleType.substr(0,pos);
	}

    cout << sampleType << "  " << systematicType << endl;


	if (std::end(allowedSampleTypes) == std::find(std::begin(allowedSampleTypes), std::end(allowedSampleTypes), sampleType)){
		cout << "This is not an allowed sample, please specify one from this list (or add to this list in the code):" << endl;
		for (int i =0; i < sizeof(allowedSampleTypes)/sizeof(allowedSampleTypes[0]); i++){
			cout << "    "<<allowedSampleTypes[i] << endl;
		}			
		return -1;
	}


	bool isMC = (sampleType.find("Data") == std::string::npos);
	PUReweight* PUweighter;

	if (isMC) {
		PUweighter = new PUReweight(ac-3, av+3, PUfilename);
	}

	bool doOverlapRemoval = false;
	bool doOverlapRemoval_WZ = false;	
	bool skipOverlap = false;
	if( sampleType == "TTbarPowheg" || sampleType == "TTbarMCatNLO") doOverlapRemoval = true;
	if( sampleType == "W1jets" || sampleType == "W2jets" ||  sampleType == "W3jets" || sampleType == "W4jets" || sampleType=="DYjetsM10to50" || sampleType=="DYjetsM50") doOverlapRemoval_WZ = true;
	if(doOverlapRemoval || doOverlapRemoval_WZ) std::cout << "########## Will apply overlap removal ###########" << std::endl;


//	EventTree* tree = new EventTree(ac-3, av+3);
//	EventTree* tree = new EventTree(ac-4, false, year, av+4);
	EventTree* tree = new EventTree(ac-3, false, "2017", av+3);
	//EventTree* tree = new EventTree(ac-4, false, "2017", av[3]);
       // cout<<"tree arg"<<av[3]<<endl;
	Selector* selector = new Selector();
	double _evtWeight = getEvtWeight(sampleType);



	EventPick* evtPick = new EventPick("nominal");
	// evtPick->MET_cut = 0;

	evtPick->saveCutflows = true;
        evtPick->year="2017";
	//selector->looseJetID = false;

	selector->useDeepCSVbTag = true;

	evtPick->Njet_ge = 4;	
	evtPick->NBjet_ge = 1;	
        evtPick->Npho_ge = 1;
	//	selector->veto_jet_pho_dR = -1.;
	//	selector->veto_pho_jet_dR = -1.;


	bool dileptonsample = false;
/*	if( systematicType=="Dilep")     {
		dileptonsample =true; 
		evtPick->Nmu_eq=2; 
		evtPick->Nele_eq=2;
		evtPick->Njet_ge = 2;	
		evtPick->NBjet_ge = 1;	
	}
	std::cout << "Dilepton Sample :" << dileptonsample << std::endl;

*/

	
	BTagCalibration calib;
	if (!selector->useDeepCSVbTag){
		calib = BTagCalibration("csvv2", "CSVv2_Moriond17_B_H.csv");
	} else {
	//	calib = BTagCalibration("deepcsv", "DeepCSV_Moriond17_B_H.csv");
		calib = BTagCalibration("deepcsv", "DeepCSV_94XSF_V3_B_F.csv");
	}

	BTagCalibrationReader reader(BTagEntry::OP_MEDIUM,  // operating point
								 "central");             // central sys type

	if (isMC){
		reader.load(calib,                // calibration instance
					BTagEntry::FLAV_B,    // btag flavour
					"comb");               // measurement type
		
		reader.load(calib,                // calibration instance
					BTagEntry::FLAV_C,    // btag flavour
					"comb");               // measurement type
		
		reader.load(calib,                // calibration instance
					BTagEntry::FLAV_UDSG,    // btag flavour
					"incl");               // measurement type
	}



	selector->smearJetPt = false;

	double _PUweight;
	double _muWeight;
	double _eleWeight;
	double _btagWeight;

	Long64_t nEntr = tree->GetEntries();
	std::string outDirName(av[2]);

	int dumpFreq = 100;
	if (nEntr >5000)    { dumpFreq = 500; }
	if (nEntr >10000)   { dumpFreq = 1000; }
	if (nEntr >50000)   { dumpFreq = 5000; }
	if (nEntr >100000)  { dumpFreq = 10000; }
	if (nEntr >500000)  { dumpFreq = 50000; }
	if (nEntr >1000000) { dumpFreq = 100000; }
	if (nEntr >5000000) { dumpFreq = 500000; }
	if (nEntr >10000000){ dumpFreq = 1000000; }
	
	dumpFreq=10000;
	for(Long64_t entry= 0; entry < nEntr; entry++){
		if(entry%dumpFreq == 0) {
			std::cout << "processing entry " << entry << " out of " << nEntr << std::endl;
		}
		tree->GetEntry(entry);

		if( isMC && doOverlapRemoval){
			if (overlapRemovalTT(tree)){
				//				cout << "removing event " << entry << endl;
				continue;
			}
		}

		
		selector->process_objects(tree);
	   
		//add in the weights
		double weight = 1.;
		if (isMC){
			weight = _evtWeight *  ((tree->genWeight_ >= 0) ? 1 : -1);
                         _PUweight    = PUweighter->getWeight(tree->nPUTrue_);
		//	_PUweight    = PUweighter->getWeight(tree->nPUInfo_, tree->puBX_, tree->puTrue_);
	//	_PUweight=1;	
			weight *= _PUweight;

			if (selector->Muons.size()==1) {
				int muInd_ = selector->Muons.at(0);
				_muWeight    = getMuSF(tree->muPt_[muInd_],tree->muEta_[muInd_],1);
				weight *= _muWeight;
			}

			if (selector->Electrons.size()==1) {
				int eleInd_ = selector->Electrons.at(0);
				//_eleWeight    = getEleSF(tree->elePt_[eleInd_],tree->eleSCEta_[eleInd_],1);
				_eleWeight    = getEleSF(tree->elePt_[eleInd_],tree->eleEta_[eleInd_],1);
				weight *= _eleWeight;
			}

			_btagWeight    = getBtagSF(tree, selector, "central", reader, evtPick->NBjet_ge);
			weight *= _btagWeight;
		}

		evtPick->process_event(tree,selector,weight);


		// if (evtPick->passPresel_mu){
		// 	cout << tree->event_ << endl;// "  " << tree->phoEt_->at(selector->PhotonsPresel.at(0)) << endl;
		// 	cout << tree->event_ << endl;// "  " << tree->phoEt_->at(selector->PhotonsPresel.at(0)) << endl;
		// }

	}

	std::cout << "e+jets cutflow" << std::endl;
	evtPick->print_cutflow_ele(evtPick->cutFlow_ele);

	std::cout << "mu+jets cutflow" << std::endl;
	evtPick->print_cutflow_mu(evtPick->cutFlow_mu);

	TFile* outputFile = TFile::Open(av[2],"RECREATE");

	outputFile->cd();
	evtPick->cutFlow_mu->Write();
	evtPick->cutFlow_ele->Write();
	evtPick->cutFlowWeight_mu->Write();
	evtPick->cutFlowWeight_ele->Write();
	outputFile->Close();


	// std::map<std::string, TH1F*> histMap;
	// // copy histograms
	// for(int fileInd = 3; fileInd < ac; ++fileInd){
	// 	TFile* tempFile = TFile::Open(av[fileInd], "READ");
	// 	TIter next(((TDirectory*)tempFile->Get("ggNtuplizer"))->GetListOfKeys());
	// 	TObject* obj;
	// 	while ((obj = next())){
	// 		std::string objName(obj->GetName());
	// 		if( objName != "EventTree"){
	// 			TH1F* hist = (TH1F*)tempFile->Get(("ggNtuplizer/"+objName).c_str());
	// 			if( histMap.find(objName) != histMap.end() ){
	// 				histMap[objName]->Add(hist);
	// 			}
	// 			else {
	// 				hist->SetDirectory(0);
	// 				histMap[objName] = hist;
	// 			}
	// 		}
	// 	}
	// 	tempFile->Close();
	// }
	
	// ggDir->cd();
	// for(std::map<std::string, TH1F*>::iterator it = histMap.begin(); it!= histMap.end(); ++it){
	// 	it->second->SetDirectory(ggDir);
	// 	it->second->Write();
	// }
	// outFile->Close();
	
	return 0;
}


double getBtagSF(EventTree *tree, Selector *selector,  string sysType, BTagCalibrationReader reader, int NBjet_ge){
	
	double weight0tag = 1.0; 		//w(0|n)
	double weight1tag = 0.0;		//w(1|n)

	double jetpt;
	double jeteta;
	int jetflavor;
	double SFb;
	double SFb2;

	if(selector->bJets.size() == 0) {
		return 1.0;
	}

	// We are following the method 1c from the twiki
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagSFMethods#1c_Event_reweighting_using_scale

	for(std::vector<int>::const_iterator bjetInd = selector->bJets.begin(); bjetInd != selector->bJets.end(); bjetInd++){
		jetpt = tree->jetPt_[*bjetInd];
		jeteta = fabs(tree->jetEta_[*bjetInd]);
		//jetflavor = abs(tree->jetPartonID_[*bjetInd]);
		jetflavor = tree->jetHadFlvr_[*bjetInd];
		
		if (jetflavor == 5) SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_B, jeteta, jetpt); 
		else if(jetflavor == 4) SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_C, jeteta, jetpt); 
		else SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_UDSG, jeteta, jetpt); 

		weight0tag *= 1.0 - SFb;


		// We also have to calculate the weight for having 1 tag, given N
		double prod = 1.;
		if (NBjet_ge==2){
			for(std::vector<int>::const_iterator bjetInd2 = selector->bJets.begin(); bjetInd2 != selector->bJets.end(); bjetInd2++){
				if (*bjetInd==*bjetInd2) continue;

				jetpt = tree->jetPt_[*bjetInd2];
				jeteta = fabs(tree->jetEta_[*bjetInd2]);
				//jetflavor = abs(tree->jetPartonID_[*bjetInd2]);
		                jetflavor = tree->jetHadFlvr_[*bjetInd];

				if (jetflavor == 5) SFb2 = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_B, jeteta, jetpt); 
				else if(jetflavor == 4) SFb2 = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_C, jeteta, jetpt); 
				else SFb2 = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_UDSG, jeteta, jetpt); 

				//product of (1-SFi), i!=j in twiki example (method 1c)
				prod *= 1.0 - SFb2;
			}

			//w(1|n) sum, SFj times product of 1-SFi
			weight1tag += prod*SFb;
		}
	}

	return 1.0 - weight0tag - weight1tag;
}

