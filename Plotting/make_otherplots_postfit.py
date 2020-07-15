## Make root files for combine with different MC signals and their systematics###
##uncertainties in both electron and muon channel####

#from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F
from ROOT import *
import math
import os
import sys
from array import array
import CMS_lumi

from Style import *
thestyle = Style()
#gStyle.SetOptStat(0)
HasCMSStyle = False
style = None
if not HasCMSStyle:
    print "Using default style defined in cuy package."
    thestyle.SetStyle()

ROOT.gROOT.ForceStyle()


#thestyle = Style()
random=TRandom3(0)

_file = {}
_file_CR ={}
from optparse import OptionParser

from sampleInformation import *

gROOT.SetBatch(True)

YesLog = True
NoLog=False

parser = OptionParser()

parser.add_option("-c", "--channel", dest="channel", default="mu",type='str',
                  help="Specify which channel mu or ele? default is mu" )
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                     help="Use 4j1t selection" )
parser.add_option("--Tight0b","--tight0b", dest="isTight0bSelection", default=False,action="store_true",
                     help="Use 4j0t selection" )
parser.add_option("--LooseCRe2g1","--looseCRe2g1", dest="isLooseCRe2g1Selection",default=False,action="store_true",
                  help="Use 2j at least 1t control region selection")
parser.add_option("--LooseCRe3g0","--looseCR3e0", dest="isLooseCRe3g0Selection",default=False,action="store_true",
                  help="Use =3j, =0 control region selection" )
parser.add_option("--LooseCRe3g1","--looseCR3e1", dest="isLooseCRe3g1Selection",default=False,action="store_true",
                  help="Use =3j, >=1 control region selection" )
parser.add_option("--onlyEGamma","--onlyEGamma", dest="onlyEGamma",default=False,action="store_true",
                  help="only makeEGamma plot" )
(options, args) = parser.parse_args()


finalState = options.channel
TightSelection = options.isTightSelection
isTight0bSelection = options.isTight0bSelection
isLooseCRe2g1Selection = options.isLooseCRe2g1Selection
isLooseCRe3g0Selection = options.isLooseCRe3g0Selection
isLooseCRe3g1Selection = options.isLooseCRe3g1Selection
onlyEGamma=options.onlyEGamma

dir_=""
regionText = ", N_{j}#geq3, N_{b}#geq1"
if TightSelection:
	dir_="_tight"
	regionText = ", N_{j}#geq4, N_{b}#geq1"
elif isLooseCRe3g0Selection:
        dir_= "_looseCRe3g0"
	regionText = ", N_{j}=3, N_{b}=0"

elif isLooseCRe3g1Selection:
	dir_= "_looseCRe3g1"
        regionText = ", N_{j}=3, N_{b}#geq1"

elif isLooseCRe2g1Selection:
	dir_= "_looseCRe2g1"
        regionText = ", N_{j}=2, N_{b}#geq1"

elif isTight0bSelection:
	dir_="_tight0b"
        regionText = ", N_{j}#geq4, N_{b}=0"

samples =["TTGamma","TTbar","TTV","TGJets","SingleTop","WJets","ZJets","WGamma","ZGamma","Diboson","QCD_DD"]
if finalState=="mu":
	samples.append("DataMu")
	_channelText = "#mu+jets"	
else:
	samples.append("DataEle")
	_channelText = "e+jets"


for s in samples:
	_file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s/%s.root"%(finalState,dir_,s))

misIDEleSF = 2.27#1.4713 
#bkgSF_misIDEle =1.079
misIDEle_unc = 0.225

ZJetsSF=1.17
if finalState=="mu":
	if TightSelection:
		ZJetsSF=1.17252
		#bkgSF_ZJets=0.982913 
               


else:
	if TightSelection:
		ZJetsSF=1.17005 
#		bkgSF_ZJets=0.9023*1.009
	elif isLooseCRe3g1Selection:
		ZJetsSF=1.23473  
	elif isLooseCRe3g0Selection:
		ZJetsSF= 1.11696 
	elif isTight0bSelection:
		ZJetsSF=0.970013
	elif isLooseCRe2g1Selection:
		ZJetsSF=1.261

#print ZJetsSF, bkgSF_ZJets, bkgSF_misIDEle, misIDEleSF
#exit()
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

