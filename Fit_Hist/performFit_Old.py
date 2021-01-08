import ROOT
import os
import sys
import json
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
parser.add_option("-d", "--decayMode", dest="decayMode", default="Semilep",type='str',
                     help="Specify which decayMode moded of ttbar Semilep or Dilep? default is Semilep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--isComb","--isComb",dest="isComb", default=False, action="store_true",
		  help="combine datacards")
parser.add_option("--combYear", dest="combYear",default=["2016"], action="append",
          help="years to be combined" )
parser.add_option("--combDecay", dest="combDecay",default=["Semilep"], action="append",
          help="decays to be combined" )
parser.add_option("--combChannel", dest="combChannel",default=["Mu"],action="append",
          help="channels to be combined" )
parser.add_option("--isMassDilep","--isMassDilep",dest="isMassDilep", default=False, action="store_true",
		  help="datacards for mass of dilepton")
parser.add_option("--isMassLepGamma","--isMassLepGamma",dest="isMassLepGamma", default=False, action="store_true",
		  help="combine datacards")
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--hist", "--hist", dest="hName", default="phosel_M3",type='str', 
                     help="which histogram to be used for making datacard")
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
parser.add_option("--isCount","--isCount",dest="isCount", default=False, action="store_true",
		  help="")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
CR              = options.CR
hName           = options.hName
combYear        = options.combYear[0].split(",")
combDecay       = options.combDecay[0].split(",")
combChannel     = options.combChannel[0].split(",")
isCount         = options.isCount
print combDecay
print combChannel

isComb          = options.isComb
isMassDilep     = options.isMassDilep
isMassLepGamma  = options.isMassLepGamma

isT2W 			= options.isT2W
isFD            = options.isFD
isImpact        = options.isImpact
isCM            = options.isCM
isTP            = options.isTP
isPlotTP        = options.isPlotTP
#-----------------------------------------
#Various functions
#----------------------------------------
def runCmd(cmd):
    print "\n\033[01;32m Excecuting: \033[00m %s"%cmd
    os.system(cmd)
with open ("DataCards.json") as jsonFile:
    jsonData = json.load(jsonFile)
rateParamKey = "rateParam"
#-----------------------------------------
#For separate datacards
#----------------------------------------
dirDC = "DirectoryOfDataCard"
if isCount:
    shapeOrCount = "CountBased"
else:
    shapeOrCount = "ShapeBased"

def getDataCard(year, decayMode, channel, CR, hName):
    global dirDC
    if CR=="":
        name  = "DC_%s_%s_%s_%s_%s_SR"%(year, decayMode, channel, shapeOrCount, hName)
        dirDC = "%s/Fit/%s/%s/%s/%s/%s/SR"%(condorHistDir, year, decayMode, channel, shapeOrCount, hName)
    else:
        name  = "DC_%s_%s_%s_%s_%s_CR_%s"%(year, decayMode, channel, shapeOrCount, hName, CR)
        dirDC = "%s/Fit/%s/%s/%s/%s/%s/CR/%s"%(condorHistDir, year, decayMode, channel, shapeOrCount, hName, CR)
    pathDC   = jsonData[name][0]
    global rateParamKey
    rateParamKey = name.replace("DC","RP")
    if not os.path.exists(pathDC):
        print "Datacard: %s does not exist"%pathDC
        sys.exit()
    return pathDC
#-----------------------------------------
#For combination of datacards
#----------------------------------------
if isComb:
    combDC = []
    if isMassDilep:
        combHist = ["presel_MassDilep"]
    elif isMassLepGamma:
        combHist = ["phosel_MassLepGamma"]
    else:
        combHist = ["presel_M3_0Pho", "phosel_M3", "phosel_noCut_ChIso"]
    for combY, combD, combCh, combH in itertools.product(combYear, combDecay,  combChannel, combHist):
        name = getDataCard(combY, combD, combCh, CR, combH)
        combDC.append(name)
    for combY, combD, combCh in itertools.product(combYear, combDecay,  combChannel):
        if not isMassDilep and not isMassLepGamma:
            combDC.append(getDataCard(combY, combD, combCh, "tight_a4j_e0b", "phosel_M3"))
            #combDC.append(getDataCard(combY, combD, combCh, "tight_e3j_e0b", "phosel_M3"))
	combDCText = ' '.join([str(dc) for dc in combDC])
    combYText  = ''.join([str(y) for y in combYear])
    combDText  = ''.join([str(d) for d in combDecay]) 
    combChText = ''.join([str(ch) for ch in combChannel]) 
    combHText  = ''.join([str(h) for h in combHist]) 
    if CR=="":
        dirDC        = "%s/Fit/Combined/%s_%s_%s/%s/%s/SR"%(condorHistDir, combYText, combDText, combChText, shapeOrCount, combHText)
        rateParamKey = "RP_Comb_%s_%s_%s_%s_%s_SR"%(combYText, combDText, combChText, shapeOrCount, combHText)
    else:
        dirDC        = "%s/Fit/Combined/%s_%s_%s/%s/%s/CR/%s"%(condorHistDir, combYText, combDText, combChText, shapeOrCount, combHText, CR)
        rateParamKey = "RP_Comb_%s_%s_%s_%s_%s_CR_%s"%(combYText, combDText, combChText, shapeOrCount, combHText, CR)
    if not os.path.exists(dirDC):
        os.makedirs(dirDC)
    pathDC  = "%s/Datacard_Comb.txt"%(dirDC)
    pathT2W = "%s/Text2W_Comb.root"%(dirDC)
    runCmd("combineCards.py %s > %s"%(combDCText, pathDC))
    print pathDC
