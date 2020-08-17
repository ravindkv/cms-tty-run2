from ROOT import TFile, TLegend, gPad, gROOT, TCanvas, THStack, TF1, TH1F, TGraphAsymmErrors
import os
import sys
from optparse import OptionParser
from PlotInfo_cff import *
from PlotInputs_cff import *
from PlotCMSLumi_cff import *
from PlotTDRStyle_cff import *
from PlotFunctions_cff import *

padGap = 0.01
iPeriod = 4;
iPosX = 10;
setTDRStyle()
xPadRange = [0.0,1.0]
yPadRange = [0.0,0.30-padGap, 0.30+padGap,1.0]
