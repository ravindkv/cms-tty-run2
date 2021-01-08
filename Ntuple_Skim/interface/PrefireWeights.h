#include<TH2F.h>
#include<TFile.h>

#include <iostream>
#include "EventTree.h"
#include "Utils.h"

using namespace std;

enum fluctuations { central = 1, up=2, down=0 };

class PrefireWeights
{
 public:
    PrefireWeights(string pho_fileName, string pho_histName, string jet_fileName, string jet_histName){
	TFile* phoFile = TFile::Open(pho_fileName.c_str(),"READ");
	TFile* jetFile = TFile::Open(jet_fileName.c_str(),"READ");

	phoEffHist = (TH2F*) phoFile->Get(pho_histName.c_str());
	jetEffHist = (TH2F*) jetFile->Get(jet_histName.c_str());
    }

    void getPrefireSF(EventTree* tree, float* scaleFactors);

    float prefiringRateSystUnc_=0.2;
    bool useEMpt_ = false;

 private:
    TH2F* phoEffHist;
    TH2F* jetEffHist;


    float getPrefiringRate(double eta, double pt, TH2F* h_prefmap, int fluctuation) const;
};


//implementation of prefiring algorith
// modeled after https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/PatUtils/plugins/L1ECALPrefiringWeightProducer.cc
float PrefireWeights::getPrefiringRate(double eta,
				       double pt,
				       TH2F* h_prefmap,
				       int fluctuation) const {
    

    int nbinsy = h_prefmap->GetNbinsY();
    double maxy = h_prefmap->GetYaxis()->GetBinLowEdge(nbinsy + 1);
    if (pt >= maxy)
	pt = maxy - 0.01;

    int thebin = h_prefmap->FindBin(eta, pt);
    
    float prefrate = h_prefmap->GetBinContent(thebin);

    float statuncty = h_prefmap->GetBinError(thebin);
    float systuncty = prefiringRateSystUnc_ * prefrate;

    if (fluctuation == 2)
	prefrate = std::min(1., prefrate + sqrt(pow(statuncty, 2) + pow(systuncty, 2)));
    if (fluctuation == 0)
	prefrate = std::max(0., prefrate - sqrt(pow(statuncty, 2) + pow(systuncty, 2)));

    return prefrate;

}


void PrefireWeights::getPrefireSF(EventTree* tree, float* scaleFactors){

    double nonPrefiringProba[3] = {1., 1., 1.};


    double pho_et, pho_eta, pho_phi, jet_pt, jet_eta, jet_phi;

    for (int fluct = 0; fluct<3; fluct++){

	//loop over photons
	for(int phoInd = 0; phoInd < tree->nPho_; ++phoInd){
	
	    pho_eta = tree->phoEta_[phoInd];
	    pho_et = tree->phoEt_[phoInd];
	    
	    if (fabs(pho_eta) < 2.) continue;
	    if (fabs(pho_eta) > 3.) continue;
	    if (pho_et < 20.) continue;
	    
	    float prefiringprob_gam = getPrefiringRate(pho_eta, pho_et, phoEffHist, fluct);

	    nonPrefiringProba[fluct] *= (1. - prefiringprob_gam);

	}
	
	

	//Now applying the prefiring maps to jets in the affected regions.
	for(int jetInd = 0; jetInd < tree->nJet_; ++jetInd){
	    jet_pt = tree->jetPt_[jetInd];
	    jet_eta = tree->jetEta_[jetInd];
	    jet_phi = tree->jetPhi_[jetInd];
	    
	    if (fabs(jet_eta) < 2.) continue;
	    if (fabs(jet_eta) > 3.) continue;
	    if (jet_pt < 20.) continue;
	    
	    //Loop over photons to remove overlap
	    float nonprefiringprobfromoverlappingphotons = 1.;
	    for(int phoInd = 0; phoInd < tree->nPho_; ++phoInd){
		
		pho_eta = tree->phoEta_[phoInd];
		pho_phi = tree->phoPhi_[phoInd];
		pho_et = tree->phoEt_[phoInd];
	
		if (fabs(pho_eta) < 2.) continue;
		if (fabs(pho_eta) > 3.) continue;
		if (pho_et < 20.) continue;

		if ( dR( pho_eta, pho_phi, jet_eta, jet_phi) > 0.4) continue;

		float prefiringprob_gam = getPrefiringRate(pho_eta, pho_et, phoEffHist, fluct);

		nonprefiringprobfromoverlappingphotons *= (1. - prefiringprob_gam);
	    }


	    if (useEMpt_)
		jet_pt *= (tree->jetchEmEF_[jetInd] + tree->jetneEmEF_[jetInd]);

	    float nonprefiringprobfromoverlappingjet = 1. - getPrefiringRate(jet_eta, jet_pt, jetEffHist, fluct);

	    if (nonprefiringprobfromoverlappingphotons == 1.) {
		nonPrefiringProba[fluct] *= nonprefiringprobfromoverlappingjet;
	    }
	    //If overlapping photons have a non prefiring rate larger than the jet, then replace these weights by the jet one
	    else if (nonprefiringprobfromoverlappingphotons > nonprefiringprobfromoverlappingjet) {
		if (nonprefiringprobfromoverlappingphotons != 0.) {
		    nonPrefiringProba[fluct] *= nonprefiringprobfromoverlappingjet / nonprefiringprobfromoverlappingphotons;
		} else {
		    nonPrefiringProba[fluct] = 0.;
		}
	    }
	    //Last case: if overlapping photons have a non prefiring rate smaller than the jet, don't consider the jet in the event weight, and do nothing.
	}
    }

    scaleFactors[0] = nonPrefiringProba[0];
    scaleFactors[1] = nonPrefiringProba[1];
    scaleFactors[2] = nonPrefiringProba[2];

    return; 

}
