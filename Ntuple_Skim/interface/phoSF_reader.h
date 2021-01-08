#include<TH2F.h>
#include<TFile.h>

#include <iostream>


using namespace std;

class PhotonSF
{
 public:
    PhotonSF(string id_fname, string eveto_fname, int _year){
	TFile* idFile = TFile::Open(id_fname.c_str(),"READ");
	idHist = (TH2F*) idFile->Get("EGamma_SF2D");
	year = _year;

	TFile* eVetoFile = TFile::Open(eveto_fname.c_str(),"READ");
	if (year==2016){
	    eVetoHist_2D = (TH2F*) eVetoFile->Get("Scaling_Factors_HasPix_R9 Inclusive");
	} else if (year==2017){
	    eVetoHist_1D = (TH1F*) eVetoFile->Get("Medium_ID");
	} else if (year==2018){
	    eVetoHist_2D = (TH2F*) eVetoFile->Get("eleVeto_SF");
	    eVetoHist_Unc_2D = (TH2F*) eVetoFile->Get("eleVeto_Unc");
	}
    }

    std::vector<double> getPhoSF(double pt, double eta, int systLevel, bool verbose=false);

 private:
    TH2F* idHist;
    TH2F* eVetoHist_2D;
    TH2F* eVetoHist_Unc_2D;
    TH1F* eVetoHist_1D;
    int year;

};



std::vector<double> PhotonSF::getPhoSF(double pt, double eta, int systLevel, bool verbose){


    int phoEtaRegion_ID = -1;
    int phoPtRegion_ID = -1;

    if (eta < -2.000) { phoEtaRegion_ID = 1;}
    else if (eta < -1.566) { phoEtaRegion_ID = 2;}
    else if (eta < -1.444) { phoEtaRegion_ID = 3;}
    else if (eta < -0.800) { phoEtaRegion_ID = 4;}
    else if (eta < 0.000) { phoEtaRegion_ID = 5;}
    else if (eta < 0.800) { phoEtaRegion_ID = 6;}
    else if (eta < 1.444) { phoEtaRegion_ID = 7;}
    else if (eta < 1.566) { phoEtaRegion_ID = 8;}
    else if (eta < 2.000) { phoEtaRegion_ID = 9;}
    else { phoEtaRegion_ID = 10; }

    if (pt < 35.) { phoPtRegion_ID = 1; }
    else if (pt < 50.) { phoPtRegion_ID = 2; }
    else if (pt < 100.) { phoPtRegion_ID = 3; }
    else if (pt < 200.) { phoPtRegion_ID = 4; }
    else { phoPtRegion_ID = 5; }

   

    double id_SF_value = idHist->GetBinContent(phoEtaRegion_ID,phoPtRegion_ID);
    double id_SF_error = idHist->GetBinError(phoEtaRegion_ID,phoPtRegion_ID);

    double id_SF = id_SF_value + (systLevel-1)*id_SF_error;


    double eVeto_SF;
    double eVeto_error;

    if (year==2016){
	if (abs(eta)< 1.5){
	    eVeto_SF = eVetoHist_2D->GetBinContent(1,1);
	    eVeto_error = eVetoHist_2D->GetBinError(1,1);
	}else{
	    eVeto_SF = eVetoHist_2D->GetBinContent(3,1);
	    eVeto_error = eVetoHist_2D->GetBinError(3,1);
	}
    } else if (year==2017){
	if (abs(eta)< 1.5){
	    eVeto_SF = eVetoHist_1D->GetBinContent(1);
	    eVeto_error = eVetoHist_1D->GetBinError(1);
	}else{
	    eVeto_SF = eVetoHist_1D->GetBinContent(4);
	    eVeto_error = eVetoHist_1D->GetBinError(4);
	}
    } else if (year==2018){
	if (abs(eta)< 1.5){
	    if (pt < 30){eVeto_SF = eVetoHist_2D->GetBinContent(1,1); eVeto_error = eVetoHist_Unc_2D->GetBinError(1,1);}
	    else if (pt < 60){eVeto_SF = eVetoHist_2D->GetBinContent(2,1); eVeto_error = eVetoHist_Unc_2D->GetBinError(2,1);}
	    else {eVeto_SF = eVetoHist_2D->GetBinContent(3,1); eVeto_error = eVetoHist_Unc_2D->GetBinError(3,1);}
	}else{
	    if (pt < 30){eVeto_SF = eVetoHist_2D->GetBinContent(1,3); eVeto_error = eVetoHist_Unc_2D->GetBinError(1,3);}
	    else if (pt < 60){eVeto_SF = eVetoHist_2D->GetBinContent(2,3); eVeto_error = eVetoHist_Unc_2D->GetBinError(2,3);}
	    else {eVeto_SF = eVetoHist_2D->GetBinContent(3,3); eVeto_error = eVetoHist_Unc_2D->GetBinError(3,3);}
	}
    }


    eVeto_SF = eVeto_SF + (systLevel-1)*eVeto_error;

    if (verbose){
	cout << "Photon Scale Factors: " << endl;
	cout << "   ID    = " << id_SF << endl;
	cout << "   eVeto = " << eVeto_SF << endl;
	cout << "   Total = " << id_SF*eVeto_SF << endl;
    }

    




    std::vector<double> phoEffSF  {id_SF*eVeto_SF, id_SF, eVeto_SF};

    return phoEffSF;

}

