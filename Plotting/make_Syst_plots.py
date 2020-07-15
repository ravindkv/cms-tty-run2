from ROOT import TFile, TPad, gROOT, gStyle, TCanvas, SetOwnership, TLegend, kBlack, kRed, kBlue, TF1
import math
import os
import sys
from array import array
import CMS_lumi
from Style import *
from optparse import OptionParser
from Quiet import Quiet

gROOT.SetBatch(True)

parser = OptionParser()
    
parser.add_option("-c", "--channel", dest="channel", default="mu",type='str',
                  help="Specify which channel mu or ele? default is mu" )
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                     help="Use 4j2t selection" )

(options, args) = parser.parse_args()

TightSelection = options.isTightSelection



finalState = options.channel
thestyle = Style()

thestyle.SetStyle()

ROOT.gROOT.ForceStyle()
# gStyle.SetOptTitle(0)
# gStyle.SetOptStat(0)
gStyle.SetMarkerStyle(1)


process_signal = {"TTGamma_Prompt":["t#bar{t}+#gamma Prompt"],
		  "TTGamma_NonPrompt":["t#bar{t}+#gamma Nonprompt"],
		  "TTbar_Prompt": ["t#bar{t} Prompt"],
		  "TTbar_NonPrompt": ["t#bar{t} Nonprompt"],
		  "VGamma_Prompt":["V+#gamma Prompt"],
		  "VGamma_NonPrompt":["V+#gamma Nonprompt"],
		  "VJets_Prompt":["V+jets Prompt"],
		  "VJets_NonPrompt":["V+jets Nonprompt"],
		  "Other_Prompt":["Other Prompt"],
		  "Other_NonPrompt":["Other Nonprompt"],
		  "Other":["Other"],
		  "VJets":["V+jets"],
		  "VGamma":["V+#gamma"],
		  "TTbar":["t#bar{t}"],
		  "TTGamma":["t#bar{t}+#gamma"],
		  "TTbar_DD":["t#bar{t} DataDriven"],
		  }

import CMS_lumi
H = 600;
W = 800;


# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W
observe_={"M3":["M3 GeV"],
	"ChHad":["Photon Charge Hadron Isolation (GeV)"],
	"M3_control":["M3 (GeV)"],
	}

c1 = TCanvas('c1','c1',W,H)
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

c2 = TCanvas('c2','c2',W,H)
c2.SetFillColor(0)
c2.SetBorderMode(0)
c2.SetFrameFillStyle(0)
c2.SetFrameBorderMode(0)
c2.SetLeftMargin( L/W )
c2.SetRightMargin( R/W )
c2.SetTopMargin( T/H )
c2.SetBottomMargin( B/H )
c2.SetTickx(0)
c2.SetTicky(0)
c2.Draw()
c2.cd()



padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
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

c2.cd()
pad1.Draw()
pad2.Draw()

SetOwnership(pad1,False)
SetOwnership(pad2,False)

if finalState=="ele":
	_file = TFile("Combine_withDDTemplateData_v2_ele.root","read")
        if TightSelection :
		_file = TFile("Combine_withDDTemplate_v2_ele_tight.root","read")
else:
	_file = TFile("Combine_withDDTemplateData_v2_mu.root","read")
	if TightSelection :
                _file = TFile("Combine_withDDTemplate_v2_mu_tight.root","read")
MC_signal = ["TTbar_Prompt","TTbar_NonPrompt","TTGamma_Prompt","TTGamma_NonPrompt","VGamma_Prompt","VGamma_NonPrompt","VJets_Prompt","VJets_NonPrompt","Other_Prompt","Other_NonPrompt"]
MC_control =["TTGamma","TTbar","VGamma","VJets","Other"]

