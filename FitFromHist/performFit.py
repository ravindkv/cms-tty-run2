from ROOT import TFile, TH1F, gDirectory
import os
import sys
import itertools
from optparse import OptionParser
import CombineHarvester.CombineTools.ch as ch
from FitInputs import *

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
		  help="run FitDiabnostics")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
CR              = options.CR
isText 			= options.isText
isT2W 			= options.isT2W
isFD           = options.isFD
isImpact       = options.isImpact

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
    myfile = TFile("%s/fitDiagnostics.root"%dirFD,"read")
    paramList = ["r", "nonPromptSF", "TTbarSF", "WGSF", "ZGSF", "OtherSF"]
    fit_s = myfile.Get("fit_s")
    for param in paramList:
        print "%s\t\t = %s"%(param, fit_s.floatParsFinal().find(param).getVal())

#-----------------------------------------
#Impacts of Systematics
#----------------------------------------
if isImpact:
    os.system("combineTool.py -M Impacts -d %s  -m 125 --doInitialFit --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2 "%pathT2W) 
    os.system("combineTool.py -M Impacts -d %s  -m 125  --doFits --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2 --parallel 10"%pathT2W)
    os.system("combineTool.py -M Impacts -d %s -m 125 -o %s/nuisImpact.json"%(pathT2W, dirImpact))
    os.system("python plotImpacts.py --cms-label \"   Internal\" -i %s/nuisImpact.json -o %s/nuisImpact.pdf"%(dirImpact, dirImpact))
