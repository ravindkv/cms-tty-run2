from ROOT import TFile, TH1F, gDirectory
import os
import sys
import itertools
from optparse import OptionParser
from HistInputs import *

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
parser.add_option("--hist", "--hist", dest="inHistName", default="phosel_M3",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--cr", "--CR", dest="CR", default="",type='str', 
                     help="which control selection and region")
parser.add_option("--isQCDDD","--qcdMC",dest="isQCDDD", default=False, action="store_true",
		  help="")
parser.add_option("--is0Photon","--is0Photon",dest="is0Photon", default=False, action="store_true",
		  help="")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
inHistName           = options.inHistName
CR              = options.CR
isQCDDD         = options.isQCDDD
is0Photon       = options.is0Photon

#-----------------------------------------
#Path of the I/O histograms/datacards
#----------------------------------------
inFile = TFile("%s/Hists/%s/%s/%s/Merged/AllInc.root"%(condorHistDir, year, decayMode, channel))
outFileName = "%s/Hists/%s/%s/%s/Merged/AllCat.root"%(condorHistDir, year, decayMode, channel)
outputFile = TFile(outFileName,"update")
#histList = ["phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake", "phosel_noCut_ChIso_GenuinePhoton","phosel_noCut_ChIso_MisIDEle","phosel_noCut_ChIso_HadronicPhoton","phosel_noCut_ChIso_HadronicFake"]
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

def writeHist(hist, procDir, histNewName, outputFile):
    if CR=="":
        outHistDir = "%s/SR/%s"%(inHistName, procDir)
    else:
        outHistDir = "%s/CR/%s/%s"%(inHistName,CR,procDir)
    if not outputFile.GetDirectory(outHistDir):
        outputFile.mkdir(outHistDir)
    outputFile.cd(outHistDir)
    gDirectory.Delete("%s;*"%(hist.GetName()))
    print "%s, \t%s, \t%s, \t%s"%(inHistName, procDir, histNewName, hist.Integral())
    hist.Write()

def getHistData(inHistName, procDir, sysType):
    if CR=="":
        histDir = "%s/%s/SR"%(procDir, sysType)
    else:
        histDir = "%s/%s/CR/%s"%(procDir, sysType, CR)
    hist = inFile.Get("%s/%s"%(histDir, inHistName)).Clone(sysType)
    return hist, procDir, sysType

def getHistMain(inHistName, procDir, sysType, isIsolated):
    hList = []
    for sample in Samples:
        if CR=="":
            histDir = "%s/%s/SR"%(sample, sysType)
        else:
            histDir = "%s/%s/CR/%s"%(sample, sysType, CR)
        if sample in procDir:
            if isIsolated:
                h1 = inFile.Get("%s/%s_GenuinePhoton"%(histDir, inHistName))
                h2 = inFile.Get("%s/%s_MisIDEle"%(histDir, inHistName))
            else:
                h1 = inFile.Get("%s/%s_HadronicPhoton"%(histDir, inHistName))
                h2 = inFile.Get("%s/%s_HadronicFake"%(histDir, inHistName))
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
        if CR=="":
            histDir = "%s/%s/SR"%(sample, sysType)
        else:
            histDir = "%s/%s/CR/%s"%(sample, sysType, CR)
        if isIsolated:
            h1 = inFile.Get("%s/%s_GenuinePhoton"%(histDir, inHistName))
            h2 = inFile.Get("%s/%s_MisIDEle"%(histDir, inHistName))
        else:
            h1 = inFile.Get("%s/%s_HadronicPhoton"%(histDir, inHistName))
            h2 = inFile.Get("%s/%s_HadronicFake"%(histDir, inHistName))
        hList.append(h1)
        hList.append(h2)
    return addHist(hList, sysType), procDir, sysType_

def getHistMain0Photon(inHistName, procDir, sysType):
    for sample in Samples:
        if CR=="":
            histDir = "%s/%s/SR"%(sample, sysType)
        else:
            histDir = "%s/%s/CR/%s"%(sample, sysType, CR)
        if sample in procDir:
            h = inFile.Get("%s/%s"%(histDir, inHistName))
    return h, procDir, sysType

def getHistOther0Photon(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in SamplesOther:
        if isQCDDD and sample=="QCD":
            sample  = "QCD_DD"
            sysType = "Base"
        if CR=="":
            histDir = "%s/%s/SR"%(sample, sysType)
        else:
            histDir = "%s/%s/CR/%s"%(sample, sysType, CR)
        h = inFile.Get("%s/%s"%(histDir, inHistName))
        hList.append(h)
    return addHist(hList, sysType), procDir, sysType_

allSysType = []
allSysType.append("Base")
for syst, level in itertools.product(Systematics, SystLevel):
    sysType = "%s%s"%(syst, level)
    allSysType.append(sysType)
writeList = []
writeList.append(getHistData(inHistName, "data_obs", "Base"))
for sysType in allSysType:
    if is0Photon:
        writeList.append(getHistMain0Photon(inHistName,  "TTGamma",  sysType))
        writeList.append(getHistMain0Photon(inHistName,  "TTbar",    sysType))
        writeList.append(getHistMain0Photon(inHistName,  "ZGamma",   sysType))
        writeList.append(getHistMain0Photon(inHistName,  "WGamma",   sysType))
        writeList.append(getHistOther0Photon(inHistName, "Other",    sysType))
    else:
        writeList.append(getHistMain(inHistName,  "isolatedTTGamma",  sysType, True))
        writeList.append(getHistMain(inHistName,  "isolatedTTbar",    sysType, True))
        writeList.append(getHistMain(inHistName,  "isolatedZGamma",   sysType, True))
        writeList.append(getHistMain(inHistName,  "isolatedWGamma",   sysType, True))
        writeList.append(getHistOther(inHistName, "isolatedOther",    sysType, True))
        writeList.append(getHistMain(inHistName,  "nonPromptTTGamma", sysType, False))
        writeList.append(getHistMain(inHistName,  "nonPromptTTbar",   sysType, False))
        writeList.append(getHistMain(inHistName,  "nonPromptWGamma",  sysType, False))
        writeList.append(getHistMain(inHistName,  "nonPromptZGamma",  sysType, False))
        writeList.append(getHistOther(inHistName, "nonPromptOther",   sysType, False))
for write in writeList:
    writeHist(write[0], write[1], write[2], outputFile)
outputFile.Close()
print outFileName
