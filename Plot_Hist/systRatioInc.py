from ROOT import TFile, TLegend, gPad, gROOT, TCanvas, THStack, TF1, TH1F, TGraphAsymmErrors
import os
import numpy
import sys
import math
from optparse import OptionParser
from PlotInputs import *
from PlotFunc import *
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

print "------------------------------------"
print "%s, %s, %s, %s, %s"%(year, decayMode, channel, sample, hName)
print "------------------------------------"
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
print rootFile
#print("%10s %10s %10s %10s, %10s"%("Systematics", "Down", "Base", "Up", "RelativeUnc"))
print("%10s %22s %22s %22s %10s"%("Syst", "Down", "Base", "Up", "Unc"))
print("%10s %6s %8s %8s %6s %8s %8s %6s %8s %8s %5s"%("", 
"UnderF", "Int", "OverF", 
"UnderF", "Int", "OverF", 
"UnderF", "Int", "OverF", ""))
def checkNanInBins(hist):
    checkNan = False
    for b in range(hist.GetNbinsX()):
        if math.isnan(hist.GetBinContent(b)):
            print "%s: bin %s is nan"%(hist.GetName(), b)
            checkNan = True
    return checkNan
            
allHistUp = []
allHistDown = []
allSystPercentage = {}
for index, syst in enumerate(Systematics):
    if CR=="":
        hPathBase = "%s/Base/SR/%s"%(sample, hName)
        hPathUp   = "%s/%sUp/SR/%s"%(sample, syst, hName)
        hPathDown   = "%s/%sDown/SR/%s"%(sample, syst, hName)
    else:
        hPathBase = "%s/Base/CR/%s/%s"%(sample, CR, hName)
        hPathUp   = "%s/%sUp/CR/%s/%s"%(sample, syst, CR, hName)
        hPathDown   = "%s/%sDown/CR/%s/%s"%(sample, syst, CR, hName)
    hBase_ = rootFile.Get(hPathBase).Clone("Base_")
    hUp_   = rootFile.Get(hPathUp).Clone("%sUp_"%syst) 
    hDown_ = rootFile.Get(hPathDown).Clone("%sDown_"%syst) 
    evtBase = hBase_.Integral()
    evtUp   = hUp_.Integral()
    evtDown = hDown_.Integral()
    #check if intergal is 0
    #if evtUp ==0.0 or evtBase ==0.0 or evtDown ==0.0:
    #i = integral, u = undeflow, o = overflow
    iEvtBase = round(hBase_.Integral(),0)
    iEvtUp   = round(hUp_.Integral(),0)
    iEvtDown = round(hDown_.Integral(),0)
    uEvtBase = round(hBase_.GetBinContent(0),0)
    uEvtUp   = round(hUp_.GetBinContent(0),0)
    uEvtDown = round(hDown_.GetBinContent(0),0)
    oEvtBase = round(hBase_.GetBinContent(hBase_.GetNbinsX()+1),0)
    oEvtUp   = round(hUp_.GetBinContent(hUp_.GetNbinsX()+1),0)
    oEvtDown = round(hDown_.GetBinContent(hDown_.GetNbinsX()+1),0)
    if uEvtBase >1000 or oEvtBase >1000:
        print "%s: Base:  Overflow or Undeflow is more than 1000"%syst
    if uEvtUp >1000 or oEvtUp >1000:
        print "%s: Up:  Overflow or Undeflow is more than 1000"%syst
    if uEvtDown >1000 or oEvtDown >1000:
        print "%s: Down:  Overflow or Undeflow is more than 1000"%syst
    if evtBase ==0.0:
        print "evtBase is zero"
        continue
    #check if intergal is NaN
    if math.isnan(evtUp) or math.isnan(evtDown):
        print "Inegral is nan"
        continue
    #check if bins are nan
    if checkNanInBins(hUp_) or checkNanInBins(hBase_) or checkNanInBins(hDown_):
        print "Some of the bins are nan"
        continue
    allSystPercentage[syst] = 100*max(abs(evtUp -evtBase),abs(evtBase-evtDown))/evtBase
    print("%10s" 
           "|%6.0f %8.0f %8.0f"
           "|%6.0f %8.0f %8.0f"
           "|%6.0f %8.0f %8.0f"
           "|%5.0f%%"%(syst, 
         uEvtDown, iEvtDown, oEvtDown, 
         uEvtBase, iEvtBase, oEvtBase, 
         uEvtUp, iEvtUp, oEvtUp,
        allSystPercentage[syst]))
    if allSystPercentage[syst] > 100.0:
        print "Large uncertainty for %s: %10.2f"%(syst, allSystPercentage[syst])
    xAxis = hBase_.GetXaxis()
    lowBinEdge = xAxis.GetBinLowEdge(1)
    upBinEdge = xAxis.GetBinUpEdge(hBase_.GetNbinsX())
    #print lowBinEdge, upBinEdge
    newWidth = int((upBinEdge - lowBinEdge)/20)
    if int(newWidth) ==0: 
        newWidth = 1
    newBins = numpy.arange(lowBinEdge,upBinEdge,newWidth)
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
    decoHistRatio(hRatioUp, hName, "#frac{SystUp}{Nominal} (solid), #frac{SystDown}{Nominal} (dashed)", myColor)
    hRatioUp.GetXaxis().SetTitleSize(0.05)
    hRatioUp.GetXaxis().SetLabelSize(0.05)
    hRatioUp.GetYaxis().SetTitleSize(0.045)
    hRatioUp.GetYaxis().SetLabelSize(0.05)
    #hRatioUp.GetYaxis().SetRangeUser(0.1, 2)
    hRatioUp.GetYaxis().SetTitleOffset(1.0)
    hRatioUp.SetMarkerStyle(index)
    hRatioUp.SetLineWidth(2)
    #Ratio Down
    hRatioDown = hDown.Clone(syst)
    hRatioDown.Divide(hBase)
    decoHistRatio(hRatioDown, hName, "#frac{SystUp}{Nominal} (solid), #frac{SystDown}{Nominal} (dashed)", myColor)
    hRatioDown.SetLineStyle(2)
    hRatioDown.SetLineWidth(2)
    hRatioDown.SetMarkerStyle(index)
    allHistUp.append(hRatioUp)#Don't comment
    allHistDown.append(hRatioDown)#Don't comment

