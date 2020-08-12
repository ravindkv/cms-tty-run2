#from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, TGraphAsymmErrors
from ROOT import *
import os
import sys
from optparse import OptionParser
from numpy import log10
from array import array
import numpy as np
from PlotInfo_cff import *
from PlotInputs_cff import *
from PlotCMSLumi_cff import *
from PlotTDRStyle_cff import *

padGap = 0.01
setTDRStyle()
xPadRange = [0.0,1.0]
yPadRange = [0.0,0.30-padGap, 0.30+padGap,1.0]
#-----------------------------------------
#INPUT command-line arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-d", "--decay", dest="ttbarDecayMode", default="SemiLep",type='str',
                     help="Specify which decay moded of ttbar SemiLep or DiLep? default is SemiLep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region such as Tight, VeryTight, Tight0b, looseCR2e1, looseCRe2g1")
parser.add_option("--plot", dest="plotList",action="append",
		  help="Add plots" )
parser.add_option("--morePlots","--MorePlots",dest="makeMorePlots",action="store_true",default=False,
                     help="Make larger list of kinematic distributions" )
parser.add_option("--allPlots","--allPlots",dest="makeAllPlots",action="store_true",default=False,
                     help="Make plots of all distributions" )
parser.add_option("--useQCDMC","--qcdMC",dest="useQCDMC", default=False, action="store_true",
		  help="")
(options, args) = parser.parse_args()
year            = options.year
ttbarDecayMode  = options.ttbarDecayMode
channel         = options.channel
CR   = options.CR
plotList        = options.plotList
useQCDMC        = options.useQCDMC
makeMorePlots   = options.makeMorePlots
makeAllPlots    = options.makeAllPlots
#print parser.parse_args()

#-----------------------------------------
#Input & ouput directories
#----------------------------------------
#inputDir = "../Histogramming/hists/%s/%s/%s"%(year, ttbarDecayMode, finalState)
#outputDir = "./plots/%s/%s/%s"%(year, ttbarDecayMode, finalState)
#inputDir = "/home/rverma/t3store/TTGammaSemiLep13TeV/Output/Hists/2016/SemiLep/Mu/Merged"
inputDir = "Merged"
outputDir = "./Plots"
if not os.path.exists(outputDir):
	os.makedirs(outputDir)

#-----------------------------------------
#Hists to be stacked/plotted
#----------------------------------------
gROOT.SetBatch(True)
YesLog = True
NoLog=False
if plotList is None:
    if makeMorePlots:
        plotList = basePlotList 
    elif makeAllPlots:
        plotList = histograms.keys()
        plotList.sort()
    else:
        plotList = otherPlotList
    
#Make dictionary of all the root files
fileDict = {}
for sample in Samples.keys():
    fileName = "%s/%s.root"%(inputDir,sample)
    fileDict[sample] = TFile(fileName, "read")

#-----------------------------------------
#Function to stack histograms and unc band
#-----------------------------------------
def getBaseHists(hName, CR):
    dataHist     = []
    bkgHists     = []
    qcdMCHist    = []
    qcdDDHist    = []
    for sample in Samples.keys():
        if CR=="":
            hPath = "Base/SignalRegion/%s"%(hName)
        else: 
            hPath = "Base/ControlRegion/%s/%s"%(CR, hName)
        hist = fileDict[sample].Get(hPath)
        hist = hist.Clone("%s_%s_%s"%(sample, CR, hName))
        if sample=="Data":
            dataHist.append(hist)
        elif sample=="QCD":
            qcdMCHist.append(hist)
        elif sample=="QCD_DD":
            qcdDDHist.append(hist)
        else:
            bkgHists.append(hist)
    return dataHist, bkgHists, qcdMCHist, qcdDDHist

def getSystHists(hName, CR, level):
    #Get systUp histogram from the file
    bkgHistsSyst     = []
    qcdMCHistSyst    = []
    for syst in Systematics:
        for sample in SamplesSyst:
            if CR=="":
                hPath = "%s%s/SignalRegion/%s"%(syst, level, hName)
            else: 
                hPath = "%s%s/ControlRegion/%s/%s"%(syst, level, CR, hName)
            hist = fileDict[sample].Get(hPath)
            hist = hist.Clone("%s_%s%s_%s_%s"%(sample,syst,level,hName,CR))
            if sample=="QCD":
                qcdMCHistSyst.append(hist)
            else:
                bkgHistsSyst.append(hist)
    #print bkgHistsSyst, qcdMCHistSyst
    return bkgHistsSyst, qcdMCHistSyst

