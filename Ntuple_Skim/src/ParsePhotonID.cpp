#include "../interface/ParsePhotonID.h"

std::vector<bool> parsePhotonVIDCuts(int bitMap, int cutLevel){

    //    *         | Int_t VID compressed bitmap (MinPtCut,PhoSCEtaMultiRangeCut,PhoSingleTowerHadOverEmCut,PhoFull5x5SigmaIEtaIEtaCut,PhoAnyPFIsoWithEACut,PhoAnyPFIsoWithEAAndQuadScalingCut,PhoAnyPFIsoWithEACut), 2 bits per cut*

    bool passHoverE  = (bitMap>>4&3)  >= cutLevel;
    bool passSIEIE   = (bitMap>>6&3)  >= cutLevel;
    bool passChIso   = (bitMap>>8&3)  >= cutLevel;
    bool passNeuIso  = (bitMap>>10&3) >= cutLevel;
    bool passPhoIso  = (bitMap>>12&3) >= cutLevel;


    bool passID = passHoverE && passSIEIE && passChIso && passNeuIso && passPhoIso;

    std::vector<bool> cuts;
    cuts.push_back(passID);
    cuts.push_back(passHoverE);
    cuts.push_back(passSIEIE);
    cuts.push_back(passChIso);
    cuts.push_back(passNeuIso);
    cuts.push_back(passPhoIso);

    return cuts;

}
