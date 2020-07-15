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
padRatio = 0.25
padOverlap = 0.15

padGap = 0.01

parser = OptionParser()

parser.add_option("-c", "--channel", dest="channel", default="ele",type='str',
                  help="Specify which channel mu or ele? default is mu" )
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                     help="Use 4j1t selection" )
parser.add_option("--Tight0b","--tight0b", dest="isTightSelection0b", default=False,action="store_true",
                     help="Use 4j0t selection" )
parser.add_option("--LooseCRe2g1","--looseCRe2g1", dest="isLooseCRe2g1Selection",default=False,action="store_true",
                  help="Use ==2j,>= 1t control region selection" )
parser.add_option("--LooseCRe3g1","--looseCRe3g1", dest="isLooseCRe3g1Selection",default=False,action="store_true",
                  help="Use exactly 3 jets and >=1btag control region selection" )

#parser.add_option("--LooseCRe3g1","--looseCRe3g1", dest="isLooseCRe3g1Selection",default=False,action="store_true",
 #                 help="Use atleats 3j exactly 0t control region selection" )
parser.add_option("--LooseCRe3g0","--looseCRe3g0", dest="isLooseCRe3g0Selection",default=False,action="store_true",
                  help="Use exactly 3j exactly 0t control region selection" )
parser.add_option("--NLO","--NLO", dest="isNLO",default=False,action="store_true",
                  help="Use ZJets NLO sample instead" )
parser.add_option("--onlybarrel","--onlybarrel", dest="isonlybarrel",default=False,action="store_true",
                  help="check only barrel region" )
(options, args) = parser.parse_args()


finalState = options.channel
TightSelection = options.isTightSelection
TightSelection0b = options.isTightSelection0b
isLooseCR2eg1Selection = options.isLooseCRe2g1Selection
isLooseCRe3g1Selection = options.isLooseCRe3g1Selection
#isLooseCR3g0Selection = options.isLooseCR3g0Selection
isNLO=options.isNLO
isLooseCRe3g0Selection=options.isLooseCRe3g0Selection
isonlybarrel=options.isonlybarrel

CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True
H = 600;
W = 800;


# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

if TightSelection:
	dir_="_tight"
	ZJetsSF=1.18019
elif TightSelection0b:
        dir_="_tight0b"
        ZJetsSF=1.10457
elif isLooseCRe3g1Selection:
	dir_="_looseCRe3g1"
#	if isNLO:
#		ZJetsSF=1.069 
#	else:
	ZJetsSF=1.23473#1.309
        bkgZJets_SF=1.
elif isLooseCR2eg1Selection:
	dir_="_looseCRe2g1"
	ZJetsSF=1.26128
	bkgZJets_SF=1
elif isLooseCR3g0Selection:
	dir_="_looseCR3g0"
        ZJetsSF=1.08725
        bkgZJets_SF=1
elif isLooseCRe2g1Selection:
	dir_="_looseCRe2g1"
	ZJetsSF=1.261
	
elif isLooseCRe3g0Selection:
        dir_="_looseCRe3g0"
        ZJetsSF=  1.11696 #1.11341
        bkgZJets_SF=1


print ZJetsSF 
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

bkgZJets_SF=1
if isNLO:
	zjets="_NLO"
else:
	zjets=""
samples ={"TTGamma":[bkgZJets_SF],
	  "TTbar":[bkgZJets_SF],
	  "TTV":[bkgZJets_SF],
          "TGJets":[bkgZJets_SF],
          "SingleTop":[bkgZJets_SF],
          "WJets":[bkgZJets_SF],
          "ZJets%s"%(zjets):[ZJetsSF],
          "WGamma":[bkgZJets_SF],
          "ZGamma":[bkgZJets_SF],
          "Diboson":[bkgZJets_SF],
          "QCD_DD":[bkgZJets_SF],
	}

process=["TTGamma","TTbar","TTV","TGJets","SingleTop","WJets","ZJets%s"%zjets,"WGamma","ZGamma","Diboson"]



for s in samples:
		if isNLO and s=="QCD_DD":
			 _file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s/%s_NLO.root"%(finalState,dir_,s))
		else:
        		_file[s] = TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/%s/hists%s/%s.root"%(finalState,dir_,s))

HistDict={}
misIDEle=1.
bins_=[]