def decoHistStack(hist, xTit, yTit, color):
    hist.SetTitle("");
    hist.GetXaxis().SetTitle(xTit);
    hist.GetYaxis().SetTitle(yTit);
    hist.GetYaxis().SetTitleOffset(1.00);
    hist.GetXaxis().SetTitleOffset(1.00);
    hist.GetYaxis().SetTitleSize(0.10);
    hist.GetXaxis().SetTitleSize(0.10);
    hist.GetXaxis().SetLabelSize(0.10);
    hist.GetYaxis().SetLabelSize(0.10);
    hist.GetXaxis().SetNdivisions(10);
    hist.GetYaxis().SetNdivisions(5);
    hist.GetYaxis().CenterTitle();
    hist.SetFillColor(color);

def decoHistRatio(hist, xTit, yTit, color):
    hist.GetXaxis().SetTitleSize(0.13);
    hist.GetXaxis().SetLabelSize(0.11);
    hist.GetXaxis().SetLabelFont(42);
    hist.GetXaxis().SetLabelColor(kBlack);
    hist.GetXaxis().SetAxisColor(kBlack);
    hist.GetYaxis().SetRangeUser(0.5, 1.5);
    hist.GetXaxis().SetTitleOffset(1);
    hist.GetXaxis().SetLabelOffset(0.01);
    hist.SetMarkerStyle(20); 
    hist.SetMarkerSize(1.2);
    hist.GetYaxis().SetTitleSize(0.13);
    hist.GetYaxis().SetLabelSize(0.11);
    hist.GetYaxis().SetLabelFont(42);
    hist.GetYaxis().SetAxisColor(1);
    hist.GetYaxis().SetNdivisions(6,5,0);
    hist.GetYaxis().SetTitleOffset(0.5);
    hist.GetYaxis().SetLabelOffset(0.01);
    hist.GetYaxis().CenterTitle();

def getUncBand(hBase, hUp, hDown, isRatio):
    yValues     = []
    yErrorsUp   = []
    yErrorsDown = []
    xValues     = []
    xErrorsUp   = []
    xErrorsDown = []
    nBins = hBase.GetNbinsX()
    for i in range(nBins):
        yValue = hBase.GetBinContent(i+1)
        yErrorUp = hUp.GetBinContent(i+1) - hBase.GetBinContent(i+1)
        yErrorDown = hBase.GetBinContent(i+1) - hDown.GetBinContent(i+1)
        if isRatio:
            yValues.append(1)
            if yValue >0:
                yErrorsUp.append(abs(yErrorUp)/yValue)
                yErrorsDown.append(abs(yErrorDown)/yValue)
            else:
                yErrorsUp.append(0.0)
                yErrorsDown.append(0.0)
        else:
            yValues.append (yValue)
            yErrorsUp.append(abs(yErrorUp))
            yErrorsDown.append(abs(yErrorDown))
    
        xValues.append(hBase.GetBinCenter(i+1))
        xErrorsUp.append(hBase.GetBinWidth(i+1)/2)
        xErrorsDown.append(hBase.GetBinWidth(i+1)/2)
    uncGraph = TGraphAsymmErrors( nBins, 
            np.array(yValues    , dtype='double'),
            np.array(yErrorsUp  , dtype='double'),
            np.array(yErrorsDown, dtype='double'),
            np.array(xValues    , dtype='double'),
            np.array(xErrorsUp  , dtype='double'),
            np.array(xErrorsDown, dtype='double'))
    return uncGraph

def getLegend(dataHist, bkgHists, qcdHist, uncGraph):
    legend = TLegend(0.6018792,0.6061504,0.9212081,0.8898861);
    legend.SetNColumns(2);
    legend.SetNColumns(3);
    legend.SetFillStyle(0);
    legend.SetBorderSize(0);
    legend.SetFillColor(kBlack);
    legend.SetTextFont(42);
    legend.SetTextAngle(0);
    legend.SetTextSize(0.03);
    legend.SetTextAlign(12);
    legend.AddEntry(dataHist[0], Samples["Data"][2], "F")
    for bkgHist in bkgHists:
        legendName = Samples[bkgHist.GetName().split("_")[0]][2] 
        legend.AddEntry(bkgHist, legendName, "F")
    legend.AddEntry(qcdHist[0], Samples["QCD"][2], "F")
    legend.AddEntry(uncGraph, "Pre-fit uncertainty","F");
    return legend

