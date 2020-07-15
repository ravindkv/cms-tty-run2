from ROOT import *
import math
import os
import sys
from array import array
import CMS_lumi
from Style import *
thestyle = Style()
gStyle.SetOptTitle(0)



from optparse import OptionParser
padRatio = 0.25
padOverlap = 0.15

padGap = 0.01

parser = OptionParser()

parser.add_option("-c", "--channel", dest="channel", default="mu",type='str',
                  help="Specify which channel mu or ele? default is mu" )
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                     help="Use 4j2t selection" )
parser.add_option("--Pseudo","--pseudo", dest="ispseudodata", default=False,action="store_true",
                     help="use pseudo data" )
parser.add_option("--noScale", dest="Rescale",action="store_false",default=True,
                     help="Option to not rescale M3 plots by bin width" )
parser.add_option("--LooseCR2g1","--looseCR2g1", dest="isLooseCR2g1Selection",default=False,action="store_true",
                  help="Use 2j at least 1t control region selection")
parser.add_option("--LooseCR3e0","--looseCR3e0", dest="isLooseCR3e0Selection",default=False,action="store_true",
                  help="Use 3j exactly 0t control region selection" )
parser.add_option("--both","--both", dest="isboth",default=False,action="store_true",
                  help="both endcap+barrel" )
parser.add_option("--others","--others", dest="isothers",default=False,action="store_true",
                  help="other plots" )
(options, args) = parser.parse_args()

ispseudodata=options.ispseudodata
finalState = options.channel
TightSelection = options.isTightSelection
isLooseCR2g1Selection = options.isLooseCR2g1Selection
isLooseCR3e0Selection = options.isLooseCR3e0Selection
isboth=options.isboth
isothers=options.isothers

if isLooseCR3e0Selection:

        dir_ = "_looseCR3e0"
elif isLooseCR2g1Selection:
        dir_ = "_looseCR2g1"
elif TightSelection:
	dir_ = "_tight"
else:
        dir_= ""
thestyle = Style()

thestyle.SetStyle()

ROOT.gROOT.ForceStyle()
gStyle.SetMarkerStyle(1)
import CMS_lumi
H = 600;
W = 800;


# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

if finalState=="mu":
	_channelText ="#mu+jets"
	regionText = ", N_{j}#geq4, N_{b}#geq1"
	Datafile = TFile("histograms/%s/hists%s/DataMu.root"%(finalState,dir_),"read")
        if isboth:
                Datafile = TFile("histograms/%s/hists_endcap%s/DataMu.root"%(finalState,dir_),"read")

	
        
else:	
	_channelText ="e+jets"
	regionText = ", N_{j}#geq4, N_{b}#geq1"
	Datafile = TFile("histograms/%s/hists%s/DataEle.root"%(finalState,dir_),"read")
	if isboth:
		Datafile = TFile("histograms/%s/hists_endcap%s/DataEle.root"%(finalState,dir_),"read")



binsChHad = [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.]


if finalState=="mu":
        systematics = ["JER","JECTotal","phosmear","phoscale","BTagSF","Q2","Pdf","Pdfsignal","PU","MuEff","PhoEff","isr","fsr","MisIDEleshape"]
elif finalState=="ele":
        systematics = ["JER","JECTotal","phosmear","phoscale","BTagSF","Q2","Pdf","Pdfsignal","PU","EleEff","PhoEff","elesmear","elescale","isr","fsr","MisIDEleshape"]
else:
	_channelText ="e/#mu+jets"
	systematics = ["JER","JECTotal","phosmear","phoscale","BTagSF","Q2","Pdf","Pdfsignal","PU","EleEff","MuEff","PhoEff","elesmear","elescale","isr","fsr","MisIDEleshape"]

