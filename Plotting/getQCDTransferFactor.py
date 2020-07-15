from ROOT import *
import sys
from sampleInformation import *
import os
from optparse import OptionParser

gROOT.SetBatch(True)

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
(options, args) = parser.parse_args()

finalState = options.channel
if finalState in ["Mu","mu"]:
    sample = "QCDMu"
    outputFileName = "histograms/mu/qcdTransferFactors.root"
    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples_2019/qcdmuons/V08_00_26_07"
    preselCut = "passPresel_Mu"
    qcdRelIsoCut = "muPFRelIso>0.15 && muPFRelIso<0.3 && "
elif finalState in ["Ele","ele","e"]:
    sample = "QCDEle"
    outputFileName = "histograms/ele/qcdTransferFactors.root"
    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples_2019/qcdelectrons/V08_00_26_07"
    preselCut = "passPresel_Ele"
    qcdRelIsoCut = "elePFRelIso>0.01 &&"
else:
    print "Unknown final state"
    sys.exit()

outputFile = TFile(outputFileName,"recreate")


tree = TChain("AnalysisTree")
fileList = samples[sample][0]
for fileName in fileList:
    tree.Add("%s/QCDcr_%s"%(analysisNtupleLocation,fileName))

nJets  = 2
nBJets = 0

extraCuts       = "(%s && %s nJet>=%i && nBJet==%i)*"%(preselCut, qcdRelIsoCut, nJets, nBJets)
extraCutsPhoton = "(%s && %s nJet>=%i && nBJet==%i && phoMediumID)*"%(preselCut, qcdRelIsoCut, nJets, nBJets)

weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets

histCR    = TH1F("histNjet_QCDcr","histNjet_QCDcr",15,0,15)
histCRPho = TH1F("pho_histNjet_QCDcr","pho_histNjet_QCDcr",15,0,15)

tree.Draw("nJet>>histNjet_QCDcr",extraCuts+weights)
tree.Draw("nJet>>pho_histNjet_QCDcr",extraCutsPhoton+weights)
outputFile.cd()
histCR.Write()

extraCuts       = "(%s && %s nJet>=%i && nBJet==%i)*"%(preselCut, qcdRelIsoCut, nJets, nBJets)
extraCutsPhoton = "(%s && %s nJet>=%i && nBJet==%i && phoMediumID)*"%(preselCut, qcdRelIsoCut, nJets, nBJets)

weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets

histCR2    = TH1F("histNjet_QCDcr2","histNjet_QCDcr2",15,0,15)
histCR2Pho = TH1F("pho_histNjet_QCDcr2","pho_histNjet_QCDcr2",15,0,15)

tree.Draw("nJet>>histNjet_QCDcr2",extraCuts+weights)
tree.Draw("nJet>>pho_histNjet_QCDcr2",extraCutsPhoton+weights)
outputFile.cd()
histCR2.Write()

if finalState in ["Mu","mu"]:
    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples_2019/muons/V08_00_26_07"
else:
    analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples_2019/electrons/V08_00_26_07"

tree = TChain("AnalysisTree")
fileList = samples[sample][0]
for fileName in fileList:
    tree.Add("%s/%s"%(analysisNtupleLocation,fileName))

fileList = samples["GJets"][0]
for fileName in fileList:
    tree.Add("%s/%s"%(analysisNtupleLocation,fileName))

nJets  = 2
nBJets = 0
extraCuts       = "(%s && nJet>=%i && nBJet==%i)*"%(preselCut, nJets, nBJets)
extraCutsPhoton = "(%s && nJet>=%i && nBJet==%i && phoMediumID)*"%(preselCut, nJets, nBJets)

weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets
hist0 = TH1F("histNjet_0b","histNjet_0b",15,0,15)
hist0Pho = TH1F("pho_histNjet_0b","pho_histNjet_0b",15,0,15)

tree.Draw("nJet>>histNjet_0b",extraCuts+weights)
tree.Draw("nJet>>pho_histNjet_0b",extraCutsPhoton+weights)
outputFile.cd()

