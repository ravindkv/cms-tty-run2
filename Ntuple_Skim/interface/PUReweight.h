
#ifndef PUREWEIGHT_H
#define PUREWEIGHT_H

#include<TH1F.h>
#include<TFile.h>
#include<iostream>
#include<vector>
#include<string>

class PUReweight{
public:
	PUReweight(int nFiles, char** fileNames, std::string PUfilename);
	~PUReweight();
	double getWeight(Float_t puTrue);
	double getAvgWeight();
	
private:
	double PUweightSum;
	long int events;
	TH1D* PUweightHist;
};

#endif
