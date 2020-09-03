#-----------------------------------------------------------------
condorHistDir  = "/eos/uscms/store/user/rverma/OutputTTGamma"
#-----------------------------------------------------------------
#Year 	      =	["2016", "2017", "2018"]
Year 	      =	["2016"]
#Channel 	  =	["Mu", "Ele"]
#Decay 	  =	["Semilep", "Dilep"]
Decay 	  =	["Semilep", "Dilep"]
#Decay 	  =	["Semilep"]
Channel 	  =	["Mu"]
SampleList    =	["TTGamma", "TTbar", "TGJets", "WJets", "ZJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","GJets"]
Samples       = SampleList+["data_obs"]
SamplesOther    =	["TGJets", "WJets", "ZJets", "Diboson", "SingleTop", "TTV","GJets", "QCD"]
#SampleList    =	["TTGamma", "TTbar"]
SampleListEle = SampleList + ["QCDEle", "DataEle", "QCD_DD"]
SampleListMu  = SampleList + ["QCDMu", "DataMu", "QCD_DD"]
Systematics   =	["PU","MuEff","PhoEff","BTagSF_b","BTagSF_l","EleEff","Q2","Pdf","isr","fsr"]
#Systematics   =	["PU"]
SystLevel     = ["Up", "Down"]
ControlRegion = ["tight_a4j_a1b", "tight_a4j_e0b"]
#ControlRegion=["tight_a4j_a1b", "veryTight_a4j_a2b", "tight_a4j_e0b", "looseCR_a2j_e1b", "looseCR_a2j_a0b", "looseCR_a2j_e0b", "looseCR_e3j_a2b", "looseCR_e3j_e0b", "looseCR_e2j_e1b", "looseCR_e2j_e0j", "looseCR_e2j_e2b", "looseCR_e3j_e1b"]

#-------------------
#For misID 
#-------------------
SampleMisIDOther =	["TTGamma", "TGJets", "WJets", "ZJets", "Diboson", "SingleTop", "TTV","GJets", "QCD"]
SampleMisIDWZGamma   =	["WGamma", "ZGamma"]
SampleMisIDAll = SampleMisIDWZGamma + SampleMisIDOther

#-------------------
#For Dilep 
#-------------------
SampleDilep   =	["ZJets"]
SampleDilepOther    =	["TTGamma", "TTbar", "TGJets", "WJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","GJets"]
