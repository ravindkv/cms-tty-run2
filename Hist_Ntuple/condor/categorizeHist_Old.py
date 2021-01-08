from ROOT import TFile, TH1F, gDirectory
import os
import sys
import numpy
import itertools
import json
from optparse import OptionParser
from HistInputs import *

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
parser.add_option("--hist", "--hist", dest="inHistName", default="phosel_M3",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--isQCDDD","--qcdMC",dest="isQCDDD", default=False, action="store_true",
		  help="")
parser.add_option("--is0PhoM3","--is0PhoM3",dest="is0PhoM3", default=False, action="store_true",
		  help="")
parser.add_option("--isMassLepGamma","--isMassLepGamma",dest="isMassLepGamma", default=False, action="store_true",
		  help="")
parser.add_option("--isMassDilep","--isMassDilep",dest="isMassDilep", default=False, action="store_true",
		  help="")
parser.add_option("--isCount","--isCount",dest="isCount", default=False, action="store_true",
		  help="")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
inHistName      = options.inHistName
CR              = options.CR
isQCDDD         = options.isQCDDD
is0PhoM3        = options.is0PhoM3
isMassLepGamma  = options.isMassLepGamma
isMassDilep     = options.isMassDilep
isCount         = options.isCount
print isCount

#-----------------------------------------
#Path of the I/O histograms/datacards
#----------------------------------------
inFile = TFile("%s/Hists/%s/%s/%s/Merged/AllInc.root"%(condorHistDir, year, decayMode, channel), "read")
if isCount:
    outDir = "%s/Hists/%s/%s/%s/Merged/CountBased"%(condorHistDir, year, decayMode, channel)
else:
    outDir = "%s/Hists/%s/%s/%s/Merged/ShapeBased"%(condorHistDir, year, decayMode, channel)
if not os.path.exists(outDir):
    os.makedirs(outDir)
outFileName = "%s/AllCat_%s.root"%(outDir, inHistName)
print inFile
outputFile = TFile(outFileName,"update")

#-----------------------------------------
#Rebinning scheme of the histograms
#----------------------------------------
if isCount:
    newBinsM3 = numpy.array([ 50.,500.])
    newBinsChIso = numpy.array([ 0.,20.])
    newBinsDilep = numpy.array([80.,102.]) 
    newBinsMisID = numpy.array([0,180.])
else:
    newBinsM3 = numpy.array([ 50.,  100., 125., 150., 175., 200.,250., 300., 500.])
    #newBinsChIso = numpy.array([0.5, 1., 2., 5., 12., 20.])
    newBinsChIso = numpy.array([ 0., 0.5, 1., 2., 5., 12., 20.])
    #newBinsDilep = numpy.arange(0,180.1,1)
    newBinsDilep = numpy.arange(80.,102.,2) #dont put space
    if "le" in channel:
        newBinsMisID = numpy.array([0,80,84,88,92,96,100,180.])
    else:
        newBinsMisID = numpy.array([0,90,180.])
def getNewBins(inHistName):
    if isMassDilep:
        return newBinsDilep
    elif isMassLepGamma:
        return newBinsMisID
    else:
	    if "M3" in inHistName:
		    return newBinsM3
	    else:
		    return newBinsChIso
#-----------------------------------------
#Function to read rateParams from json file
#----------------------------------------
jsonPath = "../../FitFromHist/RateParams.json"
if not os.path.exists(jsonPath):
    print "Json file %s does not exists"%jsonPath
    sys.exit()
with open (jsonPath) as jsonFile:
    jsonData = json.load(jsonFile)
'''
def getRateParam(year, decayMode, channel, CR, hName,proc):
    if CR=="":
        name  = "RP_Comb_%s_%s_%s_%s_SR"%(year, decayMode, channel, hName)
    else:
        name  = "RP_Comb_%s_%s_%s_%s_CR_%s"%(year, decayMode, channel, hName, CR)
    paramDicts   = jsonData[name]
    rateParam = 1.0
    for paramDict in paramDicts:
        for key, val in paramDict.iteritems():
            if proc==key:
                rateParam = val
    return rateParam
'''
def getRateParam(name, proc):
    paramDicts   = jsonData[name]
    rateParam = 1.0
    for paramDict in paramDicts:
        for key, val in paramDict.iteritems():
            if proc==key:
                rateParam = val
    return rateParam
misIDName = "RP_Nabin_MisIDEleSF_2016_looseCRge2e0"
misIDSF   = getRateParam(misIDName, "r")
zGammaSF  = getRateParam(misIDName, "ZGammaSF")
wGammaSF  = getRateParam(misIDName, "WGammaSF")
zJetsSF   = getRateParam("RP_Nabin_ZJetsSF_2016_tight","r")
print misIDSF
print zGammaSF
print wGammaSF
print zJetsSF

