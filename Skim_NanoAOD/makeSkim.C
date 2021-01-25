#include<iostream>
#include<string>
#include "interface/EventTree_Skim.h"
#include "interface/EventPick_Skim.h"
#include<TFile.h>
#include<TTree.h>
#include<TDirectory.h>
#include<TObject.h>
#include<TH1F.h>
#include<TCanvas.h>
#include <boost/program_options.hpp>


int main(int ac, char** av){

    if (std::string(av[1])=="git"){
        printf("Git Commit Number: %s\n", VERSION);
        printf("Git Commit Time: %s\n", COMMITTIME);
        printf("Git Branch: %s\n", BRANCH);
        printf("Git Status: %s\n", STATUS);
        bool gitStatus = std::string(STATUS)=="" ;
        if (!gitStatus){
            return 1;
        } else {
            return 0;
        }
    }

	if(ac < 3){
		std::cout << "usage: ./makeSkim year outputFileName inputFile[s]" << std::endl;
		return -1;
	}

	int eventNum = -1;
	std::string eventStr = "-1";

	std::cout << "Starting" << std::endl;

        printf("Git Commit Number: %s\n", VERSION);
        printf("Git Commit Time: %s\n", COMMITTIME);
        printf("Git Branch: %s\n", BRANCH);
        printf("Git Status: %s\n", STATUS);

        if (STATUS != ""){
            cout << endl;
            cout <<"=============================================" << endl;
            cout <<"=============================================" << endl;
            cout <<"Warning, files are missing from github" << endl;
            cout <<"=============================================" << endl;
            cout <<"=============================================" << endl;
            cout << endl;
        }

	// input: dealing with TTree first
	bool isMC = true;
	bool xRootDAccess = false;

	bool passAll=false;
        if (std::string(av[1])=="passAll"){
	    passAll = true;
	    cout << "Keeping all events, no skim" << endl;
	    for (int i = 1; i < ac-1; i++){
		av[i] = av[i+1];
		//cout << av[i] << " ";
	    }
	    ac = ac-1;
	}

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
	std::string checkJobs(av[2]);
	size_t pos = checkJobs.find("of");
	if (pos != std::string::npos){
	    nJob = std::stoi(checkJobs.substr(0,pos));
	    totJob = std::stoi(checkJobs.substr(pos+2,checkJobs.length()));
	    for (int i = 2; i < ac-1; i++){
		av[i] = av[i+1];
		//cout << av[i] << " ";
	    }
	    ac = ac-1;
	}
	cout << nJob << " of " << totJob << endl;
 
	std::string outDirName(av[2]);
	if( outDirName.find("Data") != std::string::npos){
	    cout << "IsData" << endl;
	    isMC = false;
	}


	//check for xrootd argument before file list
	//
	if (std::string(av[3])=="xrootd"){
	    xRootDAccess=true;
	    std::cout << "Will access files from xRootD" << std::endl;
	    for (int i = 3; i < ac-1; i++){
		av[i] = av[i+1];
		//cout << av[i] << " ";
	    }
	    ac = ac-1;
	}

	//	cout << av+4 << endl;

	bool splitByEvents=false;

	
	int nFiles = ac-3;
	int startFile = 0;

	if (nJob>0 && totJob>1){
	    if (ac-3 >= totJob){
		double filesPerJob = 1.*(ac-3)/totJob;
		cout << "Processing " << filesPerJob << " files per job on average" << endl;
		startFile = int((nJob-1)*filesPerJob);
		nFiles = int(nJob*filesPerJob) - startFile;
		cout << "   total of " << (ac-3) << " files" << endl;
		cout << "   this job will process files " << startFile << " to " << startFile+nFiles << endl;
	    } else {
		splitByEvents = true;
	    }
	    
	}

	char** fileList(av+3+startFile);

	cout << "HERE" << endl;
	EventTree* tree;

	tree = new EventTree(nFiles, xRootDAccess, year, fileList, isMC);


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

	EventPick* evtPick = new EventPick("nominal");

	evtPick->year = year;

	evtPick->printEvent = eventNum;


	auto startClock = std::chrono::high_resolution_clock::now();

	// std::clock_t startClock;
	// double duration;
	// startClock = clock();

	if (nJob>0 && totJob>0){
	    pos = outDirName.find(".root");
	    outDirName = outDirName.substr(0,pos) + "_" + checkJobs + ".root";
	    cout << "new output file name: "<< outDirName << endl;
	}

	TFile* outFile = TFile::Open( outDirName.c_str() ,"RECREATE","",207 );
	TTree* newTree = tree->chain->CloneTree(0);
	newTree->SetCacheSize(50*1024*1024);

	Long64_t nEntr = tree->GetEntries();

	std::cout << "Sample has "<<nEntr << " entries" << std::endl;

	if( outDirName.find("Test") != std::string::npos || outDirName.find("test") != std::string::npos || outDirName.find("TEST") != std::string::npos){
	    std::cout << "-------------------------------------------------------------------------" << std::endl;
	    std::cout << "Since this is a Test (based on output name) only running on 10,000 events" << std::endl;
	    std::cout << "-------------------------------------------------------------------------" << std::endl;
	    if (nEntr>10000){
		nEntr = 10000;
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
	TH1F* hPUTrue_    = new TH1F("hPUTrue",    "number of true pilepu", 200, 0, 200);

	TH1D* hEvents_    = new TH1D("hEvents",    "number of events (+/- event weight)",      3,  -1.5, 1.5);

	for(Long64_t entry= startEntry; entry < endEntry; entry++){
		if(entry%dumpFreq == 0) {
            if(entry>1000) break;
		    
			// duration =  ( clock() - startClock ) / (double) CLOCKS_PER_SEC;
			// std::cout << "processing entry " << entry << " out of " << nEntr << " : " << duration << " seconds since last progress" << std::endl;
			// startClock = clock();

			std::cout << "processing entry " << entry << " out of " << endEntry << " : " 
				  << std::chrono::duration<double>(std::chrono::high_resolution_clock::now()-startClock).count()
				  << " seconds since last progress" << std::endl;

			startClock = std::chrono::high_resolution_clock::now();			
		}
		tree->GetEntry(entry);
		
		hPU_->Fill(tree->nPU_, tree->genWeight_);
		hPUTrue_->Fill(tree->nPUTrue_, tree->genWeight_);
		if (isMC) {
		    hEvents_->Fill(tree->genWeight_/abs(tree->genWeight_));
		    hEvents_->Fill(0.,tree->genWeight_);
		}
		else {
		    hEvents_->Fill(1.);
		    hEvents_->Fill(0.);
		}

		evtPick->process_event(tree);

		if( evtPick->passSkim || passAll){
			newTree->Fill();
		}
	}

	newTree->Write();
	hPU_->Write();
	hPUTrue_->Write();
	hEvents_->Write();

        TNamed gitCommit("Git_Commit", VERSION);
        TNamed gitTime("Git_Commit_Time", COMMITTIME);
        TNamed gitBranch("Git_Branch", BRANCH);
        TNamed gitStatus("Git_Status", STATUS);

        gitCommit.Write();
        gitTime.Write();
        gitBranch.Write();
        gitStatus.Write();
    
	outFile->Close();

	
	return 0;
}
