#include<iostream>
#include<string>
#include"EventTree.h"
#include<TFile.h>
#include<TTree.h>
#include<TDirectory.h>
#include<TObject.h>

bool overlapRemovalTT(EventTree* tree);
bool overlapRemovalWZ(EventTree* tree);
bool overlapRemoval_Tchannel(EventTree* tree);

int main(int ac, char** av){
	if(ac < 4){
		std::cout << "usage: ./makeSkim channel outputFileName inputFile[s]" << std::endl;
		return -1;
	}
	// input: dealing with TTree first
	bool isMC = true;
	EventTree* tree = new EventTree(ac-3, av+3);

	std::string channel(av[1]);

	std::string outDirName(av[2]);

	Long64_t nEntr = tree->GetEntries();

	if( outDirName.find("Test") != std::string::npos || outDirName.find("test") != std::string::npos || outDirName.find("TEST") != std::string::npos){
		std::cout << "-------------------------------------------------------------------------" << std::endl;
		std::cout << "Since this is a Test (based on output name) only running on 10,000 events" << std::endl;
		std::cout << "-------------------------------------------------------------------------" << std::endl;
		nEntr = 10000;
	}


	bool doOverlapRemoval_TT = false;
	bool doOverlapRemoval_WZ = false;	
	bool doOverlapRemoval_Tchannel = false;	
	bool skipOverlap = false;

	if( outDirName.find("TTbar") != std::string::npos) {
		doOverlapRemoval_TT = true;
	}

	if( outDirName.find("W1Jets") != std::string::npos || outDirName.find("W2Jets") != std::string::npos || outDirName.find("W3Jets") != std::string::npos || outDirName.find("W4Jets") != std::string::npos || outDirName.find("DYjetsM10to50") != std::string::npos || outDirName.find("DYjetsM50") != std::string::npos) {
		doOverlapRemoval_WZ = true;
	}

	if( outDirName.find("ST_t-channel") != std::string::npos || outDirName.find("ST_tbar-channel") != std::string::npos) {
		doOverlapRemoval_Tchannel = true;
	}


	if(doOverlapRemoval_TT || doOverlapRemoval_WZ || doOverlapRemoval_Tchannel) std::cout << "########## Will apply overlap removal ###########" << std::endl;


	int count_overlapTchannel=0;
	int count_overlapVJets=0;
	int count_overlapTTbar=0;

	

	int dumpFreq = 100;
	if (nEntr >5000)   { dumpFreq = 1000; }
	if (nEntr >50000)  { dumpFreq = 10000; }
	if (nEntr >500000) { dumpFreq = 100000; }
	if (nEntr >5000000){ dumpFreq = 1000000; }
	

	for(Long64_t entry= 0; entry < nEntr; entry++){
		if(entry%dumpFreq == 0) {
			std::cout << "processing entry " << entry << " out of " << nEntr << std::endl;
		}
		tree->GetEntry(entry);

		isMC = !(tree->isData_);

		if( isMC && doOverlapRemoval_TT){
			if (overlapRemovalTT(tree)){
				count_overlapTTbar++;			
				continue;
			}
		}
		if( isMC && doOverlapRemoval_WZ){
			if (overlapRemovalWZ(tree)){
				count_overlapVJets++;
				continue;
			}
		}
		if( isMC && doOverlapRemoval_Tchannel){
			if (overlapRemoval_Tchannel(tree)){
				count_overlapTchannel++;
				continue;
			}
		}
		
	}

	if (doOverlapRemoval_TT){
		std::cout << "Total number of events removed from TTbar:"<< count_overlapTTbar <<std::endl;
	}
	if(doOverlapRemoval_WZ){
		 std::cout << "Total number of events removed from W/ZJets:"<< count_overlapVJets <<std::endl;
	}
	if(doOverlapRemoval_Tchannel){
		 std::cout << "Total number of events removed from t-channel:"<< count_overlapTchannel <<std::endl;
	}

	
	return 0;
}
