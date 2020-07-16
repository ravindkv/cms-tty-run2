from ROOT import *
import sys
from sampleInformation import *
import os
from optparse import OptionParser
gROOT.SetBatch(True)
parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s","--systematic", dest="systematic", default="nominal",type='str',
                     help="Specify up, down or nominal, default is nominal")
(options, args) = parser.parse_args()

finalState = options.channel

sample = sys.argv[-1]


if finalState=="Mu":
    sampleList[-1] = "DataMu"
    sampleList[-2] = "QCDMu"
    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/"
    outputhistName = "histograms/mu/JetBjetMultiplicityHists.root"
    if sample == "Data": sample = "DataMu"
    if sample == "QCD": 
        sample = "QCDMu"
        analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/2016"

if finalState=="Ele":
    sampleList[-1] = "DataEle"
    sampleList[-2] = "QCDEle"
    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/2016"
    outputhistName = "histograms/ele/JetBjetMultiplicityHists.root"
    if sample == "Data": sample = "DataEle"
    if sample == "QCD": 
        sample = "QCDEle"
        analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/QCD_controlRegion/2016"



if not sample in sampleList:
    print sample
    print "Sample isn't in list"
    print sampleList
    sys.exit()


tree = TChain("AnalysisTree")
if not "QCD" in sample:
    fileList = samples[sample][0]
    for fileName in fileList:
    
        tree.Add("%s/%s"%(analysisNtupleLocation,fileName))

print sample

print "Number of events:", tree.GetEntries()

hist_njets0Tag = TH1F("njets0Tag_%s"%sample,"njets0Tag_%s"%sample,10,0,10)
hist_njets1Tag = TH1F("njets1Tag_%s"%sample,"njets1Tag_%s"%sample,10,0,10)
hist_njets2Tag = TH1F("njets2Tag_%s"%sample,"njets2Tag_%s"%sample,10,0,10)
hist_phoselnjets0Tag = TH1F("phoselnjets0Tag_%s"%sample,"phoselnjets0Tag_%s"%sample,10,0,10)
hist_phoselnjets1Tag = TH1F("phoselnjets1Tag_%s"%sample,"phoselnjets1Tag_%s"%sample,10,0,10)
hist_phoselnjets2Tag = TH1F("phoselnjets2Tag_%s"%sample,"phoselnjets2Tag_%s"%sample,10,0,10)

preselCut = "passPresel_Ele"
QCDcut = "elePFRelIso>0.01"
if finalState=="Mu":
    preselCut = "passPresel_Mu"
    QCDcut = "muPFRelIso> 0.15 && muPFRelIso<0.3"



if "QCD" in sample:
    print "Making QCD Data Driven Template"

    QCDTemplate = TH1F("njets0Tag_QCD_DD","njets0Tag_QCD_DD",10,0,10)
    PhoselQCDTemplate = TH1F("phoselnjets0Tag_QCD_DD","phoselnjets0Tag_QCD_DD",10,0,10)
    tree = TChain("AnalysisTree")
    fileList = samples[sampleList[-1]][0]
    print "samples: ", samples
    print "sampleList: ", sampleList
    print "fileList: ", fileList
    print fileList
    for fileName in fileList:
        tree.Add("%s/QCDcr_%s"%(analysisNtupleLocation,fileName))

    tree.Draw("nJet>>njets0Tag_QCD_DD","(%s && nBJet==0 && %s)"%(preselCut,QCDcut))
    tree.Draw("nJet>>phoselnjets0Tag_QCD_DD","(nPho>=1 && nBJet==0 && %s && %s)"%(preselCut,QCDcut))

    tempHist       = TH1F("njets0Tag_temp","njets0Tag_temp",10,0,10)
    PhoseltempHist = TH1F("phoselnjets0Tag_temp","phoselnjets0Tag_temp",10,0,10)
    tree = TChain("AnalysisTree")
    print sampleList[:]
    print sampleList[:-3]
    for s in sampleList[:-3]:

        fileList = samples[s][0]
        for fileName in fileList:
	    print fileName
            tree.Add("%s/QCDcr_%s"%(analysisNtupleLocation,fileName))

    tree.Draw("nJet>>njets0Tag_temp","(%s && nBJet==0 && %s)*evtWeight*muEffWeight*eleEffWeight*PUweight"%(preselCut,QCDcut))
    tree.Draw("nJet>>phoselnjets0Tag_temp","(nPho>=1 && nBJet==0 && %s && %s)*evtWeight*muEffWeight*eleEffWeight*PUweight"%(preselCut,QCDcut))

    QCDTemplate.Add(tempHist,-1)
    PhoselQCDTemplate.Add(PhoseltempHist,-1)

    for i in range(1,11):
        if QCDTemplate.GetBinContent(i)<0:
            QCDTemplate.SetBinContent(i,0)
        if PhoselQCDTemplate.GetBinContent(i)<0:
            PhoselQCDTemplate.SetBinContent(i,0)


    outputFile = TFile(outputhistName,"update")
    outputFile.rmdir(sample)
    outputFile.mkdir(sample)
    outputFile.cd(sample)
    QCDTemplate.Write()
    PhoselQCDTemplate.Write()
    outputFile.Close()
    sys.exit(0)