process_signal = {"TTGamma_Prompt":["t#bar{t}+#gamma Isolated",kOrange],
           "TTGamma_NonPrompt":["t#bar{t}+#gamma Nonprompt",kAzure-4],
           "TTGamma_DD":["t#bar{t}+#gamma Data based",kAzure-4],
           "TTbar_Prompt":["t#bar{t} Isolated",kRed+1],
           "TTbar_NonPrompt": ["t#bar{t} Nonprompt",kAzure],
           "TTbar_DD":["t#bar{t} Data based",kAzure],
           "VGamma_Prompt":["V+#gamma Isolated",kOrange+7],
           "VGamma_NonPrompt":["V+#gamma Nonprompt",kCyan-3],
           "VGamma_DD":["V+#gamma Data based",kCyan-3],
	   "SingleTop_Prompt":["SingleTop Isolated",kOrange+3],
           "SingleTop_NonPrompt":["SingleTop Nonprompt",kBlue-10],
           "ZGamma_DD":["Z+#gamma Data based",kCyan-3],
           "WGamma_Prompt":["W+#gamma Isolated",kOrange+5],
           "WGamma_NonPrompt":["W+#gamma Nonprompt",kCyan-8],
           "WGamma_DD":["W+#gamma Data based",kCyan-1],
           "VJets_Prompt":["V+jets Isolated",kRed-4],
           "VJets_NonPrompt":["V+jets Nonprompt",kCyan+3],
           "VJets_DD":["V+jets Data based",kCyan+3],
           "Other_Prompt":["Other Isolated",kOrange-3],
           "Other_NonPrompt":["Other Nonprompt",kAzure+7],
           "Other_DD":["Other Data based",kAzure+7],
	   "Other":["Other",kGreen+3],
           "VJets":["V+jets",kCyan-3],
	   "VGamma":["V+#gamma",kBlue-4],
           "SingleTop":["SingleTop",kOrange-8],
           "WGamma":["W+#gamma",kBlue-2],
           "TTbar":["t#bar{t}",kRed+1],
	   "TTGamma":["t#bar{t}+#gamma",kOrange],
    
}
observe_={"M3":["phosel_M3_barrel"],
	  "ChHad":["phosel_noCut_ChIso_barrel"],
	  "M3_control":["presel_M3_control"],
	  "btag":["phosel_Njet_barrel"],
	}
observables_AxisTitles = {"M3_control":"0-photon CR",
                          "M3":"M_{3} (GeV)",
                          "ChHad":"Photon charged-hadron isolation (GeV)",
			  "btag":">=4jets,0btag",
                          }

c1 = TCanvas('c1','c1',800,600)
c1.SetFillColor(0)
c1.SetBorderMode(0)
c1.SetFrameFillStyle(0)
c1.SetFrameBorderMode(0)
c1.SetLeftMargin( L/W )
c1.SetRightMargin( R/W )
c1.SetTopMargin( T/H )
c1.SetBottomMargin( B/H )
c1.SetTickx(0)
c1.cd()
c1.ResetDrawn()

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


c1.cd()
c1.ResetDrawn()

CMS_lumi.channelText = _channelText+regionText
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True



if finalState=="ele" or finalState=="mu":
	_file = TFile("Combine_withDDTemplateData_v6_%s%s_binned_PDF.root"%(finalState,dir_),"read")
	if isothers:
		_file=TFile("Otherplots_%s_tight.root"%(finalState),"read")
		if finalState=="mu":
			 TTGammaSF=0.698727
                	 VGammaSF=0.870768
                	 OtherSF=1.15988
                	 TTbarSF=0.98084
                	 HadronicSF=0.989084
		else:
			TTGammaSF=0.634915
			VGammaSF= 0.888617
			TTbarSF= 1.00308
			OtherSF= 0.566907
			HadronicSF= 1.08698
			







else:
	_file =TFile("Combine_semilep.root","read")
#	_file=TFile("Other_combined.root","read")
	_channelText ="e/#mu+jets"

#_file=TFile("Otherplots_mu_tight.root")
ext_=""




print "using file:", _file
if isboth:
	ext_="_all"
	_file =TFile("Combine_withDDTemplateData_v6_%s_tight_all.root"%(finalState),"read")
#print "using file:", _file

MC_signal = ["Other_NonPrompt","VGamma_NonPrompt","TTbar_NonPrompt","TTGamma_NonPrompt","Other_Prompt","VGamma_Prompt","TTbar_Prompt","TTGamma_Prompt"]

MC_control = ["Other","VGamma","TTbar","TTGamma"]

#binned_CR = ["Other_NonPrompt","SingleTop_NonPrompt","VJets_NonPrompt","VGamma_NonPrompt","TTbar_NonPrompt","TTGamma_NonPrompt","Other_Prompt","SingleTop_Prompt","VJets_Prompt","VGamma_Prompt","TTbar_Prompt","TTGamma_Prompt","Other","SingleTop","VJets","VGamma","TTbar","TTGamma"]
process = MC_signal

