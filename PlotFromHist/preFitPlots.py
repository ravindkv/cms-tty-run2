from ROOT import TFile, TLegend, gPad, gROOT, TCanvas, THStack, TF1, TH1F, TGraphAsymmErrors
import os
import sys
from optparse import OptionParser
from PlotInfo import *
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
parser.add_option("-d", "--decayMode", dest="decayMode", default="SemiLep",type='str',
                     help="Specify which decayMode moded of ttbar SemiLep or DiLep? default is SemiLep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--plot", dest="plotList",action="append",default=["presel_Njet"], help="Add plots" )
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
    dataHist, bkgHists, qcdMCHist, qcdDDHist = getBaseHists(fileDict, hName, CR)
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
    hSumOtherBkgUps, hQCDUps = getSystHists(fileDict, hName, CR, "Up")
    hSumOtherBkgDowns, hQCDDowns = getSystHists(fileDict, hName, CR, "Down")
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
    uncGraphTop.SetFillColor(2);
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
    crName = formatCRString(CR)
    if CR=="":
        chName = "%s, SR"%chName
    else:
        chName = "%s, CR"%chName
    chCRName = "#splitline{#font[42]{%s}}{#font[42]{%s}}"%(chName, crName)
    extraText   = "#splitline{Preliminary}{%s}"%chCRName
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
        uncGraphRatio.SetFillColor(2);
        uncGraphRatio.SetFillStyle(3001);
        uncGraphRatio.Draw("E2same");
        baseLine = TF1("baseLine","1", -100, 2000);
        #baseLine.SetLineColor(kRed+1);
        baseLine.SetLineColor(3);
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
    makePlot(hName, CR, isQCDMC,  isData, isLog, isRatio)