print hist0.Integral(4,-1), hist0.GetBinContent(1)
hist0.Write()

nJets  = 2
nBJets = 1
extraCuts       = "(%s && nJet>=%i && nBJet==%i)*"%(preselCut, nJets, nBJets)
extraCutsPhoton = "(%s && nJet>=%i && nBJet==%i && phoMediumID)*"%(preselCut, nJets, nBJets)

weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets
hist1 = TH1F("histNjet_1b","histNjet_1b",15,0,15)
hist1Pho = TH1F("pho_histNjet_1b","pho_histNjet_1b",15,0,15)

tree.Draw("nJet>>histNjet_1b",extraCuts+weights)
tree.Draw("nJet>>pho_histNjet_1b",extraCutsPhoton+weights)
outputFile.cd()
hist1.Write()

nJets  = 2
nBJets = 2
extraCuts       = "(%s && nJet>=%i && nBJet>=%i)*"%(preselCut, nJets, nBJets)
extraCutsPhoton = "(%s && nJet>=%i && nBJet>=%i && phoMediumID)*"%(preselCut, nJets, nBJets)

weights = "evtWeight*PUweight*muEffWeight*eleEffWeight*btagWeight[%i]"%nBJets
hist2 = TH1F("histNjet_2b","histNjet_2b",15,0,15)
hist2Pho = TH1F("pho_histNjet_2b","pho_histNjet_2b",15,0,15)

tree.Draw("nJet>>histNjet_2b",extraCuts+weights)
tree.Draw("nJet>>pho_histNjet_2b",extraCutsPhoton+weights)
outputFile.cd()
hist2.Write()

histCRPho.Write()
hist0Pho.Write()
hist1Pho.Write()
hist2Pho.Write()






hist0_TF = hist0.Clone("histNjet_0b_TF")
hist0_TF.SetNameTitle("histNjet_0b_TF","histNjet_0b_TF")
hist0_TF.Divide(histCR)

hist1_TF = hist1.Clone("histNjet_1b_TF")
hist1_TF.SetNameTitle("histNjet_1b_TF","histNjet_1b_TF")
hist1_TF.Divide(histCR)

hist2_TF = hist2.Clone("histNjet_2b_TF")
hist2_TF.SetNameTitle("histNjet_2b_TF","histNjet_2b_TF")
hist2_TF.Divide(histCR)

hist0_TF.Write()
hist1_TF.Write()
hist2_TF.Write()


hist_TF = TH1F("TransferFactors","TransferFactors",3,0,3)
hist_TFCR = TH1F("TransferFactorsCR","TransferFactorsCR",3,0,3)

histCR.Rebin(15)
print hist0.GetBinContent(1)
hist0.Rebin(15)
hist1.Rebin(15)
hist2.Rebin(15)
print hist0.GetBinContent(1), hist1.GetBinContent(1), hist2.GetBinContent(1)
hist_TF.SetBinContent(1,hist0.GetBinContent(1))
hist_TF.SetBinError(1,hist0.GetBinError(1))

hist_TF.SetBinContent(2,hist1.GetBinContent(1))
hist_TF.SetBinError(2,hist1.GetBinError(1))

hist_TF.SetBinContent(3,hist2.GetBinContent(1))
hist_TF.SetBinError(3,hist2.GetBinError(1))

hist_TFCR.SetBinContent(1,histCR.GetBinContent(1))
hist_TFCR.SetBinError(1,histCR.GetBinError(1))

hist_TFCR.SetBinContent(2,histCR.GetBinContent(1))
hist_TFCR.SetBinError(2,histCR.GetBinError(1))

hist_TFCR.SetBinContent(3,histCR.GetBinContent(1))
hist_TFCR.SetBinError(3,histCR.GetBinError(1))
print hist_TF.Integral(), hist_TFCR.Integral()
hist_TF.Divide(hist_TFCR)
hist_TF.Write()
print hist_TF.GetBinContent(1)