for sys in systematics:
      
       _file_up[sys]={}
       _file_do[sys]={}
 
       for s in samples:
		if isLooseCRe3g1Selection:continue
		if s=="DataMu" or s=="DataEle":continue
		_file_up[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s/%s.root"%(finalState,sys,dir_,s))
		_file_do[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s/%s.root"%(finalState,sys,dir_,s))


for sys in systematics2:
	if isLooseCRe3g1Selection:continue
	_file_up[sys]["TTGamma"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s/TTGamma.root"%(finalState,sys,dir_))
	_file_do[sys]["TTGamma"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s/TTGamma.root"%(finalState,sys,dir_))
	
	_file_up[sys]["TTbar"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_up%s/TTbar.root"%(finalState,sys,dir_))
	_file_do[sys]["TTbar"]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s_down%s/TTbar.root"%(finalState,sys,dir_))





NoLog=False
YesLog=True
systematics.append("MisIDEleshape")
histograms={"PhotonEt": ["LeadingPhotonEt", "Photon E_{T} (GeV)", "Events/5 GeV", [20.,25.,30.,35.,40.,45.,50.,55.,60.,65.,70.,75.,80.,85.,90.,95., 100.,105.,110.,115.,120.,125.,130.,135.,140.,145.,150,], [20,150],regionText,NoLog,"","PhotonEt"],
	   # "PhotonEt": ["LeadingPhotonEt", "Photon Et (GeV)", "Events", [20.,35.,50.,65.,80.,95.,110.,140.,180.,300.], [-1,-1],regionText,NoLog,"","M3"],
#	     "MassEGamma":["MassEGamma", "m_{e,#gamma} GeV" , "Events/GeV", [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175], [25.,175.], regionText,NoLog,"","MassEGamma"],
            "Jet1Pt":["jet1Pt","Leading Jet Pt (GeV)", "Events", 5, [30,400], regionText, YesLog, " "],
	    "HT" : ["HT","H_{T} (GeV)","Events", 5, [180,1000], regionText,  NoLog, " "],
	  #  "PhotonEta":["LeadingPhotonSCEta","Photon #eta (GeV)", "Events",[0.,0.25,0.5,0.75,1.0,1.25,1.5],[0,-1],regionText,NoLog,"",""],
	    "PhotonEta":["LeadingPhotonSCEta","Photon #eta ", "Events/0.1",[-1.47,-1.37,-1.27,-1.17,-1.07,-0.97,-0.87,-0.77,-0.67,-0.57,-0.47,-0.37,-0.27,-0.17,-0.07,0.03,0.13,0.23,0.33,0.43,0.53,0.63,0.73,0.83,0.93,1.03,1.13,1.23,1.33,1.43,1.53], [-1.47,1.53],regionText,NoLog,"","PhotonEta"],
	    #"dRPhotonJet":["dRLeadingPhotonJet","dR(#gamma,jet)", "Events",[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5],[-1,-1],regionText,NoLog,"",""],
	    #"dRPhotonLepton":["dRLeadingPhotonLepton","dR(#gamma,lepton)", "Events",[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0,4.1,4.2,4.3,4.4,4.5],[-1,-1],regionText,NoLog,"",""],    
             #"ElectronPt": ["elePt","Electron p_{T} (GeV)" , "Events", 15,[35.,200.], regionText,  NoLog, " ","Njet"],
#	     "MuonPt": ["muPt","Muon p_{T} (GeV) ", "Events", 17, [30,200], regionText,  NoLog, " ",],
  	    # "ElectronEta":["eleSCEta","Electron SC#eta", "Events", 4, [-2.1,2.1], regionText,  NoLog, " "],
	     "M3":["M3","M3 (GeV)", "Events/20 GeV",[60., 80., 100, 120., 140., 160., 180., 200., 220., 240., 260.,280.,300.,320.,340.,360.,380.,400.,420.,440.,460., 480., 500.], [-1,-1],regionText,  NoLog, " "],
	     # "MuonEta":["muEta" ,"Muon #eta", "Events", 5, [-2.4,2.4], regionText,  NoLog, " "],
	     "Nphotons":["Nphotons","Number of Photons" , "Events", 1, [1,3], regionText,  YesLog, " "],
	     "Njets":["Njet","N Jets" , "Events", 1, [4,10], regionText,  NoLog, " "],
	     "PhoIso":["PhoIso","Photon Iso (GeV)", "Events", 1, [0,2.9], regionText, YesLog, " "],
	     "NeuIso":["NeuIso","Neutral Hadron Iso (GeV)" , "Events", 1, [0,3.2], regionText, YesLog, " "],
	     "ChIso":["ChIso","Charged Hadron Iso (GeV)" , "Events", 1, [0,0.441], regionText, YesLog, " "],
	     "Njet" :["Njet","N Jets", "Events", [4,5,6,7,8,9,10], [4,10],regionText,NoLog,"","Njet"],  
	     "Nbjet" :["Nbjet","Number of b Jets", "Events", [1,2,3,4], [1,4],regionText,NoLog,"","Nbjet"],  
	}
if onlyEGamma:
	histograms={ "MassEGamma":["MassEGamma", "m_{e,#gamma} GeV" , "Events/GeV", [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175], [25,175], regionText,NoLog,""],
			}



process_signal = {"TTGamma_Prompt":["TTGamma"],
           "TTGamma_NonPrompt":["TTGamma"],
           "TTbar_Prompt": ["TTbar"],
           "TTbar_NonPrompt": ["TTbar"],
           "ZGamma_Prompt":["ZGamma"],
           "ZGamma_NonPrompt":["ZGamma"],
           "WGamma_Prompt":["WGamma"],
           "WGamma_NonPrompt":["WGamma"],
           "ZJets_Prompt":["ZJets"],
           "ZJets_NonPrompt":["ZJets"],
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



for obs in histograms:
	HistDict_up[obs]={}
        HistDict_do[obs]={}
	

	for p in process_signal:
		HistDict_up[obs][p]={}
                HistDict_do[obs][p]={}
	for p in ["VGamma_Prompt","VGamma_NonPrompt","Other_Prompt","Other_NonPrompt"]:
		HistDict_up[obs][p]={}
                HistDict_do[obs][p]={}


	


##### Make Prompt and NonPrompt MC templates#######
process={}
for obs in histograms:
	if finalState=="ele" and "Mu" in obs:continue
        if finalState=="mu" and "Ele" in obs:continue
	#print "Now doing variable:",obs
	HistDict[obs]={}
	Temp[obs]={}
	Temp_up[obs]={}
	Temp_do[obs]={}
	
	for p in process_signal:
	#	print "Obs,process:",obs, p
		s= process_signal[p][0]
		if "_Prompt" in p:
			if s=="QCD_DD":continue
	#		print "now doing prompt"
			if  onlyEGamma:
				HistDict[obs][p]=(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)))
				HistDict[obs][p].Scale(misIDEleSF)
			else:
				print s, _file[s], "phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)
				HistDict[obs][p] = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s"%(obs,p))
				#HistDict[obs][p].Scale(bkgSF_misIDEle)
				HistDict[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)),misIDEleSF)
					
			if s=="ZJets":  
				HistDict[obs][p].Scale(ZJetsSF)
			#else:
			#	HistDict[obs][p].Scale(bkgSF_ZJets)
		
			for sys in systematics:
				if not TightSelection:continue
				if finalState=="mu" and "MassEGamma" in obs:continue
				if onlyEGamma:continue
	#			print "doing systematics", s, sys
				if sys=="Q2":
					if p not in ["TTGamma_Prompt", "TTGamma_NonPrompt","TTbar_Prompt", "TTbar_NonPrompt"] :continue
					#if p=="TTbar_Prompt" and finalState=="mu" and obs=="MassEGamma":continue
					else:
						#print p,sys,s,_file_up[sys][s],"phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s),bkgSF_misIDEle
						HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
					#	HistDict_up[obs][p][sys].Scale(bkgSF_misIDEle)
						HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)),misIDEleSF) 
						
					#	HistDict_up[obs][p][sys].Scale(bkgSF_ZJets)
						total_up= HistDict_up[obs][p][sys].Integral()
						HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)

						HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
					#	HistDict_do[obs][p][sys].Scale(bkgSF_misIDEle)
						HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)),misIDEleSF)     
						
	#					HistDict_do[obs][p][sys].Scale(bkgSF_ZJets)
						total_do= HistDict_do[obs][p][sys].Integral()
						HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)

				elif sys=="Pdf" and s=="TTGamma":
					HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
			#		HistDict_up[obs][p][sys].Scale(bkgSF_misIDEle)
					HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)),misIDEleSF)

	#				HistDict_up[obs][p][sys].Scale(bkgSF_ZJets)
					total_up= HistDict_up[obs][p][sys].Integral()
					HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)

					HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
					
				#	HistDict_do[obs][p][sys].Scale(bkgSF_misIDEle)
					HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)),misIDEleSF)

		#			HistDict_do[obs][p][sys].Scale(bkgSF_ZJets)
					total_do= HistDict_do[obs][p][sys].Integral()
					HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
				elif sys=="MisIDEleshape":
					HistDict_up[obs][p][sys] = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
			#		HistDict_up[obs][p][sys].Scale(bkgSF_misIDEle)
					HistDict_up[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)),misIDEleSF+misIDEle_unc)     
					#HistDict_up[obs][p][sys].Scale(bkgSF_ZJets)
					
					HistDict_do[obs][p][sys] = _file[s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
					#HistDict_do[obs][p][sys].Scale(bkgSF_misIDEle)
					HistDict_do[obs][p][sys].Add(_file[s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)),misIDEleSF-misIDEle_unc)	
						
					if s=="ZJets":
						HistDict_do[obs][p][sys].Scale(ZJetsSF)
						HistDict_up[obs][p][sys].Scale(ZJetsSF)
		#			else:
		#				HistDict_up[obs][p][sys].Scale(bkgSF_ZJets)
		#				HistDict_do[obs][p][sys].Scale(bkgSF_ZJets)

						
				else:
	#				print s,sys,_file_up[sys][s], "phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)
					HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
	#				HistDict_up[obs][p][sys].Scale(bkgSF_misIDEle)
					HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)),misIDEleSF)
					HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
					#HistDict_do[obs][p][sys].Scale(bkgSF_misIDEle)
					HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],s)),misIDEleSF)
					
					if s=="ZJets":
						HistDict_do[obs][p][sys].Scale(ZJetsSF)
						HistDict_up[obs][p][sys].Scale(ZJetsSF)
		#			else:
		#				HistDict_up[obs][p][sys].Scale(bkgSF_ZJets)
                 #                               HistDict_do[obs][p][sys].Scale(bkgSF_ZJets)
			
                        for sys in systematics:
				if onlyEGamma:continue
                                if "NonPrompt" in p and sys=="MisIDEleshape":continue
                                if sys=="Q2" or sys=="Pdf":
                                        if p not in ["TTGamma_Prompt", "TTGamma_NonPrompt","TTbar_Prompt", "TTbar_NonPrompt"] :continue

		if "_NonPrompt" in p:	
	#		print "now doing nonprompt"
			if onlyEGamma:
				if s=="QCD_DD":
					HistDict[obs][p] = _file[s].Get("phosel_%s_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s"%(obs,p))
				else:
					HistDict[obs][p] = _file[s].Get("phosel_%sOthers_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s"%(obs,p))
			else:
				if s=="QCD_DD":

                        	        HistDict[obs][p] = _file[s].Get("phosel_%s_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s"%(obs,p))
			        else:
					HistDict[obs][p] = _file[s].Get("phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s"%(obs,p))
				

			if s=="ZJets":
				HistDict[obs][p].Scale(ZJetsSF)#*bkgSF_misIDEle)
		#	else:
		#		HistDict[obs][p].Scale(bkgSF_ZJets*bkgSF_misIDEle)
			for sys in systematics:
				 if finalState=="mu" and "MassEGamma" in obs:continue
				 if onlyEGamma:continue
				 if s=="QCD_DD":
	#				print p, obs, sys
                                        HistDict_up[obs][p][sys] =HistDict[obs][p].Clone()
                                        HistDict_do[obs][p][sys] = HistDict[obs][p].Clone()
				 elif sys=="Q2":
						
					if p not in ["TTGamma_Prompt", "TTGamma_NonPrompt","TTbar_Prompt", "TTbar_NonPrompt"] :continue
					
					else:
	#					print p, obs, sys, _file_up[sys][s], "phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],s), 
						HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))
						#HistDict_up[obs][p][sys].Scale(bkgSF_ZJets*bkgSF_misIDEle)
						
						total_up= HistDict_up[obs][p][sys].Integral()
						HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)