def drawHists(hName, CR, useQCDMC, isRatio):
    dataHist, bkgHists, qcdMCHist, qcdDDHist = getBaseHists(hName, CR)
    allBkgHists = qcdMCHist[0].Clone("allBkgHists")
    allBkgHists.Reset()
    hStack = THStack(hName,hName)
    for bkgHist in bkgHists:
        hStack.Add(bkgHist)
        hColor = Samples[bkgHist.GetName().split("_")[0]][1]
        decoHistStack(bkgHist, "Events", hName, hColor)
        allBkgHists.Add(bkgHist)
    if useQCDMC:
        hStack.Add(qcdMCHist[0])
        allBkgHists.Add(qcdMCHist[0])
        decoHistStack(bkgHist, "Events", hName, Samples["QCD"][1])
    else:
        hStack.Add(qcdDDHist[0])
        allBkgHists.Add(qcdDDHist[0])
        decoHistStack(bkgHist, "Events", hName, Samples["QCD"][1])

    #-------------------------------------
    #-------------------------------------
    bkgHistsUp, qcdMCHistUp = getSystHists(hName, CR, "Up")
    bkgHistsDown, qcdMCHistDown = getSystHists(hName, CR, "Down")
    allBkgHistsUp = bkgHistsUp[0].Clone("allBkgHistsUp")
    allBkgHistsUp.Reset()
    for sysUp in bkgHistsUp:
        allBkgHistsUp.Add(sysUp)
    allBkgHistsDown = bkgHistsDown[0].Clone("allBkgHistsDown")
    allBkgHistsDown.Reset()
    for sysDown in bkgHistsDown:
        allBkgHistsDown.Add(sysDown)
    if useQCDMC:
        for qcdSysDown in qcdMCHistDown:
            allBkgHistsDown.Add(qcdMCHistDown[0])
        for qcdSysUp in qcdMCHistUp:
            allBkgHistsUp.Add(qcdMCHistUp[0])
    else:
        allBkgHistsUp.Add(qcdMCHistUp[0])
        allBkgHistsDown.Add(qcdMCHistDown[0])
    uncGraph = getUncBand(allBkgHists, allBkgHistsUp, allBkgHistsDown,False)
    uncGraph.SetFillColor(9);
    uncGraph.SetFillStyle(3008);
    
    #Draw data and stacked histogram
    canvas = TCanvas()
    canvas.Divide(1,2)
    canvas.cd(1)
    gPad.SetRightMargin(0.03);
    gPad.SetPad(xPadRange[0],yPadRange[2],xPadRange[1],yPadRange[3]);
    gPad.SetLogy(True);
    gPad.SetTopMargin(0.09);
    gPad.SetBottomMargin(padGap);
    #gPad.SetTickx(0);
    gPad.RedrawAxis();
    hStack.SetMaximum(1.1*hStack.GetMaximum())
    hStack.Draw("HIST")
    uncGraph.Draw(" E2 same ");
    decoHistStack(dataHist[0], "Events", hName, Samples["Data"][1])
    dataHist[0].SetMarkerStyle(20)
    dataHist[0].Draw("EPsame")
    plotLegend = getLegend(dataHist, bkgHists, qcdDDHist, uncGraph)
    if useQCDMC:
        plotLegend = getLegend(dataHist, bkgHists, qcdMCHist, uncGraph)

    plotLegend.Draw()
    #Draw the ratio of data and all background
    iPeriod = 4;
    iPosX = 10;
    CMS_lumi(canvas, iPeriod, iPosX)
    if isRatio:
        canvas.cd(2)
        gPad.SetTopMargin(padGap); 
        gPad.SetBottomMargin(0.30); 
        gPad.SetRightMargin(0.03);
        #gPad.SetTickx(0);
        gPad.SetPad(xPadRange[0],yPadRange[0],xPadRange[1],yPadRange[2]);
        gPad.RedrawAxis();
        hRatio = dataHist[0].Clone("hRatio")
        hRatio.Divide(allBkgHists)
        decoHistRatio(hRatio, "Events", hName, 1)
        hRatio.Draw()
        canvas.SaveAs("%s/%s.pdf"%(outputDir, hName))
        uncGraph.Draw("same")
        uncGraph = getUncBand(allBkgHists, allBkgHistsUp, allBkgHistsDown,True)
        uncGraph.SetFillColor(9);
        uncGraph.SetFillStyle(3008);
        uncGraph.Draw(" E2 same ");
    canvas.SaveAs("%s.pdf"%hName)

for hName in plotList:
    #drawHists(hName, CR, useQCDMC, False)
    useQCDMC = True
    drawHists(hName, "", useQCDMC,  True)