#print options.Rescale
#exit()
if isothers:
	observe_=["Nbjet","Njet","PhotonEt","PhotonEta"]
for o in observe_:
	#print options.Rescale
	stack = THStack("hs","hs")
        SetOwnership(stack,True)	
	#if o=="CR2" or o=="CR1" or o=="CR0_photon":continue	
	X1=0.45
        if o=="M3_control": X1 = 0.5
	legend= TLegend(X1,0.95-0.07*4-0.1,0.89,0.9)
	legend.SetBorderSize(0)
	legend.SetFillStyle(0)
	#legend.AddEntry(errorband,"Uncertainty","f")
        axisTitle = o
	if o in observables_AxisTitles:
                        axisTitle = observables_AxisTitles[o]
	data = _file.Get("%s/data_obs/nominal"%(o))
#	print _file,"%s/data_obs/nominal"%(o)
	#print o, data.Integral() 

	if o=="M3_control":
		legend.AddEntry(data,"Data",'pe')
                for p in MC_control[::-1]:
                        h1 = _file.Get("%s/%s/nominal"%(o,p))
                        h1.SetFillColor(process_signal[p][1])
                        h1.SetLineColor(process_signal[p][1])
                        legend.AddEntry(h1,process_signal[p][0],'f')
                for p in MC_control:
                        h1 = _file.Get("%s/%s/nominal"%(o,p))
                        h1.SetFillColor(process_signal[p][1])
                        h1.SetLineColor(process_signal[p][1])
                        stack.Add(h1)
	

	else:
		legend.SetNColumns(2)
		legend.AddEntry(data,"Data",'pe')
		legend.AddEntry(None,"",'')
		hName = "TTbar_Prompt"
		histsTemp = []
	      	N=len(MC_signal)
		for i in range(N/2):
			p = MC_signal[N-i-1]
			#print "first:",p
			histsTemp.append(TH1F(p,p,1,0,1))
#                               h1=infile.Get("%s/Postfit_%s_%s"%(obs,obs,hName))
			histsTemp[-1].SetFillColor(process_signal[p][1])
		     	histsTemp[-1].SetLineColor(process_signal[p][1])
	     		legend.AddEntry(histsTemp[-1],process_signal[p][0],'f')

     			p = MC_signal[N/2-i-1]
			#print "second:",p
			histsTemp.append(TH1F(p,p,1,0,1))
