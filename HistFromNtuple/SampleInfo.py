#-----------------------------------------
#INPUT AnalysisNtuples Directory
#----------------------------------------
dirBase = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples"
dirBaseDiLep = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/Dilepton"
dirBaseCR = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion"
dirSyst = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/Systematics"
dirSystCR = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/Systematics"

#-----------------------------------------
#Name of the ROOT files
#----------------------------------------
samples = {"TTGamma"   : [["TTGamma_SingleLept_2016_AnalysisNtuple.root",
                           "TTGamma_Dilepton_2016_AnalysisNtuple.root",
                           "TTGamma_Hadronic_2016_AnalysisNtuple.root"]
                          ],

           "TTGJets"   : [["TTGJets_AnalysisNtuple.root"]
                          ],

           "TTbar"     : [["TTbarPowheg_Semilept_2016_AnalysisNtuple_1of5.root",
                           "TTbarPowheg_Semilept_2016_AnalysisNtuple_2of5.root",
                           "TTbarPowheg_Semilept_2016_AnalysisNtuple_3of5.root",
                           "TTbarPowheg_Semilept_2016_AnalysisNtuple_4of5.root",
                           "TTbarPowheg_Semilept_2016_AnalysisNtuple_5of5.root",
                           "TTbarPowheg_Dilepton_2016_AnalysisNtuple_1of5.root",
                           "TTbarPowheg_Dilepton_2016_AnalysisNtuple_2of5.root",
                           "TTbarPowheg_Dilepton_2016_AnalysisNtuple_3of5.root",
                           "TTbarPowheg_Dilepton_2016_AnalysisNtuple_4of5.root",
                           "TTbarPowheg_Dilepton_2016_AnalysisNtuple_5of5.root",
                           "TTbarPowheg_Hadronic_2016_AnalysisNtuple.root"]
                          ],

           "TGJets"    :[["TGJets_2016_AnalysisNtuple.root"]
                         ],

           "WJets"     : [["W1jets_2016_AnalysisNtuple.root",
                           "W2jets_2016_AnalysisNtuple.root",
                           "W3jets_2016_AnalysisNtuple.root",
                           "W4jets_2016_AnalysisNtuple.root"]
                          ],

           "ZJets"     : [["DYjetsM10to50_2016_AnalysisNtuple.root",
                           "DYjetsM50_2016_AnalysisNtuple_1of5.root",
                           "DYjetsM50_2016_AnalysisNtuple_2of5.root",
                           "DYjetsM50_2016_AnalysisNtuple_3of5.root",
                           "DYjetsM50_2016_AnalysisNtuple_4of5.root",
                           "DYjetsM50_2016_AnalysisNtuple_5of5.root"]
                          ],

           "WGamma"    : [["WGamma_01J_5f_2016_AnalysisNtuple.root"]
                          ],

           "ZGamma"    : [["ZGamma_01J_5f_lowMass_2016_AnalysisNtuple.root"]
                          ],

           "Diboson"   : [["WWToLNuQQ_2016_AnalysisNtuple.root",
                            "WWTo4Q_2016_AnalysisNtuple.root",
                            "WZTo1L1Nu2Q_2016_AnalysisNtuple.root",
                            "WZTo1L3Nu_2016_AnalysisNtuple.root",
                            "WZTo2L2Q_2016_AnalysisNtuple.root",
                            "WZTo3L1Nu_2016_AnalysisNtuple.root",
                            "ZZTo2L2Q_2016_AnalysisNtuple.root",
                            "ZZTo2Q2Nu_2016_AnalysisNtuple.root",
                            "ZZTo4L_2016_AnalysisNtuple.root",
                            "VVTo2L2Nu_2016_AnalysisNtuple.root"]
                          ],

           "SingleTop" : [["ST_s_channel_2016_AnalysisNtuple.root",
                           "ST_t_channel_2016_AnalysisNtuple.root",
                           "ST_tW_channel_2016_AnalysisNtuple.root",
                           "ST_tbar_channel_2016_AnalysisNtuple.root",
                           "ST_tbarW_channel_2016_AnalysisNtuple.root"]
                          ],

           "TTV"       : [["TTWtoQQ_2016_AnalysisNtuple.root",
                           "TTWtoLNu_2016_AnalysisNtuple.root",
                           "TTZtoLL_2016_AnalysisNtuple.root",
                           "TTZtoLL_M1to10_2016_AnalysisNtuple.root",
                           "TTZtoQQ_2016_AnalysisNtuple.root"]
                          ],

           "QCDEle"    : [["QCD_Pt20to30_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt30to50_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt50to80_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt80to120_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt120to170_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt170to300_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt300toInf_Ele_2016_AnalysisNtuple.root"]
                          ],

           "QCDMu"    : [["QCD_Pt20to30_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt30to50_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt50to80_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt80to120_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt120to170_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt170to300_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt300to470_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt470to600_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt600to800_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt800to1000_Mu_2016_AnalysisNtuple.root",
                          "QCD_Pt1000toInf_Mu_2016_AnalysisNtuple.root"]
                         ],

           "GJets"     : [["GJets_HT40To100_2016_AnalysisNtuple.root",
                           "GJets_HT100To200_2016_AnalysisNtuple.root",
                           "GJets_HT200To400_2016_AnalysisNtuple.root",
                           "GJets_HT400To600_2016_AnalysisNtuple.root",
                           "GJets_HT600ToInf_2016_AnalysisNtuple.root"]
                          ],

           "DataMu"    : [["Data_SingleMu_b_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleMu_b_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleMu_b_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleMu_b_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleMu_b_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleMu_c_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleMu_c_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleMu_c_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleMu_c_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleMu_c_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleMu_d_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleMu_d_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleMu_d_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleMu_d_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleMu_d_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleMu_e_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleMu_e_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleMu_e_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleMu_e_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleMu_e_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleMu_f_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleMu_f_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleMu_f_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleMu_f_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleMu_f_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleMu_g_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleMu_g_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleMu_g_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleMu_g_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleMu_g_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleMu_h_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleMu_h_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleMu_h_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleMu_h_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleMu_h_2016_AnalysisNtuple_5of5.root"]
                          ],

           "DataEle"   : [["Data_SingleEle_b_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleEle_b_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleEle_b_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleEle_b_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleEle_b_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleEle_c_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleEle_c_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleEle_c_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleEle_c_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleEle_c_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleEle_d_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleEle_d_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleEle_d_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleEle_d_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleEle_d_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleEle_e_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleEle_e_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleEle_e_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleEle_e_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleEle_e_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleEle_f_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleEle_f_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleEle_f_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleEle_f_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleEle_f_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleEle_g_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleEle_g_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleEle_g_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleEle_g_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleEle_g_2016_AnalysisNtuple_5of5.root",
                           "Data_SingleEle_h_2016_AnalysisNtuple_1of5.root",
                           "Data_SingleEle_h_2016_AnalysisNtuple_2of5.root",
                           "Data_SingleEle_h_2016_AnalysisNtuple_3of5.root",
                           "Data_SingleEle_h_2016_AnalysisNtuple_4of5.root",
                           "Data_SingleEle_h_2016_AnalysisNtuple_5of5.root"]
                          ]
           }
# List that is the same as the keys of samples, but given in the order we want to draw
sampleList = ["TTGamma",
              "TTbar",
              "TGJets",
              "SingleTop",
              "WJets",
              "ZJets",
              #"ZJets_NLO",
              "WGamma",
              "ZGamma",
              "Diboson",
              "TTV",
              "GJets",
              "QCD",
              "Data",
              ]


