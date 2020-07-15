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

samples =["TTGamma","TTbar","TTV","TGJets","SingleTop","WJets","ZJets","WGamma","ZGamma","Diboson", "DataMu","GJets"]

for s in samples:
	_file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/mu/hists/%s.root"%s)

misIDEleSF = 1.
HistDict={}
HistDict_up={}
HistDict_do={}
_file_up={}
_file_do={}

systematics = ["JER","phosmear","phoscale","elesmear","elescale","BTagSF","EleEff","Q2","Pdf","Pileup","MuEff"]

for sys in systematics:
       _file_up[sys]={}
       _file_do[sys]={}
       for s in samples:
               if s =="DataMu":continue
               _file_up[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/mu/hists%s_up/%s.root"%(sys,s))
               _file_do[sys][s]=TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/mu/hists%s_down/%s.root"%(sys,s))


bins = [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.]

observables={"M3": ["M3",10],
	     "ChHad":["noCut_ChIso",bins],
	     "M3_control":["M3_control",10]
           }

print sorted(observables.keys())[:2]


process_signal = {"TTGamma_Prompt":["TTGamma"],
	   "TTGamma_NonPrompt":["TTGamma"],
           "TTbar_Prompt": ["TTbar"],
           "TTbar_NonPrompt": ["TTbar"],
           "VGamma_Prompt":["ZGamma","WGamma"],
           "VGamma_NonPrompt":["ZGamma","WGamma"],
	   "SingleTop_Prompt":["TGJets", "SingleTop"],
	   "SingleTop_NonPrompt":["TGJets", "SingleTop"],
           "VJets_Prompt":["WJets", "ZJets"],
           "VJets_NonPrompt":["WJets", "ZJets"],
           "Other_Prompt":["TTV", "Diboson"],
           "Other_NonPrompt":["TTV", "Diboson"],
	}



process_control ={"TTGamma":["TTGamma"],
		  "TTbar":  ["TTbar"],
		  "VGamma":["ZGamma", "WGamma"],
		  "VJets":["WJets", "ZJets"],
		  "SingleTop":["TGJets", "SingleTop"],
		  "Other":[ "TTV", "Diboson"],
		}	





##### Make Prompt and NonPrompt MC templates#######
process={}
for obs in observables:
	HistDict[obs]={}
	HistDict_up[obs]={}
	HistDict_do[obs]={}
        if obs=="M3_control":
		for p in process_control:
			s= process_control[p][0]
			HistDict_up[obs][p]={}
			HistDict_do[obs][p]={}
			HistDict[obs][p]   = _file[s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
			for sys in systematics:
				HistDict_up[obs][p][sys] = _file_up[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
				HistDict_do[obs][p][sys] = _file_do[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
				

			for s in process_control[p][1:]:
				HistDict[obs][p].Add(_file[s].Get("presel_%s_%s"%(observables[obs][0],s)))
				for sys	in systematics:
					HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)))
					HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("presel_%s_%s"%(observables[obs][0],s)))
			HistDict[obs][p].Rebin(observables[obs][1])
			for sys in systematics:
				HistDict_up[obs][p][sys].Rebin(observables[obs][1])
				HistDict_do[obs][p][sys].Rebin(observables[obs][1])
				
	else:
		

		for p in process_signal:
			HistDict_up[obs][p]={}
                        HistDict_do[obs][p]={}
			
		 	s = process_signal[p][0]
			if "NonPrompt" in p:
				 print "phosel_%s_HadronicPhoton_%s"%(observables[obs][0],s)
				 HistDict[obs][p]   = _file[s].Get("phosel_%s_HadronicPhoton_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
				 HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_%s"%(observables[obs][0],s)))
				 
				
				 for sys in systematics:
					 HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_HadronicPhoton_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					 HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_%s"%(observables[obs][0],s)))

					 HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_HadronicPhoton_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                         HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_%s"%(observables[obs][0],s)))

		 	if "_Prompt" in p:
			 	HistDict[obs][p]   = _file[s].Get("phosel_%s_GenuinePhoton_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
			 	HistDict[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_%s"%(observables[obs][0],s)))
				
				for sys in systematics:
					print sys,observables[obs][0],s,p
					HistDict_up[obs][p][sys] = _file_up[sys][s].Get("phosel_%s_GenuinePhoton_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
					HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_%s"%(observables[obs][0],s)))


					HistDict_do[obs][p][sys] = _file_do[sys][s].Get("phosel_%s_GenuinePhoton_%s"%(observables[obs][0],s)).Clone("%s_%s"%(obs,p))
                                        HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_%s"%(observables[obs][0],s)))
									
				
			for s in process_signal[p][1:]:
				if "_Prompt" in p:
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_GenuinePhoton_%s"%(observables[obs][0],s)))
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_MisIDEle_%s"%(observables[obs][0],s)))
					
					for sys in systematics:
						HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_GenuinePhoton_%s"%(observables[obs][0],s)))
						HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_MisIDEle_%s"%(observables[obs][0],s)))

						HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_GenuinePhoton_%s"%(observables[obs][0],s)))
                                                HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_MisIDEle_%s"%(observables[obs][0],s)))
					
				if "_NonPrompt" in p:
					HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicPhoton_%s"%(observables[obs][0],s)))
                                        HistDict[obs][p].Add(_file[s].Get("phosel_%s_HadronicFake_%s"%(observables[obs][0],s)))


					for sys in systematics:
                                                HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicPhoton_%s"%(observables[obs][0],s)))
						HistDict_up[obs][p][sys].Add(_file_up[sys][s].Get("phosel_%s_HadronicFake_%s"%(observables[obs][0],s)))


						HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicPhoton_%s"%(observables[obs][0],s)))
                                                HistDict_do[obs][p][sys].Add(_file_do[sys][s].Get("phosel_%s_HadronicFake_%s"%(observables[obs][0],s)))
			

			if "ChIso" in observables[obs][0]:
				HistDict[obs][p]= HistDict[obs][p].Rebin(21,"",array('d',bins))
				for sys in systematics:
					 HistDict_up[obs][p][sys] = HistDict_up[obs][p][sys].Rebin(21,"",array('d',bins))
					 HistDict_do[obs][p][sys] = HistDict_do[obs][p][sys].Rebin(21,"",array('d',bins))
			else:
				HistDict[obs][p].Rebin(observables[obs][1])
				for sys in systematics:
					 HistDict_up[obs][p][sys].Rebin(observables[obs][1])
					 HistDict_do[obs][p][sys].Rebin(observables[obs][1])




###make Data-Driven NonPrompt Templates######

h1 = _file["DataMu"].Get("phosel_AntiSIEIE_ChIso_barrel_DataMu").Clone("ChHad_NonPrompt")
h1.Add(_file["DataMu"].Get("phosel_AntiSIEIE_ChIso_endcap_DataMu"))
h1 = h1.Rebin(21,"",array('d',bins))
total = h1.Integral(-1,-1)
print "total antisiesie data:", total
NormFactor={}



for p in process_signal:
	NormFactor[p]={}
	if "_NonPrompt" in p:
		print p	
		p1=p.strip("NonPrompt")
		p1= p1.strip("_")
		print p1
		print "%s_DD"%p1
		HistDict["ChHad"]["%s_DD"%p1]=_file["DataMu"].Get("phosel_AntiSIEIE_ChIso_barrel_DataMu").Clone("ChHad_NonPrompt")
		HistDict["ChHad"]["%s_DD"%p1].Add(_file["DataMu"].Get("phosel_AntiSIEIE_ChIso_endcap_DataMu"))
		NormFactor["%s_DD"%p1]=HistDict["ChHad"][p].Integral(-1,-1)
		print "Scaling to:",NormFactor["%s_DD"%p1]
		print "Original number:",HistDict["ChHad"]["%s_DD"%p1].Integral(-1,-1)
		HistDict["ChHad"]["%s_DD"%p1].Scale(NormFactor["%s_DD"%p1]/total)
		print "Final number:",HistDict["ChHad"]["%s_DD"%p1].Integral(-1,-1)





		
		
	
#exit()




#print sorted(observables.keys())
#print "for control",sorted(observables.keys())[2:]
#print "for signal",sorted(observables.keys())[:2]
#for c in HistDict:
#	if c=="M3_control": 
#		HistDict = makePseudoData(HistDict,process_control.keys(),sorted(observables.keys())[2:])
#	else:
#		HistDict = makePseudoData(HistDict,process_signal.keys(),sorted(observables.keys())[:2])

canvas = TCanvas('c1','c1',1000,1000)
canvas.SetFillColor(0)
canvas.cd()

padRatio = 0.25
padOverlap = 0.15
padGap = 0.01
H = 600;
W = 800;


# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W
legendHeightPer = 0.04
legendStart = 0.69
legendEnd = 0.97-(R/W)
legend = TLegend(0.71, 1-T/H-0.01 - legendHeightPer*(6+1), 1-R/W-0.01, 1-(T/H)-0.01)
legend2 = TLegend(0.71, 1-T/H-0.01 - legendHeightPer*(6+1), 1-R/W-0.01, 1-(T/H)-0.01)
legend1 = TLegend(0.71, 1-T/H-0.01 - legendHeightPer*(6+1), 1-R/W-0.01, 1-(T/H)-0.01)
legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((6+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legendR.SetNColumns(2)

legendR.SetFillColor(0)
legendR.SetBorderSize(0)


#legend = TLegend(0.55, 0.55, 0.85, 0.85)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend1.SetBorderSize(0)
legend1.SetFillColor(0)
legend2.SetBorderSize(0)
legend2.SetFillColor(0)
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
T = 0.08*H
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



pad1.Draw()
pad2.Draw()


canvas.cd()

process_colors = {"TTGamma_Prompt":[kOrange,"TTGamma"],
           "TTGamma_DD":[kOrange,"TTGamma"],
           "TTbar_Prompt": [kRed+1,"TTbar"],
           "TTbar_DD": [kRed+1,"TTbar"],
           "VGamma_Prompt":[kBlue-9,"VGamma"],
           "VGamma_DD":[kBlue-9,"VGamma"],
           "SingleTop_Prompt":[kOrange-3,"SingleTop"],
           "SingleTop_DD":[kOrange-3,"SingleTop"],
           "VJets_Prompt":[kGreen-6,"VJets"],
           "VJets_DD":[kGreen-6,"VJets"],
           "Other_Prompt":[kBlue,"Other"],
           "Other_DD":[kBlue,"Other"],
        }
process_= ["SingleTop_Prompt","SingleTop_DD","Other_Prompt","Other_DD","VGamma_Prompt","VGamma_DD","VJets_Prompt","VJets_DD","TTbar_Prompt","TTbar_DD","TTGamma_Prompt","TTGamma_DD"]

observe_ =["ChHad"]
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
#canvas.SetLogy()
stack = THStack("hs","hs")
stack1 = THStack("hs1","hs1")
stack2 = THStack("hs2","hs2")
SetOwnership(stack,True)
h2 = _file["DataMu"].Get("phosel_noCut_ChIso_DataMu").Clone("ChHad_Iso")
h2 = h2.Rebin(21,"",array('d',bins))
print "data ChIso:", h2.Integral(-1,-1)
#print HistDict[o]
for o in observe_:
	for p in process_:
		if "DD" in p:
			print p
                        HistDict[o][p].SetFillColor(process_colors[p][0])
                        HistDict[o][p].SetLineColor(process_colors[p][0])
                        HistDict[o][p]=HistDict[o][p].Rebin(21,"",array('d',bins))
                        stack.Add(HistDict[o][p])
			stack1.Add(HistDict[o][p])
                        legend.AddEntry(HistDict[o][p],process_colors[p][1],'f')
			legend1.AddEntry(HistDict[o][p],process_colors[p][1],'f')
                        legendR.AddEntry(HistDict[o][p],process_colors[p][1],'f')

		
		else:
			print p
			HistDict[o][p].SetFillColor(process_colors[p][0])
			HistDict[o][p].SetLineColor(process_colors[p][0])
		#	HistDict[o][p]=HistDict[o][p].Rebin(21,"",array('d',bins))
			stack.Add(HistDict[o][p])
                        stack2.Add(HistDict[o][p])
			
			
#	hs.Draw('HIST')
#	h2= h2.Rebin(21,"",array('d',bins))
	h2.SetMarkerStyle(8)
        h2.SetMarkerSize(1.0)
        legend.AddEntry(h2,"Data",'pe')	
        legendR.AddEntry(h2,"Data",'pe')        	
#	canvas.SaveAs("data.pdf")
#	canvas.Clear()
	stack.Draw("hist")
	stack.GetHistogram().GetXaxis().SetTitle("Charge Hadron Isolation")
	stack.GetHistogram().GetYaxis().SetTitle("Events")	
        h2.Draw("e,x0,same")	
	legend.Draw("same")
	canvas.SaveAs("Fit_templates.pdf")
	canvas.SaveAs("Fit_templates.png")
	canvas.Clear()
        stack1.Draw("hist")
        stack1.GetHistogram().GetXaxis().SetTitle("Charge Hadron Isolation")
        stack1.GetHistogram().GetYaxis().SetTitle("Events")
	stack1.GetHistogram().SetTitle("DataDriven NonPrompt Template")
	legend.Draw("same")
	canvas.SaveAs("DataDriven_templates.pdf")
	canvas.SaveAs("DataDriven_templates.png")

        canvas.Clear()

	stack2.Draw("hist")
        stack2.GetHistogram().GetXaxis().SetTitle("Charge Hadron Isolation")
        stack2.GetHistogram().GetYaxis().SetTitle("Events")
        stack2.GetHistogram().SetTitle("MC Prompt Template")
	legend.Draw("same")
        canvas.SaveAs("MCPrompt_templates.pdf")
	canvas.SaveAs("MCPrompt_templates.png")
        canvas.Clear()

	
	##ratio plot

	ratio = h2.Clone("temp")
	ratio.Divide(stack.GetStack().Last())

        canvasRatio.cd()
        canvasRatio.ResetDrawn()
        canvasRatio.Draw()
        canvasRatio.cd()

        pad1.Draw()
        pad2.Draw()

        pad1.cd()
	
        pad1.Update()
        y2 = pad1.GetY2()


#       stack.SetMinimum(1)
        #    pad1.Update()
        stack.GetXaxis().SetTitle('')
        stack.GetYaxis().SetTitle(h1.GetYaxis().GetTitle())

        stack.SetTitle('')
        stack.GetXaxis().SetLabelSize(0)
        stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
        stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
        stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
        stack.GetYaxis().SetTitle("Events")
        
	stack.Draw('HIST')
        h2.Draw('E,X0,SAME')
        legendR.Draw("same")

        ratio.SetTitle('')

        ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
        ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
        ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
        ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
        ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
#       ratio.GetYaxis().SetRangeUser(0.5,1.5)

        maxRatio = ratio.GetMaximum()
        minRatio = ratio.GetMinimum()
        if maxRatio > 1.8:
                ratio.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
        elif maxRatio < 1:
                ratio.GetYaxis().SetRangeUser(0,1.2)
        elif maxRatio-1 < 1-minRatio:
                ratio.GetYaxis().SetRangeUser((1-(1-minRatio)*1.2),1.1*maxRatio)
        else:
                ratio.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)




	ratio.GetYaxis().SetNdivisions(504)
        ratio.GetXaxis().SetTitle("ChargeHadronIso")
        ratio.GetYaxis().SetTitle("Data/MC")
        #CMS_lumi.CMS_lumi(pad1, 4, 11)

        pad2.cd()

        ratio.SetMarkerStyle(h2.GetMarkerStyle())
        ratio.SetMarkerSize(h2.GetMarkerSize())
        ratio.SetLineColor(h2.GetLineColor())
        ratio.SetLineWidth(h2.GetLineWidth())
        ratio.Draw('e,x0')
	oneLine = TF1("oneline","1",-9e9,9e9)
	oneLine.SetLineColor(kBlack)
	oneLine.SetLineWidth(1)
	oneLine.SetLineStyle(2)

        oneLine.Draw("same")
        #    pad2.Update()
        canvasRatio.Update()
        canvasRatio.RedrawAxis()
        canvasRatio.SaveAs("FitTemplates_ratio.pdf")
        canvasRatio.SaveAs("FitTemplates_ratio.png")
        canvasRatio.SetLogy(0)

        canvas.Close()
        canvasRatio.Close()


newFile = TFile("ChargeHadIso.root","recreate")
process_DD = ["TTGamma_DD","TTbar_DD","VJets_DD","VGamma_DD","SingleTop_DD","Other_DD"]

for p in process_signal:
	HistDict["ChHad"][p].Write("%s"%p)
for p in process_DD:		
	HistDict[o][p].Write("%s_DD"%p)
h1.Write("AntiSIEIE_ChIso_DataMu")
h2.Write("noCut_ChIso_DataMu")
newFile.Close()


def makePseudoData(HistDict,processList,variables,processScales = None):
        print processList
        if processScales==None :processScales = [1.]*len(processList)
        if not len(processList)==len(processScales):
                print "different length of process list and process scales, ignoring scales"
                processScales = [1.]*len(processList)

        for c in variables:
                print c
                HistDict[c]["data_obs"] = HistDict[c][processList[0]].Clone("%s_data_obs"%c)
                HistDict[c]["data_obs"].Scale(processScales[0])
                for p,scale in zip(processList[1:],processScales[1:]):
			print c, p
                        HistDict[c]["data_obs"].Add(HistDict[c][p],scale)
                for b in range(1,HistDict[c]["data_obs"].GetNbinsX()+1):
                        HistDict[c]["data_obs"].SetBinContent(b,int(random.Poisson(HistDict[c]["data_obs"].GetBinContent(b))))
                        HistDict[c]["data_obs"].SetBinError(b,math.sqrt(HistDict[c]["data_obs"].GetBinContent(b)))
        return HistDict




process_templates = {"TTGamma_Prompt":["TTGamma"],
           "TTGamma_DD":["TTGamma"],
           "TTbar_Prompt": ["TTbar"],
           "TTbar_DD": ["TTbar"],
           "VGamma_Prompt":["ZGamma","WGamma"],
           "VGamma_DD":["ZGamma","WGamma"],
           "SingleTop_Prompt":["TGJets", "SingleTop"],
           "SingleTop_DD":["TGJets", "SingleTop"],
           "VJets_Prompt":["WJets", "ZJets"],
           "VJets_DD":["WJets", "ZJets"],
           "Other_Prompt":["TTV", "Diboson"],
           "Other_DD":["TTV", "Diboson"],
        }


all_processtemplates = {"TTGamma_Prompt":["TTGamma"],
           "TTGamma_DD":["TTGamma"],
	   "TTGamma_NonPrompt":["TTGamma"],
           "TTbar_Prompt": ["TTbar"],
           "TTbar_DD": ["TTbar"],
	   "TTbar_NonPrompt": ["TTbar"],
           "VGamma_Prompt":["ZGamma","WGamma"],
           "VGamma_DD":["ZGamma","WGamma"],
	   "VGamma_NonPrompt":["ZGamma","WGamma"],
           "SingleTop_Prompt":["TGJets", "SingleTop"],
           "SingleTop_DD":["TGJets", "SingleTop"],
	   "SingleTop_NonPrompt":["TGJets", "SingleTop"],
           "VJets_Prompt":["WJets", "ZJets"],
           "VJets_DD":["WJets", "ZJets"],
	   "VJets_NonPrompt":["WJets", "ZJets"],
           "Other_Prompt":["TTV", "Diboson"],
           "Other_DD":["TTV", "Diboson"],
	   "Other_NonPrompt":["TTV", "Diboson"],
        }




for c in HistDict:
        if c=="M3_control":
                HistDict = makePseudoData(HistDict,process_control.keys(),["M3_control"])
        if c=="M3":
		HistDict = makePseudoData(HistDict,process_signal.keys(),["M3"])
	if c =="ChHad":
                HistDict = makePseudoData(HistDict,process_templates.keys(),["ChHad"])


outputFile = TFile("Combine_withDDTemplate.root","recreate")
for obs in observables:
        outputFile.mkdir("%s/%s"%(obs,"data_obs"))
        outputFile.cd("%s/%s"%(obs,"data_obs"))
        HistDict[obs]["data_obs"].Write("nominal")
        outputFile.mkdir(obs)
        if obs=="M3_control":
                 for p in process_control.keys():
                         outputFile.mkdir("%s/%s"%(obs,p))
                         outputFile.cd("%s/%s"%(obs,p))
                         HistDict[obs][p].Write("nominal")
                         for sys in systematics:
                                HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                                HistDict_do[obs][p][sys].Write("%sDown"%(sys))
	elif obs=="ChHad":
		for p in all_processtemplates.keys():
                        outputFile.mkdir("%s/%s"%(obs,p))
                        outputFile.cd("%s/%s"%(obs,p))
                        
                        HistDict[obs][p].Write("nominal")
                
                        for sys in systematics:
                                if "_DD" in p :continue
                                print sys,obs,p
                                HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                                HistDict_do[obs][p][sys].Write("%sDown"%(sys))
		
        else:

                for p in process_signal.keys():
                        outputFile.mkdir("%s/%s"%(obs,p))
                        outputFile.cd("%s/%s"%(obs,p))
			
			print obs,p
                        HistDict[obs][p].Write("nominal")
		
                        for sys in systematics:
                               
				print sys,obs,p
                                HistDict_up[obs][p][sys].Write("%sUp"%(sys))
                                HistDict_do[obs][p][sys].Write("%sDown"%(sys))

outputFile.Close()
