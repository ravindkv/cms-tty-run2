Year 	      =	["2016", "2017", "2018"]
Channel 	  =	["Mu", "Ele"]
#SampleList    =	["TTGamma", "TTbar", "TGJets", "WJets", "ZJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","GJets"]
SampleList    =	["TTGamma", "TTbar"]
SampleListEle = SampleList + ["QCDEle", "DataEle", "QCD_DD"]
SampleListMu  = SampleList + ["QCDMu", "DataMu", "QCD_DD"]
#Systematics   =	["PU","MuEff","PhoEff","BTagSF_b","BTagSF_l","EleEff","Q2","Pdf","isr","fsr"]
Systematics   =	["PU","MuEff","PhoEff"]
SystLevel     = ["up", "down"]
ControlRegion = ["tight"]

#Jet selection naming: a3j_e2b = atleast 3 jet, out of which 2 are b jets: nJet >= 3, nBJet ==2
#ControlRegion=["tight_a4j_a1b", "veryTight_a4j_a2b", "tight_a4j_e0b", "looseCR_a2j_e1b", "looseCR_a2j_a0b", "looseCR_a2j_e0b", "looseCR_e3j_a2b", "looseCR_e3j_e0b", "looseCR_e2j_e1b", "looseCR_e2j_e0j", "looseCR_e2j_e2b", "looseCR_e3j_e1b"]
