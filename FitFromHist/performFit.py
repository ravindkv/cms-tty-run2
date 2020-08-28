import ROOT
import os
import sys
import itertools
from optparse import OptionParser
import CombineHarvester.CombineTools.ch as ch
from FitInputs import *
from array import array

#-----------------------------------------
#INPUT command-line arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specify the year of the data taking" )
parser.add_option("-d", "--decayMode", dest="decayMode", default="SemiLep",type='str',
                     help="Specify which decayMode moded of ttbar SemiLep or DiLep? default is SemiLep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--isText","--isText",dest="isText", default=False, action="store_true",
		  help="create txt datacards")
parser.add_option("--isT2W","--isT2W",dest="isT2W", default=False, action="store_true",
		  help="create text2workspace datacards")
parser.add_option("--isFD","--isFD",dest="isFD", default=False, action="store_true",
		  help="run FitDiabnostics")
parser.add_option("--isImpact","--isImpact",dest="isImpact", default=False, action="store_true",
		  help="run impacts")
parser.add_option("--isCM","--isCM",dest="isCM", default=False, action="store_true",
		  help="make plot of covariance matrix")
parser.add_option("--isTP","--isTP",dest="isTP", default=False, action="store_true",
		  help="generate toys")
parser.add_option("--isPlotTP","--isPlotTP",dest="isPlotTP", default=False, action="store_true",
		  help="plot generated toys")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
CR              = options.CR
isText 			= options.isText
isT2W 			= options.isT2W
isFD            = options.isFD
isImpact        = options.isImpact
isCM            = options.isCM
isTP            = options.isTP
isPlotTP        = options.isPlotTP

incHistList = ["presel_M3"]
catHistList = ["phosel_M3", "phosel_noCut_ChIso"]
catHistList0Pho = ["presel_M3"]
#-----------------------------------------
#Make separate datacards
#----------------------------------------
if isText:
	for hName in incHistList:
		if CR=="":
			toRun = "python makeDataCardInc.py --hist %s -y %s -d %s -c %s"
			os.system(toRun%(hName, year, decayMode, channel))
		else:
			toRun = "python makeDataCardInc.py --hist %s -y %s -d %s -c %s --cr %s"
			os.system(toRun%(hName, year, decayMode, channel, CR))
	for hName in catHistList:
		if CR=="":
			toRun = "python makeDataCardCat.py --hist %s -y %s -d %s -c %s"
			os.system(toRun%(hName, year, decayMode, channel))
		else:
			toRun = "python makeDataCardCat.py --hist %s -y %s -d %s -c %s --cr %s"
			os.system(toRun%(hName, year, decayMode, channel, CR))
	for hName in catHistList0Pho:
		if CR=="":
			toRun = "python makeDataCard0Pho.py --hist %s -y %s -d %s -c %s"
			os.system(toRun%(hName, year, decayMode, channel))
		else:
			toRun = "python makeDataCard0Pho.py --hist %s -y %s -d %s -c %s --cr %s"
			os.system(toRun%(hName, year, decayMode, channel, CR))

#-----------------------------------------
#Combine datacards
#----------------------------------------
if CR=="":
	dirDC      = "%s/Fit/%s/%s/%s/DataCard/SR"%(condorHistDir, year, decayMode, channel)
	dirFD      = "%s/Fit/%s/%s/%s/FitDiag/SR"%(condorHistDir, year, decayMode, channel)
	dirImpact  = "%s/Fit/%s/%s/%s/Impact/SR"%(condorHistDir, year, decayMode, channel)
else:
	dirDC      = "%s/Fit/%s/%s/%s/DataCard/CR/%s"%(condorHistDir, year, decayMode, channel, CR)
	dirFD      = "%s/Fit/%s/%s/%s/FitDiag/CR/%s"%(condorHistDir, year, decayMode, channel, CR)
	dirImpact  = "%s/Fit/%s/%s/%s/Impact/CR/%s"%(condorHistDir, year, decayMode, channel, CR)
for dir_ in [dirDC, dirFD, dirImpact]:
	if not os.path.exists(dir_):
		os.makedirs(dir_)
pathDC  = "%s/Combined_Datacard_%s_%s_%s.txt"%(dirDC, year, decayMode, channel)
pathT2W = "%s/Combined_Datacard_T2W_%s_%s_%s.root"%(dirDC, year, decayMode, channel)
if isT2W:
	incDCList = []
	catDCList = []
	catDCList0Pho = []
	for hName in incHistList:
		incDCList.append("%s/Datacard_Inc_%s.txt"%(dirDC, hName))
	for hName in catHistList:
		catDCList.append("%s/Datacard_Cat_%s.txt"%(dirDC, hName))
	for hName in catHistList0Pho:
		catDCList0Pho.append("%s/Datacard_0Pho_%s.txt"%(dirDC, hName))
	combinedDCList = catDCList + catDCList0Pho
	combinedDCText = ' '.join([str(dc) for dc in combinedDCList])
	os.system("combineCards.py %s > %s"%(combinedDCText, pathDC))
	os.system("text2workspace.py %s -o %s"%(pathDC, pathT2W))
        print pathDC

#-----------------------------------------
#Fit diagnostics
#----------------------------------------
if isFD:
    os.system("combine -M FitDiagnostics  %s --out %s -s 314159 --plots --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF -v2 --saveShapes --saveWithUncertainties --saveNormalizations --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2"%(pathT2W, dirFD))
    os.system("python diffNuisances.py --all %s/fitDiagnostics.root -g %s/diffNuisances.root"%(dirFD,dirFD))
    print dirFD
    #print param
    myfile = ROOT.TFile("%s/fitDiagnostics.root"%dirFD,"read")
    paramList = ["r", "nonPromptSF", "TTbarSF", "WGSF", "ZGSF", "OtherSF"]
    fit_s = myfile.Get("fit_s")
    for param in paramList:
        print "%s\t\t = %s"%(param, fit_s.floatParsFinal().find(param).getVal())
    #plot covariant matrix