#-----------------------------------------
#Functions to read/write histograms
#----------------------------------------
def addHist(histList, name):
    if len(histList) ==0:
        print "Hist list | %s, %s | is empty"%(histList, name)
        sys.exit()
    else:
        hist = histList[0].Clone(name)
        hist.Reset()
        for h in histList:
            hist.Add(h)
        return hist

def getHistDir(sample, sysType, CR):
    if CR=="":
        histDir = "%s/%s/SR"%(sample, sysType)
    else:
        histDir = "%s/%s/CR/%s"%(sample, sysType, CR)
    return histDir

def writeHist(hist, procDir, histNewName, outputFile):
    outHistDir = getHistDir(procDir, inHistName, CR)
    if not outputFile.GetDirectory(outHistDir):
        outputFile.mkdir(outHistDir)
    outputFile.cd(outHistDir)
    gDirectory.Delete("%s;*"%(hist.GetName()))
    print "%20s, %15s, %10s, %10s"%(inHistName, procDir, histNewName, round(hist.Integral()))
    hNew = hist.Rebin(len(getNewBins(inHistName))-1, histNewName, getNewBins(inHistName))
    hNew.Write()

def getHistData(inHistName, procDir, sysType):
    histDir = getHistDir(procDir, sysType, CR)
    #print "Hist: %s/%s"%(histDir, inHistName)
    hist = inFile.Get("%s/%s"%(histDir, inHistName)).Clone(sysType)
    return hist, procDir, sysType

def getHistAlone(inHistName, procDir, sysType, isIsolated):
    hList = []
    for sample in Samples:
        if sample in procDir:
            histDir = getHistDir(sample, sysType, CR)
            if isIsolated:
                h1 = inFile.Get("%s/%s_GenuinePhoton"%(histDir, inHistName))
                h2 = inFile.Get("%s/%s_MisIDEle"%(histDir, inHistName))
                h2.Scale(misIDSF)
            else:
                h1 = inFile.Get("%s/%s_HadronicPhoton"%(histDir, inHistName))
                h2 = inFile.Get("%s/%s_HadronicFake"%(histDir, inHistName))
            if "ZGamma" in sample:
                h1.Scale(zGammaSF)
                h2.Scale(zGammaSF)
            if "WGamma" in sample:
                h1.Scale(wGammaSF)
                h2.Scale(wGammaSF)
            hList.append(h1)
            hList.append(h2)
    return addHist(hList, sysType), procDir, sysType

def getHistOther(inHistName, procDir, sysType, isIsolated):
    hList = []
    sysType_ = sysType
    for sample in SamplesOther:
        if isQCDDD and sample=="QCD":
            sample  = "QCD_DD"
            sysType = "Base"
        histDir = getHistDir(sample, sysType, CR)
        if isIsolated:
            h1 = inFile.Get("%s/%s_GenuinePhoton"%(histDir, inHistName))
            h2 = inFile.Get("%s/%s_MisIDEle"%(histDir, inHistName))
            h2.Scale(misIDSF)
        else:
            h1 = inFile.Get("%s/%s_HadronicPhoton"%(histDir, inHistName))
            h2 = inFile.Get("%s/%s_HadronicFake"%(histDir, inHistName))
        if "ZJets" in sample:
            h1.Scale(zJetsSF)
            h2.Scale(zJetsSF)
        hList.append(h1)
        hList.append(h2)
    return addHist(hList, sysType), procDir, sysType_

#-----------------------------------------
#Functions for 0 photon
#----------------------------------------
def getHistAlone0Pho(inHistName, procDir, sysType):
    for sample in Samples:
        histDir = getHistDir(procDir, sysType, CR)
        if sample in procDir:
            h = inFile.Get("%s/%s"%(histDir, inHistName)).Clone(sysType)
            if "ZGamma" in sample:
                h.Scale(zGammaSF)
            if "WGamma" in sample:
                h.Scale(wGammaSF)
    return h, procDir, sysType