#						print  _file_do[sys][s]
						HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
						#HistDict_do[obs][p][sys].Scale(bkgSF_ZJets*bkgSF_misIDEle)
						total_do= HistDict_do[obs][p][sys].Integral()
						HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)
					
				 elif sys=="Pdf" and s=="TTGamma":
					if p=="TTGamma_NonPrompt" and finalState=="mu" and obs=="MassEGamma":continue
					HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))

				#	HistDict_up[obs][p][sys].Scale(bkgSF_ZJets*bkgSF_misIDEle)
					total_up= HistDict_up[obs][p][sys].Integral()
					HistDict_up[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_up)

					HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))
				#	HistDict_do[obs][p][sys].Scale(bkgSF_ZJets*bkgSF_misIDEle)
					total_do= HistDict_do[obs][p][sys].Integral()
					HistDict_do[obs][p][sys].Scale(HistDict[obs][p].Integral()/total_do)

				 elif sys=="MisIDEleshape":continue
				 else:

					HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sUp"%(obs,p,sys))

					HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],s)).Clone("%s_%s_%sDown"%(obs,p,sys))

					if s=="ZJets":
						HistDict_do[obs][p][sys].Scale(ZJetsSF)#*bkgSF_misIDEle)
						HistDict_up[obs][p][sys].Scale(ZJetsSF)#*bkgSF_misIDEle)
