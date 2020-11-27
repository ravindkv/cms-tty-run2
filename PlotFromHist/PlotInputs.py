import ROOT as rt
#-----------------------------------------------------------------
condorHistDir = "/eos/uscms/store/user/rverma/OutputTTGamma"
#-----------------------------------------------------------------
#Year 	      =	["2016", "2017", "2018"]
Year 	      =	["2016"]
#Channel 	  =	["Mu", "Ele"]
#Decay 	  =	["Semilep", "Dilep"]
Decay 	  =	["Semilep"]
Channel 	  =	["Mu"]
Systematics   =	["PU","MuEff","PhoEff","BTagSF_b","BTagSF_l","EleEff","Q2","Pdf","isr","fsr"]
#Systematics   =	["PU","Q2"]
SystLevel     = ["Up", "Down"]
ControlRegion = ["tight_a4j_a1b", "looseCR_a2j_e1b",]
#ControlRegion=["tight_a4j_a1b", "veryTight_a4j_a2b", "tight_a4j_e0b", "looseCR_a2j_e1b", "looseCR_a2j_a0b", "looseCR_a2j_e0b", "looseCR_e3j_a2b", "looseCR_e3j_e0b", "looseCR_e2j_e1b", "looseCR_e2j_e0j", "looseCR_e2j_e2b", "looseCR_e3j_e1b"]
isMC = True
isData = True
SamplesSyst    = ["TTGamma", "TTbar", "TGJets", "WJets", "ZJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","GJets", "QCD"]
Samples = {"TTGamma"   : [[""],
                          rt.kOrange,
                          "t#bar{t} + #gamma",
                          isMC
                          ],
           "TTbar"     : [[""],
                          rt.kRed+1,
                          "t#bar{t}",
                          isMC
                          ],
           "TGJets"    :[[""],
                         rt.kGray,
                         "t + #gamma",
                         isMC
                         ],
           "WJets"     : [[""],
                          rt.kCyan-3,
                          "W + jets",
                          isMC
                          ],
           "ZJets"     : [[""],
                          rt.kCyan-5,
                          "Z + jets",
                          isMC
                          ],
           "WGamma"    : [[""],
                          rt.kBlue-4,
                          "W + #gamma",
                          isMC
                          ],
           "ZGamma"    : [[""],
                          rt.kBlue-2,
                          "Z + #gamma",
                          isMC
                          ],
           "Diboson"   : [[""],
                          rt.kCyan-7,
                          "VV",
                          isMC
                          ],
           "SingleTop" : [[""],
                          rt.kOrange-3,
                          "Single t",
                          isMC
                          ],
           "TTV"       : [[""],
                          rt.kRed-7,
                          "ttV",
                          isMC
                          ],
           "QCD"    : [[""],
                          rt.kGreen,
                          "QCD MC",
                          isMC
                          ],
           "QCD_DD"    : [[""],
                          rt.kGreen,
                          "QCD DD",
                          isMC
                          ],

           "GJets"     : [[""],
                          rt.kGreen+3,
                          "#gamma + jets",
                          isMC
                          ],
           "Data"   : [[""],
                          rt.kBlack,
                          "Data",
                          isData
                          ],
           }
