## Make root files for combine with different MC signals and their systematics###
##uncertainties in both electron and muon channel####

from ROOT import *
import math
import os
import sys
from array import array
import CMS_lumi

from Style import *
thestyle = Style()
random=TRandom3(0)

_file = {}
from optparse import OptionParser


parser = OptionParser()

parser.add_option("-c", "--channel", dest="channel", default="mu",type='str',
                  help="Specify which channel mu or ele? default is mu" )
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                     help="Use 4j2t selection" )
parser.add_option("--LooseCR2g1","--looseCR2g1", dest="isLooseCR2g1Selection",default=False,action="store_true",
                  help="Use 2j at least 1t control region selection")
parser.add_option("--LooseCR3e0","--looseCR3e0", dest="isLooseCR3e0Selection",default=False,action="store_true",
                  help="Use 3j exactly 0t control region selection" )

(options, args) = parser.parse_args()


finalState = options.channel
TightSelection = options.isTightSelection
isLooseCR2g1Selection = options.isLooseCR2g1Selection
isLooseCR3e0Selection = options.isLooseCR3e0Selection


if isLooseCR3e0Selection:

        dir_ = "_looseCR3e0"
elif isLooseCR2g1Selection:
        dir_ = "_looseCR2g1"
else:
        dir_= ""



samples =["TTGamma","TTbar","TTV","TGJets","SingleTop","WJets","ZJets","WGamma","ZGamma","Diboson","QCD_DD"]
if finalState=="mu":
	samples.append("DataMu")
else:
	samples.append("DataEle")

for s in samples:
	_file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s/%s.root"%(finalState,dir_,s))

#exit()
misIDEleSF = 1.68
#misIDEleSF=1.0
misIDEle_unc = 0.071
if finalState=="mu":
	ZJetsSF=1.07
else:
	ZJetsSF=1.09


print "ZJets SF is :", ZJetsSF
HistDict={}
HistDict_up={}
HistDict_do={}
Temp={}
Temp_up={}
Temp_do={}
WJetstemp={}
WJetstemp_up={}
WJetstemp_do={}
WJets={}
WJets_up={}
WJets_do={}
_file_up={}
_file_do={}
if finalState=="mu":
	systematics = ["JER","JECTotal","phosmear","phoscale","BTagSF","Q2","Pdf","PU","MuEff","PhoEff"]
else:
	systematics = ["JER","JECTotal","phosmear","phoscale","BTagSF","Q2","Pdf","PU","EleEff","PhoEff","elesmear","elescale"]

systematics2 = ["isr","fsr"]


for sys in systematics2:
	_file_up[sys]={}
        _file_do[sys]={}


