#from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, TGraphAsymmErrors
from ROOT import *
import os
import sys
from optparse import OptionParser
import numpy as np
from PlotInfo_cff import *
from PlotInputs_cff import *
from PlotCMSLumi_cff import *
from PlotTDRStyle_cff import *

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
parser.add_option("-d", "--decayMode", dest="decayMode", default="SemiLep",type='str',
                     help="Specify which decayMode moded of ttbar SemiLep or DiLep? default is SemiLep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--plot", dest="plotList",action="append",
		  help="Add plots" )
parser.add_option("--morePlots","--MorePlots",dest="makeMorePlots",action="store_true",default=False,
                     help="Make larger list of kinematic distributions" )
parser.add_option("--allPlots","--allPlots",dest="makeAllPlots",action="store_true",default=False,
                     help="Make plots of all distributions" )
parser.add_option("--isQCDMC","--qcdMC",dest="isQCDMC", default=False, action="store_true",
		  help="")
(options, args) = parser.parse_args()
year            = options.year
decayMode  = options.decayMode
channel         = options.channel
CR   = options.CR
plotList        = options.plotList
isQCDMC        = options.isQCDMC
makeMorePlots   = options.makeMorePlots
makeAllPlots    = options.makeAllPlots

#-----------------------------------------
#Path of the I/O histrograms/plots
#----------------------------------------
inHistSubDir = "Hists/%s/%s/%s/Merged"%(year, decayMode, channel)
inHistFullDir = "%s/%s"%(condorHistDir, inHistSubDir)
if CR=="":
    outPlotSubDir = "Plots/%s/%s/%s/SR"%(year, decayMode, channel)
else:
    outPlotSubDir = "Plots/%s/%s/%s/CR/%s"%(year, decayMode, channel, CR)
outPlotFullDir = "%s/%s"%(condorHistDir, outPlotSubDir)
if not os.path.exists(outPlotFullDir):
    os.makedirs(outPlotFullDir)

fileDict = {}
for sample in Samples.keys():
    fileName = "%s/%s.root"%(inHistFullDir,sample)
    fileDict[sample] = TFile(fileName, "read")

#-----------------------------------------
#Hists to be stacked/plotted
#----------------------------------------
gROOT.SetBatch(True)
if plotList is None:
    if makeMorePlots:
        plotList = basePlotList 
    elif makeAllPlots:
        plotList = histograms.keys()
        plotList.sort()
    else:
        plotList = otherPlotList
    
#-----------------------------------------
#Get historgams from the root files 
#-----------------------------------------
def getBaseHists(hName, CR):
    '''
    Get nomninal histograms from all samples
    in form of an array. Since we make a 
    choice betweeen MC and DD QCD, we store 
    these histogs separately. Note that data
    and qcd arrays has only one element.
    '''
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
    '''
    It will return an array where sum of all 
    non-QCD background for a different syst
    is stored. For QCD MC, we make another
    array containg hists for all syst.
    It can return for up or down variation
    of the syst.
    '''
    hSumOtherBkgs = []
    hQCD    = []
    for syst in Systematics:
        hBkg = []
        for sample in SamplesSyst:
            if CR=="":
                hPath = "%s%s/SignalRegion/%s"%(syst, level, hName)
            else: 
                hPath = "%s%s/ControlRegion/%s/%s"%(syst, level, CR, hName)
            hist = fileDict[sample].Get(hPath)
            hist = hist.Clone("%s_%s%s_%s_%s"%(sample,syst,level,hName,CR))
            if sample=="QCD":
                hQCD.append(hist)
            else:
                hBkg.append(hist)
        #Sum non QCD background for a given syst
        hSum = hist.Clone("hSumOtherBkgs_%s%s_%s_%s"%(syst,level,hName,CR))
        hSum.Reset()
        for h in hBkg:
            hSum.Add(h)
        hSumOtherBkgs.append(hSum)
    return hSumOtherBkgs, hQCD

