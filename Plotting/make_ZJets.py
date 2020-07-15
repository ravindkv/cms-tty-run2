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
H = 600;
W = 800;
padRatio = 0.25
padOverlap = 0.15

padGap = 0.01

# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

parser = OptionParser()

parser.add_option("-c", "--channel", dest="channel", default="mu",type='str',
                  help="Specify which channel mu or ele? default is mu" )
parser.add_option("--Tight","--Tight", dest="isTightSelection",default=False,action="store_true",
                  help="Use 4j exactly 1t control region selection" )
parser.add_option("--Tight0b","--Tight0b", dest="isTightSelection0b",default=False,action="store_true",
                  help="Use 4j exactly 0t control region selection" )
parser.add_option("--LooseCRe3g1","--looseCRe3g1", dest="isLooseCRe3g1Selection",default=False,action="store_true",
                  help="Use 3j exactly 0t control region selection" )
parser.add_option("--LooseCR2g1","--looseCR2g1", dest="isLooseCR2g1Selection",default=False,action="store_true",
                  help="Use 2j at least 1t control region selection")
parser.add_option("--LooseCR2e1","--looseCR2e1", dest="isLooseCR2e1Selection",default=False,action="store_true",
                  help="Use 2j at least 1t control region selection")
parser.add_option("--LooseCR3g0","--looseCR3g0", dest="isLooseCR3g0Selection",default=False,action="store_true",
                  help="Use atleast 3j and 0btag")
parser.add_option("--LooseCRe3g0","--looseCRe3g0", dest="isLooseCRe3g0Selection",default=False,action="store_true",
                  help="Use exactly 3j and 0btag")
parser.add_option("--LooseCRe2g1","--looseCRe2g1", dest="isLooseCRe2g1Selection",default=False,action="store_true",
                  help="Use ==2j and >=1 btag ")
parser.add_option("--NLO","--NLO", dest="isNLO",default=False,action="store_true",
                  help="Use ZJets NLO sample")



(options, args) = parser.parse_args()
TightSelection = options.isTightSelection
TightSelection0b = options.isTightSelection0b
LooseCRe2g1Selection = options.isLooseCRe2g1Selection
LooseCRe3g1Selection = options.isLooseCRe3g1Selection
LooseCR3g0Selection = options.isLooseCR3g0Selection
LooseCRe3g0Selection=options.isLooseCRe3g0Selection

finalState = options.channel
isNLO=options.isNLO


if isNLO:
	zjets="_NLO"
else:
	zjets=""


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
samples =["TTGamma","TTbar","TTV","TGJets","SingleTop","WJets","ZJets%s"%zjets,"WGamma","ZGamma","Diboson"]

if LooseCRe3g1Selection:
	for s in samples:
		_extratext="==3jets,>=1btag"
		ext="e3jets1tag"
        	_file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/dilephists_looseCRe3g1/%s.root"%(finalState,s))

elif LooseCR3g0Selection:
	for s in samples:
		 _extratext=">=3jets,==0btag"
		 ext="loose3jets0b"
		 _file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/dilephists_looseCR3g0/%s.root"%(finalState,s))


elif LooseCRe3g0Selection:
        for s in samples:
                 _extratext="==3jets,==0btag"
                 ext="e3jets0b"
                 _file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/dilephists_looseCRe3g0/%s.root"%(finalState,s))

elif LooseCRe2g1Selection:
        for s in samples:
                 _extratext="==2jets,>=1btag"
                 ext="2jets1tag"
                 _file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/dilephists_looseCRe2g1/%s.root"%(finalState,s))


elif TightSelection:
        for s in samples:
                 _extratext=">=4jets,>=1btag"
                 ext="tight"
                 _file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/dilephists_tight/%s.root"%(finalState,s))

elif TightSelection0b:
        for s in samples:
                 _extratext=">=4jets,0btag"
                 ext="tight0b"
                 _file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/dilephists_tight0b/%s.root"%(finalState,s))

		
else:
	for s in samples:
		 _extratext=">=3jets,>=1btag"
		 ext="g3g1"
                 _file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/dilephists/%s.root"%(finalState,s))

misIDEleSF = 1.
HistDict={}

samples.remove("ZJets%s"%zjets)
bins=[]

observables={"dilep": ["presel_DilepMass",bins],
	}

from Style import *
thestyle = Style()
thestyle = Style()
bins_=[]
for i in range(20,90,10):
	bins_.append(i)

bins_.append(85)
bins_.append(95)

for i in range(100,280,10):
	bins_.append(i)
print bins_
thestyle.SetStyle()

ROOT.gROOT.ForceStyle()
gStyle.SetMarkerStyle(1)

for obs in observables:
	HistDict[obs]={}
        HistDict[obs]["ZJets%s"%zjets]   = _file["ZJets%s"%zjets].Get("%s_ZJets%s"%(observables[obs][0],zjets)).Clone("%s_ZJets"%(obs))
	HistDict[obs]["ZJets%s"%zjets]= HistDict[obs]["ZJets%s"%zjets].Rebin(len(bins_)-1, "",array('d',bins_))
	HistDict[obs]["TTGamma"]   = _file["TTGamma"].Get("%s_TTGamma"%(observables[obs][0])).Clone("%s_TTGamma"%(obs))
	for s in samples[1:]:
		HistDict[obs]["TTGamma"].Add(_file[s].Get("%s_%s"%(observables[obs][0],s)))
	HistDict[obs]["TTGamma"]=HistDict[obs]["TTGamma"].Rebin(len(bins_)-1, "",array('d',bins_))

	
				
			
					

