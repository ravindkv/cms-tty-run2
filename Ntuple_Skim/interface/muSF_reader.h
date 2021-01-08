#include<TH2D.h>
#include<TFile.h>

#include <iostream>


using namespace std;

class MuonSF
{
 public:
    MuonSF(string id_filename, string id_histName,
	   string iso_filename, string iso_histName,
	   string trig_filename, string trig_histName){

	TFile* idFile = TFile::Open(id_filename.c_str(),"READ");
	idHist = (TH2D*) idFile->Get(id_histName.c_str());

	TFile* isoFile = TFile::Open(iso_filename.c_str(),"READ");
	isoHist = (TH2D*) isoFile->Get(iso_histName.c_str());

	TFile* trigFile = TFile::Open(trig_filename.c_str(),"READ");
	trigHist = (TH2D*) trigFile->Get(trig_histName.c_str());
	
    }
    std::vector<double> getMuSF(double pt, double eta, int systLevel, int year, bool verbose=false);

    /* bool splitSystsId = false; */
    /* bool splitSystsIso = false; */
    /* bool splitSystsTrig = false; */
    
 private:
    TH2D* idHist;
    TH2D* isoHist;
    TH2D* trigHist;
    
    /* string isoName; */
    /* string idName; */
    /* string trigName; */
};