#                               h1=infile.Get("%s/Postfit_%s_%s"%(obs,obs,hName))
			histsTemp[-1].SetFillColor(process_signal[p][1])
			histsTemp[-1].SetLineColor(process_signal[p][1])
			legend.AddEntry(histsTemp[-1],process_signal[p][0],'f')

		for p in MC_signal:
			if finalState=="mu" and p=="VJets_Prompt":continue
			print p, "%s/%s/nominal"%(o,p),_file
			h1 = _file.Get("%s/%s/nominal"%(o,p))
			if isothers:
				if "TTGamma" in p:
					h1.Scale(TTGammaSF)
				if "TTbar" in p:
					h1.Scale(TTbarSF)
				if "Other" in p:
					h1.Scale(OtherSF)
				if "VGamma" in p:
					 h1.Scale(VGammaSF)
				if "NonPrompt" in p:
					h1.Scale(HadronicSF)
			h1.SetFillColor(process_signal[p][1])
			h1.SetLineColor(process_signal[p][1])
			if "ChHad" in o:
                        	h1.Scale(1,"width")
			stack.Add(h1)
	oneLine = TF1("oneline","1",-9e9,9e9)
    	oneLine.SetLineColor(kBlack)
    	oneLine.SetLineWidth(1)
    	oneLine.SetLineStyle(2)
	errorband=stack.GetStack().Last().Clone("error")
   
        errorband.SetLineColor(0)
        errorband.SetFillColor(kBlack)
        errorband.SetFillStyle(3245)
        errorband.SetMarkerSize(0)
        legend.AddEntry(errorband,"Uncertainty","f")
        h1_up={}
        h1_do={}
	if o=="M3_control":
                stackList=MC_control
        else:
                stackList=MC_signal
	for p in stackList:
        	 h1_up[p]={}
        	 h1_do[p]={}
		 if o=="ChHad" and "NonPrompt" in p:
			systematics_all=["shapeDD"]
		 else:
			systematics_all=systematics
		 print systematics_all
		 for sys in systematics_all:
			print sys, p
			if sys=="BTagSF" and o=="btag":continue
                        if sys=="MisIDEleshape" and "_Prompt" not in p:continue 
                        if sys=="Q2" or sys=="isr" or sys=="fsr":
                        #	if p not in ["TTbar","TTGamma","TTbar_Prompt","TTbar_NonPrompt","TTGamma_Prompt","TTGamma_NonPrompt"]:continue
				if "VGamma" in p: continue
				if  "Other" in p: continue #p=="VGamma_Prompt" or p=="VGamma_NonPrompt" or p=="Other_NonPrompt" or p=="Other_Prompt":continue
			if sys=="Pdf" and "TTbar" not in p:continue
			#	 if "VGamma" in p: continue
                         #        if "TTGamma" in p:continue
                          #       if "Other" in p:continue
			if sys=="Pdfsignal" and "TTGamma" not in p: continue
                 #                if "VGamma" in p: continue
                  #               if "TTbar" in p:continue
                   #              if "Other" in p:continue
			else:	
                
				print _file, "%s/%s/%sUp"%(o,p,sys) 
                        	h1_up[p][sys]=_file.Get("%s/%s/%sUp"%(o,p,sys)).Clone("%s_%s_up"%(sys,p))
                        	h1_do[p][sys]=_file.Get("%s/%s/%sDown"%(o,p,sys)).Clone("%s_%s_do"%(sys,p))

                		if o=="ChHad":
					h1_do[p][sys].Scale(1,"width")
                        		h1_up[p][sys].Scale(1,"width")

    	error=0.
    	diff={}
    	sum_={}
	
	
	for i_bin in range(1,errorband.GetNbinsX()+1):
		#if o=="ChHad" and "NonPrompt" in p:continue
                sum_[i_bin]=0.
                diff[i_bin]=[]
                for p in stackList:
			if o=="ChHad" and "NonPrompt" in p:
				systematics_all=["shapeDD"]
                 	else:
                        	systematics_all=systematics
			#f "_Prompt" in p:
	                #        systematics_all.append("MisIDEleshape")

                        for sys in systematics_all:
				print sys,p
				if sys=="BTagSF" and o=="btag":continue
			        if sys=="MisIDEleshape" and "_Prompt" not in p:continue	
                                if sys in ["Q2","isr","fsr"]:
					 if "VGamma" in p:continue 
					 if "Other" in p: continue
				if sys=="Pdf":
					if "TTbar" not in p:continue
				if sys=="Pdfsignal" and "TTGamma" not in p: continue
			#		print "doing Pdfsignal",p
			#		if "VGamma" in p: continue
			#		if "TTbar" in p:continue
			#		if "Other" in p:continue
				else:
					print o, p, sys

                                	sum_[i_bin]+=((h1_up[p][sys].GetBinContent(i_bin)-h1_do[p][sys].GetBinContent(i_bin))/2.)**2
		
	
                errorband.SetBinError(i_bin,(sum_[i_bin])**0.5)
	 
        data.Sumw2(True)
	if o=="ChHad":# or o=="M3_control":
        	data.Scale(1,"width")
        maxVal = max(stack.GetMaximum(), data.GetMaximum())
        stack.SetMaximum(1.5*maxVal)
	if "ChHad" in o :
		c1.SetLogy(1)
	else:
		c1.SetLogy(0)
	
        stack.Draw("hist")
	data.SetMarkerStyle(8)
        data.SetMarkerSize(1.0)
	data.SetLineColor(kBlack)
	data.Draw("e,x0,same")
	errorband.Draw('e2,same')
        data.SetMarkerStyle(8)
        data.SetMarkerSize(1.0)
        stack.GetHistogram().GetXaxis().SetTitle("%s"%(axisTitle))
	stack.GetHistogram().GetXaxis().Set
        #stack.GetHistogram().GetYaxis().SetTitle("Events / bin")

	if "ChHad" in o:
        	stack.GetHistogram().GetYaxis().SetTitle("#LT Events / GeV #GT")
	#elif o=="M3":
	#	stack.GetHistogram().GetYaxis().SetTitle("#LT Events / GeV #GT")
	else:
		stack.GetHistogram().GetYaxis().SetTitle("Events / GeV ")
        stack.GetHistogram().SetTitle("%s_Postfit"%(o))
       # legend.Draw("same")
        CMS_lumi.channelText = _channelText+regionText
	if o=="M3_control": CMS_lumi.channelText = _channelText + ", 0-photon"
        CMS_lumi.CMS_lumi(c1, 4, 11)
        legend.Draw("same")
	if ispseudodata:
        	c1.SaveAs("MCDDTemplateswithPseudoData_%s_%s.pdf"%(o,finalState))
	else:
		c1.SaveAs("MCDDTemplateswithData_%s_%s%s_prefit%s.pdf"%(o,finalState,dir_,ext_))
        c1.Clear()
	ratio = data.Clone("data")
        temp = stack.GetStack().Last().Clone("temp")

        for i_bin in range(1,temp.GetNbinsX()+1):
                temp.SetBinError(i_bin,0.)
        ratio.Divide(temp)
	canvasRatio.cd()
        canvasRatio.ResetDrawn()
        canvasRatio.Draw()
        canvasRatio.cd()

        #pad1.Draw()
       # pad2.Draw()

        pad1.cd()
	if o=="ChHad":
        	pad1.SetLogy(1)
	else:
		pad1.SetLogy(0)

        stack.Draw('HIST')
        y2 = pad1.GetY2()