process = MC_signal
if finalState=="mu":
	systematics = {"JER"     :["JER"],
		       "phosmear":["Photon scale"],
		       "phoscale":["Photon smear"],
		       "BTagSF"  :["BTag SF"],
		       "Q2"     :["Q2"],
		       "Pdf"    :["PDF"],
		       "PU" :["Pileup"],
		       "MuEff"  :["Muon Eff"],
		       "PhoEff" :["Photon Eff"],
		       "JECTotal": ["JEC Total"],
		       "JECSubTotalRelative" :["JEC Relative SubTotal"],
                       "JECSubTotalScale" : ["JEC Scale SubTotal"],
                       "JECSubTotalPt" :["JEC Pt SubTotal"],
                       "JECSubTotalPileUp" : ["JEC PileUp SubTotal"], 
                       "JECSubTotalMC" : ["JEC MC SubTotal"],
                       "JECSubTotalAbsolute" : ["JEC Absolute SubTotal"],   	
		       "isr":["ISR"],
		       "fsr":["FSR"],
		       "shapeDD":["Shape unc"],
		       }
	_channelText = "#mu+jets"

else:
	systematics = {"JER"     :["JER"],
		       "phosmear":["Photon scale"],
		       "phoscale":["Photon smear"],
		       "elesmear":["Electron scale"],
		       "elescale":["Electron smear"],
		       "BTagSF"  :["BTag SF"],
		       "Q2"     :["Q2"],
		       "Pdf"    :["PDF"],
		       "PU" :["Pileup"],
		       "EleEff" :["Electron Eff"],
		       "PhoEff" :["Photon Eff"],
		       "JECTotal": ["JEC Total"],
		       "JECSubTotalRelative" :["JEC Relative SubTotal"],
                       "JECSubTotalScale" : ["JEC Scale SubTotal"],
                       "JECSubTotalPt" :["JEC Pt SubTotal"],
                       "JECSubTotalPileUp" : ["JEC PileUp SubTotal"],
                       "JECSubTotalMC" : ["JEC MC SubTotal"],
                       "JECSubTotalAbsolute" : ["JEC Absolute SubTotal"],
		       "isr":["ISR"],
		       "fsr":["FSR"],
		       "shapeDD":["Shape unc"],
		       }
	_channelText = "e+jets"

CMS_lumi.channelText = _channelText
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True

#Signal =["TTGamma_Prompt","TTGamma_NonPrompt"]
#M3_control =["TTGamma"]

#process2=Signal


legend= TLegend(0.55, 0.69,0.89,0.89)
legend.SetBorderSize(0);
legend.SetFillStyle(0);

oneline = TF1("oneline","1",0,9e9)
oneline.SetLineColor(kBlack)
oneline.SetLineStyle(2)
for o in observe_:
	
	if o=="M3_control":
		process = MC_control
	else:
		process = MC_signal
		
		
	for p in process:
		if finalState=="mu" and "VJets_Prompt" in p:continue
		# print _file
		# print "%s/%s/nominal"%(o,p)		
		if o=="ChHad" and "NonPrompt" in p:
			systematics_use=["shapeDD"]
		else:
			systematics_use=systematics
		#if "TTbar_DD" in p and "ChHad" not in o:continue
		print  _file, "%s/%s/nominal"%(o,p)
                nominal = _file.Get("%s/%s/nominal"%(o,p))
	#	if "M3" in o:
		nominal.Scale(1.,"width")
		nominal.SetLineColor(kBlack)
		nominal.SetLineWidth(2)
		nominal.SetMarkerColor(kBlack)
                
		for sys in systematics_use:
			c1.Draw()
			c1.cd()
			if sys in ["isr","fsr","Q2","Pdf"] :
				print sys, p
				
				if p not in ["TTbar_Prompt","TTGamma_Prompt","TTbar_NonPrompt","TTGamma_NonPrompt","TTbar","TTGamma"] :continue
					
				
			if sys=="shapeDD" and "M3" in o: continue
			if sys=="shapeDD" and o=="ChHad" and "NonPrompt" not in p:continue
			
			

			up =  _file.Get("%s/%s/%sUp"%(o,p,sys))
			do =  _file.Get("%s/%s/%sDown"%(o,p,sys))
			#if "M3" in o:
				#print "%s/%s/%sUp"%(o,p,sys)
				#print "%s/%s/%sDown"%(o,p,sys)
			print "%s/%s/%sUp"%(o,p,sys)
			up.Scale(1.,"width")
			do.Scale(1.,"width")
			print o,p,sys	
			_max = max(up.GetMaximum(), do.GetMaximum(), nominal.GetMaximum())


			ratioUp = up.Clone("ratio_up")
			ratioDo = do.Clone("ratio_do")

			ratioUp.Divide(nominal)
			ratioDo.Divide(nominal)

			_ratiomax = max(ratioUp.GetMaximum(),ratioDo.GetMaximum())
			_ratiomin = min(ratioUp.GetMinimum(),ratioDo.GetMinimum())
