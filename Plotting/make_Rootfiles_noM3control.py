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
_file_CR ={}
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


if TightSelection:
	dir_="_tight"
else:
        dir_= ""



samples =["TTGamma","TTbar","TTV","TGJets","SingleTop","WJets","ZJets","WGamma","ZGamma","Diboson","QCD_DD"]
if finalState=="mu":
	samples.append("DataMu")
else:
	samples.append("DataEle")

for s in samples:
	_file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s/%s.root"%(finalState,dir_,s))
	_file_CR[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s0b/%s.root"%(finalState,dir_,s))

misIDEleSF = 2.27436#2.48745 
#misIDEleSF_0b = 1.65556 ## -0.0872607/+0.0848595
#misIDEleSF_0b_unc = 0.052
misIDEle_unc = 0.225#0.083
if finalState=="mu":
	ZJetsSF=1.17252#1.17514
	ZJetsSF_0b=0.982913 #0.992145

else:
	ZJetsSF=1.17005#1.13957
	ZJetsSF_0b=0.970013 #0.995392

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
_file_CR_up={}
_file_CR_do={}
if finalState=="mu":
	systematics = ["JER","JECTotal","phosmear","phoscale","BTagSF","Q2","Pdf","PU","MuEff","PhoEff"]
else:
	systematics = ["JER","JECTotal","phosmear","phoscale","BTagSF","Q2","Pdf","PU","EleEff","PhoEff","elesmear","elescale"]

systematics2 = ["isr","fsr"]


for sys in systematics2:
	_file_up[sys]={}
        _file_do[sys]={}
	_file_CR_up[sys]={}
        _file_CR_do[sys]={}

for sys in systematics:
      
       _file_up[sys]={}
       _file_do[sys]={}
       _file_CR_up[sys]={}
       _file_CR_do[sys]={}
 
       for s in samples:
		if s=="DataMu" or s=="DataEle":continue
		_file_up[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s/%s.root"%(finalState,sys,dir_,s))
		_file_do[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s/%s.root"%(finalState,sys,dir_,s))
		_file_CR_up[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s0b/%s.root"%(finalState,sys,dir_,s))
                _file_CR_do[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s0b/%s.root"%(finalState,sys,dir_,s))


for sys in systematics2:
	_file_up[sys]["TTGamma"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s/TTGamma.root"%(finalState,sys,dir_))
	_file_do[sys]["TTGamma"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s/TTGamma.root"%(finalState,sys,dir_))
	
	_file_up[sys]["TTbar"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s/TTbar.root"%(finalState,sys,dir_))
	_file_do[sys]["TTbar"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s/TTbar.root"%(finalState,sys,dir_))
	_file_CR_up[sys]["TTGamma"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s0b/TTGamma.root"%(finalState,sys,dir_))
        _file_CR_do[sys]["TTGamma"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s0b/TTGamma.root"%(finalState,sys,dir_))

        _file_CR_up[sys]["TTbar"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s0b/TTbar.root"%(finalState,sys,dir_))
        _file_CR_do[sys]["TTbar"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s0b/TTbar.root"%(finalState,sys,dir_))



binsM3=[]
#binsChHad = [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0]
#binsM3=[60., 80., 100, 110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240., 250.,260.,270.,280.,290.,300.,310.,320.,330.,340.,350.,360.,370.,380.,390. ,400., 420.,440.,460., 480., 500.]
#binsChHad = [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 11.0, 13.0, 14.0, 17.0, 20.0]
#binsM3=[60., 80., 100, 110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240., 250.,260.,270.,280.,290.,300.,310.,320.,330.,340.,350.,360.,370.,380.,390. ,400., 420.,440.,460., 480., 500.]

binsChHad = [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0]
binsM3=[60., 80., 100, 120., 140., 160., 180., 200., 220., 240., 260.,280.,300.,320.,340.,360.,380.,400.,420.,440.,460., 480., 500.]

print len(binsM3)
print len(binsChHad)
#exit()
systematics.append("MisIDEleshape")
observables={"M3": ["M3"],
	     "ChHad":["noCut_ChIso"],
             "AntiSIEIE":["AntiSIEIE_ChIso"],
	     "M3_control":["M3_control"],
	     "Njet":["Njet"]
           }

#print sorted(observables.keys())[:2]


process_signal = {"TTGamma_Prompt":["TTGamma"],
	   "TTGamma_NonPrompt":["TTGamma"],
           "TTbar_Prompt": ["TTbar"],
           "TTbar_NonPrompt": ["TTbar"],
	   "VGamma_Prompt":["ZGamma","WGamma"],
           "VGamma_NonPrompt":["ZGamma","WGamma"],
           "Other_Prompt":["ZJets","TTV", "SingleTop","TGJets","WJets","Diboson"],
           "Other_NonPrompt":["ZJets","TTV", "SingleTop","TGJets", "WJets","Diboson","QCD_DD"],
	}

process_signal_M3 = {"TTGamma_Prompt":["TTGamma"],
           "TTGamma_NonPrompt":["TTGamma"],
           "TTbar_Prompt": ["TTbar"],
           "TTbar_NonPrompt": ["TTbar"],
           "VGamma_Prompt":["ZGamma"],
           "VGamma_NonPrompt":["ZGamma"],
           "WGamma_Prompt":["WGamma"],
           "WGamma_NonPrompt":["WGamma"],
           "Other_Prompt":["ZJets"],
           "Other_NonPrompt":["ZJets"],
	   "TTV_Prompt":["TTV"],
           "TTV_NonPrompt":["TTV"], 
	   "WJets_Prompt":["WJets"],
	   "WJets_NonPrompt":["WJets"],
	   "Diboson_Prompt":["Diboson"],
	   "Diboson_NonPrompt":["Diboson"],
           "TGJets_Prompt":["TGJets"],
	   "TGJets_NonPrompt":["TGJets"],
	   "SingleTop_Prompt":["SingleTop"],
           "SingleTop_NonPrompt":["SingleTop"],
	   "QCD_NonPrompt":["QCD_DD"],
        }




sub_signal=["TTGamma_Prompt","TTGamma_NonPrompt","TTbar_Prompt","TTbar_NonPrompt"]
sub_control=["TTGamma","TTbar"]


process_control ={"TTGamma":["TTGamma"],
		  "TTbar":  ["TTbar"],
		  "VGamma":["ZGamma","WGamma"], 
		  "Other":[ "ZJets", "WJets","TTV","SingleTop","TGJets","Diboson","QCD_DD"],
		}	





##### Make Prompt and NonPrompt MC templates#######
process={}
for obs in observables:
	print "Now doing variable:",obs
	HistDict[obs]={}
	Temp[obs]={}
	Temp_up[obs]={}
	Temp_do[obs]={}
	HistDict_up[obs]={}
	HistDict_do[obs]={}
	if obs=="Njet":
		for p in process_signal:
			print "Obs,process:",obs, p
			s= process_signal[p][0]
			HistDict_up[obs][p]={}
                        HistDict_do[obs][p]={}
			if "_Prompt" in p:
				print "now doing prompt"
	#3		        print "phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)	
				HistDict[obs][p] = _file_CR[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
				HistDict[obs][p].Add(_file_CR[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
					
				if s=="ZJets":  
					#if p=="Other_Prompt" and finalState=="mu":
					#	HistDict[obs][p].Scale(-ZJetsSF_0b)
				#	else:
						HistDict[obs][p].Scale(ZJetsSF_0b)
			
	#			print p, "nominal", HistDict[obs][p].Integral()
				for sys in systematics:
					if sys=="BTagSF":continue
					#print p, sys
					if sys=="Q2":
						if p not in ["TTGamma_Prompt", "TTGamma_NonPrompt","TTbar_Prompt", "TTbar_NonPrompt"] :continue
						else:
							HistDict_up[obs][p][sys] = _file_CR_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
							HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF) 
						
						
							total_up= HistDict_up[obs][p][sys].Integral()
							HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)

							HistDict_do[obs][p][sys] = _file_CR_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
                                                	HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)     

                                                	total_do= HistDict_do[obs][p][sys].Integral()
                                                	HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
						#	print sys, "up", HistDict_up[obs][p][sys].Integral()
						#	print sys, "do", HistDict_do[obs][p][sys].Integral()

					elif sys=="Pdf" and s=="TTGamma":
						HistDict_up[obs][p][sys] = _file_CR_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
                                                HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)


                                                total_up= HistDict_up[obs][p][sys].Integral()
                                                HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)

                                                HistDict_do[obs][p][sys] = _file_CR_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
                                                HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)

                                                total_do= HistDict_do[obs][p][sys].Integral()
                                                HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
					#3	print sys, "up", HistDict_up[obs][p][sys].Integral()
                                          #      print sys, "do", HistDict_do[obs][p][sys].Integral()
					elif sys=="MisIDEleshape":
						HistDict_up[obs][p][sys] = _file_CR[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
                                                HistDict_up[obs][p][sys].Add(_file_CR[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)     

						HistDict_do[obs][p][sys] = _file_CR[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
                                                HistDict_do[obs][p][sys].Add(_file_CR[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF-misIDEle_unc)	
						
						if s=="ZJets":
							HistDict_do[obs][p][sys].Scale(ZJetsSF_0b)
							HistDict_up[obs][p][sys].Scale(ZJetsSF_0b)

					#	print sys, "up", HistDict_up[obs][p][sys].Integral()
                                         #       print sys, "do", HistDict_do[obs][p][sys].Integral()
						
					else:
						HistDict_up[obs][p][sys] = _file_CR_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
                                                HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)

                                                HistDict_do[obs][p][sys] = _file_CR_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
                                                HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)

                                                if s=="ZJets":
                                                        HistDict_do[obs][p][sys].Scale(ZJetsSF_0b)
                                                        HistDict_up[obs][p][sys].Scale(ZJetsSF_0b)
					#	print sys, "up", HistDict_up[obs][p][sys].Integral()
                                         #       print sys, "do", HistDict_do[obs][p][sys].Integral()
			if "_NonPrompt" in p:	
				print "now doing nonprompt"
				print _file_CR[s], "phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)
				HistDict[obs][p] = _file_CR[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                HistDict[obs][p].Add(_file_CR[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

                                if s=="ZJets":
                                        HistDict[obs][p].Scale(ZJetsSF_0b)
	#			print p,"nominal", HistDict[obs][p].Integral()
                                for sys in systematics:
					if sys=="BTagSF":continue
				#	print p, sys
                                        if sys=="Q2":
						if p not in ["TTGamma_Prompt", "TTGamma_NonPrompt","TTbar_Prompt", "TTbar_NonPrompt"] :continue
                                                else:
							HistDict_up[obs][p][sys] = _file_CR_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
							HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

		
							total_up= HistDict_up[obs][p][sys].Integral()
				#		print "sys up:", total_up
							HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
	
							HistDict_do[obs][p][sys] = _file_CR_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
							HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
	
							total_do= HistDict_do[obs][p][sys].Integral()
							HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
				#			print sys, "up", HistDict_up[obs][p][sys].Integral()
				#			print sys, "do", HistDict_do[obs][p][sys].Integral()
					
					elif sys=="Pdf" and s=="TTGamma":
						HistDict_up[obs][p][sys] = _file_CR_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
                                                HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))


                                                total_up= HistDict_up[obs][p][sys].Integral()
                                                HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)

                                                HistDict_do[obs][p][sys] = _file_CR_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
                                                HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

                                                total_do= HistDict_do[obs][p][sys].Integral()
                                                HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
				#		print sys, "up", HistDict_up[obs][p][sys].Integral()
                                 #               print sys, "do", HistDict_do[obs][p][sys].Integral()

                                        elif sys=="MisIDEleshape":continue
                                        else:
						HistDict_up[obs][p][sys] = _file_CR_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
                                                HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

                                                HistDict_do[obs][p][sys] = _file_CR_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
                                                HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

                                                if s=="ZJets":
                                                        HistDict_do[obs][p][sys].Scale(ZJetsSF_0b)
                                                        HistDict_up[obs][p][sys].Scale(ZJetsSF_0b)

				#		print sys, "up", HistDict_up[obs][p][sys].Integral()
                                 #               print sys, "do", HistDict_do[obs][p][sys].Integral()
		        for s in process_signal[p][1:]:
				if "_NonPrompt" in p:
					if s=="QCD_DD":
				#		print "now adding QCD"
				#		print _file_CR[s],"phosel_%s_barrel_%s"%(observables[obs][0],s)
						HistDict[obs][p].Add(_file_CR[s].Get("phosel_%s_barrel_%s"%(observables[obs][0],s)))
					else:
						HistDict[obs][p].Add(_file_CR[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
						HistDict[obs][p].Add(_file_CR[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
					for sys in systematics:
						
						
						if sys=="Q2" or sys=="Pdf" or sys=="MisIDEleshape" or sys=="BTagSF": continue

						elif s=="QCD_DD":
							 HistDict_up[obs][p][sys].Add(_file_CR[s].Get("phosel_%s_barrel_%s"%(observables[obs][0],s)))
							 HistDict_do[obs][p][sys].Add(_file_CR[s].Get("phosel_%s_barrel_%s"%(observables[obs][0],s)))
						
						else:
							HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
							HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
							
							HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
                                                        HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

				if "_Prompt" in p:
					HistDict[obs][p].Add(_file_CR[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
                                        HistDict[obs][p].Add(_file_CR[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
					for sys in systematics:
						
						if sys=="Q2" or sys=="Pdf" or sys=="BTagSF":continue
						elif sys=="MisIDEleshape":
							HistDict_up[obs][p][sys].Add(_file_CR[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
                                                        HistDict_up[obs][p][sys].Add(_file_CR[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)
							HistDict_do[obs][p][sys].Add(_file_CR[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
                                                        HistDict_do[obs][p][sys].Add(_file_CR[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF-misIDEle_unc)

						else:
							HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
                                                        HistDict_up[obs][p][sys].Add(_file_CR_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)

                                                        HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
                                                        HistDict_do[obs][p][sys].Add(_file_CR_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)	
	#		print "Rebinning",obs,p				
	#		print "number of bins:",HistDict[obs][p].GetNbinsX()	
         		HistDict[obs][p].Rebin(HistDict[obs][p].GetNbinsX())
	#		print obs,p, HistDict[obs][p].Integral()
			for sys in systematics:
				if "NonPrompt" in p and sys=="MisIDEleshape":continue
				if sys=="Q2" or sys=="Pdf":
					if p not in ["TTGamma_Prompt", "TTGamma_NonPrompt","TTbar_Prompt", "TTbar_NonPrompt"] :continue
				if sys=="BTagSF":continue
				#print "rebinning:",obs, p, sys
				HistDict_up[obs][p][sys].Rebin(HistDict_up[obs][p][sys].GetNbinsX())
				HistDict_do[obs][p][sys].Rebin(HistDict_do[obs][p][sys].GetNbinsX())
		
		for sys in systematics2:
                        for p in sub_signal:
				if "_NonPrompt" in p:
					HistDict_up[obs][p][sys] = _file_CR_up[sys][process_signal[p][0]].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_up[obs][p][sys].Add(_file_CR_up[sys][process_signal[p][0]].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],process_signal[p][0])))
		
					HistDict_do[obs][p][sys] = _file_CR_do[sys][process_signal[p][0]].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
                                        HistDict_do[obs][p][sys].Add(_file_CR_do[sys][process_signal[p][0]].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],process_signal[p][0])))

					HistDict_up[obs][p][sys].Rebin(HistDict_up[obs][p][sys].GetNbinsX())
					HistDict_do[obs][p][sys].Rebin(HistDict_do[obs][p][sys].GetNbinsX())
				if "_Prompt" in p:
					#print obs, p, sys, _file_CR_up[sys][process_signal[p][0]]
					HistDict_up[obs][p][sys] = _file_CR_up[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
                                        HistDict_up[obs][p][sys].Add(_file_CR_up[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)

                                        HistDict_do[obs][p][sys] = _file_CR_do[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
                                        HistDict_do[obs][p][sys].Add(_file_CR_do[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)

                                        HistDict_up[obs][p][sys].Rebin(HistDict_up[obs][p][sys].GetNbinsX())
                                        HistDict_do[obs][p][sys].Rebin(HistDict_do[obs][p][sys].GetNbinsX())
						
	
				
        elif obs=="M3_control":
		for p in process_control:
			s= process_control[p][0]
			HistDict_up[obs][p]={}
			HistDict_do[obs][p]={}
			HistDict[obs][p]   = _file[s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
			if s=="ZJets":
				HistDict[obs][p].Scale(ZJetsSF)	
			for sys in systematics:
				if sys=="MisIDEleshape":continue
				elif sys=="Q2":
					HistDict_up[obs][p][sys] = _file_up[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					total_up= HistDict_up[obs][p][sys].Integral()
					HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
					HistDict_do[obs][p][sys] = _file_do[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					total_do= HistDict_do[obs][p][sys].Integral()
					HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do) 

				elif sys=="Pdf" and s=="TTGamma":
			
                                        HistDict_up[obs][p][sys] = _file_up[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                        total_up= HistDict_up[obs][p][sys].Integral()
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
					if sys=="MisIDEleshape" or sys=="Q2":continue
					elif s=="QCD_DD":
						HistDict_up[obs][p][sys].Add(_file[s].Get("presel_%s_%s"%(observables[obs][0],s)))
						HistDict_do[obs][p][sys].Add(_file[s].Get("presel_%s_%s"%(observables[obs][0],s)))
	
					else:
						HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)))
						HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)))
		#	HistDict[obs][p]=HistDict[obs][p].Rebin(len(binsM3)-1,"",array('d',binsM3))

		
			for sys in systematics:
				if sys=="MisIDEleshape":continue
                 #               HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
                  #              HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
		for sys in systematics2:
			for p in sub_control:
				HistDict_up[obs][p][sys] = _file_up[sys][p].Get("presel_%s_%s"%(observables[obs][0],p)).Clone("%s_%s"%(obs,p))
		#		HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
                        	HistDict_do[obs][p][sys] = _file_do[sys][p].Get("presel_%s_%s"%(observables[obs][0],p)).Clone("%s_%s"%(obs,p))
		#		HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))	

        	
	elif obs=="M3":
		for p in process_signal_M3:
			HistDict_up[obs][p]={}
                        HistDict_do[obs][p]={}
                        Temp_up[obs][p]={}
                        Temp_do[obs][p]={}
			s = process_signal_M3[p][0]
			if "TTGamma" in s or "TTbar" in s:
				 if "NonPrompt" in p:
                                 	HistDict[obs][p]   = _file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
					for sys in systematics:
						if sys=="MisIDEleshape":continue
						elif "AntiSIEIE" in observables[obs][0]:continue
						elif sys=="Q2" :
							HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
							total_up= HistDict_up[obs][p][sys].Integral()
							HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
							HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
							total_do= HistDict_do[obs][p][sys].Integral()
							HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
						elif sys=="Pdf" and "TTGamma" in s:
							#print p, sys, obs
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
					if s=="QCD_DD":continue
					HistDict[obs][p]   = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
					for sys in systematics:
						if (finalState=="mu") and ("VJets" in p) and (dir_==""):continue
						elif "AntiSIEIE" in observables[obs][0]:continue
						elif sys=="Q2" or (sys=="Pdf" and s=="TTGamma_Prompt"):
							HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
							total_up= HistDict_up[obs][p][sys].Integral()
	
							HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
							HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
							total_do= HistDict_do[obs][p][sys].Integral()
							HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
						elif sys=="Pdf" and s=="TTGamma":
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
				
				 HistDict[obs][p]=HistDict[obs][p].Rebin(len(binsM3)-1,"",array('d',binsM3))
				 for sys in systematics:
					if "NonPrompt" in p and sys=="MisIDEleshape":continue
					HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
					HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))

	
			else:
				if "_NonPrompt" in p:
					if s=="QCD_DD":
						Temp[obs][p]      = _file[s].Get("phosel_%s_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict[obs][p]  = _file[s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))
					else:	
						Temp[obs][p]   = _file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                        	Temp[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                        
					
						HistDict[obs][p]   = _file[s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))
			
					if s=="ZJets":
                                        	Temp[obs][p].Scale(ZJetsSF)
                                                HistDict[obs][p].Scale(ZJetsSF)
						
					Temp[obs][p]=Temp[obs][p].Rebin(len(binsM3)-1,"",array('d',binsM3))
					HistDict[obs][p]=HistDict[obs][p].Rebin(len(binsM3)-1,"",array('d',binsM3))
					HistDict[obs][p].Scale(Temp[obs][p].Integral()/HistDict[obs][p].Integral())
					
					for sys in systematics:
						if s=="QCD_DD":
							HistDict_up[obs][p][sys]= HistDict[obs][p]
							HistDict_do[obs][p][sys]= HistDict[obs][p]
                                         	elif sys=="MisIDEleshape":continue
                                         	elif "AntiSIEIE" in observables[obs][0]:continue
						elif sys=="Q2":continue
						else:
							Temp_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                        Temp_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                                        
                                                        HistDict_up[obs][p][sys] = _file_up[sys][s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))
							
						
							Temp_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                        Temp_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                                       
                                                        HistDict_do[obs][p][sys] = _file_do[sys][s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))

                                                        if s=="ZJets":
								Temp_up[obs][p][sys].Scale(ZJetsSF)
								HistDict_up[obs][p][sys].Scale(ZJetsSF)
                                                                Temp_do[obs][p][sys].Scale(ZJetsSF)
                                                                HistDict_do[obs][p][sys].Scale(ZJetsSF)
							Temp_up[obs][p][sys]=Temp_up[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_up[obs][p][sys].Scale(Temp_up[obs][p][sys].Integral()/HistDict_up[obs][p][sys].Integral())
							Temp_do[obs][p][sys]=Temp_do[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_do[obs][p][sys].Scale(Temp_do[obs][p][sys].Integral()/HistDict_do[obs][p][sys].Integral())

				if "_Prompt" in p:
					
                                        Temp[obs][p]   = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                        Temp[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                        HistDict[obs][p]   = _file[s].Get("presel_M3_control_%s"%(s)).Clone("%s_%s"%(obs,p))
                                        if s=="ZJets":
                                                HistDict[obs][p].Scale(ZJetsSF)
                                                Temp[obs][p].Scale(ZJetsSF)
					Temp[obs][p]=Temp[obs][p].Rebin(len(binsM3)-1,"",array('d',binsM3))
					HistDict[obs][p]=HistDict[obs][p].Rebin(len(binsM3)-1,"",array('d',binsM3))
					HistDict[obs][p].Scale(Temp[obs][p].Integral()/HistDict[obs][p].Integral())
					
					for sys in systematics:
	                                        if (finalState=="mu") and ("VJets" in p) and (dir_==""):continue
        	                                elif "AntiSIEIE" in observables[obs][0]:continue
                	                        elif sys=="Q2":continue


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
							Temp_up[obs][p][sys]=Temp_up[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_up[obs][p][sys].Scale(Temp_up[obs][p][sys].Integral()/HistDict_up[obs][p][sys].Integral())
							Temp_do[obs][p][sys]=Temp_do[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
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
							Temp_up[obs][p][sys]=Temp_up[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_up[obs][p][sys].Scale(Temp_up[obs][p][sys].Integral()/HistDict_up[obs][p][sys].Integral())
							Temp_do[obs][p][sys]=Temp_do[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
							HistDict_do[obs][p][sys].Scale(Temp_do[obs][p][sys].Integral()/HistDict_do[obs][p][sys].Integral())

			    
					
				
                        
				
		
				
                                                
		
		for sys in systematics2:

			if "AntiSIEIE" in observables[obs][0]:continue
			for p in sub_signal:
				if "NonPrompt" in p:
					HistDict_up[obs][p][sys] = _file_up[sys][process_signal[p][0]].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_up[obs][p][sys].Add(_file_up[sys][process_signal[p][0]].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],process_signal[p][0])))

					HistDict_do[obs][p][sys] = _file_do[sys][process_signal[p][0]].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_do[obs][p][sys].Add(_file_do[sys][process_signal[p][0]].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],process_signal[p][0])))

				else:
					HistDict_up[obs][p][sys] = _file_up[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_up[obs][p][sys].Add(_file_up[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)

					HistDict_do[obs][p][sys] = _file_do[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_do[obs][p][sys].Add(_file_do[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)

		

	else:
		
		for p in process_signal:
			HistDict_up[obs][p]={}
                        HistDict_do[obs][p]={}
			
		 	s = process_signal[p][0]
			if "_NonPrompt" in p:
				 if s=="QCD_DD":
					HistDict[obs][p]   = _file[s].Get("phosel_%s_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
				 else:
				 	HistDict[obs][p]   = _file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
				 	HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
				 if s=="ZJets":
                                	HistDict[obs][p].Scale(ZJetsSF)
				 for sys in systematics:
					 if sys=="MisIDEleshape" or ("AntiSIEIE" in observables[obs][0]):continue
					 elif s=="QCD_DD":
						HistDict_up[obs][p][sys]=HistDict[obs][p]
						HistDict_do[obs][p][sys]=HistDict[obs][p]
					 elif sys=="Q2" :
	                                        HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
						HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
        	                                total_up= HistDict_up[obs][p][sys].Integral()
                	                        HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
                        	                HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                	        total_do= HistDict_do[obs][p][sys].Integral()
                                        	HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
					 elif sys=="Pdf" and s=="TTGamma":
						HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                                total_up= HistDict_up[obs][p][sys].Integral()
                                                HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
                                                HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
                                                total_do= HistDict_do[obs][p][sys].Integral()
                                                HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
					 else:
				#		print obs,p,sys, s, _file_up[sys][s] 
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
					#if (finalState=="mu") and (s=="WJets" or s=="ZJets") and (dir_=="" or dir_=="_tight"):continue	
					if "AntiSIEIE" in observables[obs][0]:continue
					elif sys=="Q2" or sys=="Pdf":
						if s=="TTGamma" or s=="TTbar":
						
						
							
                                                	HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                	HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                	total_up= HistDict_up[obs][p][sys].Integral()
						
                                                	HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
                                                	HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                	HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                	total_do= HistDict_do[obs][p][sys].Integral()
                                                	HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
						
					elif sys=="Pdf" and s=="TTGamma":
#						print p,sys,obs
                                                HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                total_up= HistDict_up[obs][p][sys].Integral()

                                                HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
                                                HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                                HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
                                                total_do= HistDict_do[obs][p][sys].Integral()
                                                HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
					elif sys=="MisIDEleshape":
                                                print sys, s
						HistDict_up[obs][p][sys]=_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
						HistDict_up[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)
						print _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)).Integral(), _file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)).Integral(), misIDEleSF+misIDEle_unc, misIDEleSF-misIDEle_unc
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
					if (finalState=="mu") and ("VJets" in p) and (dir_==""):continue	
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
					for sys in systematics:
						print sys
						if "AntiSIEIE" in observables[obs][0]:continue
						elif sys=="Q2" or sys=="Pdf":continue

						elif sys=="MisIDEleshape":
							print sys, s, 
							HistDict_up[obs][p][sys].Add(_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
							HistDict_up[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF+misIDEle_unc)

							HistDict_do[obs][p][sys].Add(_file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
                                                        HistDict_do[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF-misIDEle_unc)
							print HistDict_up[obs][p][sys].Integral(), HistDict_do[obs][p][sys].Integral()
						else:	
						#	print HistDict_up[obs][p][sys], s,sys,obs, _file_up[sys][s], "phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)

							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],s)))
							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],s)),misIDEleSF)
  
					
				if "_NonPrompt" in p:
					if s=="QCD_DD":
						HistDict[obs][p].Add(_file[s].Get("phosel_%s_barrel_%s"%(observables[obs][0],s)))
					#	print obs, s, _file[s].Get("phosel_%s_barrel_%s"%(observables[obs][0],s)).Integral()
					else:
						HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
                                        	HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))

					for sys in systematics:
						if "AntiSIEIE" in observables[obs][0] or sys=="Q2" or sys=="MisIDEleshape" or sys=="Pdf":continue
						elif s=="QCD_DD":
							HistDict_up[obs][p][sys].Add(_file[s].Get("phosel_%s_barrel_%s"%(observables[obs][0],s)))
							HistDict_do[obs][p][sys].Add(_file[s].Get("phosel_%s_barrel_%s"%(observables[obs][0],s)))
						else:

							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
							HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))


							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicPhoton_barrel_%s"%(observables[obs][0],s)))
							HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_barrel_%s"%(observables[obs][0],s)))
			

			


			if "ChIso" in observables[obs][0]:
				HistDict[obs][p]= HistDict[obs][p].Rebin(len(binsChHad)-1,"",array('d',binsChHad))
				for sys in systematics:
					 if "AntiSIEIE" in observables[obs][0]:continue
					 elif sys=="MisIDEleshape"and "NonPrompt" in p:continue
					 elif (finalState=="mu") and (("ZJets_Prompt" in p) or ("WJets_Prompt" in p))  and (dir_=="" or dir_=="_tight"):continue
					 elif sys=="Q2" and "TT" not in p:continue
					 elif sys=="Pdf" and "TT" not in p: continue 
                                         else:
				
				
						
						HistDict_up[obs][p][sys] = HistDict_up[obs][p][sys].Rebin(len(binsChHad)-1,"",array('d',binsChHad))
						HistDict_do[obs][p][sys] = HistDict_do[obs][p][sys].Rebin(len(binsChHad)-1,"",array('d',binsChHad))

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
					print p, sys
					HistDict_up[obs][p][sys] = _file_up[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_up[obs][p][sys].Add(_file_up[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)

					HistDict_do[obs][p][sys] = _file_do[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(observables[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
					HistDict_do[obs][p][sys].Add(_file_do[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(observables[obs][0],process_signal[p][0])),misIDEleSF)
			
	


print "VGamma Prompt",HistDict["ChHad"]["VGamma_Prompt"].Integral(), HistDict_up["ChHad"]["VGamma_Prompt"]["MisIDEleshape"].Integral(), HistDict_do["ChHad"]["VGamma_Prompt"]["MisIDEleshape"].Integral(),
#exit()
print "TTGamma NonPrompt",HistDict["Njet"]["TTGamma_NonPrompt"].Integral()
print "TTbar Prompt",HistDict["Njet"]["TTbar_Prompt"].Integral()
print "TTbar NonPrompt",HistDict["Njet"]["TTbar_NonPrompt"].Integral()
print "Other NonPrompt",HistDict["Njet"]["Other_NonPrompt"].Integral()
print "Other Prompt",HistDict["Njet"]["Other_Prompt"].Integral()
print "VGamma NonPrompt",HistDict["Njet"]["VGamma_NonPrompt"].Integral()
print "VGamma Prompt",HistDict["Njet"]["VGamma_Prompt"].Integral()

#exit()
print "adding the groups together"
for p in ["Other_Prompt","Other_NonPrompt","VGamma_Prompt","VGamma_NonPrompt"]:
	for s in process_signal[p][1:]:
		if "_Prompt" in p:
			if "VJets" in p and finalState=="mu":continue
#			print p,s, "%s_Prompt"%s
			HistDict["M3"][p].Add(HistDict["M3"]["%s_Prompt"%s])
			for sys in systematics:
				if sys=="Q2":continue
		#		print sys
				HistDict_up["M3"][p][sys].Add(HistDict_up["M3"]["%s_Prompt"%s][sys])
				HistDict_do["M3"][p][sys].Add(HistDict_do["M3"]["%s_Prompt"%s][sys])
		if "_NonPrompt" in p:
#			print p,s,"%s_NonPrompt"%s
			if s=="QCD_DD":
				HistDict["M3"][p].Add(HistDict["M3"]["QCD_NonPrompt"])
			else:
				HistDict["M3"][p].Add(HistDict["M3"]["%s_NonPrompt"%s])
		
			for sys in systematics:
				if sys=="MisIDEleshape" or sys=="Q2":continue
	#			print sys
				if s=="QCD_DD":
					HistDict_up["M3"][p][sys].Add(HistDict_up["M3"]["QCD_NonPrompt"][sys])
                                	HistDict_do["M3"][p][sys].Add(HistDict_do["M3"]["QCD_NonPrompt"][sys])
				else:
					HistDict_up["M3"][p][sys].Add(HistDict_up["M3"]["%s_NonPrompt"%s][sys])
                                	HistDict_do["M3"][p][sys].Add(HistDict_do["M3"]["%s_NonPrompt"%s][sys])
			



#exit()
for sys in systematics2:
	for p in sub_signal:
#		print p,sys
		HistDict_up["ChHad"][p][sys]= HistDict_up["ChHad"][p][sys].Rebin(len(binsChHad)-1,"",array('d',binsChHad))
		HistDict_up["M3"][p][sys]=HistDict_up["M3"][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))
		HistDict_do["ChHad"][p][sys]= HistDict_do["ChHad"][p][sys].Rebin(len(binsChHad)-1,"",array('d',binsChHad))
                HistDict_do["M3"][p][sys]=HistDict_do["M3"][p][sys].Rebin(len(binsM3)-1,"",array('d',binsM3))



###make Data-Driven NonPrompt Templates######
if finalState=="ele":
	h1 = _file["DataEle"].Get("phosel_AntiSIEIE_ChIso_barrel_DataEle").Clone("ChHad_NonPrompt")
else:
	h1 = _file["DataMu"].Get("phosel_AntiSIEIE_ChIso_barrel_DataMu").Clone("ChHad_NonPrompt")
h1 = h1.Rebin(len(binsChHad)-1,"",array('d',binsChHad))

total = h1.Integral()
NormFactor={}


#print "VGamma NonPrompt", HistDict["M3"]["VGamma_NonPrompt"].Integral(), "VGamma Prompt", HistDict["M3"]["VGamma_Prompt"].Integral()

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
		HistDict["ChHad"]["%s_DD"%p1]=HistDict["ChHad"]["%s_DD"%p1].Rebin(len(binsChHad)-1,"",array('d',binsChHad))
		NormFactor["%s_DD"%p1]=HistDict["ChHad"][p].Integral()
		print "Scaling to:",NormFactor["%s_DD"%p1]
		print "Original number:",HistDict["ChHad"]["%s_DD"%p1].Integral()
		HistDict["ChHad"]["%s_DD"%p1].Scale(NormFactor["%s_DD"%p1]/total)
		print "Final number:",HistDict["ChHad"]["%s_DD"%p1].Integral()




		
		
	
print "done with making Data Driven templates"

process_DDtemplates = {"TTGamma_Prompt":[kOrange,"TTGamma"],
           "TTGamma_DD":[kOrange,"TTGamma"],
           "TTbar_Prompt": [kRed+1,"TTbar"],
           "TTbar_DD": [kRed+1,"TTbar"],
           "VGamma_Prompt":[kBlue-9,"VGamma"],
           "VGamma_DD":[kBlue-9,"VGamma"],
           "Other_Prompt":[kBlue,"Other"],
           "Other_DD":[kBlue,"Other"],
        }










###We need MC NonPrompt templates in fit region for shape uncertainty on DataDriven templates

nbins = HistDict["ChHad"]["TTGamma_NonPrompt"].GetNbinsX()
print nbins
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
	print p
	HistDict_up["ChHad"]["%s_DD"%p] ={}
	HistDict_do["ChHad"]["%s_DD"%p] ={}
	HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"] = TH1F("%s_shapeDD"%p,"%s_shapeDD"%p,14,0,20)
	HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"] = HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"].Rebin(len(binsChHad)-1,"",array('d',binsChHad))
	
	HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"] = TH1F("%s_shapeDD"%p,"%s_shapeDD"%p,14,0,20)
	HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"] = HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"].Rebin(len(binsChHad)-1,"",array('d',binsChHad))
	for bin_ in range(nbins):
	
		orig_=HistDict["ChHad"]["%s_DD"%p].GetBinContent(bin_+1)
		up = orig_+orig_*unc_[bin_]
		do = orig_-orig_*unc_[bin_]
		HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"].SetBinContent(bin_+1,up)
		HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"].SetBinContent(bin_+1,do)

	##all three templates:up/down/nominal should have the same number of events, only difference in shape######
	HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"].Scale(float(HistDict["ChHad"]["%s_DD"%p].Integral()/HistDict_up["ChHad"]["%s_DD"%p]["shapeDD"].Integral()))
	HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"].Scale(float(HistDict["ChHad"]["%s_DD"%p].Integral()/HistDict_do["ChHad"]["%s_DD"%p]["shapeDD"].Integral()))


#print HistDict_up["ChHad"]["TTbar_DD"]["shapeDD"].Integral()
#print HistDict["ChHad"]["TTbar_DD"].Integral()
#print HistDict_do["ChHad"]["TTbar_DD"]["shapeDD"].Integral()



outputFile = TFile("Combine_withDDTemplateData_v6_%s%s_binned_PDF.root"%(finalState,dir_),"recreate")




for obs in observables:
	if obs=="AntiSIEIE":continue
	if obs=="Njet":
		outputFile.mkdir("%s/%s"%("btag","data_obs"))
        	outputFile.cd("%s/%s"%("btag","data_obs"))
	else:
        	outputFile.mkdir("%s/%s"%(obs,"data_obs"))
        	outputFile.cd("%s/%s"%(obs,"data_obs"))
	if finalState=="mu":
		if obs=="M3_control":
			HistDict[obs]["data"]=_file["DataMu"].Get("presel_%s_DataMu"%(observables[obs][0])).Clone("%s_DataMu"%(obs))
			HistDict[obs]["data"].Rebin(HistDict[obs]["data"].GetNbinsX())
			
			HistDict[obs]["data"].Write("nominal")
		elif obs=="Njet":
                        HistDict[obs]["data"]=_file_CR["DataMu"].Get("phosel_%s_barrel_DataMu"%(observables[obs][0])).Clone("%s_DataMu"%(obs))
                        HistDict[obs]["data"].Rebin(HistDict[obs]["data"].GetNbinsX())
			HistDict[obs]["data"].Write("nominal")
		else:
		
			HistDict[obs]["data"]=_file["DataMu"].Get("phosel_%s_barrel_DataMu"%(observables[obs][0])).Clone("%s_DataMu"%(obs))
			if obs=="M3":
				HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(len(binsM3)-1,"",array('d',binsM3))
			elif obs=="ChHad":
				HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(len(binsChHad)-1,"",array('d',binsChHad))
        		HistDict[obs]["data"].Write("nominal")
	else:
		if obs=="M3_control":
                        HistDict[obs]["data"]=_file["DataEle"].Get("presel_%s_DataEle"%(observables[obs][0])).Clone("%s_DataEle"%(obs))
			HistDict[obs]["data"].Rebin(HistDict[obs]["data"].GetNbinsX())
                        HistDict[obs]["data"].Write("nominal")
		elif obs=="Njet":
			HistDict[obs]["data"]=_file_CR["DataEle"].Get("phosel_%s_barrel_DataEle"%(observables[obs][0])).Clone("%s_DataEle"%(obs))
			HistDict[obs]["data"].Rebin(HistDict[obs]["data"].GetNbinsX())
			HistDict[obs]["data"].Write("nominal")
		else:
			HistDict[obs]["data"]=_file["DataEle"].Get("phosel_%s_barrel_DataEle"%(observables[obs][0])).Clone("%s_DataEle"%(obs))
			if obs=="M3":
                                HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(len(binsM3)-1,"",array('d',binsM3))
                        elif obs=="ChHad":
                                HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(len(binsChHad)-1,"",array('d',binsChHad))


			HistDict[obs]["data"].Write("nominal")
	if obs=="Njet":
		outputFile.mkdir("btag")
	else:
        	outputFile.mkdir(obs)
	
        if obs=="M3_control":
                 for p in process_control.keys():
                         outputFile.mkdir("%s/%s"%(obs,p))
                         outputFile.cd("%s/%s"%(obs,p))
			 HistDict[obs][p].Rebin(HistDict[obs][p].GetNbinsX())
                         HistDict[obs][p].Write("nominal")
                         for sys in systematics:
                                if sys=="MisIDEleshape":continue
				HistDict_up[obs][p][sys].Rebin(HistDict_up[obs][p][sys].GetNbinsX())
                                HistDict_do[obs][p][sys].Rebin(HistDict_do[obs][p][sys].GetNbinsX())
				if sys=="Pdf" and p=="TTGamma":
				
					HistDict_up[obs][p][sys].Write("%ssignalUp"%(sys))
					HistDict_do[obs][p][sys].Write("%ssignalDown"%(sys))
				else:
					HistDict_up[obs][p][sys].Write("%sUp"%(sys))
					HistDict_do[obs][p][sys].Write("%sDown"%(sys))


                 

                 for sys in systematics2:
			for p in sub_control:
				HistDict_up[obs][p][sys].Rebin(HistDict_up[obs][p][sys].GetNbinsX())
                                HistDict_do[obs][p][sys].Rebin(HistDict_do[obs][p][sys].GetNbinsX())
				outputFile.cd("%s/%s"%(obs,p))
                        	HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                        	HistDict_do[obs][p][sys].Write("%sDown"%(sys))

        elif obs=="M3" or obs=="Njet":
		if obs=="Njet":
			for p in process_signal.keys():
                         	outputFile.mkdir("%s/%s"%("btag",p))
                         	outputFile.cd("%s/%s"%("btag",p))
				HistDict[obs][p].Write("nominal")
				for sys in systematics:
	                                print sys,obs
                                        if sys=="MisIDEleshape" and "NonPrompt" in p:continue
                                        elif sys=="BTagSF" and obs=="Njet":continue
                                        elif  sys=="Q2" and "TT" not in p:continue
                                        elif sys=="Pdf" and "TTGamma" in p:
                                                HistDict_up[obs][p][sys].Write("%ssignalUp"%(sys))
                                                HistDict_do[obs][p][sys].Write("%ssignalDown"%(sys))
                                        else:
                                                HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                                                HistDict_do[obs][p][sys].Write("%sDown"%(sys))

		else:
                	for p in process_signal.keys():
                        	outputFile.mkdir("%s/%s"%(obs,p))
                         	outputFile.cd("%s/%s"%(obs,p))
                         	HistDict[obs][p].Write("nominal")
                
				for sys in systematics:
					#print sys,obs
					if sys=="MisIDEleshape" and "NonPrompt" in p:continue
					elif sys=="BTagSF" and obs=="Njet":continue
                                	elif  sys=="Q2" and "TT" not in p:continue
                                	elif sys=="Pdf" and "TTGamma" in p:
                                        	HistDict_up[obs][p][sys].Write("%ssignalUp"%(sys))
                                        	HistDict_do[obs][p][sys].Write("%ssignalDown"%(sys))
					else:
						HistDict_up[obs][p][sys].Write("%sUp"%(sys))
						HistDict_do[obs][p][sys].Write("%sDown"%(sys))
                
                for sys in systematics2:
			for p in sub_signal:
				if obs=="Njet":
					outputFile.cd("%s/%s"%("btag",p))
				else:
					outputFile.cd("%s/%s"%(obs,p))
                        	HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                        	HistDict_do[obs][p][sys].Write("%sDown"%(sys))

        else:

                for p in process_DDtemplates.keys():
			#print p,obs, "doing ChargeHad"
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
                               
                                elif (sys=="MisIDEleshape" and "_NonPrompt" in p):continue
                                elif sys=="Q2" and "TT" not in p:continue
				elif sys=="Pdf" and "TT" not in p:continue
				elif sys=="Pdf" and "TTGamma" in p:
                                        HistDict_up[obs][p][sys].Write("%ssignalUp"%(sys))
                                        HistDict_do[obs][p][sys].Write("%ssignalDown"%(sys))
				else:
					HistDict_up[obs][p][sys].Write("%sUp"%(sys))
					HistDict_do[obs][p][sys].Write("%sDown"%(sys))

                if obs=="Njet":
			outputFile.cd("btag/TTGamma_Prompt")
		else:
			outputFile.cd("%s/TTGamma_Prompt"%(obs))
                for sys in systematics2:
                        HistDict_up[obs]["TTGamma_Prompt"][sys].Write("%sUp"%(sys))
                        HistDict_do[obs]["TTGamma_Prompt"][sys].Write("%sDown"%(sys))
		if obs=="Njet":
			outputFile.cd("btag/TTbar_Prompt")
		outputFile.cd("%s/TTbar_Prompt"%(obs))
		for sys in systematics2:
                        HistDict_up[obs]["TTbar_Prompt"][sys].Write("%sUp"%(sys))
                        HistDict_do[obs]["TTbar_Prompt"][sys].Write("%sDown"%(sys))



outputFile.Close()
