from ROOT import TFile, TH1F, gDirectory
import os
import sys
import itertools
from optparse import OptionParser
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
parser.add_option("--isQCDMC","--qcdMC",dest="isQCDMC", default=False, action="store_true",
		  help="")
parser.add_option("--is0Photon","--is0Photon",dest="is0Photon", default=False, action="store_true",
		  help="")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
CR              = options.CR
isQCDMC         = options.isQCDMC
is0Photon       = options.is0Photon

#-----------------------------------------
#Path of the I/O histograms/datacards
#----------------------------------------
inFile = "%s/Hists/%s/%s/%s/Merged/AllInc.root"%(condorHistDir, year, decayMode, channel)
outFile = "%s/Hists/%s/%s/%s/Merged/AllCat.root"%(condorHistDir, year, decayMode, channel)
outputFile = TFile(outFile,"update")
#histList = ["phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake", "phosel_noCut_ChIso_GenuinePhoton","phosel_noCut_ChIso_MisIDEle","phosel_noCut_ChIso_HadronicPhoton","phosel_noCut_ChIso_HadronicFake"]
def addHist(histList, name):
    hist = histList[0].Clone(name)
    hist.Reset()
    for h in histList:
        hist.Add(h)
    return hist

#-----------------------------------
# Directory structure for !=0 photon 
#-----------------------------------
def getHistDict(sysType):
    histDict = {
                 "data_obs":[],
                 "nonPromptTTGamma": [], 
                 "nonPromptTTbar": [],   
                 "nonPromptZGamma": [],  
                 "nonPromptWGamma": [],  
                 "nonPromptOther": [],   
                 "isolatedTTGamma": [],  
                 "isolatedTTbar": [],
                 "isolatedZGamma": [],   
                 "isolatedWGamma": [],
                 "isolatedOther": []
                }
    for sample in Samples:
        if CR=="":
            histDir = "%s/%s/SR"%(sample, sysType)
        else:
            histDir = "%s/%s/CR/%s"%(sample, sysType, CR)
        if not sample in "Data":
            hHP = inFile.Get("%s/%s_HadronicPhoton"%(histDir, hName)
            hHF = inFile.Get("%s/%s_HadronicFake"%(histDir, hName)
            hGP = inFile.Get("%s/%s_GenuinePhoton"%(histDir, hName)
            hME = inFile.Get("%s/%s_MisIDEle"%(histDir, hName)
        for key in histDict.keys():
            if sample in "Data":
                hData = inFile.Get("%s/%s")%(histDir, hName)
                histDict["data_obs"].append(hData)
            elif sample in key:
                if "nonPrompt" in key:
                    histDict[key].append(hHP) 
                    histDict[key].append(hHF) 
                if "isolated" in key:
                    histDict[key].append(hGP) 
                    histDict[key].append(hME) 
            else:
                if "nonPrompt" in key:
                    histDict["nonPromptOther"].append(hHP) 
                    histDict["nonPromptOther"].append(hHF) 
                if "isolated" in key:
                    histDict["isolatedOther"].append(hGP) 
                    histDict["isolatedOther"].append(hME) 
    print histDict

#-----------------------------------
# Directory structure for = 0 photon 
#-----------------------------------
def getHistDict0Photon(sysType):
    histDict = {
                 "data_obs":[],
                 "TTGamma": [], 
                 "TTbar": [],   
                 "ZGamma": [],  
                 "WGamma": [],  
                 "Other": [] 
                }
    for sample in Samples:
        if CR=="":
            histDir = "%s/%s/SR"%(sample, sysType)
        else:
            histDir = "%s/%s/CR/%s"%(sample, sysType, CR)
        for key in histDict.keys():
            hist = inFile.Get("%s/%s")%(histDir, hName)
            if sample in "Data":
                histDict["data_obs"].append(hist)
            elif sample in key:
                histDict[key].append(hist)
            else:
                histDict["Other"].append(hist)
    print histDict

#-----------------------------------
#Get all directories and histograms 
#-----------------------------------
histDictAll = {}
if is0Photon:
    histDictAll["nominal"] = getHistDict0Photon("Base")
else:
    histDictAll["nominal"] = getHistDict("Base")

for syst, level in itertools.product(Systematics, SystLevel):
    sysName = "%s%s"%(syst, level)
    if is0Photon:
        histDictAll[sysName] = getHistDict0Photon(sysName)
    else:
        histDictAll[sysName] = getHistDict(sysName)

#-----------------------------------
#Write all directories and histograms 
#-----------------------------------
for key in histDictAll.keys():
    eachDict = histDictAll[key]
    for eachKey in eachDict:
        hNew = addHist(eachDict[eachKey], key)
        outHistDir = "%s/%s"%(hName,eachDict[eachKey])
        outputFile.cd(outHistDir)
        if not outputFile.GetDirectory(outHistDir):
            outputFile.mkdir(outHistDir)
        outputFile.cd(outHistDir)
        gDirectory.Delete("%s;*"%(hNew.GetName()))
        print "%s, \t%s, \t%s, \t%s"%(hName, key, hNew.GetName(), hNew.Integral())
        hNew.Write()
outputFile.Close()