else:
    tree.Draw("nJet>>njets0Tag_%s"%sample,      "(%s && nBJet==0)*evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[0]"%preselCut)
    tree.Draw("nJet>>njets1Tag_%s"%sample,      "(%s && nBJet==1)*evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[1]"%preselCut)
    tree.Draw("nJet>>njets2Tag_%s"%sample,      "(%s && nBJet==2)*evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"%preselCut)
    tree.Draw("nJet>>phoselnjets0Tag_%s"%sample,"(nPho>=1 && nBJet==0 && %s)*evtWeight*PUweight*muEffWeight*eleEffWeight*phoEffWeight[0]*btagWeight[0]"%preselCut)
    tree.Draw("nJet>>phoselnjets1Tag_%s"%sample,"(nPho>=1 && nBJet==1 && %s)*evtWeight*PUweight*muEffWeight*eleEffWeight*phoEffWeight[0]*btagWeight[1]"%preselCut)
    tree.Draw("nJet>>phoselnjets2Tag_%s"%sample,"(nPho>=1 && nBJet==2 && %s)*evtWeight*PUweight*muEffWeight*eleEffWeight*phoEffWeight[0]*btagWeight[2]"%preselCut)

# elif not "Data" in sample:
#     tree.Draw("nJet>>njets0Tag_%s"%sample,      "(%s)*evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[0]"%preselCut)
#     tree.Draw("nJet>>njets1Tag_%s"%sample,      "(%s)*evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[1]"%preselCut)
#     tree.Draw("nJet>>njets2Tag_%s"%sample,      "(%s)*evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"%preselCut)
#     tree.Draw("nJet>>phoselnjets0Tag_%s"%sample,"(phoMediumID && %s)*evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[0]"%preselCut)
#     tree.Draw("nJet>>phoselnjets1Tag_%s"%sample,"(phoMediumID && %s)*evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[1]"%preselCut)
#     tree.Draw("nJet>>phoselnjets2Tag_%s"%sample,"(phoMediumID && %s)*evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[2]"%preselCut)
# else:
#     tree.Draw("nJet>>njets0Tag_%s"%sample,      "(%s && nBJet==0)"%preselCut)
#     tree.Draw("nJet>>njets1Tag_%s"%sample,      "(%s && nBJet==1)"%preselCut)
#     tree.Draw("nJet>>njets2Tag_%s"%sample,      "(%s && nBJet>=2)"%preselCut)
#     tree.Draw("nJet>>phoselnjets0Tag_%s"%sample,"(phoMediumID && %s && nBJet==0)"%preselCut)
#     tree.Draw("nJet>>phoselnjets1Tag_%s"%sample,"(phoMediumID && %s && nBJet==1)"%preselCut)
#     tree.Draw("nJet>>phoselnjets2Tag_%s"%sample,"(phoMediumID && %s && nBJet>=2)"%preselCut)
    


# histograms = []
# for h_Info in histogramInfo:
#     print "filling", h_Info[1], sample
#     evtWeight = ""
#     histograms.append(TH1F("%s_%s"%(h_Info[1],sample),"%s_%s"%(h_Info[1],sample),h_Info[2][0],h_Info[2][1],h_Info[2][2]))
#     if h_Info[-1]=="":
#         evtWeight = "%s%s"%(h_Info[3],weights)
#     else:
#         evtWeight = h_Info[-1]
        
#     if "Data" in sample:
#         evtWeight = h_Info[3]

#     if evtWeight[-1]=="*":
#         evtWeight= evtWeight[:-1]
#     tree.Draw("%s>>%s_%s"%(h_Info[0],h_Info[1],sample),evtWeight)


outputFile = TFile(outputhistName,"update")
outputFile.rmdir(sample)
outputFile.mkdir(sample)
outputFile.cd(sample)

hist_njets0Tag.Write()
hist_njets1Tag.Write()
hist_njets2Tag.Write()
hist_phoselnjets0Tag.Write()
hist_phoselnjets1Tag.Write()
hist_phoselnjets2Tag.Write()

outputFile.Close()