#			_ratiomax=1.1
#			_ratiomin=0.9			

			up.SetMaximum(_max*1.4)

			up.SetLineWidth(2)
			up.SetLineColor(kRed)
			up.SetMarkerColor(kRed)
			up.Draw("hist")
			up.GetXaxis().SetTitle("%s"%(observe_[o][0]))
			up.GetYaxis().SetTitle("#LT Events / GeV #GT")

			do.SetLineStyle(1)
                        do.SetLineWidth(2)
			do.SetLineColor(kBlue)
			do.SetMarkerColor(kBlue)
			do.Draw("hist,same")
			nominal.Draw("E0,hist,same")		

			legend.Clear()

			legend.SetHeader("%s"%(process_signal[p][0]))
			legend.AddEntry(up,"%s"%(systematics[sys][0])+" "+"Up",'lp')
			legend.AddEntry(nominal,"Nominal",'lp')
                        legend.AddEntry(do,"%s"%(systematics[sys][0])+" "+"Down",'lp')

        		legend.Draw("same")
  			CMS_lumi.channelText = _channelText      	
        		CMS_lumi.CMS_lumi(c1, 4, 11)

#        		Quiet(c1.SaveAs)("Systematics_1/%s_%s_%s_%s.pdf"%(o,p,sys,finalState))
 #       		c1.Clear()

			c2.cd()
			c2.ResetDrawn()
			c2.Draw()
			c2.cd()
#			if :
#				c2.SetLogy(1)
#			else:
#3				c2.SetLogy(0)
		#	if sys=="shapeDD":
		#		print "it is!!"
		#		c2.SetLogy()
			pad1.Draw()
			pad2.Draw()
			
			pad1.cd()

			_ratiomax = 1+1.1*(_ratiomax-1)
			_ratiomin = 1-1.1*(1-_ratiomin)
			ratioUp.SetMaximum(_ratiomax)
			ratioUp.SetMinimum(_ratiomin)


			ratioUp.SetTitle('')
			ratioUp.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
			ratioUp.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
			ratioUp.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
			ratioUp.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))

			ratioUp.GetYaxis().SetTitle("Rel. Change")
			ratioUp.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-0.02))
			ratioUp.GetYaxis().CenterTitle()
			ratioUp.GetXaxis().SetTitle(up.GetXaxis().GetTitle())

			up.GetXaxis().SetTitle('')
			up.SetTitle('')
			up.GetXaxis().SetLabelSize(0)
			up.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
			up.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
			up.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))


			ratioUp.GetYaxis().SetNdivisions(504)

			ratioUp.SetLineColor(kRed)
			ratioDo.SetLineColor(kBlue)
			if o=="ChHad":
               #                 print "it is!!"
                                pad1.SetLogy(1)
			else:
				pad1.SetLogy(0)
				
			up.Draw("hist")
			do.Draw("hist,same")
			nominal.Draw("E0,hist,same")
			legend.Draw("same")

  			CMS_lumi.channelText = _channelText      	
        		CMS_lumi.CMS_lumi(c2, 4, 11)

			pad2.cd()
                        
			ratioUp.Draw("hist")
			ratioDo.Draw("hist,same")
			oneline.Draw("same")
			
				
        		Quiet(c2.SaveAs)("Systematics_M3shape/%s_%s_%s_%s_ratio.pdf"%(o,p,sys,finalState))