for sys in systematics:
      
       _file_up[sys]={}
       _file_do[sys]={}
       for s in samples:
		if s=="DataMu" or s=="DataEle":continue
		_file_up[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s/%s.root"%(finalState,sys,dir_,s))
		_file_do[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s/%s.root"%(finalState,sys,dir_,s))


for sys in systematics2:
	_file_up[sys]["TTGamma"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s/TTGamma.root"%(finalState,sys,dir_))
	_file_do[sys]["TTGamma"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s/TTGamma.root"%(finalState,sys,dir_))
	_file_up[sys]["TTbar"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s/TTbar.root"%(finalState,sys,dir_))
	_file_do[sys]["TTbar"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s/TTbar.root"%(finalState,sys,dir_))





binsM3=[]
binsChHad = [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0]
#print len(binsChHad)
#for i in binsChHad:
#	print i

#binsM3=[60., 80., 100, 110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240., 250., 260., 270., 280., 290., 300., 310., 320., 330., 340., 350., 360., 220., 380., 390., 400., 420., 440., 460., 480., 500.]#, 520., 540., 560., 580., 600.]
binsM3=[60., 80., 100, 120., 140., 160., 180., 200., 220., 240., 260., 280., 300., 320., 340., 360., 380., 400., 420., 440., 460., 480., 500.]

print len(binsM3)
#exit()
#for i in range(-10,300,10):
#	binsM3.append(i+10.)


#for i in range(300,595,20):
#	binsM3.append(i+20.)
#print len(binsM3)
#print binsM3

#exit()


systematics.append("MisIDEleshape")
observables={"M3": ["M3",binsM3],
	     "ChHad":["noCut_ChIso",binsChHad],
             "AntiSIEIE":["AntiSIEIE_ChIso",binsChHad],
	     "M3_control":["M3_control",binsM3]
           }

#print sorted(observables.keys())[:2]

process_signal = {"TTGamma_Prompt":["TTGamma"],
	   "TTGamma_NonPrompt":["TTGamma"],
           "TTbar_Prompt": ["TTbar"],
           "TTbar_NonPrompt": ["TTbar"],
           "VGamma_Prompt":["ZGamma","WGamma"],
           "VGamma_NonPrompt":["ZGamma","WGamma"],
           "VJets_Prompt":["ZJets", "WJets"],
           "VJets_NonPrompt":["ZJets", "WJets"],
           "SingleTop_Prompt":["TGJets", "SingleTop"],
           "SingleTop_NonPrompt":["TGJets", "SingleTop"],
           "Other_Prompt":["TTV", "Diboson","QCD_DD"],
           "Other_NonPrompt":["TTV", "Diboson","QCD_DD"],
	}



sub_signal=["TTGamma_Prompt","TTGamma_NonPrompt","TTbar_Prompt","TTbar_NonPrompt"]
sub_control=["TTGamma","TTbar"]

#exit()

process_control ={"TTGamma":["TTGamma"],
		  "TTbar":  ["TTbar"],
		  "VGamma":["ZGamma", "WGamma"],
		  "VJets":["WJets", "ZJets"],
                  "SingleTop":["TGJets", "SingleTop"],
		  "Other":[ "TTV", "Diboson","QCD_DD"],
		}	





##### Make Prompt and NonPrompt MC templates#######
process={}
for obs in observables:
	HistDict[obs]={}
	Temp[obs]={}
	WJetstemp[obs]={}
	Temp_up[obs]={}
	Temp_do[obs]={}
	WJetstemp_up[obs]={}
        WJetstemp_do[obs]={}
	WJets_up[obs]={}
        WJets_do[obs]={}
	WJets[obs]={}
	HistDict_up[obs]={}
	HistDict_do[obs]={}
        if obs=="M3_control":
		for p in process_control:
			s= process_control[p][0]
			HistDict_up[obs][p]={}
			HistDict_do[obs][p]={}
			HistDict[obs][p]   = _file[s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
			if s=="ZJets":
				HistDict[obs][p].Scale(ZJetsSF)	
			for sys in systematics:
				if sys=="MisIDEleshape":continue
				if sys=="Q2":
					HistDict_up[obs][p][sys] = _file_up[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					total_up= HistDict_up[obs][p][sys].Integral()
	
					#print total_up, "presel_%s_%s"%(observables[obs][0],s)
					HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
					HistDict_do[obs][p][sys] = _file_do[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					total_do= HistDict_do[obs][p][sys].Integral()
					HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do) 
				else:

					
					HistDict_up[obs][p][sys] = _file_up[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					HistDict_do[obs][p][sys] = _file_do[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					if s=="ZJets":
						HistDict_up[obs][p][sys].Scale(ZJetsSF)
						HistDict_do[obs][p][sys].Scale(ZJetsSF)
			
					

			for s in process_control[p][1:]:
				HistDict[obs][p].Add(_file[s].Get("presel_%s_%s"%(observables[obs][0],s)))
				for sys	in systematics:
					if sys=="MisIDEleshape":continue
					if sys=="Q2":continue
					HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)))
					HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)))
			HistDict[obs][p]=HistDict[obs][p].Rebin(22,"",array('d',binsM3))

		
			for sys in systematics:
				if sys=="MisIDEleshape":continue
                                HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
		for sys in systematics2:
			for p in sub_control:
				HistDict_up[obs][p][sys] = _file_up[sys][p].Get("presel_%s_%s"%(observables[obs][0],p)).Clone("%s_%s"%(obs,p))
				HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
                        	HistDict_do[obs][p][sys] = _file_do[sys][p].Get("presel_%s_%s"%(observables[obs][0],p)).Clone("%s_%s"%(obs,p))
				HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(22,"",array('d',binsM3))	

	
	elif obs=="M3":
		for p in process_signal:
			HistDict_up[obs][p]={}
                        HistDict_do[obs][p]={}
                        Temp_up[obs][p]={}
                        Temp_do[obs][p]={}
			WJetstemp_up[obs][p]={}
			WJetstemp_do[obs][p]={}
			WJets[obs][p]={}
			WJets_up[obs][p]={}
			WJets_do[obs][p]={}
			s = process_signal[p][0]
			if "TTGamma" in s or "TTbar" in s:
				 if "NonPrompt" in p:
                                 	HistDict[obs][p]   = _file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
					for sys in systematics:
						if sys=="MisIDEleshape":continue
						if "AntiSIEIE" in observables[obs][0]:continue
						if sys=="Q2":
							HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
							total_up= HistDict_up[obs][p][sys].Integral()
							HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
							HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
							total_do= HistDict_do[obs][p][sys].Integral()
							HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
						else:
							HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

							HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
	
				 if "_Prompt" in p:
					HistDict[obs][p]   = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
					for sys in systematics:
						if (finalState=="mu") and ("VJets" in p):continue
						if "AntiSIEIE" in observables[obs][0]:continue
						if sys=="Q2":
							HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
							total_up= HistDict_up[obs][p][sys].Integral()
	
							HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
							HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
							total_do= HistDict_do[obs][p][sys].Integral()
							HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
						elif sys=="MisIDEleshape":
							HistDict_up[obs][p][sys]=_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_up[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)

							HistDict_do[obs][p][sys]=_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_do[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF-misIDEle_unc)


						else:
							HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)

							HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
				
				 HistDict[obs][p]=HistDict[obs][p].Rebin(22,"",array('d',binsM3))
				 for sys in systematics:
					if "NonPrompt" in p and sys=="MisIDEleshape":continue
					HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
					HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(22,"",array('d',binsM3))

	
			else:
				if "_NonPrompt" in p:
					Temp[obs][p]   = _file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                        Temp[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                        
					
					HistDict[obs][p]   = _file[s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))
			
					if s=="ZJets":
                                        	Temp[obs][p].Scale(ZJetsSF)
                                                HistDict[obs][p].Scale(ZJetsSF)
						Temp[obs][p]=Temp[obs][p].Rebin(22,"",array('d',binsM3))
						HistDict[obs][p]=HistDict[obs][p].Rebin(22,"",array('d',binsM3))
						HistDict[obs][p].Scale(Temp[obs][p].Integral()/HistDict[obs][p].Integral())
					if s=="ZGamma" or s=="ZJets": print "only Z:",HistDict[obs][p].Integral(), s
						
						
					for sys in systematics:
						print sys
                                         	if sys=="MisIDEleshape":continue
                                         	if "AntiSIEIE" in observables[obs][0]:continue
						if sys=="Q2":continue
						else:
							Temp_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                        Temp_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                                        
                                                        HistDict_up[obs][p][sys] = _file_up[sys][s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))
							
						
							Temp_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                        Temp_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                                       
                                                        HistDict_do[obs][p][sys] = _file_do[sys][s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))

                                                        if s=="ZJets":
								print "s is ZJets"	
								Temp_up[obs][p][sys].Scale(ZJetsSF)
								HistDict_up[obs][p][sys].Scale(ZJetsSF)
                                                                Temp_do[obs][p][sys].Scale(ZJetsSF)
                                                                HistDict_do[obs][p][sys].Scale(ZJetsSF)
								Temp_up[obs][p][sys]=Temp_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
								HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
								HistDict_up[obs][p][sys].Scale(Temp_up[obs][p][sys].Integral()/HistDict_up[obs][p][sys].Integral())
								Temp_do[obs][p][sys]=Temp_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_do[obs][p][sys].Scale(Temp_do[obs][p][sys].Integral()/HistDict_do[obs][p][sys].Integral())
								if sys=="PU":
									print "doing PU"
									print HistDict_do[obs][p][sys].Integral(), HistDict_up[obs][p][sys].Integral(), sys


				if "_Prompt" in p:
					
                                        Temp[obs][p]   = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                        Temp[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                        HistDict[obs][p]   = _file[s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))
                                        if s=="ZJets":
                                                HistDict[obs][p].Scale(ZJetsSF)
                                                Temp[obs][p].Scale(ZJetsSF)
						Temp[obs][p]=Temp[obs][p].Rebin(22,"",array('d',binsM3))
                                                HistDict[obs][p]=HistDict[obs][p].Rebin(22,"",array('d',binsM3))
                                                HistDict[obs][p].Scale(Temp[obs][p].Integral()/HistDict[obs][p].Integral())
					
					for sys in systematics:
	                                        if (finalState=="mu") and ("VJets" in p):continue
        	                                if "AntiSIEIE" in observables[obs][0]:continue
                	                        if sys=="Q2":continue


						elif sys=="MisIDEleshape":
                                                	Temp_up[obs][p][sys]=_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                	Temp_up[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)

							
							Temp_do[obs][p][sys]=_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                        Temp_do[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF-misIDEle_unc)
								
							HistDict_up[obs][p][sys] = _file[s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))		
							HistDict_do[obs][p][sys] = _file[s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))   
							if s=="ZJets":
                                                                HistDict_up[obs][p][sys].Scale(ZJetsSF)
                                                                HistDict_do[obs][p][sys].Scale(ZJetsSF)
								Temp_up[obs][p][sys].Scale(ZJetsSF)
                                                                Temp_do[obs][p][sys].Scale(ZJetsSF)
								Temp_up[obs][p][sys]=Temp_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_up[obs][p][sys].Scale(Temp_up[obs][p][sys].Integral()/HistDict_up[obs][p][sys].Integral())
                                                                Temp_do[obs][p][sys]=Temp_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_do[obs][p][sys].Scale(Temp_do[obs][p][sys].Integral()/HistDict_do[obs][p][sys].Integral())
							

                                                else:
                                                        Temp_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                        Temp_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                        HistDict_up[obs][p][sys] = _file_up[sys][s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))


                                                        Temp_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                        Temp_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                        HistDict_do[obs][p][sys] = _file_do[sys][s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))
                                                        if s=="ZJets":
                                                                Temp_up[obs][p][sys].Scale(ZJetsSF)
                                                                HistDict_up[obs][p][sys].Scale(ZJetsSF)
                                                                Temp_do[obs][p][sys].Scale(ZJetsSF)
                                                                HistDict_do[obs][p][sys].Scale(ZJetsSF)
								Temp_up[obs][p][sys]=Temp_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_up[obs][p][sys].Scale(Temp_up[obs][p][sys].Integral()/HistDict_up[obs][p][sys].Integral())
                                                                Temp_do[obs][p][sys]=Temp_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                HistDict_do[obs][p][sys].Scale(Temp_do[obs][p][sys].Integral()/HistDict_do[obs][p][sys].Integral())


			        for s in process_signal[p][1:]:
					
					if "_Prompt" in p:
						if (finalState=="mu") and ("VJets" in p):continue
						if "VJets" in p:
							WJetstemp[obs][p] = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s))
							WJetstemp[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
							WJets[obs][p]=_file[s].Get("presel_M3_control_%s"%(s))
							WJetstemp[obs][p]=  WJetstemp[obs][p].Rebin(22,"",array('d',binsM3))
							WJets[obs][p] = WJets[obs][p].Rebin(22,"",array('d',binsM3))
							WJets[obs][p].Scale(WJetstemp[obs][p].Integral()/WJets[obs][p].Integral())
						else:
						
							Temp[obs][p].Add(_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
							Temp[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                	HistDict[obs][p].Add(_file[s].Get("presel_M3_control_%s"%(s)))
					
						for sys in systematics:
							if "AntiSIEIE" in observables[obs][0]:continue
							elif sys=="Q2":continue

							elif sys=="MisIDEleshape":
								if "VJets" in p:
									 WJetstemp_up[obs][p][sys] = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s))
									 WJetstemp_up[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)

		                                                         WJets_up[obs][p][sys]=_file[s].Get("presel_M3_control_%s"%(s))
									 WJetstemp_do[obs][p][sys] = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s))
                                                                         WJetstemp_do[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF-misIDEle_unc)

                                                                         WJets_do[obs][p][sys]=_file[s].Get("presel_M3_control_%s"%(s))
									 
									 WJetstemp_up[obs][p][sys]=  WJetstemp_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
									 WJets_up[obs][p][sys] = WJets_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
									 WJets_up[obs][p][sys].Scale(WJetstemp_up[obs][p][sys].Integral()/WJets_up[obs][p][sys].Integral())
									
                                                                         WJetstemp_do[obs][p][sys]=  WJetstemp_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                         WJets_do[obs][p][sys] = WJets_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                         WJets_do[obs][p][sys].Scale(WJetstemp_do[obs][p][sys].Integral()/WJets_do[obs][p][sys].Integral())
								else:
									Temp_up[obs][p][sys].Add(_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
									Temp_up[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)
									HistDict_up[obs][p][sys].Add(_file[s].Get("presel_M3_control_%s"%(s)))

									Temp_do[obs][p][sys].Add(_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
									Temp_do[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF-misIDEle_unc)
									HistDict_do[obs][p][sys].Add(_file[s].Get("presel_M3_control_%s"%(s)))



							else:
								if "VJets" in p:
									 if finalState=="mu":continue
                                                                         WJetstemp_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s))
                                                                         WJetstemp_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                                         WJets_up[obs][p][sys]= _file_up[sys][s].Get("presel_M3_control_%s"%(s))
                                                                         WJetstemp_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s))
                                                                         WJetstemp_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
									 #print sys, _file_up[sys][s], WJetstemp_up[obs][p][sys].Integral(), WJets_up[obs][p][sys].Integral()
                                                                         WJets_do[obs][p][sys]=_file_do[sys][s].Get("presel_M3_control_%s"%(s))
                                                                         WJetstemp_up[obs][p][sys]=  WJetstemp_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                         WJets_up[obs][p][sys] = WJets_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                         WJets_up[obs][p][sys].Scale(WJetstemp_up[obs][p][sys].Integral()/WJets_up[obs][p][sys].Integral())
                                                                         
                                                                         WJetstemp_do[obs][p][sys]=  WJetstemp_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                         WJets_do[obs][p][sys] = WJets_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                         WJets_do[obs][p][sys].Scale(WJetstemp_do[obs][p][sys].Integral()/WJets_do[obs][p][sys].Integral())
								else:
									Temp_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
									Temp_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
									HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("presel_M3_control_%s"%(s)))
									Temp_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
									Temp_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
									HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("presel_M3_control_%s"%(s)))



					if "_NonPrompt" in p:
						if "VJets" in p:
							
                                                        WJetstemp[obs][p] = _file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s))
                                                        WJetstemp[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                                        WJets[obs][p]=_file[s].Get("presel_M3_control_%s"%(s))
                                                        WJetstemp[obs][p]=  WJetstemp[obs][p].Rebin(22,"",array('d',binsM3))
                                                        WJets[obs][p] = WJets[obs][p].Rebin(22,"",array('d',binsM3))
                                                        WJets[obs][p].Scale(WJetstemp[obs][p].Integral()/WJets[obs][p].Integral())
						#3	print "should be same:",p, WJets[obs][p].Integral(), WJetstemp[obs][p].Integral()
                                                else:
					#		print s

							Temp[obs][p].Add(_file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
							Temp[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
							HistDict[obs][p].Add(_file[s].Get("presel_M3_control_%s"%(s)))
						

					#	if s=="WJets": print "now ZJets:",HistDict[obs][p].Integral(), p
						
						for sys in systematics:
							if "AntiSIEIE" in observables[obs][0]:continue
							if sys=="Q2":continue
							if sys=="MisIDEleshape":continue
							if "VJets" in p:
									
                                                                         WJetstemp_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s))
                                                                         WJetstemp_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                                                         WJets_up[obs][p][sys]=_file_up[sys][s].Get("presel_M3_control_%s"%(s))
                                                                         WJetstemp_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s))
                                                                         WJetstemp_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

                                                                         WJets_do[obs][p][sys]=_file_do[sys][s].Get("presel_M3_control_%s"%(s))

                                                                         WJetstemp_up[obs][p][sys]=  WJetstemp_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                         WJets_up[obs][p][sys] = WJets_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
									 print WJets_up[obs][p][sys].Integral(), WJetstemp_up[obs][p][sys].Integral()
                                                                         WJets_up[obs][p][sys].Scale(WJetstemp_up[obs][p][sys].Integral()/WJets_up[obs][p][sys].Integral())
									 print "should be same:",p, WJets_up[obs][p][sys].Integral(), WJetstemp_up[obs][p][sys].Integral()

                                                                         WJetstemp_do[obs][p][sys]=  WJetstemp_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                         WJets_do[obs][p][sys] = WJets_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                                                         WJets_do[obs][p][sys].Scale(WJetstemp_do[obs][p][sys].Integral()/WJets_do[obs][p][sys].Integral())                       
							else:
									Temp_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
									Temp_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

									HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("presel_M3_control_%s"%(s)))
									HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("presel_M3_control_%s"%(s)))
									Temp_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
									Temp_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
				
                        
				
			if obs=="M3":
				if "TTbar" in p or "TTGamma" in p:continue
				if (finalState=="mu") and ("VJets_Prompt" in p):continue
				if "VJets" in p:
				#	print "ZJets:", HistDict[obs][p].Integral(), "WJets:", WJets[obs][p].Integral()
                                        HistDict[obs][p].Add(WJets[obs][p])
					print p, HistDict[obs][p].Integral()
				else:
			
					HistDict[obs][p]=HistDict[obs][p].Rebin(22,"",array('d',binsM3))
					Temp[obs][p]=Temp[obs][p].Rebin(22,"",array('d',binsM3))
					#print p, Temp[obs][p].Integral(), HistDict[obs][p].Integral(), "nominal"      
					HistDict[obs][p].Scale(Temp[obs][p].Integral()/HistDict[obs][p].Integral())
				#	print p, "nominal",HistDict[obs][p].Integral()
					
				for sys in systematics:
					if sys=="isr" or sys=="fsr":continue	
					if "AntiSIEiIE" in observables[obs][0]:continue
					if sys=="Q2":continue
					if sys=="MisIDEleshape" and "_NonPrompt" in p:continue
					if "VJets" in p:
						#if finalState=="mu":continue	
						HistDict_up[obs][p][sys].Add(WJets_up[obs][p][sys])
						HistDict_do[obs][p][sys].Add(WJets_do[obs][p][sys])
						print p, sys, HistDict_up[obs][p][sys].Integral(),HistDict_do[obs][p][sys].Integral()
					else:
						HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
						HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
						Temp_up[obs][p][sys]=Temp_up[obs][p][sys].Rebin(22,"",array('d',binsM3))
						Temp_do[obs][p][sys]=Temp_do[obs][p][sys].Rebin(22,"",array('d',binsM3))
                                        	
						HistDict_up[obs][p][sys].Scale(Temp_up[obs][p][sys].Integral()/HistDict_up[obs][p][sys].Integral())
						HistDict_do[obs][p][sys].Scale(Temp_do[obs][p][sys].Integral()/HistDict_do[obs][p][sys].Integral())
						print p,obs, sys, HistDict_up[obs][p][sys].Integral(),HistDict_do[obs][p][sys].Integral()
                                                
		
		for sys in systematics2:

			if "AntiSIEIE" in observables[obs][0]:continue
			for p in sub_signal:
				if "NonPrompt" in p:
					#print p,sys,observables[obs][0]
					HistDict_up[obs][p][sys] = _file_up[sys][process_signal[p][0]].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_up[obs][p][sys].Add(_file_up[sys][process_signal[p][0]].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],process_signal[p][0])))

					HistDict_do[obs][p][sys] = _file_do[sys][process_signal[p][0]].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_do[obs][p][sys].Add(_file_do[sys][process_signal[p][0]].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],process_signal[p][0])))

				else:
					#print p, sys
					HistDict_up[obs][p][sys] = _file_up[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_up[obs][p][sys].Add(_file_up[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)

					HistDict_do[obs][p][sys] = _file_do[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_do[obs][p][sys].Add(_file_do[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)

		

	else:
		

		for p in process_signal:
			HistDict_up[obs][p]={}
                        HistDict_do[obs][p]={}
			
		 	s = process_signal[p][0]
			if "NonPrompt" in p:
				 HistDict[obs][p]   = _file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
				 HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
				 if s=="ZJets":
                                	HistDict[obs][p].Scale(ZJetsSF)
				 for sys in systematics:
					 if sys=="MisIDEleshape":continue
					 if "AntiSIEIE" in observables[obs][0]:continue
					 if sys=="Q2":
	                                        HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
						HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
        	                                total_up= HistDict_up[obs][p][sys].Integral()
                	                        HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
                        	                HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                	        total_do= HistDict_do[obs][p][sys].Integral()
                                        	HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
					 else: 
						print obs, sys, s
					 	HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					 	HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

					 	HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                         	HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                                if s=="ZJets":
                                                                HistDict_up[obs][p][sys].Scale(ZJetsSF)
                                                                HistDict_do[obs][p][sys].Scale(ZJetsSF)

		 	if "_Prompt" in p:
			 	HistDict[obs][p]   = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
			 	HistDict[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
				if s=="ZJets":
                                	HistDict[obs][p].Scale(ZJetsSF)
				for sys in systematics:
					if (finalState=="mu") and ("VJets" in p):continue	
					if "AntiSIEIE" in observables[obs][0]:continue
					if sys=="Q2":
                                                HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                total_up= HistDict_up[obs][p][sys].Integral()
						
                                                HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
                                                HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                total_do= HistDict_do[obs][p][sys].Integral()
                                                HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
					elif sys=="MisIDEleshape":
						HistDict_up[obs][p][sys]=_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
						HistDict_up[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)

						HistDict_do[obs][p][sys]=_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict_do[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF-misIDEle_unc)
						if s=="ZJets":
                                                                HistDict_up[obs][p][sys].Scale(ZJetsSF)
                                                                HistDict_do[obs][p][sys].Scale(ZJetsSF)

                                               
					else:
						HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
						HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)

						HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                        	HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
						if s=="ZJets":
                                                                HistDict_up[obs][p][sys].Scale(ZJetsSF)
                                                                HistDict_do[obs][p][sys].Scale(ZJetsSF)
									
				
			for s in process_signal[p][1:]:
				if "_Prompt" in p:
					if (finalState=="mu") and ("VJets" in p):continue	
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
					for sys in systematics:
						if "AntiSIEIE" in observables[obs][0]:continue
						elif sys=="Q2":continue

						elif sys=="MisIDEleshape":
							HistDict_up[obs][p][sys].Add(_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
							HistDict_up[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)

							HistDict_do[obs][p][sys].Add(_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
                                                        HistDict_do[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF-misIDEle_unc)
			
						else:
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)

							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
  
					
				if "_NonPrompt" in p:
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
                                        HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

					for sys in systematics:
						if "AntiSIEIE" in observables[obs][0]:continue
						if sys=="Q2":continue
						if sys=="MisIDEleshape":continue
                                                HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
						HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))


						HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
                                                HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
			

			


			if "ChIso" in observables[obs][0]:
				HistDict[obs][p]= HistDict[obs][p].Rebin(15,"",array('d',binsChHad))
				for sys in systematics:
					 if "AntiSIEIE" in observables[obs][0]:continue
					 if sys=="MisIDEleshape"and "NonPrompt" in p:continue
					 elif (finalState=="mu") and ("VJets_Prompt" in p):continue
                                         else:
						HistDict_up[obs][p][sys] = HistDict_up[obs][p][sys].Rebin(15,"",array('d',binsChHad))
						HistDict_do[obs][p][sys] = HistDict_do[obs][p][sys].Rebin(15,"",array('d',binsChHad))

		for sys in systematics2:

			if "AntiSIEIE" in observables[obs][0]:continue
			for p in sub_signal:
				if "NonPrompt" in p:
			#		print p,sys,observables[obs][0]
					HistDict_up[obs][p][sys] = _file_up[sys][process_signal[p][0]].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_up[obs][p][sys].Add(_file_up[sys][process_signal[p][0]].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],process_signal[p][0])))

					HistDict_do[obs][p][sys] = _file_do[sys][process_signal[p][0]].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_do[obs][p][sys].Add(_file_do[sys][process_signal[p][0]].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],process_signal[p][0])))
			
				else:
			#		print p, sys
					HistDict_up[obs][p][sys] = _file_up[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_up[obs][p][sys].Add(_file_up[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)

					HistDict_do[obs][p][sys] = _file_do[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_do[obs][p][sys].Add(_file_do[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)
			
	
					
for sys in systematics2:
	for p in sub_signal:
#		print p,sys
		HistDict_up["ChHad"][p][sys]= HistDict_up["ChHad"][p][sys].Rebin(15,"",array('d',binsChHad))
		HistDict_up["M3"][p][sys]=HistDict_up["M3"][p][sys].Rebin(22,"",array('d',binsM3))
		HistDict_do["ChHad"][p][sys]= HistDict_do["ChHad"][p][sys].Rebin(15,"",array('d',binsChHad))
                HistDict_do["M3"][p][sys]=HistDict_do["M3"][p][sys].Rebin(22,"",array('d',binsM3))



###make Data-Driven NonPrompt Templates######
if finalState=="ele":
	h1 = _file["DataEle"].Get("phosel_AntiSIEIE_ChIso_barrel_DataEle").Clone("ChHad_NonPrompt")
else:
	h1 = _file["DataMu"].Get("phosel_AntiSIEIE_ChIso_barrel_DataMu").Clone("ChHad_NonPrompt")
h1 = h1.Rebin(15,"",array('d',binsChHad))

total = h1.Integral()
NormFactor={}


print "VGamma NonPrompt", HistDict["M3"]["VGamma_NonPrompt"].Integral(), "VGamma Prompt", HistDict["M3"]["VGamma_Prompt"].Integral()

#exit()
for p in process_signal:
	NormFactor[p]={}
	if "_NonPrompt" in p:
		print p	
		p1=p.strip("NonPrompt")
		p1= p1.strip("_")
#		print p1
		print "%s_DD"%p1
		if finalState=="ele":
			HistDict["ChHad"]["%s_DD"%p1] = _file["DataEle"].Get("phosel_AntiSIEIE_ChIso_barrel_DataEle").Clone("ChHad_NonPrompt")
		else:
			HistDict["ChHad"]["%s_DD"%p1] = _file["DataMu"].Get("phosel_AntiSIEIE_ChIso_barrel_DataMu").Clone("ChHad_NonPrompt")
		HistDict["ChHad"]["%s_DD"%p1]=HistDict["ChHad"]["%s_DD"%p1].Rebin(15,"",array('d',binsChHad))
		NormFactor["%s_DD"%p1]=HistDict["ChHad"][p].Integral()
		print "Scaling to:",NormFactor["%s_DD"%p1]
		print "Original number:",HistDict["ChHad"]["%s_DD"%p1].Integral()
		HistDict["ChHad"]["%s_DD"%p1].Scale(NormFactor["%s_DD"%p1]/total)
		print "Final number:",HistDict["ChHad"]["%s_DD"%p1].Integral()




#print HistDict["ChHad"]["Other_DD"].Integral()
		
		
	
print "done with making Data Driven templates"

process_DDtemplates = {"TTGamma_Prompt":[kOrange,"TTGamma"],
           "TTGamma_DD":[kOrange,"TTGamma"],
           "TTbar_Prompt": [kRed+1,"TTbar"],
           "TTbar_DD": [kRed+1,"TTbar"],
           "VGamma_Prompt":[kBlue-9,"VGamma"],
           "VGamma_DD":[kBlue-9,"VGamma"],
           "VJets_Prompt":[kGreen-6,"VJets"],
           "VJets_DD":[kGreen-6,"VJets"],
           "Other_Prompt":[kBlue,"Other"],
           "Other_DD":[kBlue,"Other"],
        }
#process_= ["Other_Prompt","Other_DD","VGamma_Prompt","VGamma_DD","VJets_Prompt","VJets_DD","TTbar_Prompt","TTbar_DD","TTGamma_Prompt","TTGamma_DD"]










###We need MC NonPrompt templates in fit region for shape uncertainty on DataDriven templates

nbins = HistDict["ChHad"]["TTGamma_NonPrompt"].GetNbinsX()

if nbins != HistDict["AntiSIEIE"]["TTGamma_NonPrompt"].GetNbinsX():
	print "binsChHad not equal in two regions !! abort !!"
	exit()
diff=0.

unc_=[]
for p in process_control:


       if p=="TTbar":continue
       HistDict["AntiSIEIE"]["TTbar_NonPrompt"].Add(HistDict["AntiSIEIE"]["%s_NonPrompt"%p])
       HistDict["ChHad"]["TTbar_NonPrompt"].Add(HistDict["ChHad"]["%s_NonPrompt"%p])

HistDict["AntiSIEIE"]["TTbar_NonPrompt"].Scale(1/HistDict["AntiSIEIE"]["TTbar_NonPrompt"].Integral())
HistDict["ChHad"]["TTbar_NonPrompt"].Scale(1/HistDict["ChHad"]["TTbar_NonPrompt"].Integral())

for bin_ in range(nbins):

        diff=HistDict["ChHad"]["TTbar_NonPrompt"].GetBinContent(bin_+1)-HistDict["AntiSIEIE"]["TTbar_NonPrompt"].GetBinContent(bin_+1)
        unc_.append(diff/HistDict["AntiSIEIE"]["TTbar_NonPrompt"].GetBinContent(bin_+1))



for p in process_control:
	
	HistDict_up["ChHad"]["%s_DD"%p] ={}
	HistDict_do["ChHad"]["%s_DD"%p] ={}
	HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"] = TH1F("%s_shapeDD"%p,"%s_shapeDD"%p,15,0,20)
	HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"] = HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"].Rebin(15,"",array('d',binsChHad))
	
	HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"] = TH1F("%s_shapeDD"%p,"%s_shapeDD"%p,15,0,20)
	HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"] = HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"].Rebin(15,"",array('d',binsChHad))
	for bin_ in range(nbins):
	
		orig_=HistDict["ChHad"]["%s_DD"%p].GetBinContent(bin_+1)
		up = orig_+orig_*unc_[bin_]
		do = orig_-orig_*unc_[bin_]
		HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"].SetBinContent(bin_+1,up)
		HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"].SetBinContent(bin_+1,do)


##make DataDriven templates root file with actual data###

outputFile = TFile("Combine_withDDTemplateData_v2_%s%s.root"%(finalState,dir_),"recreate")




for obs in observables:
	print "doing data "
	print obs
	if obs=="AntiSIEIE":continue
        outputFile.mkdir("%s/%s"%(obs,"data_obs"))
        outputFile.cd("%s/%s"%(obs,"data_obs"))
	if finalState=="mu":
		if obs=="M3_control":
			HistDict[obs]["data"]=_file["DataMu"].Get("presel_%s_DataMu"%(observables[obs][0])).Clone("%s_DataMu"%(obs))
			HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(22,"",array('d',binsM3))
			print "just rebinned for M3_control"
			HistDict[obs]["data"].Write("nominal")
		else:
			HistDict[obs]["data"]=_file["DataMu"].Get("phosel_%s_barrel_DataMu"%(observables[obs][0])).Clone("%s_DataMu"%(obs))
			if obs=="M3":
				HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(22,"",array('d',binsM3))
			else:
				HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(15,"",array('d',binsChHad))
        		HistDict[obs]["data"].Write("nominal")
	else:
		if obs=="M3_control":
                        HistDict[obs]["data"]=_file["DataEle"].Get("presel_%s_DataEle"%(observables[obs][0])).Clone("%s_DataEle"%(obs))
			HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(22,"",array('d',binsM3))
                        HistDict[obs]["data"].Write("nominal")
		else:
			HistDict[obs]["data"]=_file["DataEle"].Get("phosel_%s_barrel_DataEle"%(observables[obs][0])).Clone("%s_DataEle"%(obs))
			if obs=="M3":
                                HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(22,"",array('d',binsM3))
                        else:
                                HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(15,"",array('d',binsChHad))

			HistDict[obs]["data"].Write("nominal")
        outputFile.mkdir(obs)
        if obs=="M3_control":
                 for p in process_control.keys():
                         outputFile.mkdir("%s/%s"%(obs,p))
                         outputFile.cd("%s/%s"%(obs,p))
                         HistDict[obs][p].Write("nominal")
                         for sys in systematics:
                                if sys=="MisIDEleshape":continue
                                HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                                HistDict_do[obs][p][sys].Write("%sDown"%(sys))


                 

                 for sys in systematics2:
			for p in sub_control:
				outputFile.cd("%s/%s"%(obs,p))
                        	HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                        	HistDict_do[obs][p][sys].Write("%sDown"%(sys))

        elif obs=="M3":
                for p in process_signal.keys():
                         outputFile.mkdir("%s/%s"%(obs,p))
                         outputFile.cd("%s/%s"%(obs,p))
                         HistDict[obs][p].Write("nominal")
                         for sys in systematics:
				if sys=="MisIDEleshape" and "NonPrompt" in p:continue
                                if finalState=="mu" and p=="VJets_Prompt":continue
                                if  sys=="Q2" and "TT" not in p:continue
                                HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                                HistDict_do[obs][p][sys].Write("%sDown"%(sys))
                
                for sys in systematics2:
			for p in sub_signal:
				outputFile.cd("%s/%s"%(obs,p))
                        	HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                        	HistDict_do[obs][p][sys].Write("%sDown"%(sys))

        else:

                for p in process_DDtemplates.keys():
			if "DD" in p:
				p1=p.strip("DD")
                		p1= p1.strip("_")
			
                        	outputFile.mkdir("%s/%s_NonPrompt"%(obs,p1))
                        	outputFile.cd("%s/%s_NonPrompt"%(obs,p1))
			else:
				outputFile.mkdir("%s/%s"%(obs,p))
                                outputFile.cd("%s/%s"%(obs,p))


                        HistDict[obs][p].Write("nominal")
                        if "_DD" in p:
                                HistDict_up["ChHad"][p]["shapeDD"].Write("shapeDDUp")
                                HistDict_do["ChHad"][p]["shapeDD"].Write("shapeDDDown")


                        for sys in systematics:
                                if "_DD" in p:continue
                                print sys, obs, p
                                if finalState=="mu" and p=="VJets_Prompt":continue
                                HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                                HistDict_do[obs][p][sys].Write("%sDown"%(sys))

                outputFile.cd("%s/TTGamma_Prompt"%(obs))
                for sys in systematics2:
                        HistDict_up[obs]["TTGamma_Prompt"][sys].Write("%sUp"%(sys))
                        HistDict_do[obs]["TTGamma_Prompt"][sys].Write("%sDown"%(sys))
		outputFile.cd("%s/TTbar_Prompt"%(obs))
		for sys in systematics2:
                        HistDict_up[obs]["TTbar_Prompt"][sys].Write("%sUp"%(sys))
                        HistDict_do[obs]["TTbar_Prompt"][sys].Write("%sDown"%(sys))


bins=TFile("binned.root","read")
outputFile.mkdir("binned_3CR/data_obs")
outputFile.cd("binned_3CR/data_obs")
hist_data= bins.Get("data")
hist_data.Write("nominal")
sample=["TTGamma","TTbar","WGamma","ZGamma","WJets","ZJets","SingleTop","TGJets","TTV","Diboson","QCD_DD"]
for s in sample:
	outputFile.mkdir("binned_3CR/%s"%s)
	outputFile.cd("binned_3CR/%s"%s)
	hist= bins.Get("binnedCR_%s"%s)
	hist.Write("nominal")
	outputFile.mkdir("binned_3CR/%s_Prompt"%s)
        outputFile.cd("binned_3CR/%s_Prompt"%s)
        hist= bins.Get("binned1CR_%s"%s)
        hist.Write("nominal")
	outputFile.mkdir("binned_3CR/%s_NonPrompt"%s)
        outputFile.cd("binned_3CR/%s_NonPrompt"%s)
        hist= bins.Get("binned2CR_%s"%s)
        hist.Write("nominal")
	


outputFile.Close()