def getHistOther0Pho(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in SamplesOther:
        if isQCDDD and sample=="QCD":
            sample  = "QCD_DD"
            sysType = "Base"
        histDir = getHistDir(sample, sysType, CR)
        h = inFile.Get("%s/%s"%(histDir, inHistName))
        if "ZJets" in sample:
            h.Scale(zJetsSF)
        hList.append(h)
    return addHist(hList, sysType), procDir, sysType_

#-----------------------------------------
#Functions for Dilep 
#----------------------------------------
def getHistAloneDilep(inHistName, procDir, sysType):
    for sample in SampleDilep:
        histDir = getHistDir(sample, sysType, CR)
        if sample in procDir:
            h = inFile.Get("%s/%s"%(histDir, inHistName)).Clone(sysType)
    return h, procDir, sysType

def getHistOtherDilep(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in SampleDilepOther:
        if isQCDDD and sample=="QCD":
            sample  = "QCD_DD"
            sysType = "Base"
        histDir = getHistDir(sample, sysType, CR)
        h = inFile.Get("%s/%s"%(histDir, inHistName))
        hList.append(h)
    return addHist(hList, sysType), procDir, sysType_

#-----------------------------------------
#Functions for misID 
#----------------------------------------
def getHistAloneMisID(inHistName, procDir, sysType):
    hList = []
    for sample in SampleMisIDWZGamma:
        if sample in procDir:
            histDir = getHistDir(sample, sysType, CR)
            h1 = inFile.Get("%s/%s_GenuinePhoton"%(histDir, inHistName))
            h2 = inFile.Get("%s/%s_HadronicPhoton"%(histDir, inHistName))
            h3 = inFile.Get("%s/%s_HadronicFake"%(histDir, inHistName))
            hList.append(h1)
            hList.append(h2)
            hList.append(h3)
    return addHist(hList, sysType), procDir, sysType

def getHistOtherMisID(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in SampleMisIDOther:
        if isQCDDD and sample=="QCD":
            sample  = "QCD_DD"
            sysType = "Base"
        histDir = getHistDir(sample, sysType, CR)
        h1 = inFile.Get("%s/%s_GenuinePhoton"%(histDir, inHistName))
        h2 = inFile.Get("%s/%s_HadronicPhoton"%(histDir, inHistName))
        h3 = inFile.Get("%s/%s_HadronicFake"%(histDir, inHistName))
        hList.append(h1)
        hList.append(h2)
        hList.append(h3)
    return addHist(hList, sysType), procDir, sysType_

def getHistAllMisID(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in SampleMisIDAll:
        if isQCDDD and sample=="QCD":
            sample  = "QCD_DD"
            sysType = "Base"
        histDir = getHistDir(sample, sysType, CR)
        h = inFile.Get("%s/%s_MisIDEle"%(histDir, inHistName))
        hList.append(h)
    return addHist(hList, sysType), procDir, sysType_

#-----------------------------------------
#Categorise hists here
#----------------------------------------
allSysType = []
allSysType.append("Base")
for syst, level in itertools.product(Systematics, SystLevel):
    sysType = "%s%s"%(syst, level)
    allSysType.append(sysType)
writeList = []
for sysType in allSysType:
    if is0PhoM3:
        writeList.append(getHistData(inHistName, "data_obs", "Base"))
        writeList.append(getHistAlone0Pho(inHistName,  "TTGamma",  sysType))
        writeList.append(getHistAlone0Pho(inHistName,  "TTbar",    sysType))
        writeList.append(getHistAlone0Pho(inHistName,  "ZGamma",   sysType))
        writeList.append(getHistAlone0Pho(inHistName,  "WGamma",   sysType))
        writeList.append(getHistOther0Pho(inHistName, "Other",    sysType))
    elif isMassLepGamma:
        writeList.append(getHistData(inHistName, "data_obs", "Base"))
        writeList.append(getHistAloneMisID(inHistName,  "OtherPhotonsZGamma",  sysType))
        writeList.append(getHistAloneMisID(inHistName,  "OtherPhotonsWGamma",   sysType))
        writeList.append(getHistOtherMisID(inHistName, "OtherPhotonsOthers",   sysType))
        writeList.append(getHistAllMisID(inHistName,   "MisIDPhotonAll",    sysType))
    elif isMassDilep:
        writeList.append(getHistData(inHistName, "data_obs", "Base"))
        writeList.append(getHistAloneDilep(inHistName,  "ZJets",  sysType))
        writeList.append(getHistOtherDilep(inHistName, "Others",   sysType))
    else:
        writeList.append(getHistData(inHistName, "data_obs", "Base"))
        writeList.append(getHistAlone(inHistName,  "isolatedTTGamma",  sysType, True))
        writeList.append(getHistAlone(inHistName,  "isolatedTTbar",    sysType, True))
        writeList.append(getHistAlone(inHistName,  "isolatedZGamma",   sysType, True))
        writeList.append(getHistAlone(inHistName,  "isolatedWGamma",   sysType, True))
        writeList.append(getHistOther(inHistName, "isolatedOther",    sysType, True))
        writeList.append(getHistAlone(inHistName,  "nonPromptTTGamma", sysType, False))
        writeList.append(getHistAlone(inHistName,  "nonPromptTTbar",   sysType, False))
        writeList.append(getHistAlone(inHistName,  "nonPromptWGamma",  sysType, False))
        writeList.append(getHistAlone(inHistName,  "nonPromptZGamma",  sysType, False))
        writeList.append(getHistOther(inHistName, "nonPromptOther",   sysType, False))
for write in writeList:
    writeHist(write[0], write[1], write[2], outputFile)
outputFile.Close()
print outFileName