if finalState=="ele":
	_channelText="ee+jets"
	datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/ele/dilephists/DataEle.root")
	if LooseCRe3g1Selection:
		datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/ele/dilephists_looseCRe3g1/DataEle.root")
	elif LooseCR3g0Selection:	
		datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/ele/dilephists_looseCR3g0/DataEle.root")
	elif LooseCRe3g0Selection:
                datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/ele/dilephists_looseCRe3g0/DataEle.root")
	elif LooseCRe2g1Selection:
                datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/ele/dilephists_looseCRe2g1/DataEle.root")
	elif TightSelection:
		datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/ele/dilephists_tight/DataEle.root")
	elif TightSelection0b:
                datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/ele/dilephists_tight0b/DataEle.root")

	data =  datafile.Get("presel_DilepMass_DataEle").Clone("DataEle")
	
else:
	_channelText="#mu#mu+jets"
	datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/mu/dilephists/DataMu.root")
	if LooseCRe3g1Selection:
                datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/mu/dilephists_looseCRe3g1/DataMu.root")
	#elif LooseCR2g1Selection:   
         #       datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/mu/dilephists_looseCR2g1/DataMu.root")
        elif TightSelection:
		datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/mu/dilephists_tight/DataMu.root")
        elif TightSelection0b:
                datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/mu/dilephists_tight0b/DataMu.root")

        data =  datafile.Get("presel_DilepMass_DataMu").Clone("DataMu")
data=data.Rebin(len(bins_)-1,"",array('d',bins_))

CMS_lumi.writeChannelText1 = True
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True
outputFile = TFile("Combine_ZJets_%s_%s%s.root"%(finalState,ext,zjets),"recreate")
	
outputFile.mkdir("dilepmass/data_obs")
outputFile.cd("dilepmass/data_obs")
data.Write("nominal")
outputFile.mkdir("dilepmass/signal")
outputFile.cd("dilepmass/signal")
HistDict["dilep"]["ZJets%s"%zjets].Write("nominal")
outputFile.mkdir("dilepmass/bkg")
outputFile.cd("dilepmass/bkg")
HistDict["dilep"]["TTGamma"].Write("nominal")

legend= TLegend(0.6, 0.65,0.92,0.89)
legend.SetBorderSize(0)
legend.SetFillStyle(0)	

data_= outputFile.Get("dilepmass/data_obs/nominal")
legend.AddEntry(data_,"Data",'pe')
sig_=outputFile.Get("dilepmass/signal/nominal")
sig_.SetLineColor(kGreen+3)
sig_.SetMarkerColor(kGreen+3)
sig_.SetLineStyle(9)
#legend.AddEntry(sig_,"Z+Jets",'lp')

bkg_=outputFile.Get("dilepmass/bkg/nominal")
bkg_.SetLineColor(kBlue)
bkg_.SetMarkerColor(kBlue)
bkg_.SetLineStyle(2)
#legend.AddEntry(bkg_,"Others",'lp')

sum_= outputFile.Get("dilepmass/signal/nominal")
sum_.Add(outputFile.Get("dilepmass/bkg/nominal"))
sum_.SetLineColor(kRed)
sum_.SetMarkerColor(kRed)
legend.AddEntry(sum_,"Sum",'lp')
legend.AddEntry(sig_,"Z+Jets",'lp')
legend.AddEntry(bkg_,"Background",'lp')
#data_.Draw('E,X0')
data_.SetMarkerStyle(8)
data_.SetMarkerSize(1.0)
#sum_.Draw('hist,same')

ratio = data_.Clone("temp")
temp = sum_.Clone("temp_2")

for i_bin in range(1,temp.GetNbinsX()+1):
        temp.SetBinError(i_bin,0.)
ratio.Divide(temp)
canvasRatio.cd()
canvasRatio.ResetDrawn()
canvasRatio.Draw()
canvasRatio.cd()
oneLine = TF1("oneline","1",-9e9,9e9)
oneLine.SetLineColor(kBlack)
oneLine.SetLineWidth(1)
oneLine.SetLineStyle(2)
pad1.Draw()
pad2.Draw()

err=Double(0.0)
yield_ = sig_.IntegralAndError(-1,-1,err)


print "Signal ZJets:",yield_
print "error on ZJets:",err

err=Double(0.0)
yield_ = bkg_.IntegralAndError(-1,-1,err)


print "Bkg:",yield_
print "error on bkg:",err


pad1.cd()
data_.Scale(1.,"width")
sum_.Scale(1.,"width")
sig_.Scale(1.,"width")
bkg_.Scale(1.,"width")
#data_.Draw('E,X0')
data_.GetYaxis().SetTitle("<Events/GeV>")

#sum_.Draw('hist')
data_.Draw('E,X0')
sum_.Draw('hist,same')
sig_.Draw('hist,same')
bkg_.Draw('hist,same')
CMS_lumi.channelText = _channelText
legend.Draw("same")
ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
ratio.GetYaxis().SetRangeUser(0.5,1.5)
ratio.GetYaxis().SetNdivisions(504)
if finalState=="mu":
        ratio.GetXaxis().SetTitle("(#mu^{+},#mu^{-}) invariant mass (GeV)")
else:
        ratio.GetXaxis().SetTitle("(e^{+},e^{-}) invariant mass (GeV)")

ratio.GetYaxis().SetTitle("Data/MC")
CMS_lumi.CMS_lumi(pad1, 4, 11)

pad2.cd()

ratio.Draw('e,x0')
oneLine.Draw("same")

canvasRatio.Update()
canvasRatio.RedrawAxis()
CMS_lumi.channelText = _channelText
canvasRatio.SaveAs("DilepMass_prefit_%s_%s%s_ratio.pdf"%(finalState,ext,zjets))

