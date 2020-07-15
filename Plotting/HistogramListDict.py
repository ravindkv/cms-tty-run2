btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]


def GetHistogramInfo_2Dplot(extraCuts="(passPresel_Mu && nJet>=3 && nBJet>=1)*", extraPhotonCuts="(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*", nBJets=1):
    histogramInfo = {#"2D_PhotonEt" :["phoEt[0]", "mcPt", "2D_PhotonEt", [300,0,300], [300,0,300],"
		     "phosel_2DChIsoSIEIE"         : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                     "phosel_2DChIsoSIEIE_barrel"  : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_barrel", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel"), "", True],
                     "phosel_2DChIsoSIEIE_endcap"  : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_endcap", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && !loosePhoIsBarrel"), "", True],

                     "phosel_2DChIsoSIEIE_GenuinePhoton"   : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_GenuinePhoton",  [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine"), "", False],
                     "phosel_2DChIsoSIEIE_MisIDEle"        : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_MisIDEle",       [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle"), "", False],
                     "phosel_2DChIsoSIEIE_HadronicPhoton"  : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_HadronicPhoton", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton"), "", False],
                     "phosel_2DChIsoSIEIE_HadronicFake"    : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_HadronicFake",   [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake"), "", False],

                     "phosel_2DChIsoSIEIE_GenuinePhoton_barrel"   : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_GenuinePhoton_barrel",  [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_MisIDEle_barrel"        : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_MisIDEle_barrel",       [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_HadronicPhoton_barrel"  : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_HadronicPhoton_barrel", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_HadronicFake_barrel"    : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_HadronicFake_barrel",   [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel"), "", False],

                     "phosel_2DChIsoSIEIE_GenuinePhoton_endcap"   : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_GenuinePhoton_endcap",  [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && !loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_MisIDEle_endcap"        : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_MisIDEle_endcap",       [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && !loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_HadronicPhoton_endcap"  : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_HadronicPhoton_endcap", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && !loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_HadronicFake_endcap"    : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_HadronicFake_endcap",   [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && !loosePhoIsBarrel"), "", False],

                     "phosel_2DChIsoHoverE_barrel"    : ["loosePhoPFChIso", "loosePhoHoverE", "phosel_2DChIsoHoverE_barrel",   [400,0,0.2], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel"), "", True],
                     "phosel_2DChIsoHoverE_endcap"    : ["loosePhoPFChIso", "loosePhoHoverE", "phosel_2DChIsoHoverE_endcap",   [400,0,0.2], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && !loosePhoIsBarrel"), "", True],

                     "phosel_2DChIsoHoverE_Nonprompt_barrel"    : ["loosePhoPFChIso", "loosePhoHoverE", "phosel_2DChIsoHoverE_Nonprompt_barrel",   [400,0,0.2], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel && (loosePhotonIsHadronicFake || loosePhotonIsHadronicPhoton)"), "", False],
                     "phosel_2DChIsoHoverE_Nonprompt_endcap"    : ["loosePhoPFChIso", "loosePhoHoverE", "phosel_2DChIsoHoverE_Nonprompt_endcap",   [400,0,0.2], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && !loosePhoIsBarrel && (loosePhotonIsHadronicFake || loosePhotonIsHadronicPhoton)"), "", False],

                     "phosel_2DdRjetphoChIso"      : ["dRPhotonJet[0]", "loosePhoPFChIso", "phosel_2DdRjetphoChIso", [200,0,5], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"),"", True], 


                     ###########
                     "phosel_2DChIsoSIEIE_dRcut_barrel"  : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_barrel", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel"), "", True],
                     "phosel_2DChIsoSIEIE_dRcut_GenuinePhoton_barrel"   : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_GenuinePhoton_barrel",  [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_dRcut_MisIDEle_barrel"        : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_MisIDEle_barrel",       [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_dRcut_HadronicPhoton_barrel"  : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_HadronicPhoton_barrel", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_dRcut_HadronicFake_barrel"    : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_HadronicFake_barrel",   [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel"), "", False],

                     "phosel_2DChIsoSIEIE_dRcut_endcap"  : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_endcap", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel"), "", True],
                     "phosel_2DChIsoSIEIE_dRcut_GenuinePhoton_endcap"   : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_GenuinePhoton_endcap",  [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_dRcut_MisIDEle_endcap"        : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_MisIDEle_endcap",       [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_dRcut_HadronicPhoton_endcap"  : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_HadronicPhoton_endcap", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"), "", False],
                     "phosel_2DChIsoSIEIE_dRcut_HadronicFake_endcap"    : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_dRcut_HadronicFake_endcap",   [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoJetDR>0.4 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel"), "", False],




                     }

    return histogramInfo

		