hist_TFPho = TH1F("TransferFactorsPho","TransferFactorsPho",3,0,3)
hist_TFCRPho = TH1F("TransferFactorsCRPho","TransferFactorsCRPho",3,0,3)

histCRPho.Rebin(15)
hist0Pho.Rebin(15)
hist1Pho.Rebin(15)
hist2Pho.Rebin(15)

hist_TFPho.SetBinContent(1,hist0Pho.GetBinContent(1))
hist_TFPho.SetBinError(1,hist0Pho.GetBinError(1))

hist_TFPho.SetBinContent(2,hist1Pho.GetBinContent(1))
hist_TFPho.SetBinError(2,hist1Pho.GetBinError(1))

hist_TFPho.SetBinContent(3,hist2Pho.GetBinContent(1))
hist_TFPho.SetBinError(3,hist2Pho.GetBinError(1))

hist_TFCRPho.SetBinContent(1,histCRPho.GetBinContent(1))
hist_TFCRPho.SetBinError(1,histCRPho.GetBinError(1))

hist_TFCRPho.SetBinContent(2,histCRPho.GetBinContent(1))
hist_TFCRPho.SetBinError(2,histCRPho.GetBinError(1))

hist_TFCRPho.SetBinContent(3,histCRPho.GetBinContent(1))
hist_TFCRPho.SetBinError(3,histCRPho.GetBinError(1))

hist_TFPho.Divide(hist_TFCRPho)
hist_TFPho.Write()


###################



hist_TF2 = TH1F("TransferFactors_CR2","TransferFactors_CR2",3,0,3)

histCR2.Rebin(15)

hist_TF2.SetBinContent(1,hist0.GetBinContent(1))
hist_TF2.SetBinError(1,hist0.GetBinError(1))

hist_TF2.SetBinContent(2,hist1.GetBinContent(1))
hist_TF2.SetBinError(2,hist1.GetBinError(1))

hist_TF2.SetBinContent(3,hist2.GetBinContent(1))
hist_TF2.SetBinError(3,hist2.GetBinError(1))

hist_TFCR.SetBinContent(1,histCR2.GetBinContent(1))
hist_TFCR.SetBinError(1,histCR2.GetBinError(1))

hist_TFCR.SetBinContent(2,histCR2.GetBinContent(1))
hist_TFCR.SetBinError(2,histCR2.GetBinError(1))

hist_TFCR.SetBinContent(3,histCR2.GetBinContent(1))
hist_TFCR.SetBinError(3,histCR2.GetBinError(1))

hist_TF2.Divide(hist_TFCR)
hist_TF2.Write()



hist_TFPho2 = TH1F("TransferFactorsPho_CR2","TransferFactorsPho_CR2",3,0,3)

histCR2Pho.Rebin(15)

hist_TFPho2.SetBinContent(1,hist0Pho.GetBinContent(1))
hist_TFPho2.SetBinError(1,hist0Pho.GetBinError(1))

hist_TFPho2.SetBinContent(2,hist1Pho.GetBinContent(1))
hist_TFPho2.SetBinError(2,hist1Pho.GetBinError(1))

hist_TFPho2.SetBinContent(3,hist2Pho.GetBinContent(1))
hist_TFPho2.SetBinError(3,hist2Pho.GetBinError(1))

hist_TFCRPho.SetBinContent(1,histCR2Pho.GetBinContent(1))
hist_TFCRPho.SetBinError(1,histCR2Pho.GetBinError(1))

hist_TFCRPho.SetBinContent(2,histCR2Pho.GetBinContent(1))
hist_TFCRPho.SetBinError(2,histCR2Pho.GetBinError(1))

hist_TFCRPho.SetBinContent(3,histCR2Pho.GetBinContent(1))
hist_TFCRPho.SetBinError(3,histCR2Pho.GetBinError(1))

hist_TFPho2.Divide(hist_TFCRPho)
hist_TFPho2.Write()