if isTP:
    os.system("combine -M FitDiagnostics %s --name TP --out %s --seed=314159 --saveWithUncertainties --saveNormalizations --saveTPs --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 --expectSignal=1 -t 500 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi_13TeV,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF &"%(pathT2W, dirFD))
    print dirFD

#-----------------------------------------
#Impacts of Systematics
#----------------------------------------
if isImpact:
    os.system("combineTool.py -M Impacts -d %s  -m 125 --doInitialFit --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2 "%pathT2W) 
    os.system("combineTool.py -M Impacts -d %s  -m 125  --doFits --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2 --parallel 10"%pathT2W)
    os.system("combineTool.py -M Impacts -d %s -m 125 -o %s/nuisImpact.json"%(pathT2W, dirImpact))
    os.system("python plotImpacts.py --cms-label \"   Internal\" -i %s/nuisImpact.json -o %s/nuisImpact.pdf"%(dirImpact, dirImpact))

#-----------------------------------------
# Make covariance matrix
#----------------------------------------
if isCM:
    ROOT.gROOT.SetBatch(True)
    Red    = [ 1.00, 0.00, 0.00, 0.87, 1.00, 0.51 ]
    Green  = [ 1.00, 0.00, 0.81, 1.00, 0.20, 0.00 ]
    Blue   = [ 1.00, 0.51, 1.00, 0.12, 0.00, 0.00 ]
    Length = [ 0.00, 0.02, 0.34, 0.51, 0.64, 1.00 ]
    lengthArray = array('d', Length)
    redArray = array('d', Red)
    greenArray = array('d', Green)
    blueArray = array('d', Blue)

    #ROOT.TColor.CreateGradientColorTable(6,lengthArray,redArray,greenArray,blueArray,99)
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetPaintTextFormat('5.1f');
    canvas = ROOT.TCanvas()
    canvas.SetFillColor(10);
    canvas.SetBorderMode(0);
    canvas.SetBorderSize(0);
    canvas.SetTickx();
    canvas.SetTicky();
    canvas.SetLeftMargin(0.15);
    canvas.SetRightMargin(0.15);
    canvas.SetTopMargin(0.15);
    canvas.SetBottomMargin(0.15);
    canvas.SetFrameFillColor(0);
    canvas.SetFrameBorderMode(0);
       
    f1 = ROOT.TFile.Open('%s/fitDiagnostics.root'%(dirFD),'read')
    h_background = f1.Get('covariance_fit_b')
    h_signal = f1.Get('covariance_fit_s')
    h_signal.GetYaxis().SetLabelSize(0.02)
    h_signal.GetXaxis().SetLabelSize(0.02)
    h_signal.GetZaxis().SetLabelSize(0.03)
    h_signal.SetMarkerSize(0.7)
    h_signal.LabelsOption("v", "X")
    h_signal.SetContour(99)
    h_signal.Draw('colz, Y+, TEXT0')

    mypal = h_signal.GetListOfFunctions().FindObject('palette')
    print mypal
    mypal.SetX1NDC(0.02);
    mypal.SetX2NDC(0.06);
    mypal.SetY1NDC(0.1);
    mypal.SetY2NDC(0.9);
    canvas.Modified();
    canvas.Update();
    #ROOT.gApplication.Run()
    canvas.SaveAs('%s/covarianceMatrix.pdf'%dirFD) 

if isPlotTP:
    ROOT.gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetOptFit(1)
    c1 = ROOT.TCanvas( 'c1', '', 800,800 )
    c1.SetFillColor(10)
    c1.SetBorderMode(0)
    c1.SetBorderSize(0)
    c1.SetTickx()
    c1.SetTicky()
    c1.SetLeftMargin(0.15)
    c1.SetRightMargin(0.15)
    c1.SetTopMargin(0.15)
    c1.SetBottomMargin(0.15)
    c1.SetFrameFillColor(0)
    c1.SetFrameBorderMode(0)
    c1.SetGrid()
    outputDir = "%s/NuisancePlots"%dirFD
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)
    listOfParameters = ["r","BTagSF_b","BTagSF_l","EleEff","MuEff","PhoEff","lumi_13TeV","ZGSF","TTbarSF","OtherSF","WGSF"]#,"nonPromptSF"]
    myfile = ROOT.TFile("%s/fitDiagnosticsTP.root"%dirFD,"read")
    mytree=myfile.tree_fit_sb
    for param in listOfParameters:
        hist = ROOT.TH1F("hist","",100,-2,2)
        mytree.Draw("%s >> hist"%(param))
        hist.Fit("gaus")
        hist.SetTitle("%s;"%param)
        hist.GetYaxis().SetLabelSize(0.03)
        hist.GetXaxis().SetLabelSize(0.03)
        ROOT.gPad.Update()
        mypal = hist.GetListOfFunctions().FindObject('stats')
        mypal.SetX1NDC(0.17)
        mypal.SetX2NDC(0.4)
        mypal.SetY1NDC(0.7)
        mypal.SetY2NDC(0.9)
        c1.Draw()
        c1.Modified()
        c1.Update()
        c1.Print("%s/%s.pdf"%(outputDir,param))
        hist.Delete()