#					else:
#						HistDict_do[obs][p][sys].Scale(bkgSF_ZJets*bkgSF_misIDEle)
 #                                               HistDict_up[obs][p][sys].Scale(bkgSF_ZJets*bkgSF_misIDEle)
			for sys in systematics:
				if onlyEGamma:continue
				if "NonPrompt" in p and sys=="MisIDEleshape":continue
				if sys=="Q2" or sys=="Pdf":
					if p not in ["TTGamma_Prompt", "TTGamma_NonPrompt","TTbar_Prompt", "TTbar_NonPrompt"] :continue
		
		for p in sub_signal:
			
                        for sys in systematics2:
				if onlyEGamma:continue
				if "_NonPrompt" in p:
	#				print _file_up[sys][process_signal[p][0]], "phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],process_signal[p][0])
					HistDict_up[obs][p][sys] = _file_up[sys][process_signal[p][0]].Get("phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
		
					HistDict_do[obs][p][sys] = _file_do[sys][process_signal[p][0]].Get("phosel_%s_NonPrompt_barrel_%s"%(histograms[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
		#			HistDict_do[obs][p][sys].Scale(bkgSF_ZJets*bkgSF_misIDEle)
                 #                       HistDict_up[obs][p][sys].Scale(bkgSF_ZJets*bkgSF_misIDEle)

				if "_Prompt" in p:
	#				print _file_up[sys][process_signal[p][0]]
					HistDict_up[obs][p][sys] = _file_up[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))

		#			HistDict_up[obs][p][sys].Scale(bkgSF_misIDEle)
                                        HistDict_up[obs][p][sys].Add(_file_up[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],process_signal[p][0])),misIDEleSF)

		#			HistDict_up[obs][p][sys].Scale(bkgSF_ZJets)
                                        HistDict_do[obs][p][sys] = _file_do[sys][process_signal[p][0]].Get("phosel_%s_GenuinePhoton_barrel_%s"%(histograms[obs][0],process_signal[p][0])).Clone("%s_%s"%(obs,p))
#					HistDict_do[obs][p][sys].Scale(bkgSF_misIDEle)
                                        HistDict_do[obs][p][sys].Add(_file_do[sys][process_signal[p][0]].Get("phosel_%s_MisIDEle_barrel_%s"%(histograms[obs][0],process_signal[p][0])),misIDEleSF)
#					HistDict_do[obs][p][sys].Scale(bkgSF_ZJets)
				

#exit()

process=["TTGamma","TTbar","TTV","SingleTop","TGJets","WJets","ZJets","WGamma","ZGamma","Diboson"]

for obs in histograms:
	for p in process:
		if finalState=="ele" and "Mu" in obs:continue
        	if finalState=="mu" and "Ele" in obs:continue
		if finalState=="mu" and "MassEGamma" in obs:continue
		HistDict[obs]["%s_Prompt"%p].Add(HistDict[obs]["%s_NonPrompt"%p])
		for sys in systematics:
			 if onlyEGamma:continue
			 if sys=="MisIDEleshape":
				HistDict_up[obs]["%s_Prompt"%p][sys].Add(HistDict[obs]["%s_NonPrompt"%p])
				HistDict_do[obs]["%s_Prompt"%p][sys].Add(HistDict[obs]["%s_NonPrompt"%p])
			 else:
				if sys=="Q2" or sys=="Pdf":
					if p not in ["TTbar","TTGamma"]:continue
			 	HistDict_up[obs]["%s_Prompt"%p][sys].Add(HistDict_up[obs]["%s_NonPrompt"%p][sys])
			 	HistDict_do[obs]["%s_Prompt"%p][sys].Add(HistDict_do[obs]["%s_NonPrompt"%p][sys])
        	for sys in systematics2:
			if onlyEGamma:continue
			if p not in ["TTGamma","TTbar"]:continue
			HistDict_up[obs]["%s_Prompt"%p][sys].Add(HistDict_up[obs]["%s_NonPrompt"%p][sys])
                        HistDict_do[obs]["%s_Prompt"%p][sys].Add(HistDict_do[obs]["%s_NonPrompt"%p][sys])
				
	

#exit()

sampleList[-2] = "QCD_DD"
stackList = sampleList[:-1]
stackList.remove("GJets")

from sampleInformation import *
samples["QCD_DD"] = [[],kGreen+3,"Multijet",isMC]

stackList.reverse()
legList = stackList[:]
legList.reverse()

if finalState=="mu":
        _channelText = "#mu+jets"
	plotDirectory="tightplots_mu_corrected"
elif finalState=="ele":
        _channelText = "e+jets"
	plotDirectory="tightplots_ele_corrected"
	if isLooseCRe3g1Selection:
		plotDirectory="CRplots_ele_corrected"
CMS_lumi.channelText = _channelText
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True

H = 600;
W = 800;
padRatio = 0.25
padOverlap = 0.15

padGap = 0.01

T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

legendHeightPer = 0.04
legList = stackList[:]
legList.reverse()

legendStart = 0.69
legendEnd = 0.97-(R/W)
legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legend.SetNColumns(2)
legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd-0.1, 0.99-(T/H)/(1.-padRatio+padOverlap))

legendR.SetNColumns(2)

legendR.SetBorderSize(0)
legendR.SetFillColor(0)



legend.SetBorderSize(0)
legend.SetFillColor(0)
for obs in histograms:
#	print "getting data"
#	print histograms[obs][3]
	if finalState=="ele" and "Mu" in obs:continue
        if finalState=="mu" and "Ele" in obs:continue
	if finalState=="mu" and "MassEGamma" in obs:continue
        if finalState=='ele':
#		 print _file["DataEle"]
                 HistDict[obs]["data"]=_file["DataEle"].Get("phosel_%s_barrel_DataEle"%(histograms[obs][0])).Clone("%s_DataEle"%(obs))
		 HistDict[obs]["data"].Sumw2()
                 if type(histograms[obs][3]) is type(list()):
#			print "Rebinning data"
                	HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))
#			if "MassEGamma" not in histograms[obs][0]:
#				HistDict[obs]["data"].Scale(1.,"width")
        	 else:
                	HistDict[obs]["data"].Rebin(histograms[obs][3]) 
		 if -1 not in histograms[obs][4]:
                 	HistDict[obs]["data"].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])

        elif finalState=='mu':
#		print _file["DataMu"], "phosel_%s_barrel_DataMu"%(histograms[obs][0])
                HistDict[obs]["data"]=_file["DataMu"].Get("phosel_%s_barrel_DataMu"%(histograms[obs][0])).Clone("%s_DataMu"%(obs))
		HistDict[obs]["data"].Sumw2()
		if type(histograms[obs][3]) is type(list()):
                        HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))
#			HistDict[obs]["data"].Scale(1.,"width")
                else:
                        HistDict[obs]["data"].Rebin(histograms[obs][3])
		if -1 not in histograms[obs][4]:
                	HistDict[obs]["data"].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])

#print HistDict[obs]["data"].Integral()
#exit()
HistDict[obs]["data"].SetMarkerStyle(8)
HistDict[obs]["data"].SetMarkerSize(1.0)
HistDict[obs]["data"].SetMarkerColor(kBlack)
legend.AddEntry(HistDict[obs]["data"], "Data", 'pe')
legendR.AddEntry(HistDict[obs]["data"], "Data", 'pe')




