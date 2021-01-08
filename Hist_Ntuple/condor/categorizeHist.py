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
#inFile = TFile("%s/Hists/%s/%s/%s/Merged/AllInc.root"%(condorHistDir, year, decayMode, channel), "read")
inFile = TFile.Open("root://cmsxrootd.fnal.gov/%s/Hists/%s/%s/%s/Merged/AllInc.root"%(condorHistDir, year, decayMode, channel), "read")
outFileName = "AllCat_%s.root"%(inHistName)
print inFile
print outFileName
outputFile = TFile(outFileName,"update")
print outputFile

#-----------------------------------------
#Rebinning scheme of the histograms
#----------------------------------------
if isCount:
    newBinsM3 = numpy.array([50.,500.])
    newBinsChIso = numpy.array([0.,20.])
    newBinsDilep = numpy.array([80.,102.]) 
    newBinsMisID = numpy.array([0,180.])
else:
    newBinsM3 = numpy.array([50.,  100., 125., 150., 175., 200.,250., 300., 500.])
    newBinsChIso = numpy.array([0.5, 1., 2., 5., 12., 20.])
    #newBinsChIso = numpy.array([ 0., 0.5, 1., 2., 5., 12., 20.])
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

def getHistAlone(inHistName, procDir, sysType, isIsolated, isMisId):
    hList = []
    for sample in Samples:
        if sample in procDir:
            histDir = getHistDir(sample, sysType, CR)
            if isIsolated:
                if isMisId:
                    h1 = inFile.Get("%s/%s_MisIDEle"%(histDir, inHistName))
                else:
                    h1 = inFile.Get("%s/%s_GenuinePhoton"%(histDir, inHistName))
                hList.append(h1)
            else:
                h1 = inFile.Get("%s/%s_HadronicPhoton"%(histDir, inHistName))
                h2 = inFile.Get("%s/%s_HadronicFake"%(histDir, inHistName))
                hList.append(h1)
                hList.append(h2)
    return addHist(hList, sysType), procDir, sysType

def getHistOther(inHistName, procDir, sysType, isIsolated, isMisId):
    hList = []
    sysType_ = sysType
    for sample in SamplesOther:
        if isQCDDD and sample=="QCD":
            sample  = "QCD_DD"
            sysType = "Base"
        histDir = getHistDir(sample, sysType, CR)
        if isIsolated:
            if isMisId:
                h1 = inFile.Get("%s/%s_MisIDEle"%(histDir, inHistName))
            else:
                h1 = inFile.Get("%s/%s_GenuinePhoton"%(histDir, inHistName))
            hList.append(h1)
        else:
            h1 = inFile.Get("%s/%s_HadronicPhoton"%(histDir, inHistName))
            h2 = inFile.Get("%s/%s_HadronicFake"%(histDir, inHistName))
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
    return h, procDir, sysType

