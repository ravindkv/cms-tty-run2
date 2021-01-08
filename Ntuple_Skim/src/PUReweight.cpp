#include"../interface/PUReweight.h"
#include<iostream>
//#include<TCanvas.h> 
PUReweight::PUReweight(int nFiles, char** fileNames, std::string PUfilename){
	PUweightSum = 0.0;
	events = 0;
	TFile* pileupFile = new TFile(PUfilename.c_str(),"READ");
	PUweightHist = (TH1D*)pileupFile->Get("pileup");
	PUweightHist->SetDirectory(0);
	pileupFile->Close();
	TH1D* PUbackup;

	int nBinsData = PUweightHist->GetNbinsX();

	if(PUweightHist->GetNbinsX() != 200){
		std::cout << "Wrong number of bins in the pileup histogram" << std::endl;
		PUbackup = new TH1D("pileup_new","pileup_new",200,0,200);
		for(int ibin=1; ibin <= PUweightHist->GetNbinsX(); ibin++){
			PUbackup->SetBinContent(ibin, PUweightHist->GetBinContent(ibin));
			// assuming the same scale
		}
		PUweightHist = PUbackup;
	}

	double PUweightInt = PUweightHist->Integral();


	TH1F* mcPU = NULL;
	for(int nmcfile = 0; nmcfile<nFiles; nmcfile++){
		//		std::cout << "reading file " << std::string(fileNames[nmcfile]) << std::endl;
		TFile* mcFile = TFile::Open(fileNames[nmcfile],"READ");
		if(!(mcFile->Get("hPUTrue"))) {
			std::cout << "no hPU histogram here!" << std::endl;
			delete PUweightHist;
			PUweightHist = NULL;
			return;
		}
		if( mcPU==NULL) mcPU = (TH1F*)mcFile->Get("hPUTrue");
		else mcPU->Add((TH1F*)mcFile->Get("hPUTrue"));
		mcPU->SetDirectory(0);
		mcFile->Close();
	}
	// TCanvas *c1 = new TCanvas("c1","A Simple Graph Example",1000,500);
	// c1->SetFillColor(0);
	// c1->SetGrid();

	// mcPU for some reason seems to be 1000 bins, rebin by 1000/200 (factor of 5) to get same binning in both to allow the scaling to work

	if (mcPU->GetNbinsX()!=PUweightHist->GetNbinsX()){
		if (mcPU->GetNbinsX()>PUweightHist->GetNbinsX()){
			mcPU->Rebin(mcPU->GetNbinsX()/PUweightHist->GetNbinsX());
		}
	}


	if (nBinsData!=200){
	    for(int ibin=nBinsData; ibin <= mcPU->GetNbinsX(); ibin++){
		mcPU->SetBinContent(ibin,0);
	    }
	}

	mcPU->Scale(1.0/mcPU->Integral());
	PUweightHist->Divide(mcPU);
	PUweightHist->Scale(1.0/PUweightInt);
	// PUweightHist->Draw();
	// c1->SaveAs("PUReweight.png");	
	delete mcPU;
}

PUReweight::~PUReweight(){
	delete PUweightHist;
}

double PUReweight::getWeight(Float_t puTrue){
    double PUweight=0.0;
    if(!PUweightHist) {
	std::cout << "you are calling getWeight by mistake" << std::endl; 
	return 1.0;
    }
    
    PUweight = PUweightHist->GetBinContent(PUweightHist->GetXaxis()->FindBin(puTrue));
    
    events++;
    PUweightSum+=PUweight;
    return PUweight;
}

double PUReweight::getAvgWeight(){
    if(events!=0) return PUweightSum/events;
    else return -1.0;
}