#-----------------------------------------
#Decorate a histogram
#-----------------------------------------
def decoHist(hist, xTit, yTit, color):
    hist.GetXaxis().SetTitle(xTit);
    hist.GetYaxis().SetTitle(yTit);
    hist.SetFillColor(color);

def decoHistStack(hist, xTit, yTit):
    #hist.GetXaxis().SetTitle(xTit);
    hist.GetYaxis().SetTitle(yTit)
    #hist.GetYaxis().CenterTitle()
    hist.GetYaxis().SetTitleOffset(1.15)
    hist.GetYaxis().SetTitleSize(0.055);
    hist.GetXaxis().SetTitleSize(0.11);

def decoHistRatio(hist, xTit, yTit, color):
    hist.GetXaxis().SetTitle(xTit);
    hist.GetYaxis().SetTitle(yTit);
    hist.GetXaxis().SetTitleSize(0.11);
    hist.GetXaxis().SetLabelSize(0.10);
    hist.GetXaxis().SetLabelFont(42);
    hist.GetXaxis().SetLabelColor(kBlack);
    hist.GetXaxis().SetAxisColor(kBlack);
    hist.GetYaxis().SetRangeUser(0.5, 1.5);
    hist.GetXaxis().SetTitleOffset(1);
    hist.GetXaxis().SetLabelOffset(0.01);
    hist.SetMarkerStyle(20); 
    #hist.SetMarkerSize(1.2);
    hist.GetYaxis().SetTitleSize(0.11);
    hist.GetYaxis().SetLabelSize(0.10);
    hist.GetYaxis().SetLabelFont(42);
    #hist.GetYaxis().SetAxisColor(1);
    hist.GetYaxis().SetNdivisions(6,5,0);
    hist.GetXaxis().SetTickLength(0.06);
    hist.GetYaxis().SetTitleOffset(0.6);
    hist.GetYaxis().SetLabelOffset(0.01);
    hist.GetYaxis().CenterTitle();

#-----------------------------------------
#Get uncertainty band for the total bkg
#-----------------------------------------
def getUncBand(hBase, hDiffUp, hDiffDown, isRatio):
    '''
    The uncertainty band is formed by up and down
    fluctuation of nominal event yield. In every
    bin we have a nominal value from the base
    histogram and up/down values from other two.
    We draw nominal + up and nominal - down as 
    error band on the top pannel. On the bottom (ratio)
    pannel, we draw 1+ up/nominal, 1-nominal/down as
    error band.
    '''
    yValues     = []
    yErrorsUp   = []
    yErrorsDown = []
    xValues     = []
    xErrorsUp   = []
    xErrorsDown = []
    nBins = hBase.GetNbinsX()
    for i in range(nBins):
        yValue      = hBase.GetBinContent(i+1)
        statError   = hBase.GetBinError(i+1)
        yErrorUp    = abs(hDiffUp.GetBinContent(i+1))+statError 
        yErrorDown  = abs(hDiffDown.GetBinContent(i+1))+statError 
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
            np.array(xValues    , dtype='double'),
            np.array(yValues    , dtype='double'),
            np.array(xErrorsDown, dtype='double'),
            np.array(xErrorsUp  , dtype='double'),
            np.array(yErrorsDown, dtype='double'),
            np.array(yErrorsUp  , dtype='double'))
    return uncGraph

