#define testSF_cxx
#include "../interface/muSF_reader.h"
#include "../interface/eleSF_reader.h"

#include <iostream>

using namespace std;

int main(){

    MuonSF muSF = MuonSF("../MuEleSF/mu2017/RunBCDEF_SF_ID.root", "NUM_TightID_DEN_genTracks_pt_abseta",
			 "../MuEleSF/mu2017/RunBCDEF_SF_ISO.root", "NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta",
			 "../MuEleSF/mu2017/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root", "IsoMu27_PtEtaBins/abseta_pt_ratio");

    // muSF.setIdName("NUM_TightID_DEN_genTracks/abseta_pt");
    // muSF.setIsoName("NUM_TightRelIso_DEN_TightIDandIPCut/abseta_pt");
    // muSF.setTrigName("IsoMu27_PtEtaBins/abseta_pt_DATA");

    muSF.verbose=true;
    std::cout << muSF.getMuSF(29.5,0,1, 2017) << std::endl;

    ElectronSF eleSF = ElectronSF("../MuEleSF/ele2017/2017_ElectronTight.root",
				  "../MuEleSF/ele2017/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root");

    eleSF.verbose=true;
    std::cout << eleSF.getEleSF(29.5,0,1) << std::endl;
    return 1;
}
