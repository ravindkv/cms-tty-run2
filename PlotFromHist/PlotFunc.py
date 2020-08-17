from ROOT import TLegend, TGraphAsymmErrors
from PlotInputs_cff import *
import numpy as np
#-----------------------------------------
#Get historgams from the root files 
#-----------------------------------------
def getBaseHists(fileDict, hName, CR):
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

def getSystHists(fileDict, hName, CR, level):
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
    #hist.GetXaxis().SetLabelColor(kBlack);
    #hist.GetXaxis().SetAxisColor(kBlack);
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
    #legend.SetFillColor(kBlack);
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

#----------------------------------------------------------
#Reformat jet multiplicity string 
#----------------------------------------------------------
#Jet selection naming: a3j_e2b = atleast 3 jet, out of which 2 are b jets: nJet >= 3, nBJet ==2
def formatCRString(controlRegion="tight_a4j_e0b"):
    allJetSel = "jets >=3, b jets >=1"
    if not controlRegion=="":
    	splitCR = controlRegion.split("_")
    	jetCut  = splitCR[1].strip()
    	bJetCut = splitCR[2].strip()
    	#For total jets 
    	operationJet, numberJet = jetCut[0].strip(), jetCut[1].strip()
    	expresssionJet = "=="
    	if operationJet=="a": 
    	    expresssionJet=">="
    	newJetCut = "jets %s%s"%(expresssionJet, numberJet)
    	#For b jets
    	operationBJet, numberBJet = bJetCut[0].strip(), bJetCut[1].strip()
    	expresssionBJet = "=="
    	if(operationBJet=="a"): 
    	    expresssionBJet=">="
    	newBJetCut = "b jets %s%s"%(expresssionBJet, numberBJet)
    	#Combine the two selection
        allJetSel = "%s, %s"%(newJetCut, newBJetCut) 
    return allJetSel