for sample in legList:
#	 print sample
	 if onlyEGamma:
		hist = _file[sample].Get("phosel_MassEGamma_barrel_%s"%(sample))
	 else:
	 	hist = _file[sample].Get("phosel_LeadingPhotonEt_barrel_%s"%(sample))
 #	      	print _file[sample],"phosel_LeadingPhotonEt_barrel_%s"%(sample)
    	 hist.SetFillColor(samples[sample][1])
         hist.SetLineColor(samples[sample][1])
    	 legend.AddEntry(hist,samples[sample][2],'f')



X = int(len(legList)/2)
sample = legList[X]
#print histName, _file[sample], "%s_%s"%(histName,sample)
if onlyEGamma:
        hist = _file[sample].Get("phosel_MassEGamma_barrel_%s"%(sample))
else:

	hist = _file[sample].Get("phosel_LeadingPhotonEt_barrel_%s"%(sample))
hist.SetFillColor(samples[sample][1])
hist.SetLineColor(samples[sample][1])
legendR.AddEntry(hist,samples[sample][2],'f')

for i in range(X):
	
        sample = legList[i]
	if onlyEGamma:
                hist = _file[sample].Get("phosel_MassEGamma_barrel_%s"%(sample))
        else:
        	hist = _file[sample].Get("phosel_LeadingPhotonEt_barrel_%s"%(sample))
       
        hist.SetFillColor(samples[sample][1])
        hist.SetLineColor(samples[sample][1])
        legendR.AddEntry(hist,samples[sample][2],'f')

        if X+i+1 < len(legList):
               
                sample = legList[i+X+1]
                if onlyEGamma:
                	hist = _file[sample].Get("phosel_MassEGamma_barrel_%s"%(sample))
         	else:
                	hist = _file[sample].Get("phosel_LeadingPhotonEt_barrel_%s"%(sample))
                hist.SetFillColor(samples[sample][1])
                hist.SetLineColor(samples[sample][1])
                legendR.AddEntry(hist,samples[sample][2],'f')




errorband=TH1F("error","error",20,0,20)
errorband.SetLineColor(0)
errorband.SetFillColor(kBlack)
errorband.SetFillStyle(3245)
errorband.SetMarkerSize(0)
legendR.AddEntry(errorband,"Uncertainty","f")
from numpy import log10
TGaxis.SetMaxDigits(3)
sub_signal=["TTGamma_Prompt","TTGamma_NonPrompt","TTbar_Prompt","TTbar_NonPrompt"]
systematics2 = ["isr","fsr"]
def drawHist(histName,plotInfo, plotDirectory, _file):
    #print "start drawing"


    canvas = TCanvas('c1','c1',W,H)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetLeftMargin( L/W )
    canvas.SetRightMargin( R/W )
    canvas.SetTopMargin( T/H )
    canvas.SetBottomMargin( B/H )
    canvas.SetTickx(0)


    canvasRatio = TCanvas('c1Ratio','c1Ratio',W,H)
    canvasRatio.SetFillColor(0)
    canvasRatio.SetBorderMode(0)
    canvasRatio.SetFrameFillStyle(0)
    canvasRatio.SetFrameBorderMode(0)
    canvasRatio.SetLeftMargin( L/W )
    canvasRatio.SetRightMargin( R/W )
    canvasRatio.SetTopMargin( T/H )
    canvasRatio.SetBottomMargin( B/H )
    canvasRatio.SetTickx(0)
    canvasRatio.SetTicky(0)
    canvasRatio.Draw()
    canvasRatio.cd()

    pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
    pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
    pad1.SetLeftMargin( L/W )
    pad1.SetRightMargin( R/W )
    pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
    pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
    pad2.SetLeftMargin( L/W )
    pad2.SetRightMargin( R/W )
    pad2.SetTopMargin( (padOverlap)/(padRatio+padOverlap) )
    pad2.SetBottomMargin( B/H/(padRatio+padOverlap) )

    pad1.SetFillColor(0)
    pad1.SetBorderMode(0)
    pad1.SetFrameFillStyle(0)
    pad1.SetFrameBorderMode(0)
    pad1.SetTickx(0)
    pad1.SetTicky(0)

    pad2.SetFillColor(0)
    pad2.SetFillStyle(4000)
    pad2.SetBorderMode(0)
    pad2.SetFrameFillStyle(0)
    pad2.SetFrameBorderMode(0)
    pad2.SetTickx(0)
    pad2.SetTicky(0)


    canvasRatio.cd()
    pad1.Draw()
    pad2.Draw()


    canvas.cd()
    canvas.ResetDrawn()
    stack = THStack(histName,histName)
    SetOwnership(stack,True)
    for sample in stackList:
	print sample
        if finalState=="ele" and "Mu" in histName:continue
        if finalState=="mu" and "Ele" in histName:continue
	if finalState=="mu" and "MassEGamma" in obs:continue
	if sample=="QCD_DD":
		hist = HistDict[histName]["QCD_NonPrompt"].Clone()
	else:
        	hist = HistDict[histName]["%s_Prompt"%sample].Clone()
		#print HistDict[histName]["%s_Prompt"%sample]
        if type(hist)==type(TObject()):
		continue
	else:
        	hist = hist.Clone(sample)
        	hist.SetFillColor(samples[sample][1])
        	hist.SetLineColor(samples[sample][1])
#	if "TTGamma" in sample:
#		print "scaling TTGamma"
#		hist.Scale(TTGammaSF)
#	elif "TTbar" in sample:
#		hist.Scale(TTbarSF)
#	elif "VGamma" in sample:
#		hist.Scale(VGammaSF)
#	elif "Other" in sample:
#		hist.Scale(OtherSF)
#	if "NonPrompt" in sample:
#		hist.Scale(NPSF)	
 #       print histName, histograms[histName][3], 
	if type(histograms[histName][3]) is type(list()):
#		print "rebinning", hist, histName
		
		hist=hist.Rebin(len(histograms[histName][3])-1,"",array('d',histograms[histName][3]))