else:
    pathDC = getDataCard(year, decayMode, channel, CR, hName)
    pathT2W = "%s/Text2W_Cat.root"%(dirDC) 
    #dirDC = "/eos/uscms/store/user/rverma/OutputTTGamma/Fit/Combined/2016_Semilep_Mu/CountBased/presel_M3_0Phophosel_M3phosel_noCut_ChIso/SR/"
    #pathDC = "/eos/uscms/store/user/rverma/OutputTTGamma/Fit/Combined/2016_Semilep_Mu/CountBased/presel_M3_0Phophosel_M3phosel_noCut_ChIso/SR/Datacard_Comb.txt"
    #pathT2W = "/eos/uscms/store/user/rverma/OutputTTGamma/Fit/Combined/2016_Semilep_Mu/CountBased/presel_M3_0Phophosel_M3phosel_noCut_ChIso/SR/Text2W_Comb.root"
    print pathDC

if isT2W:
	runCmd("text2workspace.py %s -o %s"%(pathDC, pathT2W))
        print pathT2W

#-----------------------------------------
#Fit diagnostics
#----------------------------------------
if isMassLepGamma:
    rMin = -5
    rMax = +5
    paramList = ["r","OtherPhotonsZGammaSF","OtherPhotonsWGammaSF","OtherPhotonsOthersSF"] 
elif isMassDilep:
    rMin = -5
    rMax = +5
    paramList = ["r","OthersSF"]
else:
    rMin = 0
    rMax = 2
    #paramList = ["r", "nonPromptSF", "TTbarSF", "WGSF", "ZGSF", "OtherSF", "lumi_13TeV"]
    paramList = ["r", "nonPromptSF"]
params    = ','.join([str(param) for param in paramList])
if isFD:
    runCmd("combine -M FitDiagnostics  %s --out %s -t -1 --plots --redefineSignalPOIs %s -v2 --saveShapes --saveWithUncertainties --saveNormalizations --cminDefaultMinimizerStrategy 0 --rMin=%s --rMax=%s"%(pathT2W, dirDC, params, rMin, rMax))
    #runCmd("combine -M FitDiagnostics  %s --out %s -t -1 --expectSignal 1 --plots --redefineSignalPOIs %s -v2 --saveShapes --saveWithUncertainties --saveNormalizations --cminDefaultMinimizerStrategy 0 --rMin=%s --rMax=%s"%(pathT2W, dirDC, params, rMin, rMax))
    #runCmd("combine -M FitDiagnostics %s --out %s -t -1 --plots -v2 --saveShapes --saveWithUncertainties --saveNormalizations --cminDefaultMinimizerStrategy 0 --rMin=%s --rMax=%s"%(pathT2W, dirDC, rMin, rMax))
    #runCmd("python diffNuisances.py --abs --all %s/fitDiagnostics.root -g %s/diffNuisances.root"%(dirDC,dirDC))
    runCmd("python diffNuisances.py --all %s/fitDiagnostics.root -g %s/diffNuisances.root"%(dirDC,dirDC))
    print dirDC
    #store rateparams in a json file 
    myfile = ROOT.TFile("%s/fitDiagnostics.root"%dirDC,"read")
    fit_s = myfile.Get("fit_s")
    with open ('RateParams.json') as jsonFile:
        jsonData = json.load(jsonFile)
    jsonData[rateParamKey] = []
    for param in paramList:
        val = fit_s.floatParsFinal().find(param).getVal()
        #print "%20s = %10s"%(param, val)
        print "%20s = %10s"%(param, round(val,5))
        paramDict = {}
        paramDict[param] = round(val,4)
        jsonData[rateParamKey].append(paramDict)
    #plot covariant matrix
    with open ('RateParams.json', 'w') as jsonFile:
        json.dump(jsonData, jsonFile)

if isTP:
    runCmd("combine -M FitDiagnostics %s --name TP -t -1 --out %s --seed=314159 --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 --expectSignal=1 -t 500 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi_13TeV,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF &"%(pathT2W, dirDC))
    print dirDC

#-----------------------------------------
#Impacts of Systematics
#----------------------------------------
if isImpact:
    #runCmd("combineTool.py -M Impacts -d %s  -m 125 -t -1 --doInitialFit --robustFit 1 --cminDefaultMinimizerStrategy 0 --expectSignal 1 --redefineSignalPOIs %s "%(pathT2W, params)) 
    #runCmd("combineTool.py -M Impacts -d %s  -m 125 -t -1 --doFits --robustFit 1 --cminDefaultMinimizerStrategy 0 --expectSignal 1 --redefineSignalPOIs %s --parallel 10"%(pathT2W, params))
    #runCmd("combineTool.py -M Impacts -d %s -m 125 -o %s/nuisImpact.json --redefineSignalPOIs %s "%(pathT2W, dirDC, params))
    runCmd("python ./plotImpacts.py --cms-label \"   Internal\" -i %s/nuisImpact.json -o %s/nuisImpact.pdf"%(dirDC, dirDC))


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
       
    f1 = ROOT.TFile.Open('%s/fitDiagnostics.root'%(dirDC),'read')
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
    #canvas.SaveAs('%s/covarianceMatrix.pdf'%dirDC) 
    canvas.SaveAs('%s/covarianceMatrix.png'%dirDC) 

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
    outputDir = "%s/NuisancePlots"%dirDC
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)
    listOfParameters = ["r","BTagSF_b","BTagSF_l","EleEff","MuEff","PhoEff","lumi_13TeV","ZGSF","TTbarSF","OtherSF","WGSF"]#,"nonPromptSF"]
    myfile = ROOT.TFile("%s/fitDiagnosticsTP.root"%dirDC,"read")
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

