#include<iostream>
#include<string>
#include"../interface/EventTree.h"
#include"../interface/Selector.h"
#include"../interface/EventPick.h"
#include<TFile.h>
#include<TTree.h>
#include<TDirectory.h>
#include<TObject.h>
#include<TH1F.h>
#include<TCanvas.h>
#include <boost/program_options.hpp>


// bool overlapRemovalTT(EventTree* tree);
// bool overlapRemovalWZ(EventTree* tree);
// bool overlapRemoval_Tchannel(EventTree* tree);


int main(int ac, char** av){
	if(ac < 4){
		std::cout << "usage: ./makeSkim year channel outputFileName inputFile[s]" << std::endl;
		return -1;
	}

	int eventNum = -1;
	std::string eventStr = "-1";

	std::cout << "Starting" << std::endl;

	// input: dealing with TTree first
	bool isMC = true;
	bool xRootDAccess = false;

	//TEMP
        if (std::string(av[1])=="event"){

	    std::string tempEventStr(av[2]);
	    eventNum = std::stoi(tempEventStr);
	    for (int i = 1; i < ac-2; i++){
		av[i] = av[i+2];
		//cout << av[i] << " ";
	    }
	    ac = ac-2;
	    //cout  << endl;
	    eventStr = tempEventStr;
	    //cout << eventStr << "  "  << eventNum << endl;
	}

	std::string year(av[1]);	

	//check if NofM type format is before output name (for splitting jobs)

	int nJob = -1;
	int totJob = -1;
	std::string checkJobs(av[3]);
	size_t pos = checkJobs.find("of");
	if (pos != std::string::npos){
	    nJob = std::stoi(checkJobs.substr(0,pos));
	    totJob = std::stoi(checkJobs.substr(pos+2,checkJobs.length()));
	    for (int i = 3; i < ac-1; i++){
		av[i] = av[i+1];
		//cout << av[i] << " ";
	    }
	    ac = ac-1;
	}
	cout << nJob << " of " << totJob << endl;
 
	std::string outDirName(av[3]);
	if( outDirName.find("Data") != std::string::npos){
	    isMC = false;
	}


	    
	

	//check for xrootd argument before file list
	//
	if (std::string(av[4])=="xrootd"){
	    xRootDAccess=true;
	    std::cout << "Will access files from xRootD" << std::endl;
	    for (int i = 4; i < ac-1; i++){
		av[i] = av[i+1];
		//cout << av[i] << " ";
	    }
	    ac = ac-1;
	}

	cout << av+5 << endl;

	bool splitByEvents=false;

	
	int nFiles = ac-4;
	int startFile = 0;

	if (nJob>0 && totJob>0){
	    if (ac-4 >= totJob){
		double filesPerJob = 1.*(ac-4)/totJob;
		cout << "Processing " << filesPerJob << " files per job on average" << endl;
		startFile = int((nJob-1)*filesPerJob);
		nFiles = int(nJob*filesPerJob) - startFile;
		cout << "   total of " << (ac-4) << " files" << endl;
		cout << "   this job will process files " << startFile << " to " << startFile+nFiles << endl;
	    } else {
		splitByEvents = true;
	    }
	    
	}

	char** fileList(av+4+startFile);


	EventTree* tree;

	tree = new EventTree(nFiles, xRootDAccess, year, fileList);


	// if (xRootDAccess){
	//     tree = new EventTree(ac-5, xRootDAccess, year, av+5);
	// } else {
	//     tree = new EventTree(ac-4, xRootDAccess, year, av+4);
	// }

	tree->isData_ = !isMC;

	if (eventNum > -1) {
	    string cut = "event=="+eventStr;
	    cout << "Selecting only entries with "<<cut << endl;
	    tree->chain = (TChain*) tree->chain->CopyTree(cut.c_str());
	}

	Selector* selector = new Selector();

	selector->smearJetPt = false;

	selector->smearEle = false;

	selector->scaleEle = false;



	selector->year = year;

	EventPick* evtPick = new EventPick("nominal");
	evtPick->MET_cut = -1.0;	

	evtPick->year = year;

	selector->printEvent = eventNum;
	evtPick->printEvent = eventNum;


	// antiselection for QCD fit
	// if( outDirName.find("QCD") != std::string::npos){
	// 	std::cout << "muon antiselection is on" << std::endl;
	// 	selector->mu_RelIso_range[0] = 0.25; 
	// 	selector->mu_RelIso_range[1] = 1.;
	// 	selector->mu_Iso_invert = true;
	// }

	// reduce the pt cuts by 10% in the skim, so that energy corrections can still be done on same skims
	selector->jet_Pt_cut = 27.;
	selector->ele_Pt_cut = 32.;
	selector->mu_Pt_cut = 27.;

	// remove the jet dR cuts, so we can play with these levels later on
	selector->veto_lep_jet_dR = -1;

	evtPick->SkimNjet_ge = 2;
	evtPick->SkimNBjet_ge = 0;
	std::string channel(av[2]);

	if (channel=="ele"){
		evtPick->skimEle = true;
	} else if (channel=="mu"){
		evtPick->skimMu = true;
	} else if (channel=="dimu"){
		evtPick->skimMu = true;
		evtPick->Nmu_eq = 2;
	} else if (channel=="diele"){
		evtPick->skimEle=true;
		evtPick->Nele_eq = 2;
	} else if (channel=="qcdele"){
		evtPick->skimEle=true;
		evtPick->Nele_eq = 1;
		selector->QCDselect = true;
	} else if (channel=="qcdmu"){
		evtPick->skimMu=true;
		evtPick->Nmu_eq = 1;
		selector->QCDselect = true;
	}else if (channel=="qcdDimu"){
		evtPick->skimMu=true;
		evtPick->Nele_eq = 2;
		selector->QCDselect = true;
	}else if (channel=="qcdDiele"){
		evtPick->skimEle=true;
		evtPick->Nele_eq = 2;
		selector->QCDselect = true;
	}else {
		cout << av[2] << endl;
		cout << (av[2]=="ele") << endl;
		cout << (channel=="ele") << endl;
		cout << "please specify either ele or mu for the skim channel (or diele/dimu)" << endl;
		return -1;		
	}

	auto startClock = std::chrono::high_resolution_clock::now();

	// std::clock_t startClock;
	// double duration;
	// startClock = clock();

	if (nJob>0 && totJob>0){
	    pos = outDirName.find(".root");
	    outDirName = outDirName.substr(0,pos) + "_" + checkJobs + ".root";
	    cout << "new output file name: "<< outDirName << endl;
	}

	TFile* outFile = TFile::Open( outDirName.c_str() ,"RECREATE" );
	TTree* newTree = tree->chain->CloneTree(0);
	newTree->SetCacheSize(50*1024*1024);

	Long64_t nEntr = tree->GetEntries();

	std::cout << "Sample has "<<nEntr << " entries" << std::endl;

	if( outDirName.find("Test") != std::string::npos || outDirName.find("test") != std::string::npos || outDirName.find("TEST") != std::string::npos){
		if (selector->QCDselect){
			std::cout << "-------------------------------------------------------------------------" << std::endl;
			std::cout << "Since this is a Test (based on output name) only running on 100,000 events" << std::endl;
			std::cout << "-------------------------------------------------------------------------" << std::endl;
			nEntr = 100000;
		}
		else{
			std::cout << "-------------------------------------------------------------------------" << std::endl;
			std::cout << "Since this is a Test (based on output name) only running on 50,001 events" << std::endl;
			std::cout << "-------------------------------------------------------------------------" << std::endl;
			if (nEntr>50001){
			    nEntr = 50001;
			}
		}
	}


	int startEntry = 0;
	int endEntry = nEntr;
	int eventsPerJob = nEntr;

	if (splitByEvents) {
	    eventsPerJob = int(1.*nEntr/totJob);
	    startEntry = (nJob-1)*eventsPerJob;
	    endEntry = nJob*eventsPerJob;
	    if (nJob==totJob){
		endEntry=nEntr;
	    }
	}
	cout << "Processing events "<<startEntry<< " to " << endEntry << endl;
	    

	int dumpFreq = 100;
	if (eventsPerJob >5000)   { dumpFreq = 1000; }
	if (eventsPerJob >50000)  { dumpFreq = 10000; }
	if (eventsPerJob >500000) { dumpFreq = 100000; }
	if (eventsPerJob >5000000){ dumpFreq = 1000000; }
	


	TH1F* hPU_        = new TH1F("hPU",        "number of pileup",      200,  0, 200);
	TH1F* hPUTrue_    = new TH1F("hPUTrue",    "number of true pilepu", 1000, 0, 200);

	TH1D* hEvents_    = new TH1D("hEvents",    "number of events (+/- event weight)",      3,  -1.5, 1.5);

	for(Long64_t entry= startEntry; entry < endEntry; entry++){
	//	for(Long64_t entry= 0; entry < 300; entry++){ 	
		if(entry%dumpFreq == 0) {
		    
			// duration =  ( clock() - startClock ) / (double) CLOCKS_PER_SEC;
			// std::cout << "processing entry " << entry << " out of " << nEntr << " : " << duration << " seconds since last progress" << std::endl;
			// startClock = clock();

			std::cout << "processing entry " << entry << " out of " << endEntry << " : " 
				  << std::chrono::duration<double>(std::chrono::high_resolution_clock::now()-startClock).count()
				  << " seconds since last progress" << std::endl;

			startClock = std::chrono::high_resolution_clock::now();			
		}
		tree->GetEntry(entry);

		//		if (tree->event_!=year) continue;
		
		hPU_->Fill(tree->nPU_);
		hPUTrue_->Fill(tree->nPUTrue_);

		hEvents_->Fill(tree->genWeight_/abs(tree->genWeight_));

		//selector->process_objects(tree);
		selector->clear_vectors();
		                              
		evtPick->process_event(tree,selector);

		if( evtPick->passSkim ){
			newTree->Fill();
		}
		
	        //std::cout << "finished with entry " <<  entry << std::endl;	
	}

	newTree->Write();
	hPU_->Write();
	hPUTrue_->Write();
	hEvents_->Write();

	// std::map<std::string, TH1F*> histMap;
	// copy histograms
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
	outFile->Close();

	
	return 0;
}