#		if "MassEGamma" not in histName:
#			hist.Scale(1.,"width")
	else:
		hist.Rebin(histograms[histName][3])
		if -1 not in histograms[histName][4]:
        		hist.GetXaxis().SetRangeUser(histograms[histName][4][0],histograms[obs][4][1])


        stack.Add(hist)
    noData = False
    if type(HistDict[histName]["data"])==type(TObject()): noData = True
    oneLine = TF1("oneline","1",-9e9,9e9)
    oneLine.SetLineColor(kBlack)
    oneLine.SetLineWidth(1)
    oneLine.SetLineStyle(2)

    _text = TPaveText(0.35,.75,0.45,0.85,"NDC")
    _text.SetTextColor(kBlack)
    _text.SetFillColor(0)
    _text.SetTextSize(0.04)
    _text.SetTextFont(42)

    canvas.SetLogy(histograms[histName][6])
    maxVal = stack.GetMaximum()
    if not noData:
            maxVal = max(HistDict[histName]["data"].GetMaximum(),maxVal)

    minVal = 1
    if plotInfo[6]:
            stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
            stack.SetMinimum(minVal)
    else:
            stack.SetMaximum(1.5*maxVal)
            stack.SetMinimum(minVal)

    errorband=stack.GetStack().Last().Clone("error")
    errorband.Sumw2()
    errorband.SetLineColor(kBlack)
    errorband.SetFillColor(kBlack)
    errorband.SetFillStyle(3245)
    errorband.SetMarkerSize(0)
    h1_up={}
    h1_do={}
    for sample in stackList:
	for sys in systematics:
		if onlyEGamma:continue
#		print "now doing systematics"
		if sample=="QCD_DD":
		        if sys=="Pdf" or sys=="Q2" or sys=="isr" or sys=="fsr" or sys=="MisIDEleshape":continue	
			HistDict_up[histName]["QCD_NonPrompt"][sys]= HistDict[histName]["QCD_NonPrompt"].Clone()
			HistDict_do[histName]["QCD_NonPrompt"][sys]= HistDict[histName]["QCD_NonPrompt"].Clone()
			if type(histograms[histName][3]) is type(list()):
                        	HistDict_do[histName]["QCD_NonPrompt"][sys]=HistDict_do[histName]["QCD_NonPrompt"][sys].Rebin(len(histograms[histName][3])-1,"",array('d',histograms[histName][3]))
                        	HistDict_up[histName]["QCD_NonPrompt"][sys]=HistDict_up[histName]["QCD_NonPrompt"][sys].Rebin(len(histograms[histName][3])-1,"",array('d',histograms[histName][3]))
		#		HistDict_up[histName]["QCD_NonPrompt"][sys].Scale(1.,"width")
                 #3               HistDict_do[histName]["QCD_NonPrompt"][sys].Scale(1.,"width")
                	else:
                        	HistDict_do[histName]["QCD_NonPrompt"][sys].Rebin(histograms[histName][3])
     	                  	HistDict_up[histName]["QCD_NonPrompt"][sys].Rebin(histograms[histName][3])
                		HistDict_do[histName]["QCD_NonPrompt"][sys].GetXaxis().SetRangeUser(histograms[histName][4][0],histograms[histName][4][1])
                		HistDict_up[histName]["QCD_NonPrompt"][sys].GetXaxis().SetRangeUser(histograms[histName][4][0],histograms[histName][4][1])
		else:
			if sys=="Q2" or sys=="Pdf" or sys=="isr" or sys=="fsr":
                        	if sample not in ["TTbar","TTGamma"]:continue
                	elif finalState=="mu" and "ele" in histName:continue
                	elif finalState=="ele" and "mu" in histName:continue
			elif sample=="TTGamma" and (sys=="Pdf" or sys=="Q2"):
				total=HistDict[histName][sample].Integral()
				HistDict_up[histName]["%s_Prompt"%sample][sys].Scale(total/HistDict_up[histName]["%s_Prompt"%sample][sys].Integral())
				HistDict_do[histName]["%s_Prompt"%sample][sys].Scale(total/HistDict_do[histName]["%s_Prompt"%sample][sys].Integral())
			elif sample=="TTbar" and sys=="Q2":
				total=HistDict[histName][sample].Integral()
				HistDict_up[histName]["%s_Prompt"%sample][sys].Scale(total/HistDict_up[histName]["%s_Prompt"%sample][sys].Integral())
				HistDict_do[histName]["%s_Prompt"%sample][sys].Scale(total/HistDict_do[histName]["%s_Prompt"%sample][sys].Integral())
			if type(histograms[histName][3]) is type(list()):
			
				HistDict_do[histName]["%s_Prompt"%sample][sys]=HistDict_do[histName]["%s_Prompt"%sample][sys].Rebin(len(histograms[histName][3])-1,"",array('d',histograms[histName][3]))
				HistDict_up[histName]["%s_Prompt"%sample][sys]=HistDict_up[histName]["%s_Prompt"%sample][sys].Rebin(len(histograms[histName][3])-1,"",array('d',histograms[histName][3]))
			
	#			HistDict_up[histName]["%s_Prompt"%sample][sys].Scale(1.,"width")
	#			HistDict_do[histName]["%s_Prompt"%sample][sys].Scale(1.,"width")

			else:
				HistDict_do[histName]["%s_Prompt"%sample][sys].Rebin(histograms[histName][3])
				HistDict_up[histName]["%s_Prompt"%sample][sys].Rebin(histograms[histName][3])
				HistDict_do[histName]["%s_Prompt"%sample][sys].GetXaxis().SetRangeUser(histograms[histName][4][0],histograms[histName][4][1])
				HistDict_up[histName]["%s_Prompt"%sample][sys].GetXaxis().SetRangeUser(histograms[histName][4][0],histograms[histName][4][1])


    error=0.
    diff={}
    sum_={}
    for i_bin in range(1,errorband.GetNbinsX()+1):
	        if onlyEGamma:continue
                sum_[i_bin]=0.
                diff[i_bin]=[]
                for sys in systematics:
			if onlyEGamma:continue
                        for sample in stackList:
				if sys=="Q2" or sys=="Pdf" or sys=="isr" or sys=="fsr":
                                        if sample not in ["TTbar","TTGamma"]:continue
                                if finalState=="mu" and "ele" in histName:continue
                                if finalState=="ele" and "mu" in histName:continue
                                if finalState=="mu" and "MassEGamma" in histName:continue
				if sample=="QCD_DD":
					sum_[i_bin]+=((HistDict_up[histName]["QCD_NonPrompt"][sys].GetBinContent(i_bin)-HistDict_do[histName]["QCD_NonPrompt"][sys].GetBinContent(i_bin))/2.)**2.
				else:
					sum_[i_bin]+=((HistDict_up[histName]["%s_Prompt"%sample][sys].GetBinContent(i_bin)-HistDict_do[histName]["%s_Prompt"%sample][sys].GetBinContent(i_bin))/2.)**2.