def getHistOther0Pho(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in SamplesOther0Pho:
        if isQCDDD and sample=="QCD":
            sample  = "QCD_DD"
            sysType = "Base"
        histDir = getHistDir(sample, sysType, CR)
        h = inFile.Get("%s/%s"%(histDir, inHistName))
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
def getHistAloneMassLG(inHistName, procDir, sysType):
    hList = []
    for sample in SampleWZGammaMassLG:
        if sample in procDir:
            histDir = getHistDir(sample, sysType, CR)
            h1 = inFile.Get("%s/%s_GenuinePhoton"%(histDir, inHistName))
            h2 = inFile.Get("%s/%s_HadronicPhoton"%(histDir, inHistName))
            h3 = inFile.Get("%s/%s_HadronicFake"%(histDir, inHistName))
            hList.append(h1)
            hList.append(h2)
            hList.append(h3)
    return addHist(hList, sysType), procDir, sysType

def getHistOtherMassLG(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in SampleOtherMassLG:
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

def getHistAloneMisIDMassLG(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in SampleAllMassLG:
        if sample in procDir:
            histDir = getHistDir(sample, sysType, CR)
            h = inFile.Get("%s/%s_MisIDEle"%(histDir, inHistName))
            hList.append(h)
    return addHist(hList, sysType), procDir, sysType_

def getHistOtherMisIDMassLG(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in SampleNoZJetsMassLG:
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
    writeList.append(getHistData(inHistName, "data_obs", "Base"))
    if is0PhoM3:
        writeList.append(getHistAlone0Pho(inHistName,  "TTGamma",  sysType))
        writeList.append(getHistAlone0Pho(inHistName,  "TTbar",    sysType))
        writeList.append(getHistAlone0Pho(inHistName,  "ZGamma",   sysType))
        writeList.append(getHistAlone0Pho(inHistName,  "WGamma",   sysType))
        writeList.append(getHistAlone0Pho(inHistName,  "ZJets",    sysType))
        writeList.append(getHistOther0Pho(inHistName,  "Other",    sysType))
    elif isMassLepGamma:
        writeList.append(getHistAloneMassLG(inHistName,     "OtherPhotonsZGamma",  sysType))
        writeList.append(getHistAloneMassLG(inHistName,     "OtherPhotonsWGamma",  sysType))
        writeList.append(getHistAloneMassLG(inHistName,     "OtherPhotonsZJets",   sysType))
        writeList.append(getHistOtherMassLG(inHistName,     "OtherPhotonsOthers",  sysType))
        writeList.append(getHistAloneMisIDMassLG(inHistName,"MisIdPhotonZJets",    sysType))
        writeList.append(getHistOtherMisIDMassLG(inHistName,"MisIdPhotonOther",    sysType))
    elif isMassDilep:
        writeList.append(getHistAloneDilep(inHistName,  "ZJetsDilep",  sysType))
        writeList.append(getHistOtherDilep(inHistName,  "OthersDilep",   sysType))
    else:
        #misID
        writeList.append(getHistAlone(inHistName,  "MisIdTTGamma",  sysType, True, True))
        writeList.append(getHistAlone(inHistName,  "MisIdTTbar",    sysType, True, True))
        writeList.append(getHistAlone(inHistName,  "MisIdWGamma",   sysType, True, True))
        writeList.append(getHistAlone(inHistName,  "MisIdZGamma",   sysType, True, True))
        writeList.append(getHistAlone(inHistName,  "MisIdZJets",    sysType, True, True))
        writeList.append(getHistOther(inHistName,  "MisIdOther",    sysType, True, True))
        #genuine
        writeList.append(getHistAlone(inHistName,  "GenuineTTGamma",  sysType, True, False))
        writeList.append(getHistAlone(inHistName,  "GenuineTTbar",    sysType, True, False))
        writeList.append(getHistAlone(inHistName,  "GenuineWGamma",   sysType, True, False))
        writeList.append(getHistAlone(inHistName,  "GenuineZGamma",   sysType, True, False))
        writeList.append(getHistAlone(inHistName,  "GenuineZJets",    sysType, True, False))
        writeList.append(getHistOther(inHistName,  "GenuineOther",    sysType, True, False))
        #other
        writeList.append(getHistAlone(inHistName,  "NonPromptTTGamma", sysType, False, False))
        writeList.append(getHistAlone(inHistName,  "NonPromptTTbar",   sysType, False, False))
        writeList.append(getHistAlone(inHistName,  "NonPromptWGamma",  sysType, False, False))
        writeList.append(getHistAlone(inHistName,  "NonPromptZGamma",  sysType, False, False))
        writeList.append(getHistAlone(inHistName,  "NonPromptZJets",   sysType, False, False))
        writeList.append(getHistOther(inHistName,  "NonPromptOther",   sysType, False, False))
for write in writeList:
    writeHist(write[0], write[1], write[2], outputFile)
outputFile.Close()
print outFileName