#-----------------------------------------
#Legends for all histograms, graphs
#-----------------------------------------
def getLegend(dataHist, bkgHists, uncGraph):
    '''
    The background hists are sorted in the
    decending order of the event yield. That
    is the proccess having highest contribution
    comes first.
    '''
    legend = TLegend(0.45,0.70,0.92,0.88);
    #legend = TLegend(0.55,0.60,0.92,0.88); for 3 col
    #legend = TLegend(0.70,0.50,0.95,0.88); 
    legend.SetNColumns(4);
    legend.SetFillStyle(0);
    legend.SetBorderSize(0);
    legend.SetFillColor(kBlack);
    legend.SetTextFont(42);
    legend.SetTextAngle(0);
    legend.SetTextSize(0.035);
    legend.SetTextAlign(12);
    legend.AddEntry(dataHist[0], Samples["Data"][2], "PEL")
    for bkgHist in bkgHists:
        legendName = Samples[bkgHist.GetName().split("_")[0]][2] 
        legend.AddEntry(bkgHist, legendName, "F")
    legend.AddEntry(uncGraph, "Pre-fit unc.","F");
    return legend

#-----------------------------------------
#Sort histograms w.r.t to the event yield
#-----------------------------------------
def sortHists(hAllBkgs, isReverse):
    '''
    We sort the histograms in both orders.
    They are sorted in acending/decending
    orders for stack/legend.
    '''
    yieldDict = {}
    for h in hAllBkgs:
        yieldDict[h.GetName()] = h.Integral()
    if isReverse:
        newDict = sorted(yieldDict.items(), key=lambda x: x[1], reverse=True)
    else:
        newDict = sorted(yieldDict.items(), key=lambda x: x[1])
    hSorted = []
    for i in newDict:
        for h in hAllBkgs:
            if i[0]==h.GetName():
                hSorted.append(h)
    return hSorted