#		print i_bin, (sum_[i_bin])**0.5
		errorband.SetBinError(i_bin,(sum_[i_bin])**0.5)
    stack.Draw('hist')
    stack.GetHistogram().GetXaxis().SetTitle(histograms[histName][1])
    if not -1 in plotInfo[4]:
        stack.GetHistogram().GetXaxis().SetRangeUser(histograms[histName][4][0],histograms[histName][4][1])
    if not noData:
	HistDict[histName]["data"].SetMarkerStyle(8)
        HistDict[histName]["data"].SetMarkerSize(1.0)
	HistDict[histName]["data"].SetMarkerColor(kBlack)
        HistDict[histName]["data"].SetLineColor(kBlack)
        HistDict[histName]["data"].Draw("e,X0,same")

    legend.Draw("same")
    CMS_lumi.channelText = _channelText+histograms[histName][5]
    CMS_lumi.CMS_lumi(canvas, 4, 11)

    canvas.Print("%s/%s.pdf"%(plotDirectory,histName))

    if not noData:
        ratio =HistDict[histName]["data"].Clone("temp")
        temp = stack.GetStack().Last().Clone("temp")

        for i_bin in range(1,temp.GetNbinsX()+1):
                temp.SetBinError(i_bin,0.)
        ratio.Divide(temp)
	canvasRatio.cd()
        canvasRatio.ResetDrawn()
        canvasRatio.Draw()
        canvasRatio.cd()

        pad1.Draw()
        pad2.Draw()

        pad1.cd()
        pad1.SetLogy(plotInfo[6])

        stack.Draw('HIST')
        y2 = pad1.GetY2()


        stack.GetXaxis().SetTitle('')
        stack.GetYaxis().SetTitle(HistDict[histName]["data"].GetYaxis().GetTitle())

        stack.SetTitle('')
        stack.GetXaxis().SetLabelSize(0)
        stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
        stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
        stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
        stack.GetYaxis().SetTitle(plotInfo[2])
        HistDict[histName]["data"].Draw('E,X0,SAME')
        legendR.Draw()

        _text = TPaveText(0.42,.75,0.5,0.85,"NDC")
        _text.AddText(plotInfo[5])
        _text.SetTextColor(kBlack)
        _text.SetFillColor(0)
        _text.SetTextSize(0.05)
        _text.SetTextFont(42)
        ratio.SetTitle('')

        ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
        ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
	ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
        ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
        ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))

        maxRatio = ratio.GetMaximum()
        minRatio = ratio.GetMinimum()


        maxRatio = 1.5
        minRatio = 0.5
        for i_bin in range(1,ratio.GetNbinsX()+1):
                if ratio.GetBinError(i_bin)<1:
                        if ratio.GetBinContent(i_bin)>maxRatio:
                                maxRatio = ratio.GetBinContent(i_bin)
                        if ratio.GetBinContent(i_bin)<minRatio:
                                minRatio = ratio.GetBinContent(i_bin)

        if maxRatio > 1.8:
                ratio.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
        elif maxRatio < 1:
                ratio.GetYaxis().SetRangeUser(0,1.2)
        elif maxRatio-1 < 1-minRatio:
                ratio.GetYaxis().SetRangeUser((1-(1-minRatio)*1.2),1.1*maxRatio)

	else:
                ratio.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)

	ratio.GetYaxis().SetRangeUser(0.45,1.45)
        ratio.GetYaxis().SetNdivisions(504)
        ratio.GetXaxis().SetTitle(histograms[histName][1])
        ratio.GetYaxis().SetTitle("Data/MC")
        CMS_lumi.CMS_lumi(pad1, 4, 11)

        pad2.cd()
        maxRatio = 1.5
        minRatio = 0.5
        ratio.SetMarkerStyle(HistDict[histName]["data"].GetMarkerStyle())
        ratio.SetMarkerSize(HistDict[histName]["data"].GetMarkerSize())
        ratio.SetLineColor(HistDict[histName]["data"].GetLineColor())
        ratio.SetLineWidth(HistDict[histName]["data"].GetLineWidth())
        ratio.Draw('e,x0')
	#if not isLooseCRe3g1Selection:
		
	
        errorband.Divide(temp)
        errorband.Draw('e2,same')
        oneLine.Draw("same")

        canvasRatio.Update()
        canvasRatio.RedrawAxis()
        canvasRatio.SaveAs("%s/%s_ratio.pdf"%(plotDirectory,histName))
        canvasRatio.SetLogy(0)

    canvas.Close()
    canvasRatio.Close()

for histName in histograms:
	if finalState=="ele" and "Mu" in histName:continue
        if finalState=="mu" and "Ele" in histName:continue
	if finalState=="mu" and "MassEGamma" in histName:continue
	drawHist(histName,histograms[histName],plotDirectory,_file)
	



exit()

print "making root file now"

outputFile = TFile("Otherplots_%s%s.root"%(finalState,dir_),"recreate")


groups ={"VGamma":["ZGamma","WGamma"],
         "Other":["TTV","SingleTop","TGJets","WJets","ZJets","Diboson"],
	 }




for obs in histograms:
	for g in groups:
		#print "cloning","%s_Prompt"%groups[g][0]
		HistDict[obs]["%s_Prompt"%g]=HistDict[obs]["%s_Prompt"%groups[g][0]].Clone()
		HistDict[obs]["%s_NonPrompt"%g]=HistDict[obs]["%s_NonPrompt"%groups[g][0]].Clone()
		for sys in systematics:
			if sys in ["Pdf","Q2","isr","fsr"]:continue
		#	print "%s_Prompt"%g, sys, obs
			HistDict_up[obs]["%s_Prompt"%g][sys]=HistDict_up[obs]["%s_Prompt"%groups[g][0]][sys].Clone()
			HistDict_do[obs]["%s_Prompt"%g][sys]=HistDict_do[obs]["%s_Prompt"%groups[g][0]][sys].Clone()
			if sys=="MisIDEleshape":continue
			HistDict_up[obs]["%s_NonPrompt"%g][sys]=HistDict_up[obs]["%s_NonPrompt"%groups[g][0]][sys].Clone()
                        HistDict_do[obs]["%s_NonPrompt"%g][sys]=HistDict_do[obs]["%s_NonPrompt"%groups[g][0]][sys].Clone()
		for i in range(len(groups[g])-1):
		#	print "Adding", "%s_Prompt"%groups[g][i+1], "to", "%s_Prompt"%g
			HistDict[obs]["%s_Prompt"%g].Add(HistDict[obs]["%s_Prompt"%groups[g][i+1]])
			for sys in systematics:
				if sys in ["Pdf","Q2","isr","fsr"]:continue
                        	HistDict_up[obs]["%s_Prompt"%g][sys].Add(HistDict_up[obs]["%s_Prompt"%groups[g][0]][sys])
				HistDict_do[obs]["%s_Prompt"%g][sys].Add(HistDict_do[obs]["%s_Prompt"%groups[g][0]][sys])
                        	if sys=="MisIDEleshape":continue
                        	HistDict_up[obs]["%s_NonPrompt"%g][sys].Add(HistDict_up[obs]["%s_NonPrompt"%groups[g][0]][sys])
				HistDict_do[obs]["%s_NonPrompt"%g][sys].Add(HistDict_do[obs]["%s_NonPrompt"%groups[g][0]][sys])
				



