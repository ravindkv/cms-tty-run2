#EOS specific commands
#https://uscms.org/uscms_at_work/computing/LPC/usingEOSAtLPC.shtml#doNot
#-----------------------------------------------------------------
condorHistDir  = "/store/user/rverma/OutputTTGamma"
#condorHistDir  = "/eos/uscms/store/user/rverma/OutputTTGamma"
#condorHistDir  = "root://cmseos.fnal.gov//store/user/rverma/OutputTTGamma/"
#-----------------------------------------------------------------
Year 	      =	["2016", "2017", "2018"]
#Year 	      =	["2016"]
Channel 	  =	["Mu", "Ele"]
#Channel 	  =	["Mu"]
Decay 	  =	["Semilep", "Dilep"]
#Decay 	  =	["Semilep"]
SampleList    =	["TTGamma", "TTbar", "TGJets", "WJets", "ZJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","GJets"]
Samples       = SampleList+["data_obs"]
SamplesOther    =	["TGJets", "WJets", "Diboson", "SingleTop", "TTV","GJets", "QCD"]
#SamplesOther    =	["TGJets", "WJets", "ZJets", "Diboson", "SingleTop", "TTV","GJets", "QCD"]
#SampleList    =	["TTGamma", "TTbar"]
SampleListEle = SampleList + ["QCDEle", "DataEle", "QCD_DD"]
SampleListMu  = SampleList + ["QCDMu", "DataMu", "QCD_DD"]
Systematics   =	["PU","MuEff","PhoEff","BTagSF_b","BTagSF_l","EleEff","Q2","Pdf","isr","fsr","JER", "JECTotal"]
#Systematics   =	["isr","fsr"]
SystLevel     = ["Up", "Down"]
ControlRegion = ["tight_a4j_e0b"] 
#ControlRegion = ["tight_a4j_e0b","tight_a2j_e0b"] 
#ControlRegion = ["tight_a4j_a1b", "tight_a4j_e0b", "tight_a3j_a1b", "tight_a3j_e0b","tight_e3j_a1b", "tight_e3j_e0b"]
#ControlRegion=["tight_a4j_a1b", "veryTight_a4j_a2b", "tight_a4j_e0b", "looseCR_a2j_e1b", "looseCR_a2j_a0b", "looseCR_a2j_e0b", "looseCR_e3j_a2b", "looseCR_e3j_e0b", "looseCR_e2j_e1b", "looseCR_e2j_e0b", "looseCR_e2j_e2b", "looseCR_e3j_e1b"]
#CountBased = ["--isCount",""]
CountBased = [""]

#-------------------
#For MassLepGamma 
#-------------------
SampleWZGammaMassLG   =	["WGamma", "ZGamma", "ZJets"]
SampleOtherMassLG =	["TTGamma", "TGJets", "WJets", "Diboson", "SingleTop", "TTV","GJets", "QCD"]
SampleAllMassLG = SampleWZGammaMassLG + SampleOtherMassLG
SampleNoZJetsMassLG = ["WGamma", "ZGamma"] + SampleOtherMassLG 

#-------------------
#For 0Pho 
#-------------------
SamplesOther0Pho    =	["TGJets", "WJets", "Diboson", "SingleTop", "TTV","GJets", "QCD"]

#-------------------
#For Dilep 
#-------------------
SampleDilep   =	["ZJets"]
SampleDilepOther    =	["TTGamma", "TTbar", "TGJets", "WJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","GJets"]

import os
def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)
