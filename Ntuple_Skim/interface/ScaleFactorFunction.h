
//////////////////////////
// Cross Sections Used  //
//////////////////////////

std::map<std::string, vector<double> > crossSections;

void initCrossSections(){

    crossSections["TTbarPowheg"]  =  {831.76, 831.76, 831.76};  //ttbar NNLO (http://inspirehep.net/search?p=find+eprint+1112.5675)
    crossSections["TTbarPowheg_Dilepton"]             =  { 87.315, 87.315, 87.315};
    crossSections["TTbarPowheg_Semilept"]             =  {364.352,364.352,364.352};
    crossSections["TTbarPowheg_Hadronic"]             =  {380.095,380.095,380.095};
    crossSections["HplusM080"]                        =  {6.77, 6.77, 6.77}; 
    crossSections["HplusM090"]                        =  {6.77, 6.77, 6.77}; 
    crossSections["HplusM100"]                        =  {6.77, 6.77, 6.77}; 
    crossSections["HplusM120"]                        =  {6.77, 6.77, 6.77}; 
    crossSections["HplusM140"]                        =  {6.77, 6.77, 6.77}; 
    crossSections["HplusM150"]                        =  {6.77, 6.77, 6.77}; 
    crossSections["HplusM155"]                        =  {6.77, 6.77, 6.77}; 
    crossSections["HplusM160"]                        =  {6.77, 6.77, 6.77}; 

    // Unused crossSections["WjetsInclusive"]    = {61526.7, 61526.7, 61526.7}; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#W_jets
    crossSections["W1jets"]            =  {11775.9345, 11775.9345, 11775.9345};//9493.0;
    crossSections["W2jets"]            =  { 3839.4345,  3839.4345,  3839.4345}; //3120.0;
    crossSections["W3jets"]            =  { 1165.8108,  1165.8108,  1165.8108};//942.3;
    crossSections["W4jets"]            =  {  592.9176,   592.9176,   592.9176};//524.2;

    crossSections["DYjetsM50"]         =  {6077.22, 6077.22, 6077.22}; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
    crossSections["DYjetsM10to50"]     =  {18610., 18610., 18610.}; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns

    crossSections["DYjetsM10to50"] = {18610.0, 18610.0, 18610.0}; 
    crossSections["DYjetsM50"]     = {6077.22, 6077.22, 6077.22};
    crossSections["TTWtoQQ"]               =  {0.4062, 0.4062, 0.4062}; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
    crossSections["TTWtoLNu"]              =  {0.2043, 0.2043, 0.2043}; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
    crossSections["TTZtoLL"]               =  {0.2728, 0.2728, 0.2728};  //????? https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns lists it as 0.2529
    crossSections["TTZtoLL_M1to10"]        =  {0.0493, 0.0493, 0.0493};  //????? https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns lists it as 0.2529
    crossSections["TTZtoQQ"]               =  {0.5297, 0.5297, 0.5297};  //????? https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns lists it as 0.2529

    crossSections["WW"]                = {75.8 ,75.8 ,75.8 };
    crossSections["WZ"]                = {27.6 ,27.6 ,27.6 };
    crossSections["ZZ"]                = {12.14,12.14,12.14};

    crossSections["WWToLNuQQ"]      = {49.997, 49.997, 49.997};
    crossSections["WWTo4Q"]         = {51.723, 51.723, 51.723};

    crossSections["WZTo1L3Nu"]      = { 3.033  ,  3.033  ,  3.033  };
    crossSections["WZTo1L1Nu2Q"]    = {10.71   , 10.71   , 10.71   };
    crossSections["WZTo2L2Q"]       = { 5.595  ,  5.595  ,  5.595  };
    crossSections["WZTo3LNu"]      = { 4.42965,  4.42965,  4.42965};

    crossSections["ZZTo2L2Q"]       = { 3.28, 3.28, 3.28};
    crossSections["ZZTo2Q2Nu"]      = { 4.04, 4.04, 4.04};
    crossSections["ZZTo4L"]         = { 1.3816, 1.3816, 1.3816};

    crossSections["VVTo2L2Nu"]      = {11.95, 11.95, 11.95};

    crossSections["ST_tW_channel"]      =  { 35.85,  35.85,  35.85};
    crossSections["ST_tbarW_channel"]   =  { 35.85,  35.85,  35.85};
    crossSections["ST_t_channel"]       =  {136.02, 136.02, 136.02};
    crossSections["ST_tbar_channel"]    =  { 80.95,  80.95,  80.95};
    crossSections["ST_s_channel"]       =  {3.68064, 3.68064, 3.68064};

    //Product fo XS and filter eff from table at:
    //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
    crossSections["QCD_Pt15to20_Mu"]    = {3819570.0, 3819570.0, 3819570.0};
    crossSections["QCD_Pt20to30_Mu"]    = {2960198.4   , 2960198.4   , 2960198.4   };
    crossSections["QCD_Pt30to50_Mu"]    = {1652471.46  , 1652471.46  , 1652471.46  };
    crossSections["QCD_Pt50to80_Mu"]    = { 437504.1   ,  437504.1   ,  437504.1   };
    crossSections["QCD_Pt80to120_Mu"]   = { 106033.6648,  106033.6648,  106033.6648};
    crossSections["QCD_Pt120to170_Mu"]  = {  25190.5151,   25190.5151,   25190.5151};
    crossSections["QCD_Pt170to300_Mu"]  = {   8654.4932,    8654.4932,    8654.4932};
    crossSections["QCD_Pt300to470_Mu"]  = {    797.3527,     797.3527,     797.3527};
    crossSections["QCD_Pt470to600_Mu"]  = {     79.0255,      79.0255,      79.0255};
    crossSections["QCD_Pt600to800_Mu"]  = {     25.0951,      25.0951,      25.0951};
    crossSections["QCD_Pt800to1000_Mu"] = {      4.7074,       4.7074,       4.7074};
    crossSections["QCD_Pt1000toInf_Mu"] = {      1.6213,       1.6213,       1.6213};
    crossSections["QCD_Pt20to30_Ele"]   = {5352960., 5352960., 5352960.};
    crossSections["QCD_Pt30to50_Ele"]   = {9928000., 9928000., 9928000.};
    crossSections["QCD_Pt50to80_Ele"]   = {2890800., 2890800., 2890800.};
    crossSections["QCD_Pt80to120_Ele"]  = { 350000.,  350000.,  350000.};
    crossSections["QCD_Pt120to170_Ele"] = {  62964.,   62964.,   62964.};
    crossSections["QCD_Pt170to300_Ele"] = {  18810.,   18810.,   18810.};
    crossSections["QCD_Pt300toInf_Ele"] = {   1350.,    1350.,    1350.};

    return;
}