for i in range(25,185,10):
        bins_.append(i)

if isonlybarrel:
	observables={"signal": ["phosel_MassEGamma_MisIDEle_barrel"],
             "bkg"   : ["phosel_MassEGammaOthers_barrel"],
	}
else:
	observables={"signal": ["phosel_MassEGammaMisIDEle"],
	     "bkg"   : ["phosel_MassEGammaOthers"],
	}

from Style import *
thestyle = Style()
thestyle = Style()

thestyle.SetStyle()

ROOT.gROOT.ForceStyle()
gStyle.SetMarkerStyle(1)
if isonlybarrel:
	ZJets_signal = _file["ZJets%s"%zjets].Get("phosel_MassEGamma_MisIDEle_barrel_ZJets%s"%zjets).Clone("ZJets_sig")
	ZJets_bkg = _file["ZJets%s"%zjets].Get("phosel_MassEGammaOthers_barrel_ZJets%s"%zjets).Clone("ZJets_bkg")
else:
	ZJets_signal = _file["ZJets%s"%zjets].Get("phosel_MassEGammaMisIDEle_ZJets%s"%zjets).Clone("ZJets_sig")
	ZJets_bkg = _file["ZJets%s"%zjets].Get("phosel_MassEGammaOthers_ZJets%s"%zjets).Clone("ZJets_bkg")

ZJets_signal.Scale(ZJetsSF)
ZJets_signal=ZJets_signal.Rebin(len(bins_)-1,"",array('d',bins_))

ZJets_bkg.Scale(ZJetsSF)
ZJets_bkg=ZJets_bkg.Rebin(len(bins_)-1,"",array('d',bins_))

err=Double(0.0)
yield_= ZJets_signal.IntegralAndError(-1,-1,err)

print "total ZJets signal:",yield_
print "ZJets signal error:",err



err=Double(0.0)

yield_=ZJets_bkg.IntegralAndError(-1,-1,err)

print "total ZJets bkg:", yield_
print "ZJets bkg error:",err




for obs in observables:
        HistDict[obs]={}
        HistDict[obs]["TTGamma"] = _file["TTGamma"].Get("%s_TTGamma"%(observables[obs][0])).Clone("%s_TTGamma"%(obs))
        for s in process[1:]:
		if "ZJets" in s:continue

                HistDict[obs]["TTGamma"].Add(_file[s].Get("%s_%s"%(observables[obs][0],s)),samples[s][0])
        HistDict[obs]["TTGamma"]=HistDict[obs]["TTGamma"].Rebin(len(bins_)-1,"",array('d',bins_))

err=Double(0.0)
yield_sig = HistDict["signal"]["TTGamma"].IntegralAndError(-1,-1,err)
print "signal not from ZJets", yield_sig,"+/-",err

err=Double(0.0)
yield_bkg = HistDict["bkg"]["TTGamma"].IntegralAndError(-1,-1,err)
print "Bkg not from ZJets", yield_bkg,"+/-",err

for obs in observables:
	HistDict[obs]={}
        HistDict[obs]["TTGamma"] = _file["TTGamma"].Get("%s_TTGamma"%(observables[obs][0])).Clone("%s_TTGamma"%(obs))
	for s in process[1:]:
		
			
		HistDict[obs]["TTGamma"].Add(_file[s].Get("%s_%s"%(observables[obs][0],s)),samples[s][0])
	HistDict[obs]["TTGamma"]=HistDict[obs]["TTGamma"].Rebin(len(bins_)-1,"",array('d',bins_))

				
file_QCD_= TFile("histograms/ele/hists%s/QCD_DD.root"%dir_)
if isonlybarrel:
	h_QCD= file_QCD_.Get("phosel_MassEGamma_barrel_QCD_DD").Clone()
else:
	h_QCD= file_QCD_.Get("phosel_MassEGamma_QCD_DD").Clone()

h_QCD=h_QCD.Rebin(len(bins_)-1,"",array('d',bins_))
HistDict["bkg"]["TTGamma"].Add(h_QCD)			


if finalState=="ele":
	datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/ele/hists%s/DataEle.root"%(dir_))
	if isonlybarrel:
		data =  datafile.Get("phosel_MassEGamma_barrel_DataEle").Clone("DataEle")
	else:
		data =  datafile.Get("phosel_MassEGamma_DataEle").Clone("DataEle")
	
