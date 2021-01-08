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

std::string PUfilename = "Data_2016BCDGH_Pileup.root";
std::string PUfilename_up = "Data_2016BCDGH_Pileup_scaledUp.root";
std::string PUfilename_down = "Data_2016BCDGH_Pileup_scaledDown.root";

#include"PUReweight.h"
#include "BTagCalibrationStandalone.h"
#include "ScaleFactors.h"
#include "elemuSF.h"

bool overlapRemovalTT(EventTree* tree);
double getBtagSF(EventTree *tree, Selector_gen *selector_gen,  string sysType, BTagCalibrationReader reader, int NBjet_ge);

int main(int ac, char** av){
        if(ac < 4){
                std::cout << "usage: ./makeSkim channel outputFileName inputFile[s]" << std::endl;
                return -1;
        }
	bool isMC = true;
        EventTree* tree = new EventTree(ac-3, av+3);
        Selector_gen* selector_gen = new Selector_gen();


        EventPick_gen* evtPick_gen = new EventPick_gen("nominal");
        evtPick_gen->MET_cut = -1.0;
        std::string outDirName(av[2]);

        evtPick_gen->SkimNjet_ge = 4;
        evtPick_gen->SkimNBjet_ge = 1;
        std::string channel(av[1]);

	std::clock_t startClock;
        double duration;
        startClock = clock();

        TFile* outFile = TFile::Open( av[2] ,"RECREATE" );
        TDirectory* ggDir = outFile->mkdir("ggNtuplizer","ggNtuplizer");
        ggDir->cd();
        TTree* newTree = tree->chain->CloneTree(0);

        Long64_t nEntr = tree->GetEntries();




        int dumpFreq = 100;
        if (nEntr >5000)   { dumpFreq = 1000; }
        if (nEntr >50000)  { dumpFreq = 10000; }
        if (nEntr >500000) { dumpFreq = 100000; }
        if (nEntr >5000000){ dumpFreq = 1000000; }

	for(Long64_t entry= 0; entry < nEntr; entry++){
			if(entry%dumpFreq == 0) {
                        duration =  ( clock() - startClock ) / (double) CLOCKS_PER_SEC;
                        std::cout << "processing entry " << entry << " out of " << nEntr << " : " << duration << " seconds since last progress" << std::endl;
                        startClock = clock();
                       }
                	tree->GetEntry(entry);

                	isMC = !(tree->isData_);
			evtPick_gen->process_event(tree,selector_gen);

                	if( evtPick_gen->passSkim ){
                        newTree->Fill();
                	}

		}
	
	newTree->Write();

//	}

	std::cout << "e+jets cutflow" << std::endl;
	evtPick_gen->print_cutflow_ele(evtPick_gen->cutFlow_ele);

	std::cout << "mu+jets cutflow" << std::endl;
	evtPick_gen->print_cutflow_mu(evtPick_gen->cutFlow_mu);

//	TFile* outFile = TFile::Open(av[2],"RECREATE");

	outFile->cd();
	evtPick_gen->cutFlow_mu->Write();
	evtPick_gen->cutFlow_ele->Write();
	evtPick_gen->cutFlowWeight_mu->Write();
	evtPick_gen->cutFlowWeight_ele->Write();
	outFile->Close();


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


double getBtagSF(EventTree *tree, Selector_gen *selector_gen,  string sysType, BTagCalibrationReader reader, int NBjet_ge){
	
	double weight0tag = 1.0; 		//w(0|n)
	double weight1tag = 0.0;		//w(1|n)

	double jetpt;
	double jeteta;
	int jetflavor;
	double SFb;
	double SFb2;

	if(selector_gen->bJets.size() == 0) {
		return 1.0;
	}

	// We are following the method 1c from the twiki
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagSFMethods#1c_Event_reweighting_using_scale

	for(std::vector<int>::const_iterator bjetInd = selector_gen->bJets.begin(); bjetInd != selector_gen->bJets.end(); bjetInd++){
		jetpt = tree->jetGenJetPt_->at(*bjetInd);
		jeteta = fabs(tree->jetGenJetEta_->at(*bjetInd));
		jetflavor = abs(tree->jetGenPartonID_->at(*bjetInd));
		
		if (jetflavor == 5) SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_B, jeteta, jetpt); 
		else if(jetflavor == 4) SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_C, jeteta, jetpt); 
		else SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_UDSG, jeteta, jetpt); 

		weight0tag *= 1.0 - SFb;


		// We also have to calculate the weight for having 1 tag, given N
		double prod = 1.;
		if (NBjet_ge==2){
			for(std::vector<int>::const_iterator bjetInd2 = selector_gen->bJets.begin(); bjetInd2 != selector_gen->bJets.end(); bjetInd2++){
				if (*bjetInd==*bjetInd2) continue;

				jetpt = tree->jetGenJetPt_->at(*bjetInd2);
				jeteta = fabs(tree->jetGenJetEta_->at(*bjetInd2));
				jetflavor = abs(tree->jetGenPartonID_->at(*bjetInd2));

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