def GetHistogramInfo(extraCuts="(passPresel_Mu && nJet>=3 && nBJet>=1)*", extraPhotonCuts="(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*", nBJets=1):

    histogramInfo = { "presel_jet1Pt"                         : ["jetPt[0]"  , "presel_jet1Pt"   ,    [1000,0,1000], extraCuts      , "", True],
                      "presel_fwdjet1Pt"                      : ["fwdJetPt[0]","presel_fwdjet1Pt"   , [1000,0,1000], extraCuts      , "", True],
                      "presel_jet2Pt"                         : ["jetPt[1]"  , "presel_jet2Pt"   ,      [600,0,600], extraCuts      , "", True],
                      "presel_jet3Pt"                         : ["jetPt[2]"  , "presel_jet3Pt"   ,      [600,0,600], extraCuts      , "", True],
                      "presel_jet4Pt"                         : ["jetPt[3]"  , "presel_jet4Pt"   ,      [600,0,600], extraCuts      , "", True],
                      "presel_Njet"                           : ["nJet"      , "presel_Njet"     ,        [15,0,15], extraCuts      , "", True],
                      "presel_NFwdjet"                        : ["nfwdJet"   , "presel_NFwdjet"     ,        [15,0,15], extraCuts      , "", True],
                      "presel_Nbjet"                          : ["nBJet"     , "presel_Nbjet"    ,        [10,0,10], extraCuts      , "", True],
                      "presel_muPt"                           : ["muPt"      , "presel_muPt"     ,      [600,0,600], extraCuts      , "", True],
                      "presel_muEta"                          : ["muEta"     , "presel_muEta"    ,   [100,-2.4,2.4], extraCuts      , "", True],
                      "presel_muPhi"                          : ["muPhi"     , "presel_muPhi"    , [100,-3.15,3.15], extraCuts      , "", True],
                      "presel_elePt"                          : ["elePt"     , "presel_elePt"    ,      [600,0,600], extraCuts      , "", True],
                      "presel_eleSCEta"                       : ["eleSCEta"  , "presel_eleSCEta" ,   [100,-2.4,2.4], extraCuts      , "", True],
                      "presel_elePhi"                         : ["elePhi"    , "presel_elePhi"   , [100,-3.15,3.15], extraCuts      , "", True],
                      "presel_M3"                             : ["M3"        , "presel_M3"       ,     [550,50,600], extraCuts      , "", True],
                      "presel_M3_control"                     : ["M3"        , "presel_M3_control", [550,50,600],extraPhotonCuts%("nPho==0"), "", True],
                      "presel_MET"                            : ["pfMET"     , "presel_MET"      ,      [300,0,600], extraCuts      , "", True],
   #                   "presel_METPhi"                         : ["pfMETPhi"  , "presel_METPhi"   , [100,-3.15,3.15], extraCuts      , "", True],
                      "presel_nVtx"                           : ["nVtx"      , "presel_nVtx"     ,        [50,0,50], extraCuts      , "", True],
                      "presel_WtransMass"                     : ["WtransMass","presel_WtransMass",      [200,0,200], extraCuts      , "", True],
                      "presel_HT"                             : ["HT"        ,"presel_HT"        ,   [1500,0,1500], extraCuts      , "", True],
                      "presel_nVtxup"                         : ["nVtx"      , "presel_nVtxup"   ,        [50,0,50], extraCuts      , "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets]), False],
                      "presel_nVtxdo"                         : ["nVtx"      , "presel_nVtxdo"   ,        [50,0,50], extraCuts      , "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets]), False],
                      "presel_nVtxNoPU"                       : ["nVtx"      , "presel_nVtxNoPU" ,        [50,0,50], extraCuts      , "%sevtWeight*muEffWeight*eleEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets]), False],
                      "phosel_nVtxup"                         : ["nVtx"      , "phosel_nVtxup"   ,        [50,0,50], extraPhotonCuts%("nPho>=1"), "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("nPho>=1"),btagWeightCategory[nBJets]), False],
                      "phosel_nVtxdo"                         : ["nVtx"      , "phosel_nVtxdo"   ,        [50,0,50], extraPhotonCuts%("nPho>=1"), "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("nPho>=1"),btagWeightCategory[nBJets]), False],
                      "phosel_nVtxNoPU"                       : ["nVtx"      , "phosel_nVtxNoPU" ,        [50,0,50], extraPhotonCuts%("nPho>=1"), "%sevtWeight*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("nPho>=1"),btagWeightCategory[nBJets]), False],
                      "phosel_nVtxup_barrel"                         : ["nVtx"      , "phosel_nVtxup_barrel"   ,        [50,0,50], extraPhotonCuts%("nPhoBarrel>=1"), "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("nPhoBarrel>=1"),btagWeightCategory[nBJets]), False],
                      "phosel_nVtxdo_barrel"                         : ["nVtx"      , "phosel_nVtxdo_barrel"   ,        [50,0,50], extraPhotonCuts%("nPhoBarrel>=1"), "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("nPhoBarrel>=1"),btagWeightCategory[nBJets]), False],
                      "phosel_nVtxNoPU_barrel"                       : ["nVtx"      , "phosel_nVtxNoPU_barrel" ,        [50,0,50], extraPhotonCuts%("nPhoBarrel>=1"), "%sevtWeight*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("nPhoBarrel>=1"),btagWeightCategory[nBJets]), False],

		      "phosel_jet1Pt_barrel"                  : ["jetPt[0]"  , "phosel_jet1Pt_barrel"   ,    [1000,0,1000], extraPhotonCuts%("nPhoBarrel>=1") , "", True],
                      "phosel_jet1Pt_GenuinePhoton_barrel"    : ["jetPt[0]"  , "phosel_jet1Pt_GenuinePhoton_barrel" , [1000,0,1000], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine") , "", True],
		      "phosel_jet1Pt_MisIDEle_barrel"    : ["jetPt[0]"  , "phosel_jet1Pt_MisIDEle_barrel" , [1000,0,1000], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle") , "", True],
		      "phosel_jet1Pt_NonPrompt_barrel"   : ["jetPt[0]" , "phosel_jet1Pt_NonPrompt_barrel" , [1000,0,1000], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)") , "", True],

	             

		      "phosel_nVtx"                           : ["nVtx"      , "phosel_nVtx"     ,        [50,0,50], extraPhotonCuts%("nPho>=1") , "", True],
		      "phosel_nVtx_barrel"                    : ["nVtx"      , "phosel_nVtx_barrel"     ,        [50,0,50], extraPhotonCuts%("nPhoBarrel>=1") , "", True],
		      "phosel_fwdjet1Pt"                      : ["fwdJetPt[0]","phosel_fwdjet1Pt"   , [1000,0,1000], extraPhotonCuts%("nPho>=1") , "", True],
                      "phosel_NFwdjet"                        : ["nfwdJet"   , "phosel_NFwdjet"     ,        [15,0,15], extraPhotonCuts%("nPho>=1")     , "", True],
    #		  "phosel_DiphoMass"                      : ["DiphoMass"     , "phosel_DiphoMass"                     ,       [80,0,400], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_Nphotons"                       : ["nPho"          , "phosel_Nphotons"            ,          [3,1,4], extraPhotonCuts%("nPho>=1"), "", True],
		      "phosel_Nphotons_barrel"                : ["nPho"          , "phosel_Nphotons_barrel"     ,          [3,1,4], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_Nphotons_GenuinePhoton_barrel" : ["nPho", "phosel_Nphotons_GenuinePhoton_barrel",  [3,1,4], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_Nphotons_MisIDEle_barrel" : ["nPho" , "phosel_Nphotons_MisIDEle_barrel",  [3,1,4], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      "phosel_Nphotons_NonPrompt_barrel" : ["nPho" , "phosel_Nphotons_NonPrompt_barrel",  [3,1,4], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],
		      

                      "phosel_LeadingPhotonEt"                : ["phoEt[0]"      , "phosel_LeadingPhotonEt"        , [300,0,300], extraPhotonCuts%("nPho>=1"), "", True],
		      "phosel_LeadingPhotonEt_barrel"         : ["phoEt[0]"      , "phosel_LeadingPhotonEt_barrel" , [300,0,300], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_GenPhoPt"                       : ["mcPt", "phosel_GenPho_barrel" , [300,0,300] , "(mcPID==22 && mcPt>=20 && abs(mcEta)<=1.5 && (mcStatus==1 || mcStatus==71))*","", True],
          
                      "phosel_GenPhoEta"                      :["abs(mcEta)", "phosel_GenEta_barrel" , [15,0,1.5], "(mcPID==22 && mcPt>=20 && abs(mcEta)<=1.5 && (mcStatus==1 || mcStatus==71))*","",True],
		      "phosel_LeadingPhotonEt_GenuinePhoton_barrel": ["phoEt[0]"      , "phosel_LeadingPhotonEt_GenuinePhoton_barrel" , [300,0,300], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_LeadingPhotonEt_MisIDEle_barrel": ["phoEt[0]" , "phosel_LeadingPhotonEt_MisIDEle_barrel" , [300,0,300], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      

		      "phosel_LeadingPhotonEt_Isolated"       : ["phoEt[0]" , "phosel_LeadingPhotonEt_Isolated_barrel" , [300,0,300], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsGenuine||photonIsMisIDEle)"), "", True],
		      "phosel_LeadingPhotonEt_NonPrompt_barrel"  : ["phoEt[0]" , "phosel_LeadingPhotonEt_NonPrompt_barrel", [300,0,300], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],
      #                "phosel_SecondLeadingPhotonEt"          : ["phoEt[1]"      , "phosel_SecondLeadingPhotonEt"         ,      [300,0,300], extraPhotonCuts%("nPho>=1"), "", True],

                      "phosel_LeadingPhotonEta"               : ["phoEta[0]"     , "phosel_LeadingPhotonEta"              ,    [50,-2.5,2.5], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_LeadingPhotonSCEta"             : ["phoSCEta[0]"   , "phosel_LeadingPhotonSCEta"            ,    [50,-2.5,2.5], extraPhotonCuts%("nPho>=1"), "", True],
		      "phosel_LeadingPhotonEta_barrel"        : ["phoEta[0]"     , "phosel_LeadingPhotonEta_barrel"       ,    [50,-2.5,2.5], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
                      "phosel_LeadingPhotonSCEta_barrel"      : ["phoSCEta[0]"   , "phosel_LeadingPhotonSCEta_barrel"     ,    [50,-2.5,2.5], extraPhotonCuts%("nPhoBarrel>=1"), "", True],

		      "phosel_LeadingPhotonSCEta_GenuinePhoton_barrel"      : ["phoSCEta[0]"   , "phosel_LeadingPhotonSCEta_GenuinePhoton_barrel"     ,    [50,-2.5,2.5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		     "phosel_LeadingPhotonSCEta_MisIDEle_barrel": ["phoSCEta[0]", "phosel_LeadingPhotonSCEta_MisIDEle_barrel", [50,-2.5,2.5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		     "phosel_LeadingPhotonSCEta_NonPrompt_barrel"      : ["phoSCEta[0]"   , "phosel_LeadingPhotonSCEta_NonPrompt_barrel", [50,-2.5,2.5], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],



                     "phosel_LeadingPhotonabsSCEta_barrel"      : ["abs(phoSCEta[0])"   , "phosel_LeadingPhotonabsSCEta_barrel"     ,    [50,-2.5,2.5], extraPhotonCuts%("nPhoBarrel>=1"), "", True],

                      "phosel_LeadingPhotonabsSCEta_GenuinePhoton_barrel"      : ["abs(phoSCEta[0])"   , "phosel_LeadingPhotonabsSCEta_GenuinePhoton_barrel"     ,    [50,-2.5,2.5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
                     "phosel_LeadingPhotonabsSCEta_MisIDEle_barrel": ["phoSCEta[0]", "phosel_LeadingPhotonabsSCEta_MisIDEle_barrel", [50,-2.5,2.5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
                     "phosel_LeadingPhotonabsSCEta_NonPrompt_barrel"      : ["abs(phoSCEta[0])"   , "phosel_LeadingPhotonabsSCEta_NonPrompt_barrel", [50,-2.5,2.5], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],
                     "phosel_dRLeadingPhotonJet_barrel"      : ["dRPhotonJet[0]"   , "phosel_dRLeadingPhotonJet_barrel"            ,        [500,0,5], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_dRLeadingPhotonJet_GenuinePhoton_barrel"  : ["dRPhotonJet[0]"   , "phosel_dRLeadingPhotonJet_GenuinePhoton_barrel"            , [500,0,5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_dRLeadingPhotonJet_MisIDEle_barrel"  : ["dRPhotonJet[0]"   , "phosel_dRLeadingPhotonJet_MisIDEle_barrel" , [500,0,5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      
                      "phosel_dRLeadingPromptPhotonJet"       : ["dRPhotonJet[0]"   , "phosel_dRLeadingPromptPhotonJet"      ,        [200,0,5], extraPhotonCuts%("nPho>=1 && (photonIsGenuine||photonIsMisIDEle)"), "", False],
                      "phosel_dRLeadingPhotonJet_NonPrompt_barrel"  : ["dRPhotonJet[0]"   , "phosel_dRLeadingPhotonJet_NonPrompt_barrel"   ,  [500,0,5], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", False],
                      "phosel_dRLeadingPromptPhotonLepton"    : ["dRPhotonLepton[0]", "phosel_dRLeadingPromptPhotonLepton"   ,        [120,0,6], extraPhotonCuts%("nPho>=1 && (photonIsGenuine||photonIsMisIDEle)"), "", False],
                      "phosel_dRLeadingPhotonLepton_NonPrompt_barrel" : ["dRPhotonLepton[0]", "phosel_dRLeadingPhotonLepton_NonPrompt_barrel", [600,0,6], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", False],
                      "phosel_dRLeadingPhotonLepton_GenuinePhoton_barrel"   : ["dRPhotonLepton[0]", "phosel_dRLeadingPhotonLepton_GenuinePhoton_barrel"  ,        [600,0,6], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"),"", False],
                      "phosel_dRLeadingPhotonLepton_MisIDEle_barrel"        : ["dRPhotonLepton[0]", "phosel_dRLeadingPhotonLepton_MisIDEle_barrel"       ,        [600,0,6], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"),"", False],
                      "phosel_dRLeadingHadronicPhotonLepton"  : ["dRPhotonLepton[0]", "phosel_dRLeadingHadronicPhotonLepton" ,        [120,0,6], extraPhotonCuts%("nPho>=1 && photonIsHadronicPhoton"),"", False],
                      "phosel_dRLeadingHadronicFakeLepton"    : ["dRPhotonLepton[0]", "phosel_dRLeadingHadronicFakeLepton"   ,        [120,0,6], extraPhotonCuts%("nPho>=1 && photonIsHadronicFake"),"", False],
                      "phosel_dRLeadingPhotonLepton_barrel"   : ["dRPhotonLepton[0]", "phosel_dRLeadingPhotonLepton_barrel"         ,        [600,0,6], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
                      "phosel_phoJetDR"                       : ["phoJetDR"         , "phosel_phoJetDR"                      ,        [200,0,5], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_WtransMass"                     : ["WtransMass"    , "phosel_WtransMass"      ,     [200,0,200], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_WtransMass_GenuinePhoton"  :["WtransMass"    , "phosel_WtransMass_GenuinePhoton" ,     [200,0,200], extraPhotonCuts%("nPho>=1 && photonIsGenuine"), "", True], 
		      "phosel_WtransMass_MisIDEle"       :["WtransMass"    , "phosel_WtransMass_MisIDEle"      ,     [200,0,200], extraPhotonCuts%("nPho>=1 && photonIsMisIDEle"), "", True],
		      "phosel_WtransMass_HadronicPhoton" :["WtransMass"    , "phosel_WtransMass_HadronicPhoton",     [200,0,200], extraPhotonCuts%("nPho>=1 && photonIsHadronicPhoton"), "", True],
		      "phosel_WtransMass_HadronicFake" :["WtransMass"    , "phosel_WtransMass_HadronicFake",     [200,0,200], extraPhotonCuts%("nPho>=1 && photonIsHadronicFake"), "", True],
		
		      "phosel_WtransMass_barrel"                     : ["WtransMass"    , "phosel_WtransMass_barrel"      ,     [200,0,200], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_WtransMass_endcap"                     : ["WtransMass"    , "phosel_WtransMass_endcap"      ,     [200,0,200], extraPhotonCuts%("nPhoEndcap>=1"), "", True],
		      "phosel_WtransMass_GenuinePhoton_barrel"       : ["WtransMass"    , "phosel_WtransMass_GenuinePhoton_barrel"      ,     [200,0,200], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],		
		      "phosel_WtransMass_MisIDEle_barrel"            : ["WtransMass"    , "phosel_WtransMass_MisIDEle_barrel"      ,     [200,0,200], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      "phosel_WtransMass_HadronicPhoton_barrel"      : ["WtransMass"    , "phosel_WtransMass_HadronicPhoton_barrel"      ,     [200,0,200], extraPhotonCuts%("nPhoBarrel>=1 && photonIsHadronicPhoton"), "", True],
		      "phosel_WtransMass_HadronicFake_barrel"        : ["WtransMass"    , "phosel_WtransMass_HadronicFake_barrel"      ,     [200,0,200], extraPhotonCuts%("nPhoBarrel>=1 && photonIsHadronicFake"), "", True],
		     
                      "phosel_WtransMass_GenuinePhoton_endcap"       : ["WtransMass"    , "phosel_WtransMass_GenuinePhoton_endcap"      ,     [200,0,200], extraPhotonCuts%("nPhoEndcap>=1 && photonIsGenuine"), "", True],
                      "phosel_WtransMass_MisIDEle_endcap"            : ["WtransMass"    , "phosel_WtransMass_MisIDEle_endcap"      ,     [200,0,200], extraPhotonCuts%("nPho>=1 && photonIsMisIDEle && !phoIsBarrel[0]"), "", True],
                      "phosel_WtransMass_HadronicPhoton_endcap"      : ["WtransMass"    , "phosel_WtransMass_HadronicPhoton_endcap"      ,     [200,0,200], extraPhotonCuts%("nPho>=1 && photonIsHadronicPhoton && !phoIsBarrel[0]"), "", True],
                      "phosel_WtransMass_HadronicFake_endcap"        : ["WtransMass"    , "phosel_WtransMass_HadronicFake_endcap"      ,     [200,0,200], extraPhotonCuts%("nPho>=1 && photonIsHadronicFake && !phoIsBarrel[0]"), "", True],
		      "phosel_HT_barrel"                             : ["HT"            , "phosel_HT_barrel"              ,  [1500,0,1500], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_HT_GenuinePhoton_barrel"        : ["HT" , "phosel_HT_GenuinePhoton_barrel" ,  [1500,0,1500], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_HT_MisIDEle_barrel"             : ["HT" , "phosel_HT_MisIDEle_barrel" ,  [1500,0,1500], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      "phosel_HT_NonPrompt_barrel"            : ["HT" , "phosel_HT_NonPrompt_barrel" ,  [1500,0,1500], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicFake||photonIsHadronicPhoton)"), "", True],
                      #########
                      "phosel_M3"                             : ["M3"            , "phosel_M3"              ,    [550,50,600], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_M3_GenuinePhoton"               : ["M3"            , "phosel_M3_GenuinePhoton",    [550,50,600], extraPhotonCuts%("nPho>=1 && photonIsGenuine")       , "", False],
                      "phosel_M3_MisIDEle"                    : ["M3"            , "phosel_M3_MisIDEle"     ,    [550,50,600], extraPhotonCuts%("nPho>=1 && photonIsMisIDEle")      , "", False],
                      "phosel_M3_HadronicPhoton"              : ["M3"            , "phosel_M3_HadronicPhoton",    [550,50,600], extraPhotonCuts%("nPho>=1 && photonIsHadronicPhoton"), "", False],
                      "phosel_M3_HadronicFake"                : ["M3"            , "phosel_M3_HadronicFake" ,    [550,50,600], extraPhotonCuts%("nPho>=1 && photonIsHadronicFake")  , "", False],
                      #####
                      "phosel_M3_barrel"                      : ["M3"            , "phosel_M3_barrel"               ,    [550,50,600], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
                      "phosel_M3_gamma"                       : ["M3_gamma"      , "phosel_M3_gamma"                ,    [1000,0,1000], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_Mbjj_gamma"                      : ["M_bjjgamma"    , "phosel_Mbjj_gamma"                ,    [1000,0,1000], extraPhotonCuts%("nPho>=1"), "", True],

                      "phosel_M3_GenuinePhoton_barrel"        : ["M3"            , "phosel_M3_GenuinePhoton_barrel" ,    [550,50,600], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine")       , "", False],
                      "phosel_M3_MisIDEle_barrel"             : ["M3"            , "phosel_M3_MisIDEle_barrel"      ,    [550,50,600], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle")      , "", False],
                      "phosel_M3_HadronicPhoton_barrel"       : ["M3"            , "phosel_M3_HadronicPhoton_barrel",    [550,50,600], extraPhotonCuts%("nPhoBarrel>=1 && photonIsHadronicPhoton"), "", False],
                      "phosel_M3_HadronicFake_barrel"         : ["M3"            , "phosel_M3_HadronicFake_barrel"  ,    [550,50,600], extraPhotonCuts%("nPhoBarrel>=1 && photonIsHadronicFake")  , "", False],
		      "phosel_M3_NonPrompt_barrel"         : ["M3"            , "phosel_M3_NonPrompt_barrel"  ,    [550,50,600], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicFake||photonIsHadronicPhoton)")  , "", False],
                      #####
                      "phosel_M3_endcap"                      : ["M3"            , "phosel_M3_endcap"               ,    [550,50,600], extraPhotonCuts%("nPho>=1 && !phoIsBarrel[0]"), "", True],
                      "phosel_M3_GenuinePhoton_endcap"        : ["M3"            , "phosel_M3_GenuinePhoton_endcap" ,    [550,50,600], extraPhotonCuts%("nPho>=1 && photonIsGenuine && !phoIsBarrel[0]")       , "", False],
                      "phosel_M3_MisIDEle_endcap"             : ["M3"            , "phosel_M3_MisIDEle_endcap"      ,    [550,50,600], extraPhotonCuts%("nPho>=1 && photonIsMisIDEle && !phoIsBarrel[0]")      , "", False],
                      "phosel_M3_HadronicPhoton_endcap"       : ["M3"            , "phosel_M3_HadronicPhoton_endcap",    [550,50,600], extraPhotonCuts%("nPho>=1 && photonIsHadronicPhoton && !phoIsBarrel[0]"), "", False],
                      "phosel_M3_HadronicFake_endcap"         : ["M3"            , "phosel_M3_HadronicFake_endcap"  ,    [550,50,600], extraPhotonCuts%("nPho>=1 && photonIsHadronicFake && !phoIsBarrel[0]")  , "", False],
                      #####
                      "phosel_MET"                            : ["pfMET"         , "phosel_MET"             ,     [300,0,600], extraPhotonCuts%("nPho>=1"), "", True],
		      "phosel_elePt"                          : ["elePt"         , "phosel_elePt"           ,     [600,0,600], extraPhotonCuts%("nPho>=1"), "", True],

                      "phosel_elePt_barrel"                   : ["elePt"         , "phosel_elePt_barrel"           ,     [600,0,600], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_elePt_GenuinePhoton_barrel"     : ["elePt"         , "phosel_elePt_GenuinePhoton_barrel" , [600,0,600], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_elePt_MisIDEle_barrel"          : ["elePt"       , "phosel_elePt_MisIDEle_barrel" , [600,0,600], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
                      
		      "phosel_elePt_NonPrompt_barrel"         : ["elePt"       , "phosel_elePt_NonPrompt_barrel" , [600,0,600], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],

	              "phosel_eleSCEta"                       : ["eleSCEta"      , "phosel_eleSCEta"        ,  [100,-2.4,2.4], extraPhotonCuts%("nPho>=1"), "", True],
		      "phosel_eleSCEta_barrel"                : ["eleSCEta"      , "phosel_eleSCEta_barrel" ,  [100,-2.4,2.4], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_eleSCEta_GenuinePhoton_barrel"  : ["eleSCEta"      , "phosel_eleSCEta_GenuinePhoton_barrel" ,  [100,-2.4,2.4], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_eleSCEta_MisIDEle_barrel"  : ["eleSCEta"      , "phosel_eleSCEta_MisIDEle_barrel" ,  [100,-2.4,2.4], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      "phosel_eleSCEta_NonPrompt_barrel"  : ["eleSCEta"      , "phosel_eleSCEta_NonPrompt_barrel" ,  [100,-2.4,2.4], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],

                      "phosel_muPt_barrel"                    : ["muPt"          , "phosel_muPt_barrel"  ,     [600,0,600], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_muPt_GenuinePhoton_barrel"      : ["muPt"          , "phosel_muPt_GenuinePhoton_barrel"  ,     [600,0,600], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		
		      "phosel_muPt_MisIDEle_barrel"      : ["muPt"          , "phosel_muPt_MisIDEle_barrel"  ,     [600,0,600], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		
		      "phosel_muPt_NonPrompt_barrel"     : ["muPt" , "phosel_muPt_NonPrompt_barrel"  ,     [600,0,600], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],	

                      "phosel_muEta_barrel"                   : ["muEta"         , "phosel_muEta_barrel"           ,  [100,-2.4,2.4], extraPhotonCuts%("nPhoBarrel>=1"), "", True],

		      "phosel_muEta_GenuinePhoton_barrel"     : ["muEta"         , "phosel_muEta_GenuinePhoton_barrel" ,  [100,-2.4,2.4], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_muEta_MisIDEle_barrel"     : ["muEta"         , "phosel_muEta_MisIDEle_barrel" ,  [100,-2.4,2.4], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      "phosel_muEta_NonPrompt_barrel"     : ["muEta" , "phosel_muEta_NonPrompt_barrel" ,  [100,-2.4,2.4], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],
		      "phosel_muPt"                           : ["muPt"          , "phosel_muPt"            ,     [600,0,600], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_muEta"                          : ["muEta"         , "phosel_muEta"           ,  [100,-2.4,2.4], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_Njet"                           : ["nJet"          , "phosel_Njet"            ,       [15,0,15], extraPhotonCuts%("nPho>=1"), "", True],
		      "phosel_Njet_barrel"                    : ["nJet"          , "phosel_Njet_barrel"            ,       [15,0,15], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_Njet_GenuinePhoton_barrel"      : ["nJet"          , "phosel_Njet_GenuinePhoton_barrel" ,       [15,0,15], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_Njet_MisIDEle_barrel"           : ["nJet" , "phosel_Njet_MisIDEle_barrel" , [15,0,15], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
	              "phosel_Njet_NonPrompt_barrel"  : ["nJet","phosel_Njet_NonPrompt_barrel" , [15,0,15], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],
		      "phosel_Njet_HadronicPhoton_barrel"      : ["nJet"          , "phosel_Njet_HadronicPhoton_barrel"            ,       [15,0,15], extraPhotonCuts%("nPhoBarrel>=1 && photonIsHadronicPhoton"), "", True],	
                      "phosel_Njet_HadronicFake_barrel"      : ["nJet"          , "phosel_Njet_HadronicFake_barrel"            ,       [15,0,15], extraPhotonCuts%("nPhoBarrel>=1 && photonIsHadronicFake"), "", True],
		      "phosel_Njet_GenuinePhoton_endcap"      : ["nJet"          , "phosel_Njet_GenuinePhoton_endcap"            ,       [15,0,15], extraPhotonCuts%("nPho>=1 && photonIsGenuine && !phoIsBarrel[0]"), "", True],
                      "phosel_Njet_MisIDEle_endcap"           : ["nJet"          , "phosel_Njet_MisIDEle_endcap"            ,       [15,0,15], extraPhotonCuts%("nPho>=1 && photonIsMisIDEle[0] && !phoIsBarrel[0]"), "", True],
                      "phosel_Njet_HadronicPhoton_endcap"      : ["nJet"          , "phosel_Njet_HadronicPhoton_endcap"            ,       [15,0,15], extraPhotonCuts%("nPho>=1 && photonIsHadronicPhoton[0] && !phoIsBarrel[0]"), "", True],
                      "phosel_Njet_HadronicFake_endcap"      : ["nJet"          , "phosel_Njet_HadronicFake_endcap"            ,       [15,0,15], extraPhotonCuts%("nPho>=1 && photonIsHadronicFake[0] && !phoIsBarrel[0]"), "", True],

		      "phosel_NfwdJet"                        : ["nfwdJet"       , "phosel_Nfwdjet"            ,       [15,0,15], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_Nbjet"                          : ["nBJet"         , "phosel_Nbjet"           ,       [10,0,10], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_HoverE"                         : ["phoHoverE"     , "phosel_HoverE"          ,    [100,0.,.04], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_SIEIE"                          : ["phoSIEIE"      , "phosel_SIEIE"           ,    [100,0.,.07], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_ChIso"                          : ["phoPFChIso"    , "phosel_ChIso"           ,      [100,0,.5], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_NeuIso"                         : ["phoPFNeuIso"   , "phosel_NeuIso"          ,      [100,0,5.], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_PhoIso"                         : ["phoPFPhoIso"   , "phosel_PhoIso"          ,        [50,0,5], extraPhotonCuts%("nPho>=1"), "", True],
		      "phosel_SIEIE_barrel"  : ["phoSIEIE"  , "phosel_SIEIE_barrel"  ,  [100,0.,.07], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_SIEIE_GenuinePhoton_barrel" : ["phoSIEIE", "phosel_SIEIE_GenuinePhoton_barrel"  ,    [100,0.,.07], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_SIEIE_MisIDEle_barrel" : ["phoSIEIE", "phosel_SIEIE_MisIDEle_barrel"  ,  [100,0.,.07], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      "phosel_SIEIE_NonPrompt_barrel" : ["phoSIEIE", "phosel_SIEIE_NonPrompt_barrel"  ,  [100,0.,.07], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],
		
                      "phosel_ChIso_barrel"   : ["phoPFChIso"    , "phosel_ChIso_barrel"  ,  [100,0,.5], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      "phosel_ChIso_GenuinePhoton_barrel"   : ["phoPFChIso"    , "phosel_ChIso_GenuinePhoton_barrel"  ,  [100,0,.5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
		      "phosel_ChIso_MisIDEle_barrel" : ["phoPFChIso" , "phosel_ChIso_MisIDEle_barrel",  [100,0,.5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      "phosel_ChIso_NonPrompt_barrel" : ["phoPFChIso" , "phosel_ChIso_NonPrompt_barrel",  [100,0,.5], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],
                      "phosel_NeuIso_barrel"  : ["phoPFNeuIso"   , "phosel_NeuIso_barrel" ,      [100,0,5.], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		       "phosel_NeuIso_GenuinePhoton_barrel"   : ["phoPFNeuIso"    , "phosel_NeuIso_GenuinePhoton_barrel"  ,  [100,0,5.], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
                      "phosel_NeuIso_MisIDEle_barrel" : ["phoPFNeuIso" , "phosel_NeuIso_MisIDEle_barrel",  [100,0,5.], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
                      "phosel_NeuIso_NonPrompt_barrel" : ["phoPFNeuIso" , "phosel_NeuIso_NonPrompt_barrel",  [100,0,5.], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],	
			
                      "phosel_PhoIso_barrel"  : ["phoPFPhoIso"   , "phosel_PhoIso_barrel" ,        [100,0,5], extraPhotonCuts%("nPhoBarrel>=1"), "", True],


		       "phosel_PhoIso_GenuinePhoton_barrel"   : ["phoPFPhoIso"    , "phosel_PhoIso_GenuinePhoton_barrel"  ,  [100,0,5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
                      "phosel_PhoIso_MisIDEle_barrel" : ["phoPFPhoIso" , "phosel_PhoIso_MisIDEle_barrel",  [100,0,5], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
                      "phosel_PhoIso_NonPrompt_barrel" : ["phoPFPhoIso" , "phosel_PhoIso_NonPrompt_barrel",  [100,0,5], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", True],
                      "phosel_HoverE_barrel"  : ["phoHoverE"     , "phosel_HoverE_barrel"          ,    [100,0.,.04], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
		      ###############
                      "phosel_noCut_HoverE"                   : ["loosePhoHoverE"  , "phosel_noCut_HoverE"               ,      [100,0.,.2], extraPhotonCuts%("loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                       "phosel_noCut_HoverE_barrel"                   : ["loosePhoHoverE"  , "phosel_noCut_HoverE_barrel"               ,      [100,0.,.2], extraPhotonCuts%("loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel"), "", True],
			#print h1_up[sample][sys].Integral(), h1_up[sample][sys]
                      "phosel_noCut_SIEIE_barrel"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_barrel"         ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel"),"", True],
                       "phosel_noCut_SIEIE_GenuinePhoton_barrel"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_GenuinePhoton_barrel"         ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel && loosePhotonIsGenuine"),"", True],
                      "phosel_noCut_SIEIE_MisIDEle_barrel" : ["loosePhoSIEIE", "phosel_noCut_SIEIE_MisIDEle_barrel",[700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel && loosePhotonIsMisIDEle"),"", True],
		      "phosel_noCut_SIEIE_NonPrompt_barrel" : ["loosePhoSIEIE", "phosel_noCut_SIEIE_NonPrompt_barrel",[700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel && (loosePhotonIsHadronicFake||loosePhotonIsHadronicPhoton)"),"", True],

		      "phosel_noCut_SIEIE_noChIso_barrel"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_noChIso_barrel"         ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel"),"", True],
		      "phosel_noCut_SIEIE_noChIso_GenuinePhoton_barrel"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_noChIso_GenuinePhoton_barrel"         ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel"),"", True],	 
		      "phosel_noCut_SIEIE_noChIso_MisIDEle_barrel"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_noChIso_MisIDEle_barrel" ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel"),"", True],
		      "phosel_noCut_SIEIE_noChIso_NonPrompt_barrel"  : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_noChIso_NonPrompt_barrel" ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && (loosePhotonIsHadronicFake||loosePhotonIsHadronicPhoton) && loosePhoIsBarrel"),"", True],
		      "phosel_noCut_SIEIE_barrel_noChIso_HadronicPhoton"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_noChIso_barrel_HadronicPhoton"         ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"),"", True],
		      "phosel_noCut_SIEIE_barrel_noChIso_HadronicFake"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_barrel_noChIso_HadronicFake"         ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel"),"", True],
		      "phosel_noCut_SIEIE_endcap"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_endcap"         ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && !loosePhoIsBarrel"),"", True],
                      "phosel_noCut_SIEIE"                    : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE"                ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      "phosel_noCut_SIEIE_GenuinePhoton"      : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_GenuinePhoton"  ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine"), "", False],
                      "phosel_noCut_SIEIE_MisIDEle"           : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_MisIDEle"       ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle"), "", False],
                      "phosel_noCut_SIEIE_HadronicPhoton"     : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_HadronicPhoton" ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton"), "", False],
                      "phosel_noCut_SIEIE_HadronicFake"       : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_HadronicFake"   ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake"), "", False],

                      "phosel_noCut_SIEIE_GenuinePhoton_barrel"      : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_GenuinePhoton_barrel"  ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel"), "", False],
                      "phosel_noCut_SIEIE_MisIDEle_barrel"           : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_MisIDEle_barrel"       ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel"), "", False],
                      "phosel_noCut_SIEIE_HadronicPhoton_barrel"     : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_HadronicPhoton_barrel" ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"), "", False],
                      "phosel_noCut_SIEIE_HadronicFake_barrel"       : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_HadronicFake_barrel"   ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel"), "", False],

                      "phosel_noCut_SIEIE_GenuinePhoton_endcap"      : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_GenuinePhoton_endcap"  ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && !loosePhoIsBarrel"), "", False],
                      "phosel_noCut_SIEIE_MisIDEle_endcap"           : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_MisIDEle_endcap"       ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && !loosePhoIsBarrel"), "", False],
                      "phosel_noCut_SIEIE_HadronicPhoton_endcap"     : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_HadronicPhoton_endcap" ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && !loosePhoIsBarrel"), "", False],
                      "phosel_noCut_SIEIE_HadronicFake_endcap"       : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_HadronicFake_endcap"   ,     [700,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && !loosePhoIsBarrel"), "", False],


                      ##########
                      "phosel_noCut_ChIso"                    : ["loosePhoPFChIso" , "phosel_noCut_ChIso"                ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      "phosel_noCut_ChIso_barrel"             : ["loosePhoPFChIso" , "phosel_noCut_ChIso_barrel"         ,       [200,0,20], extraPhotonCuts%("loosePhoIsBarrel && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      "phosel_noCut_ChIso_endcap"             : ["loosePhoPFChIso" , "phosel_noCut_ChIso_endcap"         ,       [200,0,20], extraPhotonCuts%("!loosePhoIsBarrel && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      ####

                      "phosel_noCut_ChIso_PUdown"             : ["loosePhoPFChIso" , "phosel_noCut_ChIso_PUdown"         ,       [200,0,20], "", "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"),btagWeightCategory[nBJets]), False],
                      "phosel_noCut_ChIso_PUup"               : ["loosePhoPFChIso" , "phosel_noCut_ChIso_PUup"           ,       [200,0,20], "", "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"),btagWeightCategory[nBJets]), False],
                      "phosel_noCut_ChIso_0nVtx15"            : ["loosePhoPFChIso" , "phosel_noCut_ChIso_0nVtx15"        ,       [200,0,20], extraPhotonCuts%("nVtx<=15 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      "phosel_noCut_ChIso_15nVtx20"            : ["loosePhoPFChIso" , "phosel_noCut_ChIso_15nVtx20"        ,       [200,0,20], extraPhotonCuts%("15<nVtx && nVtx<=20 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      "phosel_noCut_ChIso_20nVtx25"            : ["loosePhoPFChIso" , "phosel_noCut_ChIso_20nVtx25"        ,       [200,0,20], extraPhotonCuts%("20<nVtx && nVtx<=25 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      "phosel_noCut_ChIso_25nVtx50"            : ["loosePhoPFChIso" , "phosel_noCut_ChIso_25nVtx50"        ,       [200,0,20], extraPhotonCuts%("25<nVtx && nVtx<=50 && loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],

                      "phosel_noCut_ChIso_Nonprompt_barrel_PUdown"   : ["loosePhoPFChIso" , "phosel_noCut_ChIso_Nonprompt_barrel_PUdown",  [200,0,20], "", "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel && (loosePhotonIsHadronicFake || loosePhotonIsHadronicPhoton)"),btagWeightCategory[nBJets]), False],
                      "phosel_noCut_ChIso_Nonprompt_endcap_PUdown"   : ["loosePhoPFChIso" , "phosel_noCut_ChIso_Nonprompt_endcap_PUdown",  [200,0,20], "", "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && !loosePhoIsBarrel && (loosePhotonIsHadronicFake || loosePhotonIsHadronicPhoton)"),btagWeightCategory[nBJets]), False],

                      "phosel_noCut_ChIso_Nonprompt_barrel_PUup"     : ["loosePhoPFChIso" , "phosel_noCut_ChIso_Nonprompt_barrel_PUup",    [200,0,20], "", "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel && (loosePhotonIsHadronicFake || loosePhotonIsHadronicPhoton)"),btagWeightCategory[nBJets]), False],
                      "phosel_noCut_ChIso_Nonprompt_endcap_PUup"     : ["loosePhoPFChIso" , "phosel_noCut_ChIso_Nonprompt_endcap_PUup",    [200,0,20], "", "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && !loosePhoIsBarrel && (loosePhotonIsHadronicFake || loosePhotonIsHadronicPhoton)"),btagWeightCategory[nBJets]), False],


                      "phosel_noCut_ChIso_GenuinePhoton"      : ["loosePhoPFChIso" , "phosel_noCut_ChIso_GenuinePhoton"  ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine"), "", False],
                      "phosel_noCut_ChIso_MisIDEle"           : ["loosePhoPFChIso" , "phosel_noCut_ChIso_MisIDEle"       ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle"), "", False],
                      "phosel_noCut_ChIso_HadronicPhoton"     : ["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicPhoton" ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton"), "", False],
                      "phosel_noCut_ChIso_HadronicFake"       : ["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicFake"   ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake"), "", False],

                      "phosel_noCut_ChIso_GenuinePhoton_barrel"      : ["loosePhoPFChIso" , "phosel_noCut_ChIso_GenuinePhoton_barrel"  ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel"), "", False],
                      "phosel_noCut_ChIso_MisIDEle_barrel"           : ["loosePhoPFChIso" , "phosel_noCut_ChIso_MisIDEle_barrel"       ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel"), "", False],
                      "phosel_noCut_ChIso_HadronicPhoton_barrel"     : ["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicPhoton_barrel" ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"), "", False],
                      "phosel_noCut_ChIso_HadronicFake_barrel"       : ["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicFake_barrel"   ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel"), "", False],

                      "phosel_noCut_ChIso_GenuinePhoton_endcap"      : ["loosePhoPFChIso" , "phosel_noCut_ChIso_GenuinePhoton_endcap"  ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && !loosePhoIsBarrel"), "", False],
                      "phosel_noCut_ChIso_MisIDEle_endcap"           : ["loosePhoPFChIso" , "phosel_noCut_ChIso_MisIDEle_endcap"       ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && !loosePhoIsBarrel"), "", False],
                      "phosel_noCut_ChIso_HadronicPhoton_endcap"     : ["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicPhoton_endcap" ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && !loosePhoIsBarrel"), "", False],
                      "phosel_noCut_ChIso_HadronicFake_endcap"       : ["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicFake_endcap"   ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && !loosePhoIsBarrel"), "", False],
                      ####
                      "phosel_noCut_ChIso_PromptPhoton"       : ["loosePhoPFChIso" , "phosel_noCut_ChIso_PromptPhoton"   ,       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && (loosePhotonIsGenuine||loosePhotonIsMisIDEle)")           , "", False],
                      "phosel_noCut_ChIso_NonPromptPhoton"    : ["loosePhoPFChIso" , "phosel_noCut_ChIso_NonPromptPhoton",       [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && (loosePhotonIsHadronicPhoton||loosePhotonIsHadronicFake)"), "", False],

                      "phosel_noCut_NeuIso"                   : ["loosePhoPFNeuIso", "phosel_noCut_NeuIso"               ,       [400,0,40], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassPhoIso")                                 , "", True],
                      "phosel_noCut_PhoIso"                   : ["loosePhoPFPhoIso", "phosel_noCut_PhoIso" ,       [400,0,40], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso")                                 , "", True],
		      "phosel_noCut_NeuIso_barrel"   : ["loosePhoPFNeuIso", "phosel_noCut_NeuIso_barrel" ,       [400,0,40], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassPhoIso && loosePhoIsBarrel")                                 , "", True],
                      "phosel_noCut_PhoIso_barrel"   : ["loosePhoPFPhoIso", "phosel_noCut_PhoIso_barrel",       [400,0,40], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoIsBarrel")  , "", True],
                      "phosel_AntiSIEIE_ChIso"                : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso"           ,   [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && ((loosePhoIsBarrel && (loosePhoSIEIE>00.011 && loosePhoSIEIE<0.02))||(!loosePhoIsBarrel && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.045)))") , "", True],
                      "phosel_AntiSIEIE_ChIso_barrel"       : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_barrel"    ,   [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.02) && loosePhoIsBarrel && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")  , "", True],
                      "phosel_AntiSIEIE_ChIso_endcap"         : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_endcap"    ,   [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.045) && !loosePhoIsBarrel && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")  , "", True],

                      "phosel_AntiSIEIE_ChIso_GenuinePhoton_barrel"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_GenuinePhoton_barrel"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel")       , "", False],
                      "phosel_AntiSIEIE_ChIso_GenuinePhoton"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_GenuinePhoton"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine")       , "", False],
		      "phosel_AntiSIEIE_ChIso_MisIDEle"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_MisIDEle"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle")       , "", False],
		      "phosel_AntiSIEIE_ChIso_HadronicPhoton"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_HadronicPhoton"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton")       , "", False],
		      "phosel_AntiSIEIE_ChIso_HadronicFake"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_HadronicFake"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake")       , "", False],
		      "phosel_AntiSIEIE_ChIso_GenuinePhoton_endcap"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_GenuinePhoton_endcap"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.045) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && !loosePhoIsBarrel")       , "", False],
		      "phosel_AntiSIEIE_ChIso_MisIDEle_barrel"          : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_MisIDEle_barrel"       ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel")      , "", False],
                      "phosel_AntiSIEIE_ChIso_MisIDEle_endcap"          : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_MisIDEle_endcap"       ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.045) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && !loosePhoIsBarrel")      , "", False],
		       "phosel_AntiSIEIE_ChIso_HadronicPhoton_endcap"   : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_HadronicPhoton_endcap" ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.045) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && !loosePhoIsBarrel"), "", False],
			"phosel_AntiSIEIE_ChIso_HadronicPhoton_barrel"  : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_HadronicPhoton_barrel" ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"), "", False],
                      "phosel_AntiSIEIE_ChIso_HadronicFake_barrel"      : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_HadronicFake_barrel"   ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel")  , "", False],
                       "phosel_AntiSIEIE_ChIso_HadronicFake_endcap"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_HadronicFake_endcap"   ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.045) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && !loosePhoIsBarrel")  , "", False],


                      "phosel_AntiSIEIE_SB1_ChIso"                : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso"           ,   [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && ((loosePhoIsBarrel && (loosePhoSIEIE>00.011 && loosePhoSIEIE<0.015))||(!loosePhoIsBarrel && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.0375)))") , "", True],
                      "phosel_AntiSIEIE_SB1_ChIso_barrel"       : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_barrel"    ,   [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.015) && loosePhoIsBarrel && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")  , "", True],
                      "phosel_AntiSIEIE_SB1_ChIso_endcap"         : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_endcap"    ,   [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.0375) && !loosePhoIsBarrel && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")  , "", True],

                      "phosel_AntiSIEIE_SB1_ChIso_GenuinePhoton_barrel"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_GenuinePhoton_barrel"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.015) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel")       , "", False],
                      "phosel_AntiSIEIE_SB1_ChIso_GenuinePhoton_endcap"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_GenuinePhoton_endcap"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.0375) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && !loosePhoIsBarrel")       , "", False],
		      "phosel_AntiSIEIE_SB1_ChIso_MisIDEle_barrel"          : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_MisIDEle_barrel"       ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.015) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel")      , "", False],
                      "phosel_AntiSIEIE_SB1_ChIso_MisIDEle_endcap"          : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_MisIDEle_endcap"       ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.0375) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && !loosePhoIsBarrel")      , "", False],
		       "phosel_AntiSIEIE_SB1_ChIso_HadronicPhoton_endcap"   : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_HadronicPhoton_endcap" ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.0375) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && !loosePhoIsBarrel"), "", False],
			"phosel_AntiSIEIE_SB1_ChIso_HadronicPhoton_barrel"  : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_HadronicPhoton_barrel" ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.015) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"), "", False],
                      "phosel_AntiSIEIE_SB1_ChIso_HadronicFake_barrel"      : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_HadronicFake_barrel"   ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.011 && loosePhoSIEIE<0.015) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel")  , "", False],
                       "phosel_AntiSIEIE_SB1_ChIso_HadronicFake_endcap"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB1_ChIso_HadronicFake_endcap"   ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.031 && loosePhoSIEIE<0.0375) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && !loosePhoIsBarrel")  , "", False],


                      "phosel_AntiSIEIE_SB2_ChIso"                : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso"           ,   [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && ((loosePhoIsBarrel && (loosePhoSIEIE>00.014 && loosePhoSIEIE<0.02))||(!loosePhoIsBarrel && (loosePhoSIEIE>0.0375 && loosePhoSIEIE<0.045)))") , "", True],
                      "phosel_AntiSIEIE_SB2_ChIso_barrel"       : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_barrel"    ,   [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.015 && loosePhoSIEIE<0.02) && loosePhoIsBarrel && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")  , "", True],
                      "phosel_AntiSIEIE_SB2_ChIso_endcap"         : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_endcap"    ,   [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.0375 && loosePhoSIEIE<0.045) && !loosePhoIsBarrel && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")  , "", True],

                      "phosel_AntiSIEIE_SB2_ChIso_GenuinePhoton_barrel"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_GenuinePhoton_barrel"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.015 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel")       , "", False],
                      "phosel_AntiSIEIE_SB2_ChIso_GenuinePhoton_endcap"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_GenuinePhoton_endcap"  ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.0375 && loosePhoSIEIE<0.045) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && !loosePhoIsBarrel")       , "", False],
		      "phosel_AntiSIEIE_SB2_ChIso_MisIDEle_barrel"          : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_MisIDEle_barrel"       ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.015 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel")      , "", False],
                      "phosel_AntiSIEIE_SB2_ChIso_MisIDEle_endcap"          : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_MisIDEle_endcap"       ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.0375 && loosePhoSIEIE<0.045) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && !loosePhoIsBarrel")      , "", False],
		       "phosel_AntiSIEIE_SB2_ChIso_HadronicPhoton_endcap"   : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_HadronicPhoton_endcap" ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.0375 && loosePhoSIEIE<0.045) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && !loosePhoIsBarrel"), "", False],
			"phosel_AntiSIEIE_SB2_ChIso_HadronicPhoton_barrel"  : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_HadronicPhoton_barrel" ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.015 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"), "", False],
                      "phosel_AntiSIEIE_SB2_ChIso_HadronicFake_barrel"      : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_HadronicFake_barrel"   ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.015 && loosePhoSIEIE<0.02) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel")  , "", False],
                       "phosel_AntiSIEIE_SB2_ChIso_HadronicFake_endcap"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_SB2_ChIso_HadronicFake_endcap"   ,  [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE>0.0375 && loosePhoSIEIE<0.045) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && !loosePhoIsBarrel")  , "", False],


                      #################
		      "phosel_R9_barrel"                      : ["phoR9"             , "phosel_R9_barrel",  [100,0.3,1.2], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
 
                      "phosel_NGenuinePhoton"                 : ["nPho"              , "phosel_NGenuinePhoton"       ,          [2,0,2], extraPhotonCuts%("photonIsGenuine")                       , "", False],
                      "phosel_NMisIDEle"                      : ["nPho"              , "phosel_NMisIDEle"         ,          [2,0,2], extraPhotonCuts%("photonIsMisIDEle")                      , "", False],
                      "phosel_NHadronicPhoton"                : ["nPho"              , "phosel_NHadronicPhoton"      ,          [2,0,2], extraPhotonCuts%("photonIsHadronicPhoton")                , "", False],
                      "phosel_NHadronicFake"                  : ["nPho"              , "phosel_NHadronicFake"     ,          [2,0,2], extraPhotonCuts%("photonIsHadronicFake")                  , "", False],
                      "phosel_mcMomPIDGenuinePhoton"          : ["photonParentPID"   , "phosel_mcMomPIDGenuinePhoton",[2000,-1000,1000], extraPhotonCuts%("nPho>=1 && photonIsGenuine")        , "", False],
         #             "phosel_mcMomPIDMisIDEle"              : ["photonParentPID"   , "phosel_mcMomPIDMisIDEle"  ,[2000,-1000,1000], extraPhotonCuts%("nPho>=1 && photonIsMisIDEle")       , "", False],
          #            "phosel_mcMomPIDHadronicPhoton"        : ["photonParentPID"   , "phosel_mcMomPIDHadronicPhoton"    ,[2000,-1000,1000], extraPhotonCuts%("nPho>=1 && photonIsHadronicPhoton") , "", False],
           #           "phosel_mcMomPIDHadronicFake"          : ["photonParentPID"   , "phosel_mcMomPIDHadronicFake"   ,[2000,-1000,1000], extraPhotonCuts%("nPho>=1 && photonIsHadronicFake")   , "", False],
                      "phosel_PhotonCategory"                 : ["photonIsGenuine[0] + 2*photonIsMisIDEle[0] + 3*photonIsHadronicPhoton[0] + 4*photonIsHadronicFake[0]", "phosel_PhotonCategory", [4,1,5], extraPhotonCuts%("nPho>=1"), "", False],
		      "phosel_PhotonCategory_barrel"                 : ["photonIsGenuine[0] + 2*photonIsMisIDEle[0] + 3*photonIsHadronicPhoton[0] + 4*photonIsHadronicFake[0]", "phosel_PhotonCategory_barrel", [4,1,5], extraPhotonCuts%("nPhoBarrel>=1"), "", False],
                      ################
                      "phosel_MassLepGamma"                   : ["phoMassLepGamma", "phosel_MassLepGamma", [300,0,300], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_MassLepGammaFromW"             : ["phoMassLepGamma", "phosel_MassLepGammaFromW", [300,0,300], extraPhotonCuts%("nPho>=1 && phoEt>40 && (phoGenMatchInd>0 && abs(mcMomPID[phoGenMatchInd])==24 )"), "", True],
                      "phosel_MassLepGammaNotFromW"             : ["phoMassLepGamma", "phosel_MassLepGammaNotFromW", [300,0,300], extraPhotonCuts%("nPho>=1 && phoEt>40 && !(phoGenMatchInd>0 && abs(mcMomPID[phoGenMatchInd])==24 )"), "", True],

                      "phosel_MassEGamma"        : ["phoMassEGamma", "phosel_MassEGamma", [200,0,200], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_MassEGammaMisIDEle"             : ["phoMassEGamma", "phosel_MassEGammaMisIDEle", [200,0,200], extraPhotonCuts%("nPho>=1 && photonIsMisIDEle"), "", True],
                      "phosel_MassEGammaOthers"               : ["phoMassEGamma", "phosel_MassEGammaOthers", [200,0,200], extraPhotonCuts%("nPho>=1 && (photonIsGenuine||photonIsHadronicFake||photonIsHadronicPhoton)"), "", True],
                      "phosel_MassEGamma_barrel" : ["phoMassEGamma", "phosel_MassEGamma_barrel", [200,0,200], extraPhotonCuts%("nPhoBarrel>=1"), "", True],
                      "phosel_MassEGamma_MisIDEle_barrel"  : ["phoMassEGamma", "phosel_MassEGamma_MisIDEle_barrel", [200,0,200], extraPhotonCuts%("nPhoBarrel>=1 && photonIsMisIDEle"), "", True],
		      "phosel_MassEGamma_GenuinePhoton_barrel" : ["phoMassEGamma", "phosel_MassEGamma_GenuinePhoton_barrel", [200,0,200], extraPhotonCuts%("nPhoBarrel>=1 && photonIsGenuine"), "", True],
                      "phosel_MassEGammaOthers_barrel"               : ["phoMassEGamma", "phosel_MassEGammaOthers_barrel", [200,0,200], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsGenuine||photonIsHadronicFake||photonIsHadronicPhoton)"), "", True],
		      "phosel_MassEGamma_NonPrompt_barrel"  : ["phoMassEGamma", "phosel_MassEGamma_NonPrompt_barrel", [200,0,200], extraPhotonCuts%("nPhoBarrel>=1 && (photonIsHadronicFake||photonIsHadronicPhoton)"), "", True],
                      "phosel_MassEGamma_endcap"                     : ["phoMassEGamma", "phosel_MassEGamma_endcap", [200,0,200], extraPhotonCuts%("nPho>=1 && !phoIsBarrel[0]"), "", True],
                      "phosel_MassEGammaMisIDEle_endcap"             : ["phoMassEGamma", "phosel_MassEGammaMisIDEle_endcap", [200,0,200], extraPhotonCuts%("nPho>=1 && photonIsMisIDEle && !phoIsBarrel[0]"), "", True],
                      "phosel_MassEGammaOthers_endcap"               : ["phoMassEGamma", "phosel_MassEGammaOthers_endcap", [200,0,200], extraPhotonCuts%("nPho>=1 && !phoIsBarrel[0] && (photonIsGenuine||photonIsHadronicFake||photonIsHadronicPhoton)"), "", True],

                      "phosel_Mt_blgammaMET"                  : ["Mt_blgammaMET" , "phosel_Mt_blgammaMET" , [600,0,600], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_Mt_lgammaMET"                   : ["Mt_lgammaMET"  , "phosel_Mt_lgammaMET"  , [600,0,600], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_M_bjj"                          : ["M_bjj"         , "phosel_M_bjj"         , [600,0,600], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_M_jj"                           : ["M_jj"          , "phosel_M_jj"          , [600,0,600], extraPhotonCuts%("nPho>=1"), "", True],
                      "phosel_MassCuts"                       : ["MassCuts"      , "phosel_MassCuts"      , [2,0,2], extraPhotonCuts%("nPho>=1"), "", True],                  
                      "presel_DilepMass"                      : ["DilepMass"     , "presel_DilepMass"     , [300,0,300],extraCuts,"",True],
                      "presel_DilepDR"                      : ["DilepDelR"     , "presel_DilepDR"       , [100,0,6],extraCuts,"",True],
                      #"phosel_DilepMass"                      : ["DilepMass"     , "phosel_DilepMass"     , [300,0,300],extraPhotonCuts%("nPho>=1"),"",True],
                      #"phosel_DilepDR"                      : ["DilepDelR"     , "phosel_DilepDR"       , [100,0,6]  ,extraPhotonCuts%("nPho>=1"),"",True],
                      "phosel_noCutSIEIEChIso_GenuinePhoton_barrel"         : ["loosePhoPFChIso"   , "phosel_noCutSIEIEChIso_GenuinePhoton_barrel"     ,     [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && loosePhoIsBarrel"), "", False],
                      "phosel_noCutSIEIEChIso_MisIDEle_barrel"           : ["loosePhoPFChIso"   , "phosel_noCutSIEIEChIso_MisIDEle_barrel"       ,     [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && loosePhoIsBarrel"), "", False],
                      "phosel_noCutSIEIEChIso_HadronicPhoton_barrel"             : ["loosePhoPFChIso"   , "phosel_noCutSIEIEChIso_HadronicPhoton_barrel"         ,     [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && loosePhoIsBarrel"), "", False],
                      "phosel_noCutSIEIEChIso_HadronicFake_barrel"            : ["loosePhoPFChIso"   , "phosel_noCutSIEIEChIso_HadronicFake_barrel"        ,     [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && loosePhoIsBarrel"), "", False],
                      "phosel_noCutSIEIEChIso_GenuinePhoton_endcap"         : ["loosePhoPFChIso"   , "phosel_noCutSIEIEChIso_GenuinePhoton_endcap"     ,     [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine && !loosePhoIsBarrel"), "", False],
                      "phosel_noCutSIEIEChIso_MisIDEle_endcap"           : ["loosePhoPFChIso"   , "phosel_noCutSIEIEChIso_MisIDEle_endcap"       ,     [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle && !loosePhoIsBarrel"), "", False],
                      "phosel_noCutSIEIEChIso_HadronicPhoton_endcap"             : ["loosePhoPFChIso"   , "phosel_noCutSIEIEChIso_HadronicPhoton_endcap"         ,     [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton && !loosePhoIsBarrel"), "", False],
                      "phosel_noCutSIEIEChIso_HadronicFake_endcap"            : ["loosePhoPFChIso"   , "phosel_noCutSIEIEChIso_HadronicFake_endcap"        ,    [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake && !loosePhoIsBarrel"), "", False],
		      "phosel_noCutSIEIEChIso"  : ["loosePhoPFChIso"   , "phosel_noCutSIEIEChIso", [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      }
    return histogramInfo
