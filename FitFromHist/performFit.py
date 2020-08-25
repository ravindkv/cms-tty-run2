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
parser.add_option("--runFD","--runFD",dest="runFD", default=False, action="store_true",
		  help="run FitDiabnostics")
parser.add_option("--runImpact","--runImpact",dest="runImpact", default=False, action="store_true",
		  help="run FitDiabnostics")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
CR              = options.CR
isText 			= options.isText
isT2W 			= options.isT2W
runFD           = options.runFD
runImpact       = options.runImpact

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
	outFileDir      = "%s/Fit/%s/%s/%s/DataCard/SR"%(condorHistDir, year, decayMode, channel)
else:
	outFileDir      = "%s/Fit/%s/%s/%s/DataCard/CR/%s"%(condorHistDir, year, decayMode, channel, CR)
combinedDCName = "%s/Combined_Datacard_%s_%s_%s.txt"%(outFileDir, year, decayMode, channel)
combinedT2WName = "%s/Combined_Datacard_T2W_%s_%s_%s.root"%(outFileDir, year, decayMode, channel)
if isT2W:
	incDCList = []
	catDCList = []
	catDCList0Pho = []
	for hName in incHistList:
		incDCList.append("%s/Datacard_Inc_%s.txt"%(outFileDir, hName))
	for hName in catHistList:
		catDCList.append("%s/Datacard_Cat_%s.txt"%(outFileDir, hName))
	for hName in catHistList0Pho:
		catDCList0Pho.append("%s/Datacard_0Pho_%s.txt"%(outFileDir, hName))
	combinedDCList = catDCList + catDCList0Pho
	combinedDCText = ' '.join([str(dc) for dc in combinedDCList])
	os.system("combineCards.py %s > %s"%(combinedDCText, combinedDCName))
	os.system("text2workspace.py %s -o %s"%(combinedDCName, combinedT2WName))

#-----------------------------------------
#Fit diagnostics
#----------------------------------------
if runFD:
	os.system("combine %s --mass 125 -M FitDiagnostics --plots --saveShapes --saveWithUncertainties  --saveNormalizations --initFromBonly "%combinedT2WName)
	os.system("python diffNuisances.py --all fitDiagnostics.root -g fitDiag.pdf")
combine -M FitDiagnostics -n   mu_2016   datacard_mu_2016.root   -s 314159 --plots --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF --saveShapes --saveWithUncertainties --saveNormalizations  -v2  --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2

#-----------------------------------------
#Impacts of Systematics
#----------------------------------------
if runImpact:
	os.system("combineTool.py -M Impacts -d %s -m 125 --doInitialFit --robustFit 1 -t -1"%combinedT2WName) 
	os.system("combineTool.py -M Impacts -d %s -m $mass -o nuisImpactJSON"%combinedT2WName)
	os.system("plotImpacts.py --cms-label \"   Internal\" -i nuisImpactJSON -o nuisImpactPDF")