double getEvtWeight(string sampleType, int year, double luminosity, double nEvents_MC){
    
    double evtWeight = -1.;

    if( sampleType.substr(0,4)=="Data") {evtWeight = 1.;}
    else if( sampleType=="Test") {evtWeight = 1.;}
    else if( sampleType=="TestAll") {evtWeight = 1.;}
    else if( sampleType=="TestFull") {evtWeight = 1.;}
    else {
	//	initCrossSections();
	if (crossSections.find(sampleType) != crossSections.end()) {
	    int index = year - 2016;
	    evtWeight = crossSections[sampleType][index] * luminosity / nEvents_MC;
	}
	else {
	    cout << "-------------------------------------------------" << endl;
	    cout << "-------------------------------------------------" << endl;
	    cout << "-- Unable to find event weight for this sample --" << endl;
	    cout << "-- Sample will be saved with a weight of -1    --" << endl;
	    cout << "-------------------------------------------------" << endl;
	    cout << "-------------------------------------------------" << endl;
	}
    }
    cout << "Using event weight " << evtWeight << endl;
    cout << "XS = " << evtWeight/luminosity*nEvents_MC << endl;
    cout << "lumi = " << luminosity << endl;
    cout << "nEvents_MC = " << nEvents_MC << endl;
    
    return evtWeight;
}

