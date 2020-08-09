isMC=999
isData=1

from ROOT import *
import sys

samples = {"TTGamma"   : [["TTGamma_SingleLept_2016_AnalysisNtuple.root",
                           "TTGamma_Dilepton_2016_AnalysisNtuple.root",
                           "TTGamma_Hadronic_2016_AnalysisNtuple.root",
                           ],
                          kOrange,#kAzure+7,
                          "t#bar{t}+#gamma",
                          isMC
                          ],
           "TTGJets"   : [["TTGJets_AnalysisNtuple.root",
                           ],
                          kOrange,#kAzure+7,
                          "t#bar{t}+#gamma",
                          isMC
                          ],
           "TTbar"     : [["TTbarPowheg_Semilept_2016_AnalysisNtuple_1of5.root",
                           "TTbarPowheg_Semilept_2016_AnalysisNtuple_2of5.root",
                           "TTbarPowheg_Semilept_2016_AnalysisNtuple_3of5.root",
                           "TTbarPowheg_Semilept_2016_AnalysisNtuple_4of5.root",
                           "TTbarPowheg_Semilept_2016_AnalysisNtuple_5of5.root"
                           ],
                          kRed+1,
                          "t#bar{t}",
                          isMC
                          ],
           "TGJets"    :[["TGJets_2016_AnalysisNtuple.root",
                          ],
                         kGray,
                         "t+#gamma",
                         isMC
                         ],
           "WJets"     : [["W1jets_2016_AnalysisNtuple.root",
                           "W2jets_2016_AnalysisNtuple.root",
                           "W3jets_2016_AnalysisNtuple.root",
                           "W4jets_2016_AnalysisNtuple.root",
                           ],
                          kCyan-3,
                          "W+jets",
                          isMC
                          ],
           "ZJets"     : [["DYjetsM10to50_2016_AnalysisNtuple.root",#"DYjetsM10to50_MLM_AnalysisNtuple.root",
                           "DYjetsM50_2016_AnalysisNtuple_1of5.root",
                           "DYjetsM50_2016_AnalysisNtuple_2of5.root",
                           "DYjetsM50_2016_AnalysisNtuple_3of5.root",
                           "DYjetsM50_2016_AnalysisNtuple_4of5.root",
                           "DYjetsM50_2016_AnalysisNtuple_5of5.root",
                           ],
                          kCyan-5,
                          "Z+jets",
                          isMC
                          ],

           "WGamma"    : [["WGamma_01J_5f_2016_AnalysisNtuple.root",
                           ],
                          kBlue-4,
                          "W+#gamma",
                          isMC
                          ],
           "ZGamma"    : [["ZGamma_01J_5f_LoosePt_2016_AnalysisNtuple.root", "ZGamma_01J_5f_lowMass_2016_AnalysisNtuple.root",
                           ],
                          kBlue-2,
                          "Z+#gamma",
                          isMC
                          ],
           "Diboson"   : [["WW_2016_AnalysisNtuple.root",
                           "WZ_2016_AnalysisNtuple.root",
                           "ZZ_2016_AnalysisNtuple.root",
                           ],
                          kCyan-7,
                          "WW/WZ/ZZ",
                          isMC
                          ],
           "SingleTop" : [["ST_s_channel_2016_AnalysisNtuple.root",
                           "ST_t_channel_2016_AnalysisNtuple.root",
                           "ST_tW_channel_2016_AnalysisNtuple.root",
                           "ST_tbar_channel_2016_AnalysisNtuple.root",
                           "ST_tbarW_channel_2016_AnalysisNtuple.root",
                           ],
                          kOrange-3,
                          "Single top",
                          isMC
                          ],
           "TTV"       : [["TTWtoQQ_2016_AnalysisNtuple.root",
                           "TTWtoLNu_2016_AnalysisNtuple.root",
                           "TTZtoLL_2016_AnalysisNtuple.root",
                           ],
                          kRed-7,
                          "ttV",
                          isMC
                          ],
           "QCDEle"    : [["QCD_Pt20to30_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt30to50_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt50to80_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt80to120_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt120to170_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt170to300_Ele_2016_AnalysisNtuple.root",
                           "QCD_Pt300toInf_Ele_2016_AnalysisNtuple.root",
                           ],
                          kGreen+3,
                          "QCD",
                          isMC
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
                          "QCD_Pt1000toInf_Mu_2016_AnalysisNtuple.root",
                          ],
                         kGreen+3,
                         "QCD",
                         isMC
                         ],
           "GJets"     : [["GJets_HT40To100_2016_AnalysisNtuple.root",
                           "GJets_HT100To200_2016_AnalysisNtuple.root",
                           "GJets_HT200To400_2016_AnalysisNtuple.root",
                           "GJets_HT400To600_2016_AnalysisNtuple.root",
                           "GJets_HT600ToInf_2016_AnalysisNtuple.root",
                           ],
                          kGreen+3,
                          "#gamma+jets",
                          isMC
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
                           "Data_SingleMu_h_2016_AnalysisNtuple_5of5.root"
                           ],
                          kBlack,
                          "Data",
                          isData
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
                           "Data_SingleEle_h_2016_AnalysisNtuple_5of5.root"
                           ],
                          kBlack,
                          "Data",
                          isData
                          ],
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


#----------------------------------------------------------
#NICE WAY TO PRINT STRINGS
#----------------------------------------------------------
def toPrint(string, value):
    length = (len(string)+len(str(value))+2)
    line = "-"*length
    print ""
    print "* "+ line +                    " *"
    print "| "+ " "*length +              " |"
    print "| "+ string+ ": "+ str(value)+ " |"
    print "| "+ " "*length +              " |"
    print "* "+ line +                    " *"

#----------------------------------------------------------
#Get jet multiplicity cuts in a different control regions
#----------------------------------------------------------
#Jet selection naming: a3j_e2b = atleast 3 jet, out of which 2 are b jets: nJet >= 3, nBJet ==2
def getJetMultiCut(controlRegion="tight_a4j_e0b", isQCDMC=False):
        if not len(controlRegion.split("_"))==3 and not controlRegion=="":
    	        print "Please provide control region in NAME_ExpNumJet_ExpNumBJet formate such as tight_a4j_e0b"
                sys.exit()
	nBJets, finalCuts=1, "nJet>=3 && nBJet>=1"
	if isQCDMC: 
		finalCuts="nJet>=3 && nBJet==0"
	if not controlRegion=="":
		splitCR = controlRegion.split("_")
		jetCut  = splitCR[1].strip()
		bJetCut = splitCR[2].strip()
		#For total jets 
		operationJet, numberJet = jetCut[0].strip(), jetCut[1].strip()
		expresssionJet = "=="
		if operationJet=="a": 
			expresssionJet=">="
		newJetCut = "nJet%s%s"%(expresssionJet, numberJet)
		#For b jets
		operationBJet, numberBJet = bJetCut[0].strip(), bJetCut[1].strip()
		expresssionBJet = "=="
		if(operationBJet=="a"): 
			expresssionBJet=">="
		newBJetCut = "nBJet%s%s"%(expresssionBJet, numberBJet)
		#Combine the two selection
       	        finalCuts = "%s && %s"%(newJetCut, newBJetCut) 
		nBJets = int(numberBJet)
		if isQCDMC: 
		    	finalCuts = "%s && %s"%(newJetCut, "nBJet==0") 
			nBJets = 0
	print nBJets, finalCuts
	return nBJets, finalCuts

