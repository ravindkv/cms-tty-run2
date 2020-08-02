
import itertools
import os
SampleList    =	["TTGamma", "TTbar", "TGJets", "WJets", "ZJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","GJets", "WJets", "TGJets"]
#Systematics   =	["Base","PU","MuEff","PhoEff","BTagSF_b","BTagSF_l","EleEff","Q2","Pdf","isr","fsr"]
Systematics   =	["Base","PU"]
SystLevel     = ["up", "down"]
SampleListMu  = SampleList + ["QCDMu", "DataMu"]

for sample, syst in itertools.product(SampleListMu, Systematics):
    if syst=="Base":
        cmd = "python makeHists13TeV.py -s %s --syst %s --plot presel_Njet &"%(sample, syst)
        print cmd
        #os.system(cmd)
    else:
	for level in SystLevel:
	    cmd = "python makeHists13TeV.py -s %s --syst %s --level %s --plot presel_Njet &"%(sample, syst, level)
            print cmd
            #os.system(cmd)