process=["TTGamma_Prompt","TTGamma_NonPrompt","TTbar_Prompt","TTbar_NonPrompt","VGamma_Prompt","VGamma_NonPrompt","Other_Prompt","Other_NonPrompt"]
for obs in histograms:
	if finalState=="ele" and "Mu" in obs:continue
        if finalState=="mu" and "Ele" in obs:continue
	
        outputFile.mkdir("%s/%s"%(histograms[obs][8],"data_obs"))
        outputFile.cd("%s/%s"%(histograms[obs][8],"data_obs"))
	if finalState=="mu":
		HistDict[obs]["data"]=_file["DataMu"].Get("phosel_%s_barrel_DataMu"%(histograms[obs][0])).Clone("%s_DataMu"%(obs))
		if -1 not in histograms[obs][4]:
                 #       print "setting x axis data", obs, histograms[obs][4]
                        HistDict[obs]["data"].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])
		if type(histograms[obs][3]) is type(list()):
                	

                	HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))
              
        	else:
			
                	HistDict[obs]["data"].Rebin(histograms[obs][3])
		HistDict[obs]["data"].Write("nominal")
	else:
		HistDict[obs]["data"]=_file["DataEle"].Get("phosel_%s_barrel_DataEle"%(histograms[obs][0])).Clone("%s_DataEle"%(obs))
		if -1 not in histograms[obs][4]:
                  #      print "setting x axis data", obs, histograms[obs][4]
                        HistDict[obs]["data"].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])
                if type(histograms[obs][3]) is type(list()):
                   #     print "rebinning data", obs

                        HistDict[obs]["data"]=HistDict[obs]["data"].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))
                 #       HistDict[obs]["data"].Scale(1.,"width")
                else:
		#	print "rebinning data", obs, histograms[obs][3]
		#	print "original bins:", HistDict[obs]["data"].GetNbinsX()
                        HistDict[obs]["data"].Rebin(histograms[obs][3])
                 #       print "new bins:", HistDict[obs]["data"].GetNbinsX()
                HistDict[obs]["data"].Write("nominal")
        outputFile.mkdir(histograms[obs][8])
	

	for p in process:
	#	print "%s/%s"%(obs,p)
	      	outputFile.mkdir("%s/%s"%(histograms[obs][8],p))
     		outputFile.cd("%s/%s"%(histograms[obs][8],p))
		if -1 not in histograms[obs][4]:
                        HistDict[obs][p].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])
		if type(histograms[obs][3]) is type(list()):
                     

                        HistDict[obs][p]=HistDict[obs][p].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))
               
                else:
                        HistDict[obs][p].Rebin(histograms[obs][3])
		HistDict[obs][p].Write("nominal")
		for sys in systematics:
			if isLooseCRe3g1Selection: continue
			if sys in ["Pdf", "Q2" ,"isr", "fsr"] and p not in ["TTbar_Prompt","TTbar_NonPrompt","TTGamma_Prompt","TTGamma_NonPrompt"]:continue
			if sys=="MisIDEleshape" and "NonPrompt" in p:continue
			elif  sys=="Q2" and p not in ["TTbar_Prompt","TTbar_NonPrompt","TTGamma_Prompt","TTGamma_NonPrompt"]:continue
			elif sys=="Pdf" and "TTGamma" in p:
				if -1 not in histograms[obs][4]:
                                        HistDict_up[obs][p][sys].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])
                                        HistDict_do[obs][p][sys].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])
				if type(histograms[obs][3]) is type(list()):
                        

                                	HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))
					HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))
                
                        	else:
                                	HistDict_up[obs][p][sys].Rebin(histograms[obs][3])
					HistDict_do[obs][p][sys].Rebin(histograms[obs][3])
					
				HistDict_up[obs][p][sys].Write("%ssignalUp"%(sys))
				HistDict_do[obs][p][sys].Write("%ssignalDown"%(sys))
			else:
				if -1 not in histograms[obs][4]:
                                        HistDict_up[obs][p][sys].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])
                                        HistDict_do[obs][p][sys].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])
				if type(histograms[obs][3]) is type(list()):


                                        HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))
                                        HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))

                                else:
                                        HistDict_up[obs][p][sys].Rebin(histograms[obs][3])
                                        HistDict_do[obs][p][sys].Rebin(histograms[obs][3])

				HistDict_up[obs][p][sys].Write("%sUp"%(sys))
				HistDict_do[obs][p][sys].Write("%sDown"%(sys))
        for p in sub_signal:
		outputFile.cd("%s/%s"%(histograms[obs][8],p))         
                for sys in systematics2:
			if isLooseCRe3g1Selection: continue
			
			outputFile.cd("%s/%s"%(histograms[obs][8],p))
			if -1 not in histograms[obs][4]:
                                        HistDict_up[obs][p][sys].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])
                                        HistDict_do[obs][p][sys].GetXaxis().SetRangeUser(histograms[obs][4][0],histograms[obs][4][1])
			if type(histograms[obs][3]) is type(list()):


                                        HistDict_up[obs][p][sys]=HistDict_up[obs][p][sys].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))
                                        HistDict_do[obs][p][sys]=HistDict_do[obs][p][sys].Rebin(len(histograms[obs][3])-1,"",array('d',histograms[obs][3]))

                        else:
                                        HistDict_up[obs][p][sys].Rebin(histograms[obs][3])
                                        HistDict_do[obs][p][sys].Rebin(histograms[obs][3])

			HistDict_up[obs][p][sys].Write("%sUp"%(sys))
			HistDict_do[obs][p][sys].Write("%sDown"%(sys))




outputFile.Close()