#-----------------------------------------
#Make a plot for one histogram
#----------------------------------------
def makePlot(hName, CR, isQCDMC, isData, isLog, isRatio):
    '''
    We first draw stacked histograms then data then unc band.
    The ratio of data and background is drawn next in a separate
    pad.
    '''
    #Divide canvas for the ratio plot
    canvas = TCanvas()
    if isRatio and isData:
        canvas.Divide(1,2)
        canvas.cd(1)
        gPad.SetRightMargin(0.03);
        gPad.SetPad(xPadRange[0],yPadRange[2],xPadRange[1],yPadRange[3]);
        gPad.SetTopMargin(0.09);
        gPad.SetBottomMargin(padGap);
        #gPad.SetTickx(0);
        gPad.RedrawAxis();
    if isLog:
        gPad.SetLogy(True);

    #Get nominal histograms
    dataHist, bkgHists, qcdMCHist, qcdDDHist = getBaseHists(hName, CR)
    hSumOtherBkg = bkgHists[0].Clone("hSumOtherBkg")
    hSumOtherBkg.Reset()
    hAllBkgs = bkgHists
    for bkgHist in bkgHists:
        hColor = Samples[bkgHist.GetName().split("_")[0]][1]
        hSumOtherBkg.Add(bkgHist)
    hSumAllBkg = hSumOtherBkg.Clone("hSumAllBkg")
    if isQCDMC:
        hSumAllBkg.Add(qcdMCHist[0])
        hAllBkgs.append(qcdMCHist[0])
    else:
        hSumAllBkg.Add(qcdDDHist[0])
        hAllBkgs.append(qcdDDHist[0])

    #Stack nominal hists
    xTitle = histograms[hName][0]
    yTitle = histograms[hName][1]
    hStack = THStack(hName,hName)
    hForStack = sortHists(hAllBkgs, False)
    for h in hForStack: 
        sampleName = h.GetName().split("_")[0]
        decoHist(h, xTitle, yTitle, Samples[sampleName][1])
        hStack.Add(h)
    hStack.SetMinimum(1.0)
    if isLog:
        hStack.SetMaximum(100*hStack.GetMaximum())
    else: 
        hStack.SetMaximum(1.3*hStack.GetMaximum())
    hStack.Draw("HIST")
    decoHistStack(hStack, xTitle, yTitle)

    #Get histograms for the difference between nominal and syst up/down
    hSumOtherBkgUps, hQCDUps = getSystHists(hName, CR, "Up")
    hSumOtherBkgDowns, hQCDDowns = getSystHists(hName, CR, "Down")
    hDiffUp = hSumOtherBkg.Clone("hDiffUp")
    hDiffUp.Reset()
    hDiffDown = hSumOtherBkg.Clone("hDiffDown")
    hDiffDown.Reset()
    for hUp in hSumOtherBkgUps:
        hDiff = hUp.Clone("hDiff")
        hDiff.Add(hSumOtherBkg, -1)    
        hDiffUp.Add(hDiff)
        print "hDiffUp = ", hDiffUp.Integral()
    for hDown in hSumOtherBkgDowns:
        hDiff = hSumOtherBkg.Clone("hDiff")
        hDiff.Add(hDown, -1)    
        hDiffDown.Add(hDiff)
    if isQCDMC:
        for hUp in hQCDUps:
            hDiff = hUp.Clone("hDiff")
            hDiff.Add(qcdMCHist[0], -1)    
            hDiffUp.Add(hDiff)
        for hDown in hQCDDowns:
            hDiff = qcdMCHist[0].Clone("hDiff")
            hDiff.Add(hDown, -1)    
            hDiffDown.Add(hDiff)

    #Get unc band for the top plot
    uncGraphTop = getUncBand(hSumAllBkg, hDiffUp, hDiffDown,False)
    uncGraphTop.SetFillColor(kOrange+2);
    uncGraphTop.SetFillStyle(3001);
    uncGraphTop.Draw(" E2 same ");
    
    #Draw data
    decoHist(dataHist[0], xTitle, yTitle, Samples["Data"][1])
    dataHist[0].SetMarkerStyle(20)
    if isData:
        dataHist[0].Draw("EPsame")

    #Draw legend
    hForLegend = sortHists(hAllBkgs, True)
    plotLegend = getLegend(dataHist, hForLegend, uncGraphTop)
    plotLegend.Draw()

    #Draw CMS, Lumi, channel
    if channel in ["mu", "Mu", "m"]:
        chName = "#mu + jets"
    else:
        chName = "e + jets"
    chCR = "#splitline{#font[42]{%s}}{#font[42]{%s}}"%(chName, CR)
    extraText   = "#splitline{Preliminary}{%s}"%chCR
    CMS_lumi(canvas, iPeriod, iPosX, extraText)

    #Draw the ratio of data and all background
    if isData and isRatio:
        canvas.cd(2)
        gPad.SetTopMargin(padGap); 
        gPad.SetBottomMargin(0.30); 
        gPad.SetRightMargin(0.03);
        #gPad.SetTickx(0);
        gPad.SetPad(xPadRange[0],yPadRange[0],xPadRange[1],yPadRange[2]);
        gPad.RedrawAxis();
        hRatio = dataHist[0].Clone("hRatio")
        hRatio.Divide(hSumAllBkg)
        decoHistRatio(hRatio, xTitle, "Obs./Exp.", 1)
        hRatio.Draw()
        uncGraphRatio = getUncBand(hSumAllBkg, hDiffUp, hDiffDown,True)
        uncGraphRatio.SetFillColor(kOrange+3);
        uncGraphRatio.SetFillStyle(3001);
        uncGraphRatio.Draw("E2same");
        baseLine = TF1("baseLine","1", -100, 2000);
        baseLine.SetLineColor(kRed+1);
        baseLine.Draw("SAME");
        hRatio.Draw("same")
    canvas.SaveAs("%s/%s.pdf"%(outPlotFullDir, hName))

#-----------------------------------------
#Finally make the plot for each histogram
#----------------------------------------
for hName in plotList:
    isQCDMC  = False
    isData   = True
    isLog    = True
    isRatio  = True
    if hName not in histograms.keys():
        print "hist name = %s, is not found"%hName
        sys.exit()
    makePlot(hName, "", isQCDMC,  isData, isLog, isRatio)
