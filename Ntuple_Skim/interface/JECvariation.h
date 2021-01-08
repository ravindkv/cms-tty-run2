#ifndef JECVARIATION_H
#define JECVARIATION_H
        
#include<vector>
#include<iostream>
#include<algorithm>
#include<TH1F.h>
#include<TMath.h>
#include<TLorentzVector.h>
#include"JetCorrectorParameters.h"
#include"FactorizedJetCorrector.h"
#include"JetCorrectionUncertainty.h"
#include"../interface/EventTree.h"

class JECvariation{
public: 
	//JetCorrectionUncertainty();
    	//JetCorrectionUncertainty(const std::string& fDataFile);
    	//JetCorrectionUncertainty(const JetCorrectorParameters& fParameters);
    	//~JetCorrectionUncertainty();

	//JetCorrectorParameters() { valid_ = false;}
    	//JetCorrectorParameters(const std::string& fFile, const std::string& fSection = "");
    	//JetCorrectorParameters(const JetCorrectorParameters::Definitions& fDefinitions,
          //               const std::vector<JetCorrectorParameters::Record>& fRecords)
      	//: mDefinitions(fDefinitions),mRecords(fRecords) { valid_ = true;}


	JECvariation(std::string inputPrefix, bool isMC, string systematicLevel);
        ~JECvariation();

        void applyJEC(EventTree* tree, int scaleDownNormUp012);

private:
        JetCorrectionUncertainty *jecUnc;

        JetCorrectorParameters *ResJetPar;
        JetCorrectorParameters *L3JetPar;
        JetCorrectorParameters *L2JetPar;
	JetCorrectorParameters *L1JetPar;

        FactorizedJetCorrector *JetCorrector;
};


#endif