std::vector<double> MuonSF::getMuSF(double pt, double eta, int systLevel, int year, bool verbose){

    double abseta = fabs(eta);

    int muEtaRegion_IDIso = -1;
    int muEtaRegion_Trigger = -1;
    int muPtRegion_IDIso = -1;
    int muPtRegion_Trigger = -1;

    int idX = -1;
    int idY = -1;
    int trigX = -1;
    int trigY = -1;

    if (year==2016){

	if (eta < -2.3 ) {  muEtaRegion_IDIso = 1 ; }
	else if (eta < -2.2 ) {  muEtaRegion_IDIso = 2 ; }
	else if (eta < -2.1 ) {  muEtaRegion_IDIso = 3 ; }
	else if (eta < -2   ) {  muEtaRegion_IDIso = 4 ; }
	else if (eta < -1.7 ) {  muEtaRegion_IDIso = 5 ; }
	else if (eta < -1.6 ) {  muEtaRegion_IDIso = 6 ; }
	else if (eta < -1.5 ) {  muEtaRegion_IDIso = 7 ; }
	else if (eta < -1.4 ) {  muEtaRegion_IDIso = 8 ; }
	else if (eta <  -1.2) {  muEtaRegion_IDIso = 9 ; }
	else if (eta <  -0.8) {  muEtaRegion_IDIso = 10; }
	else if (eta <  -0.5) {  muEtaRegion_IDIso = 11; }
	else if (eta <  -0.3) {  muEtaRegion_IDIso = 12; }
	else if (eta <  -0.2) {  muEtaRegion_IDIso = 13; }
	else if (eta <  0   ) {  muEtaRegion_IDIso = 14; }
	else if (eta <  0.2 ) {  muEtaRegion_IDIso = 15; }
	else if (eta <  0.3 ) {  muEtaRegion_IDIso = 16; }
	else if (eta <  0.5 ) {  muEtaRegion_IDIso = 17; }
	else if (eta <  0.8 ) {  muEtaRegion_IDIso = 18; }
	else if (eta <  1.2 ) {  muEtaRegion_IDIso = 19; }
	else if (eta <  1.4 ) {  muEtaRegion_IDIso = 20; }
	else if (eta <  1.5 ) {  muEtaRegion_IDIso = 21; }
	else if (eta <  1.6 ) {  muEtaRegion_IDIso = 22; }
	else if (eta <  1.7 ) {  muEtaRegion_IDIso = 23; }
	else if (eta <  2   ) {  muEtaRegion_IDIso = 24; }
	else if (eta <  2.1 ) {  muEtaRegion_IDIso = 25; }
	else if (eta <  2.2 ) {  muEtaRegion_IDIso = 26; }
	else if (eta <  2.3 ) {  muEtaRegion_IDIso = 27; }
	else {  muEtaRegion_IDIso = 28; }


	if (pt < 25.0) { muPtRegion_IDIso =   1; }
	else if (pt < 30.0) { muPtRegion_IDIso =   2; }
	else if (pt < 40.0) { muPtRegion_IDIso =   3; } 
	else if (pt < 50.0) { muPtRegion_IDIso =   4; }
	else if (pt < 60.0) { muPtRegion_IDIso =   5; }
	else { muPtRegion_IDIso =   6; }

	if (abseta < 0.9) {muEtaRegion_Trigger = 1;}
	else if (abseta < 1.2) {muEtaRegion_Trigger = 2;}
	else if (abseta < 2.1) {muEtaRegion_Trigger = 3;}
	else {muEtaRegion_Trigger = 4;}
    
	if (pt < 30.) { muPtRegion_Trigger = 1;}
	else if (pt < 40.) { muPtRegion_Trigger = 2;}
	else if (pt < 50.) { muPtRegion_Trigger = 3;}
	else if (pt < 60.) { muPtRegion_Trigger = 4;}
	else if (pt < 120.) { muPtRegion_Trigger = 5;}
	else if (pt < 200.) { muPtRegion_Trigger = 6;}
	else { muPtRegion_Trigger = 7;}

	idX = muEtaRegion_IDIso;
	idY = muPtRegion_IDIso;

	trigX = muEtaRegion_Trigger;
	trigY = muPtRegion_Trigger;

    } else if (year==2017) {


	if (abseta < 0.9) {muEtaRegion_IDIso = 1;}
	else if (abseta < 1.2) {muEtaRegion_IDIso = 2;}
	else if (abseta < 2.1) {muEtaRegion_IDIso = 3;}
	else {muEtaRegion_IDIso = 4;}
    
	if (pt < 25.) { muPtRegion_IDIso = 1;}
	else if (pt < 30.) { muPtRegion_IDIso = 2;}
	else if (pt < 40.) { muPtRegion_IDIso = 3;}
	else if (pt < 50.) { muPtRegion_IDIso = 4;}
	else if (pt < 60.) { muPtRegion_IDIso = 5;}
	else { muPtRegion_IDIso = 6;}

	if (abseta < 0.9) {muEtaRegion_Trigger = 1;}
	else if (abseta < 1.2) {muEtaRegion_Trigger = 2;}
	else if (abseta < 2.1) {muEtaRegion_Trigger = 3;}
	else {muEtaRegion_Trigger = 4;}
    
	if (pt < 32.) { muPtRegion_Trigger = 1;}
	else if (pt < 40.) { muPtRegion_Trigger = 2;}
	else if (pt < 50.) { muPtRegion_Trigger = 3;}
	else if (pt < 60.) { muPtRegion_Trigger = 4;}
	else if (pt < 120.) { muPtRegion_Trigger = 5;}
	else if (pt < 200.) { muPtRegion_Trigger = 6;}
	else { muPtRegion_Trigger = 7;}

	idX = muPtRegion_IDIso;
	idY = muEtaRegion_IDIso;

	trigX = muEtaRegion_Trigger;
	trigY = muPtRegion_Trigger;

    } else if (year==2018) {

	if (abseta < 0.9) {muEtaRegion_IDIso = 1;}
	else if (abseta < 1.2) {muEtaRegion_IDIso = 2;}
	else if (abseta < 2.1) {muEtaRegion_IDIso = 3;}
	else {muEtaRegion_IDIso = 4;}
    
	if (pt < 20.) { muPtRegion_IDIso = 1;}
	else if (pt < 25.) { muPtRegion_IDIso = 2;}
	else if (pt < 30.) { muPtRegion_IDIso = 3;}
	else if (pt < 40.) { muPtRegion_IDIso = 4;}
	else if (pt < 50.) { muPtRegion_IDIso = 5;}
	else if (pt < 60.) { muPtRegion_IDIso = 6;}
	else { muPtRegion_IDIso = 7;}


	if (abseta < 0.9) {muEtaRegion_Trigger = 1;}
	else if (abseta < 1.2) {muEtaRegion_Trigger = 2;}
	else if (abseta < 2.1) {muEtaRegion_Trigger = 3;}
	else {muEtaRegion_Trigger = 4;}
    
	if (pt < 30.) { muPtRegion_Trigger = 1;}
	else if (pt < 40.) { muPtRegion_Trigger = 2;}
	else if (pt < 50.) { muPtRegion_Trigger = 3;}
	else if (pt < 60.) { muPtRegion_Trigger = 4;}
	else if (pt < 120.) { muPtRegion_Trigger = 5;}
	else if (pt < 200.) { muPtRegion_Trigger = 6;}
	else if (pt < 300.) { muPtRegion_Trigger = 7;}
	else { muPtRegion_Trigger = 8;}
	
	idX = muPtRegion_IDIso;
	idY = muEtaRegion_IDIso;

	trigX = muEtaRegion_Trigger;
	trigY = muPtRegion_Trigger;

    }

    double id_SF_value = idHist->GetBinContent(idX, idY);
    double id_SF_error = idHist->GetBinError(idX, idY);

    double id_SF = id_SF_value + (systLevel-1)*id_SF_error;

    double iso_SF_value = isoHist->GetBinContent(idX, idY);
    double iso_SF_error = isoHist->GetBinError(idX, idY);

    double iso_SF = iso_SF_value + (systLevel-1)*iso_SF_error;


    double trig_SF_value = trigHist->GetBinContent(trigX, trigY);
    double trig_SF_error = trigHist->GetBinError(trigX, trigY);

    double trig_SF = trig_SF_value + (systLevel-1)*trig_SF_error;

    //    double muEffSF=id_SF*iso_SF*trig_SF;
    std::vector<double> muSF {id_SF*iso_SF*trig_SF, id_SF, iso_SF, trig_SF};

    if (verbose) { 
	cout << "Muon Scale Factors: " << endl;
	cout << "    ID   = " << id_SF << endl;
	cout << "    Iso  = " << iso_SF << endl;
	cout << "    Trig = " << trig_SF << endl;
	cout << "    Total= " << id_SF*iso_SF*trig_SF << endl;
    }
	
    return muSF;

}

