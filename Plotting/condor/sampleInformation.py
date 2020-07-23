

from ROOT import *
def main(args):
	isMC=999
	isData=1
	selYear = args[0]
	samples = {"TTGamma"   : [[#"TTGamma_SingleLeptFromTbar_%s_AnalysisNtuple.root"%selYear,
	                           #"TTGamma_SingleLeptFromT_%s_AnalysisNtuple.root"%selYear,
	                           "TTGamma_SingleLept_%s_AnalysisNtuple.root"%selYear,
	                           "TTGamma_Dilepton_%s_AnalysisNtuple.root"%selYear,
	                           "TTGamma_Hadronic_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kOrange,#kAzure+7,
	                          "t#bar{t}+#gamma",
	                          isMC
	                          ],
	           "TTGJets"   : [["TTGJets_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kOrange,#kAzure+7,
	                          "t#bar{t}+#gamma",
	                          isMC
	                          ],
	           "TTbar"     : [["TTbarPowheg_Dilepton_%s_AnalysisNtuple.root"%selYear,
	                           "TTbarPowheg_Hadronic_%s_AnalysisNtuple.root"%selYear,
	                           "TTbarPowheg_Semilept_%s_AnalysisNtuple.root"%selYear],
	                           #"TTbarPowheg_Semilept_%s_AnalysisNtuple_1of5.root"%selYear,
	                           #"TTbarPowheg_Semilept_%s_AnalysisNtuple_2of5.root"%selYear,
	                           #"TTbarPowheg_Semilept_%s_AnalysisNtuple_3of5.root"%selYear,
	                           #"TTbarPowheg_Semilept_%s_AnalysisNtuple_4of5.root"%selYear,	                           	                           	                           
	                           #"TTbarPowheg_Semilept_%s_AnalysisNtuple_5of5.root"%selYear,],
	                          kRed+1,
	                          "t#bar{t}",
	                          isMC
	                          ],
	           "TGJets"    :[["TGJets_%s_AnalysisNtuple.root"%selYear,
	                          ],
	                         kGray,
	                         "t+#gamma",
	                         isMC
	                         ],
	           "WJets"     : [["W1jets_%s_AnalysisNtuple.root"%selYear,
	                           "W2jets_%s_AnalysisNtuple.root"%selYear,
	                           "W3jets_%s_AnalysisNtuple.root"%selYear,
	                           "W4jets_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kCyan-3,
	                          "W+jets",
	                          isMC
	                          ],
	           "WJetsInclusive"     : [["WjetsInclusive1_%s_AnalysisNtuple.root"%selYear,
	                                    "WjetsInclusive2_%s_AnalysisNtuple.root"%selYear,
	                                    "WjetsInclusive3_%s_AnalysisNtuple.root"%selYear,
	                                    "WjetsInclusive4_%s_AnalysisNtuple.root"%selYear,
	                                    "WjetsInclusive5_%s_AnalysisNtuple.root"%selYear,
	                                    "WjetsInclusive6_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kCyan-3,
	                          "W+jets",
	                          isMC
	                          ],
	           "ZJets"     : [["DYjetsM10to50_%s_AnalysisNtuple.root"%selYear,#"DYjetsM10to50_MLM_%s_AnalysisNtuple.root"%selYear,
	                           "DYjetsM50_%s_AnalysisNtuple.root"%selYear,#"DYjetsM50_MLM_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kCyan-5,
	                          "Z+jets",
	                          isMC
	                          ],



		   "ZJets_NLO" : [["DYjetsM10to50_%s_AnalysisNtuple.root"%selYear,#"DYjetsM10to50_MLM_%s_AnalysisNtuple.root"%selYear,
	                           "DYjetsM50_%s_AnalysisNtuple.root"%selYear,#"DYjetsM50_MLM_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kCyan-5,
	                          "Z+jets",
	                          isMC
	                          ],

	           "WGamma"    : [["WGamma_01J_5f_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kBlue-4,
	                          "W+#gamma",
	                          isMC
	                          ],
	           "ZGamma"    : [["ZGamma_01J_5f_lowMass_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kBlue-2,
	                          "Z+#gamma",
	                          isMC
	                          ],
	           "Diboson"   : [["WW_%s_AnalysisNtuple.root"%selYear,
	                           "WZ_%s_AnalysisNtuple.root"%selYear,
	                           "ZZ_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kCyan-7,
	                          "WW/WZ/ZZ",
	                          isMC
	                          ],
	           "SingleTop" : [["ST_s_channel_%s_AnalysisNtuple.root"%selYear,
	                           "ST_t_channel_%s_AnalysisNtuple.root"%selYear,
	                           "ST_tW_channel_%s_AnalysisNtuple.root"%selYear,
	                           "ST_tbar_channel_%s_AnalysisNtuple.root"%selYear,
	                           "ST_tbarW_channel_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kOrange-3,
	                          "Single top",
	                          isMC
	                          ],
	           "ST-tch" : [["ST_t_channel_%s_AnalysisNtuple.root"%selYear,
	                        "ST_tbar_channel_%s_AnalysisNtuple.root"%selYear,
	                        ],
	                       kOrange-3,
	                       "Single top (t-ch.)",
	                       isMC
	                       ],
	           "ST-sch" : [["ST_s_channel_%s_AnalysisNtuple.root"%selYear,
	                        ],
	                       kOrange-4,
	                       "Single top (s-ch.)",
	                       isMC
	                       ],
	           "ST-tW" : [["ST_tW_channel_%s_AnalysisNtuple.root"%selYear,
	                        "ST_tbarW_channel_%s_AnalysisNtuple.root"%selYear,
	                        ],
	                       kOrange-5,
	                       "Single top (tW)",
	                       isMC
	                       ],
	           "TTV"       : [["TTWtoQQ_%s_AnalysisNtuple.root"%selYear,
	                           "TTWtoLNu_%s_AnalysisNtuple.root"%selYear,
	                           "TTZtoLL_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kRed-7,
	                          "ttV",
	                          isMC
	                          ],
	           "QCDEle"    : [["QCD_Pt20to30_Ele_%s_AnalysisNtuple.root"%selYear,
	                           "QCD_Pt30to50_Ele_%s_AnalysisNtuple.root"%selYear,
	                           "QCD_Pt50to80_Ele_%s_AnalysisNtuple.root"%selYear,
	                           "QCD_Pt80to120_Ele_%s_AnalysisNtuple.root"%selYear,
	                           "QCD_Pt120to170_Ele_%s_AnalysisNtuple.root"%selYear,
	                           "QCD_Pt170to300_Ele_%s_AnalysisNtuple.root"%selYear, 
	                           "QCD_Pt300toInf_Ele_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kGreen+3,
	                          "QCD",
	                          isMC
	                          ],

	           "QCDMu"    : [["QCD_Pt20to30_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt30to50_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt50to80_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt80to120_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt120to170_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt170to300_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt300to470_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt470to600_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt600to800_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt800to1000_Mu_%s_AnalysisNtuple.root"%selYear,
	                          "QCD_Pt1000toInf_Mu_%s_AnalysisNtuple.root"%selYear,
	                          ],
	                         kGreen+3,
	                         "QCD",
	                         isMC
	                         ],
	           "GJets"     : [["GJets_HT40To100_%s_AnalysisNtuple.root"%selYear,
	                           "GJets_HT100To200_%s_AnalysisNtuple.root"%selYear,
	                           "GJets_HT200To400_%s_AnalysisNtuple.root"%selYear,
	                           "GJets_HT400To600_%s_AnalysisNtuple.root"%selYear,
	                           "GJets_HT600ToInf_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kGreen+1,
	                          "#gamma+jets",
	                          isMC
	                          ],
	           "DataMu"    : [["Data_SingleMu_a_%s_AnalysisNtuple.root"%selYear,
					           "Data_SingleMu_b_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleMu_c_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleMu_d_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleMu_e_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleMu_f_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleMu_g_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleMu_h_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kBlack,
	                          "Data",
	                          isData
	                          ],
	           "DataEle"   : [["Data_SingleEle_a_%s_AnalysisNtuple.root"%selYear,
		           			   "Data_SingleEle_b_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleEle_c_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleEle_d_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleEle_e_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleEle_f_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleEle_g_%s_AnalysisNtuple.root"%selYear,
	                           "Data_SingleEle_h_%s_AnalysisNtuple.root"%selYear,
	                           ],
	                          kBlack,
	                          "Data",
	                          isData
	                          ],
	           }






	return samples
# List that is the same as the keys of samples, but given in the order we want to draw
sampleList = ["TTGamma",
              "TTbar",
              "TGJets",
              "SingleTop",
              "WJets",
              "ZJets",
              #"ZJets_NLO", # because we use SF in ZJets
              "WGamma",
              "ZGamma",
              "Diboson",
              "TTV",
              "GJets",
              "QCD",
              "Data",
              ]
if __name__ == '__main__':
	import sys
	main(sys.argv[0])