else:
	datafile= TFile("/uscms_data/d3/troy2012/CMSSW_8_0_26_patch1/src/TTGammaSemiLep_13TeV/Plotting/histograms/mu/hists%s/DataMu.root"%(dir_))
        data =  datafile.Get("phosel_MassEGamma_DataMu").Clone("DataMu")
data.Sumw2()
data=data.Rebin(len(bins_)-1,"",array('d',bins_))
#data.GetYaxis().SetRangeUser(0.,700.)
if isonlybarrel:
	outputFile = TFile("Combine_MisIDEle%s%s_barrel.root"%(dir_,zjets),"recreate")
else:
	outputFile = TFile("Combine_MisIDEle%s%s.root"%(dir_,zjets),"recreate")
	
outputFile.mkdir("MisIDEle/data_obs")
outputFile.cd("MisIDEle/data_obs")
data.Write("nominal")
outputFile.mkdir("MisIDEle/signal")
outputFile.cd("MisIDEle/signal")
#print "signal in the root output file:", HistDict["signal"]["TTGamma"].Integral(-1,-1)

HistDict["signal"]["TTGamma"].Write("nominal")
outputFile.mkdir("MisIDEle/bkg")
outputFile.cd("MisIDEle/bkg")
HistDict["bkg"]["TTGamma"].Write("nominal")

legend= TLegend(0.6, 0.65,0.92,0.89)
legend.SetBorderSize(0)
legend.SetFillStyle(0)	

data_= outputFile.Get("MisIDEle/data_obs/nominal")
legend.AddEntry(data_,"Data",'pe')
sig_=outputFile.Get("MisIDEle/signal/nominal")
sig_.SetLineColor(kGreen+3)
sig_.SetMarkerColor(kGreen+3)
sig_.SetLineStyle(9)

bkg_=outputFile.Get("MisIDEle/bkg/nominal")
bkg_.SetLineColor(kBlue)
bkg_.SetMarkerColor(kBlue)
bkg_.SetLineStyle(2)

sum_= outputFile.Get("MisIDEle/signal/nominal")
sum_.Add(outputFile.Get("MisIDEle/bkg/nominal"))
sum_.SetLineColor(kRed)
sum_.SetMarkerColor(kRed)
data.Sumw2()
#data_.GetYaxis().SetRange(0,170)
data_.Draw('E,X0')
data_.SetMarkerStyle(8)
data_.SetMarkerSize(1.0)
data_.SetLineColor(kBlack)
legend.AddEntry(sum_,"Sum",'lp')
legend.AddEntry(sig_,"Z->ee (e to #gamma)",'lp')
legend.AddEntry(bkg_,"Background",'lp')


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

pad1.cd()
data_.GetYaxis().SetTitle("Events")
#data_.Draw('E,X0')



err=Double(0.0)
	
yield_= (float(sig_.IntegralAndError(-1,-1,err)))


print "total signal:",yield_
print "signal error:",err


err2=Double(0.0)


yield2_=(float(bkg_.IntegralAndError(-1,-1,err2)))

print "total bkg:",yield2_ #total_
print "bkg error:",err2 #error


print "signal+bkg:",yield_+yield2_
print "total error:",(err**2+err**2)**0.5

sum_.Draw('hist')
data_.Draw('E,X0,same')
sig_.Draw('hist,same')
bkg_.Draw('hist,same')
legend.Draw("same")
ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
ratio.GetYaxis().SetRangeUser(0.5,1.5)
ratio.GetYaxis().SetNdivisions(504)
ratio.GetXaxis().SetTitle("e+#gamma mass (GeV)")
ratio.GetYaxis().SetTitle("Data/MC")
CMS_lumi.CMS_lumi(pad1, 4, 11)

pad2.cd()
ratio.Draw('e,x0')
oneLine.Draw("same")
canvasRatio.Update()
canvasRatio.RedrawAxis()
CMS_lumi.channelText ="e+jets"
if isonlybarrel:
	canvasRatio.SaveAs("EGamma_prefit%s_barrel%s_ratio.pdf"%(dir_,zjets))
else:
	canvasRatio.SaveAs("EGamma_prefit%s%s_ratio.pdf"%(dir_,zjets))