#       stack.SetMinimum(1)
        #    pad1.Update()
        stack.GetXaxis().SetTitle('')
        stack.GetYaxis().SetTitle(data.GetYaxis().GetTitle())

        stack.SetTitle('')
        stack.GetXaxis().SetLabelSize(0)
        stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
        stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
        stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
        if "ChHad" in o:
                stack.GetHistogram().GetYaxis().SetTitle("#LT Events / GeV #GT")
        elif o=="M3":
                stack.GetHistogram().GetYaxis().SetTitle("Events /20  GeV ")
        else:
                stack.GetHistogram().GetYaxis().SetTitle("Events / GeV ")
        data.Draw('E,X0,SAME')
 #       legendR.AddEntry(errorband,"Uncertainty","f")
        #legend.Draw()

        _text = TPaveText(0.42,.75,0.5,0.85,"NDC")
        #_text.AddText(_channelText+"#GT4jets,#GT1btag") 
        _text.SetTextColor(kBlack)
        _text.SetFillColor(0)
        _text.SetTextSize(0.05)
        _text.SetTextFont(42)
        _text.Draw("same")
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
        for i_bin in range(1,ratio.GetNbinsX()):
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


        #maxRatio = 1.5
        #minRatio = 0.5 
        #ratio.GetYaxis().SetRangeUser(0.5,1.5)
        ratio.GetYaxis().SetNdivisions(504)
        #ratio.GetXaxis().SetTitle(plotInfo[0])
        ratio.GetYaxis().SetTitle("Data/MC")
	ratio.GetXaxis().SetTitle("%s"%(axisTitle))
        CMS_lumi.CMS_lumi(pad1, 4, 11)
        legend.Draw("same")
        pad2.cd()
        #for i_bin in range(1,errorband.GetNbinsX()):
        #       errorband.SetBinContent(i_bin,1.)
        maxRatio = 1.5
        minRatio = 0.5
        ratio.SetMarkerStyle(data.GetMarkerStyle())
        ratio.SetMarkerSize(data.GetMarkerSize())
        ratio.SetLineColor(data.GetLineColor())
        ratio.SetLineWidth(data.GetLineWidth())
        ratio.Draw('e,x0')
        errorband.Divide(temp)
        errorband.Draw('e2,same')
        oneLine.Draw("same")
	canvasRatio.Update()
        canvasRatio.RedrawAxis()
        canvasRatio.SaveAs("MCDDTemplateswithData_%s_%s%s_prefit%s_ratio.pdf"%(o,finalState,dir_,ext_))
        #canvasRatio.SaveAs("%s/%s_ratio.png"%(plotDirectory,histName))
        #canvasRatio.Clear()
        canvasRatio.SetLogy(0)
	






	
