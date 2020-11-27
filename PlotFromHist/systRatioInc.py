from ROOT import TFile, TLegend, gPad, gROOT, TCanvas, THStack, TF1, TH1F, TGraphAsymmErrors
import os
import numpy
import sys
from optparse import OptionParser
from PlotFunc import *
from PlotInputs import *
from PlotCMSLumi import *
from PlotTDRStyle import *


padGap = 0.01
iPeriod = 4;
iPosX = 10;
setTDRStyle()
xPadRange = [0.0,1.0]
yPadRange = [0.0,0.30-padGap, 0.30+padGap,1.0]

#-----------------------------------------
#INPUT command-line arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-d", "--decayMode", dest="decayMode", default="Semilep",type='str',
                     help="Specify which decayMode moded of ttbar SemiLep or DiLep? default is SemiLep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s", "--sample", dest="sample", default="TTGamma",type='str',
		  help="name of the MC sample" )
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--hist", "--hist", dest="hName", default="phosel_M3",type='str', 
                     help="name of the histogram")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
sample          = options.sample
hName            = options.hName
CR              = options.CR

#-----------------------------------------
#Path of the I/O histrograms/plots
#----------------------------------------
inHistSubDir = "Hists/%s/%s/%s/Merged"%(year, decayMode, channel)
inHistFullDir = "%s/%s"%(condorHistDir, inHistSubDir)
if CR=="":
    outPlotSubDir = "Plots/Syst/%s/%s/%s/SR"%(year, decayMode, channel)
else:
    outPlotSubDir = "Plots/%s/Syst/%s/%s/CR/%s"%(year, decayMode, channel, CR)
outPlotFullDir = "%s/%s"%(condorHistDir, outPlotSubDir)
if not os.path.exists(outPlotFullDir):
    os.makedirs(outPlotFullDir)

gROOT.SetBatch(True)
canvas = TCanvas("ImpactOfSyst", "ImpactOfSyst", 1600, 1000)
canvas.cd()
gPad.SetRightMargin(0.03);
gPad.SetTopMargin(0.09);
gPad.SetLeftMargin(0.11);
#gPad.SetBottomMargin(0.30);
#gPad.SetTickx(0);
#gPad.SetLogy(True);
gPad.RedrawAxis();
rootFile = TFile("%s/%s.root"%(inHistFullDir,sample), "read")
print("Systematics, \tDown, \tBase, \tUp")
allHistUp = []
allHistDown = []
for index, syst in enumerate(Systematics):
    if CR=="":
        hPathBase = "%s/Base/SR/%s"%(sample, hName)
        hPathUp   = "%s/%sUp/SR/%s"%(sample, syst, hName)
        hPathDown   = "%s/%sDown/SR/%s"%(sample, syst, hName)
    else:
        hPathBase = "%s/Base/CR/%s/%s"%(sample, CR, hName)
        hPathUp   = "%s/%sUp/CR/%s/%s"%(sample, syst, CR, hName)
        hPathDown   = "%s/%sDown/CR/%s/%s"%(sample, syst, CR, hName)
    hBase_ = rootFile.Get(hPathBase) 
    hUp_   = rootFile.Get(hPathUp) 
    hDown_ = rootFile.Get(hPathDown) 
    print("%10s %10.2f %10.2f %10.2f"%(syst, 
        round(hDown_.Integral(),2), 
        round(hBase_.Integral(),2), 
        round(hUp_.Integral(),2)
        ))
    xAxis = hBase_.GetXaxis()
    lowBinEdge = xAxis.GetBinLowEdge(1)
    upBinEdge = xAxis.GetBinUpEdge(hBase_.GetNbinsX())
    nBins = int((upBinEdge - lowBinEdge)/30)
    if nBins < 10: 
        nBins = upBinEdge -lowBinEdge
    newBins = numpy.arange(lowBinEdge,upBinEdge,nBins)
    newBins = numpy.concatenate([newBins, [upBinEdge]])
    hBase = hBase_.Rebin(len(newBins)-1, "RebinnedBase", newBins)
    hUp = hUp_.Rebin(len(newBins)-1, "RebinnedUp", newBins)
    hDown = hDown_.Rebin(len(newBins)-1, "RebinnedDown", newBins)
    #Ratio Up
    hRatioUp = hUp.Clone(syst)
    hRatioUp.Divide(hBase)
    myColor = index+2
    if myColor >9:
        myColor = 32+index
    decoHistRatio(hRatioUp, hName, "#frac{Up}{Nominal} (solid), #frac{Down}{Nominal} (dashed)", myColor)
    hRatioUp.GetXaxis().SetTitleSize(0.05)
    hRatioUp.GetXaxis().SetLabelSize(0.05)
    hRatioUp.GetYaxis().SetTitleSize(0.05)
    hRatioUp.GetYaxis().SetLabelSize(0.05)
    #hRatioUp.GetYaxis().SetRangeUser(0.1, 2)
    hRatioUp.GetYaxis().SetTitleOffset(1.0)
    hRatioUp.SetMarkerStyle(index)
    hRatioUp.SetLineWidth(2)
    #Ratio Down
    hRatioDown = hDown.Clone(syst)
    hRatioDown.Divide(hBase)
    decoHistRatio(hRatioDown, hName, "#frac{Up}{Nominal} (solid), #frac{Down}{Nominal} (dashed)", myColor)
    hRatioDown.SetLineStyle(2)
    hRatioDown.SetLineWidth(2)
    hRatioDown.SetMarkerStyle(index)
    allHistUp.append(hRatioUp)#Don't comment
    allHistDown.append(hRatioDown)#Don't comment

#Draw Leg
leg = TLegend(0.20,0.15,0.92,0.28)
decoLegend(leg, 5, 0.05)
allHistUpSorted = sortHists(allHistUp, True)
maxRatio = []
for h in allHistUpSorted:
    ratio = []
    for i in range(h.GetNbinsX()):
        ratio.append(h.GetBinContent(i))
    maxRatio.append(max(ratio))
yMax = max(maxRatio)
for i, h in enumerate(allHistUpSorted):
    h.GetYaxis().SetRangeUser(1-yMax, 1+yMax)
    leg.AddEntry(h, h.GetName(), "L")
    if(i==0):
        h.Draw("hist")
    else:
        h.Draw("hist same")
    allHistDown[i].Draw("hist same")
leg.Draw("same")

#Draw CMS, Lumi, channel
if channel in ["mu", "Mu", "m"]:
    chName = "%s, #mu + jets"%sample
else:
    chName = "%s, e + jets"%sample
crName = formatCRString(CR)
if CR=="":
    chName = "%s, SR"%chName
else:
    chName = "%s, CR"%chName
chCRName = "#font[42]{%s}, #font[42]{%s}"%(chName, crName)
extraText   = "Preliminary, %s"%chCRName
CMS_lumi(canvas, iPeriod, iPosX, extraText)
#Draw Baseline
baseLine = TF1("baseLine","1", -100, 2000);
baseLine.SetLineColor(1);
baseLine.Draw("same");

#canvas.SaveAs("%s/%s.pdf"%(outPlotFullDir, hName))
canvas.SaveAs("%s_SystRatio_%s.pdf"%(hName, sample))