#Draw Leg
leg = TLegend(0.13,0.15,0.93,0.28)
decoLegend(leg, 5, 0.034)
allHistUpSorted = sortHists(allHistUp, True)
maxRatio = []
for h in allHistUpSorted:
    ratio = []
    for i in range(h.GetNbinsX()):
        ratio.append(round(h.GetBinContent(i),2))
    maxRatio.append(max(ratio))
    #print h.GetName(), ratio
yMax = max(maxRatio)
for i, h in enumerate(allHistUpSorted):
    h.GetYaxis().SetRangeUser(1-yMax, 1+yMax)
    systPercentage = int(round(allSystPercentage[h.GetName()]))
    legName = "%s (%s%%)"%(h.GetName(), str(systPercentage))
    leg.AddEntry(h, legName, "L")
    if(i==0):
        h.Draw("hist")
    else:
        h.Draw("hist same")
    allHistDown[i].Draw("hist same")
leg.Draw("same")

#Draw CMS, Lumi, channel
if channel in ["mu", "Mu", "m"]:
    chName = "mu + jets"
else:
    chName = "e + jets"
crName = formatCRString(CR)
if CR=="":
    chName = "%s, SR"%chName
else:
    chName = "%s, CR"%chName
nBase = "#font[42]{%s, Nominal Events = %s}"%(sample, str(int(round(evtBase))))
chCRName = "#font[42]{%s (%s)}"%(chName, crName)
extraText   = "#splitline{Preliminary, %s}{%s}"%(chCRName, nBase)

lumi_13TeV = "35.9 fb^{-1}"
if "16" in year:
    lumi_13TeV = "35.9 fb^{-1} (2016)"
if "17" in year:
    lumi_13TeV = "41.5 fb^{-1} (2017)"
if "18" in year:
    lumi_13TeV = "59.7 fb^{-1} (2018)"
CMS_lumi(lumi_13TeV, canvas, iPeriod, iPosX, extraText)
#Draw Baseline
baseLine = TF1("baseLine","1", -100, 2000);
baseLine.SetLineColor(1);
baseLine.Draw("same");

#canvas.SaveAs("%s/%s.pdf"%(outPlotFullDir, hName))
#canvas.SaveAs("SystRatio_%s_%s_%s_%s_%s_%s.pdf"%(year, decayMode, channel, hName, sample, CR))
