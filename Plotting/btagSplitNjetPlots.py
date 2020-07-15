####
# make pdf figures of the Njet/Nbjet bins
# uses output files created with btagSplitNjetHistograms.py
####

from ROOT import *
import os
import CMS_lumi
from numpy import log10
from optparse import OptionParser

gROOT.SetBatch(True)

padRatio = 0.25
padOverlap = 0.15
padGap = 0.01
parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s","--systematic", dest="systematic", default="nominal",type='str',
                     help="Specify up, down or nominal, default is nominal")
parser.add_option("--Presel","--presel","--runPresel", dest="runPresel", default=False,action="store_true",
                     help="Specify whether to run presel")
parser.add_option("--no0","--nozero","--noZero", dest="useZero", default=True,action="store_false",
                     help="Specify whether to plot the 0b bins")
(options, args) = parser.parse_args()

finalState = options.channel

runPresel = options.runPresel

useZero = options.useZero

TGaxis.SetMaxDigits(3)

from Style import *
thestyle = Style()
HasCMSStyle = False
style = None
if os.path.isfile('tdrstyle.C'):
    ROOT.gROOT.ProcessLine('.L tdrstyle.C')
    ROOT.setTDRStyle()
    print "Found tdrstyle.C file, using this style."
    HasCMSStyle = True
    if os.path.isfile('CMSTopStyle.cc'):
        gROOT.ProcessLine('.L CMSTopStyle.cc+')
        style = CMSTopStyle()
        style.setupICHEPv1()
        print "Found CMSTopStyle.cc file, use TOP style if requested in xml file."
if not HasCMSStyle:
    print "Using default style defined in cuy package."
    thestyle.SetStyle()

ROOT.gROOT.ForceStyle()
H = 600;
W = 800;

canvas = TCanvas('c1','c1',W,H)
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(0)
canvasRatio = TCanvas('c1Ratio','c1Ratio',W,H)
canvasRatio.SetFillColor(0)
canvasRatio.SetBorderMode(0)
canvasRatio.SetFrameFillStyle(0)
canvasRatio.SetFrameBorderMode(0)
canvasRatio.SetLeftMargin( L/W )
canvasRatio.SetRightMargin( R/W )
canvasRatio.SetTopMargin( T/H )
canvasRatio.SetBottomMargin( B/H )
canvasRatio.SetTickx(0)
canvasRatio.SetTicky(0)

pad1 = TPad("p1","p1",0,padRatio-padOverlap,1,1)
pad2 = TPad("p2","p2",0,0,1,padRatio+padOverlap)
pad1.SetLeftMargin( L/W )
pad1.SetRightMargin( R/W )
pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
pad2.SetLeftMargin( L/W )
pad2.SetRightMargin( R/W )
pad2.SetTopMargin( (padOverlap)/(padRatio+padOverlap) )
pad2.SetBottomMargin( B/H/(padRatio+padOverlap) )

pad1.SetFillColor(0)
pad1.SetBorderMode(0)
pad1.SetFrameFillStyle(0)
pad1.SetFrameBorderMode(0)
pad1.SetTickx(0)
pad1.SetTicky(0)

pad2.SetFillColor(0)
pad2.SetFillStyle(4000)
pad2.SetBorderMode(0)
pad2.SetFrameFillStyle(0)
pad2.SetFrameBorderMode(0)
pad2.SetTickx(0)
pad2.SetTicky(0)

SetOwnership(canvas, False)
SetOwnership(canvasRatio, False)
SetOwnership(pad1, False)
SetOwnership(pad2, False)

#canvasRatio.cd()
#canvasRatio.SetLogy()
pad1.Draw()
pad2.Draw()


canvas.cd()
mcList = {'TTGamma': [kOrange],
          'TTbar': [kRed+1],
          'TGJets':[kGray],
          'TTV': [kRed-7],
          'SingleTop': [kOrange-3],
          'WGamma': [kBlue-4],
          'ZGamma': [kBlue-2],
          'WJets': [kCyan-3],
          'ZJets': [kCyan-5],
          'Diboson': [kCyan+4],
          'QCDMu': [kGreen+3],
          'QCDEle': [kGreen+3],
          }

outputDir = ""
if finalState=="Mu":
	_file = TFile("histograms/mu/JetBjetMultiplicityHists.root","read")
        _qcdInputFile = TFile("histograms/mu/qcdTransferFactors.root","read")
        outputDir = "plots_mu"
	samples = ['TTGamma',
                   'TTbar',
                   'TGJets',
                   'WGamma',
                   'ZGamma',
                   'ZJets',
                   'WJets',
                   'SingleTop',
                   'TTV',
                   'Diboson',
                   'QCDMu',
                   'DataMu',
                   ]


if finalState=="Ele":
	_file = TFile("histograms/ele/JetBjetMultiplicityHists.root","read")
        _qcdInputFile = TFile("histograms/ele/qcdTransferFactors.root","read")
        outputDir = "plots_ele"
	samples = ['TTGamma',	  
                   'TTbar',
                   'TGJets',	  
                   'WGamma',	  
                   'ZGamma',	  
                   'ZJets',	  
                   'WJets',
                   'SingleTop', 
                   'TTV',	  	  
                   'Diboson',
                   'QCDEle',
                   'DataEle',	  
                   ]


histograms = []

for s in samples:   
    print s 
    if useZero:
        histograms.append(TH1F("jbMult_%s"%s,"jbMult_%s"%s,15,0,15))
    else:
        histograms.append(TH1F("jbMult_%s"%s,"jbMult_%s"%s,10,0,10))
    if not "QCD" in s:
        if runPresel:
            h0 = _file.Get("%s/njets0Tag_%s"%(s,s))
            h1 = _file.Get("%s/njets1Tag_%s"%(s,s))
            h2 = _file.Get("%s/njets2Tag_%s"%(s,s))
        else:
            h0 = _file.Get("%s/phoselnjets0Tag_%s"%(s,s))
            h1 = _file.Get("%s/phoselnjets1Tag_%s"%(s,s))
            h2 = _file.Get("%s/phoselnjets2Tag_%s"%(s,s))
    else:
        h0 = _file.Get("QCD%s/njets0Tag_QCD_DD"%finalState).Clone("histNjet_0b")
        h1 = _file.Get("QCD%s/njets0Tag_QCD_DD"%finalState).Clone("histNjet_1b")
        h2 = _file.Get("QCD%s/njets0Tag_QCD_DD"%finalState).Clone("histNjet_2b")
        if not runPresel:
            h0 = _file.Get("QCD%s/phoselnjets0Tag_QCD_DD"%finalState).Clone("pho_histNjet_0b")
            h1 = _file.Get("QCD%s/phoselnjets0Tag_QCD_DD"%finalState).Clone("pho_histNjet_1b")
            h2 = _file.Get("QCD%s/phoselnjets0Tag_QCD_DD"%finalState).Clone("pho_histNjet_2b")

        hTR = _qcdInputFile.Get("TransferFactors")
	print hTR.GetBinContent(1), hTR.GetBinContent(2), hTR.GetBinContent(3)
        print "original:", h0.Integral(4,-1)
        h0.Scale(hTR.GetBinContent(1))
        h1.Scale(hTR.GetBinContent(2))
        h2.Scale(hTR.GetBinContent(3))

#    print s
    for i in range(4):
        if useZero:
            histograms[-1].SetBinContent(i+1,h0.GetBinContent(3+i))
            histograms[-1].SetBinContent(i+6,h1.GetBinContent(3+i))
            histograms[-1].SetBinContent(i+11,h2.GetBinContent(3+i))
            
            histograms[-1].SetBinError(i+1,h0.GetBinError(3+i))
            histograms[-1].SetBinError(i+6,h1.GetBinError(3+i))
            histograms[-1].SetBinError(i+11,h2.GetBinError(3+i))
        else:
            histograms[-1].SetBinContent(i+1,h1.GetBinContent(3+i))
            histograms[-1].SetBinContent(i+6,h2.GetBinContent(3+i))

            histograms[-1].SetBinError(i+1,h1.GetBinError(3+i))
            histograms[-1].SetBinError(i+6,h2.GetBinError(3+i))
   

    errorVal = Double(0)
    if useZero:
        integral = h0.IntegralAndError(7,-1,errorVal)
        histograms[-1].SetBinContent(5 ,integral)
        histograms[-1].SetBinError(5 ,errorVal)
        
        integral = h1.IntegralAndError(7,-1,errorVal)
        histograms[-1].SetBinContent(10 ,integral)
        histograms[-1].SetBinError(10 ,errorVal)
        
        integral = h2.IntegralAndError(7,-1,errorVal)
        histograms[-1].SetBinContent(15 ,integral)
        histograms[-1].SetBinError(15 ,errorVal)
    else:
        integral = h1.IntegralAndError(7,-1,errorVal)
        histograms[-1].SetBinContent(5 ,integral)
        histograms[-1].SetBinError(5 ,errorVal)
        
        integral = h2.IntegralAndError(7,-1,errorVal)
        histograms[-1].SetBinContent(10 ,integral)
        histograms[-1].SetBinError(10 ,errorVal)
        
    if not "Data" in s:
        histograms[-1].SetFillColor(mcList[s][0])
        histograms[-1].SetLineColor(mcList[s][0])
    else:
        histograms[-1].SetFillColor(h1.GetFillColor())
        histograms[-1].SetLineColor(h1.GetLineColor())
        histograms[-1].SetMarkerSize(h1.GetMarkerSize())
        histograms[-1].SetMarkerStyle(20)
        histograms[-1].SetMarkerColor(kBlack)
    if useZero:
        histograms[-1].GetXaxis().SetBinLabel(1,"=2j=0b")
        histograms[-1].GetXaxis().SetBinLabel(2,"=3j=0b")
        histograms[-1].GetXaxis().SetBinLabel(3,"=4j=0b")
        histograms[-1].GetXaxis().SetBinLabel(4,"=5j=0b")
        histograms[-1].GetXaxis().SetBinLabel(5,"#geq6j=0b")
        histograms[-1].GetXaxis().SetBinLabel(6,"=2j=1b")
        histograms[-1].GetXaxis().SetBinLabel(7,"=3j=1b")
        histograms[-1].GetXaxis().SetBinLabel(8,"=4j=1b")
        histograms[-1].GetXaxis().SetBinLabel(9,"=5j=1b")
        histograms[-1].GetXaxis().SetBinLabel(10,"#geq6j=1b")
        histograms[-1].GetXaxis().SetBinLabel(11,"=2j#geq2b")
        histograms[-1].GetXaxis().SetBinLabel(12,"=3j#geq2b")
        histograms[-1].GetXaxis().SetBinLabel(13,"=4j#geq2b")
        histograms[-1].GetXaxis().SetBinLabel(14,"=5j#geq2b")
        histograms[-1].GetXaxis().SetBinLabel(15,"#geq6j#geq2b")
    else:
        histograms[-1].GetXaxis().SetBinLabel(1,"=2j=1b")
        histograms[-1].GetXaxis().SetBinLabel(2,"=3j=1b")
        histograms[-1].GetXaxis().SetBinLabel(3,"=4j=1b")
        histograms[-1].GetXaxis().SetBinLabel(4,"=5j=1b")
        histograms[-1].GetXaxis().SetBinLabel(5,"#geq6j=1b")
        histograms[-1].GetXaxis().SetBinLabel(6,"=2j#geq2b")
        histograms[-1].GetXaxis().SetBinLabel(7,"=3j#geq2b")
        histograms[-1].GetXaxis().SetBinLabel(8,"=4j#geq2b")
        histograms[-1].GetXaxis().SetBinLabel(9,"=5j#geq2b")
        histograms[-1].GetXaxis().SetBinLabel(10,"#geq6j#geq2b")
        
    histograms[-1].GetXaxis().SetLabelSize(0.07)


systLegendEntry = TH1F("syst","syst",1,0,1)
systLegendEntry.SetFillColor(kGray+2)
systLegendEntry.SetLineWidth(0)
systLegendEntry.SetFillStyle(3245)
systLegendEntry.SetMarkerSize(0)

legendHeightPer = 0.04
legendwidth =  1-R/W-0.73
legendNColumns = 2


legend1 = TLegend(1-R/W-0.03-2*legendwidth, 1-T/H-0.01 - legendHeightPer*(round((1+len(samples))/2.)), 1-R/W-0.03 - legendwidth, 1-(T/H)-0.01)
legend2 = TLegend(1-R/W-0.03-legendwidth, 1-T/H-0.01 - legendHeightPer*(int((1+len(samples))/2.)), 1-R/W-0.03, 1-(T/H)-0.01)


legend1.SetBorderSize(0)
legend1.SetFillColor(0)
legend1.SetLineColor(0)
legend2.SetBorderSize(0)
legend2.SetFillColor(0)
legend2.SetLineColor(0)

legendR1 = TLegend(1-R/W-0.01-2*legendwidth, 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*(round((1+len(samples))/2.)), 0.99-(R/W)-legendwidth, 0.99-(T/H)/(1.-padRatio+padOverlap))
legendR2 = TLegend(1-R/W-0.01-legendwidth, 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*(int((1+len(samples))/2.))  , 0.99-(R/W), 0.99-(T/H)/(1.-padRatio+padOverlap))

legendR1.SetBorderSize(0)
legendR1.SetFillColor(0)
legendR2.SetBorderSize(0)
legendR2.SetFillColor(0)


legendName = ['t#bar{t}+#gamma',
              't#bar{t}+jets',
              't+#gamma'  ,
              'W+#gamma'       ,
              'Z+#gamma'       ,
              'Z+jets'         ,
              'W+jets'         ,
              'Single t'       ,
              't#bar{t}+V'     ,
              'WW/WZ/ZZ'     ,
              'Multijet'     ]
              
legend1.AddEntry(histograms[-1],"Data","pe")
legendR1.AddEntry(histograms[-1],"Data","pe")
for i in range((1+len(histograms))/2):
    legend1.AddEntry(histograms[i],legendName[i],'f')
    legendR1.AddEntry(histograms[i],legendName[i],'f')
for i in range((1+len(histograms))/2,len(histograms)-1):
    legend2.AddEntry(histograms[i],legendName[i],'f')
    legendR2.AddEntry(histograms[i],legendName[i],'f')

legend2.AddEntry(systLegendEntry, 'Uncert.','f')
legendR2.AddEntry(systLegendEntry, 'Uncert.','f')

# legend1.AddEntry(histograms[0],'t#bar{t}+#gamma','f')
# legend1.AddEntry(histograms[1],'t#bar{t}+jets'  ,'f')
# legend1.AddEntry(histograms[2],'t+#gamma'  ,'f')
# legend1.AddEntry(histograms[3],'W+#gamma'       ,'f')
# legend1.AddEntry(histograms[4],'Z+#gamma'       ,'f')
# legend2.AddEntry(histograms[5],'Z+jets'         ,'f')
# legend2.AddEntry(histograms[6],'W+jets'         ,'f')
# legend2.AddEntry(histograms[7],'Single t'       ,'f')
# legend2.AddEntry(histograms[8],'t#bar{t}+V'     ,'f')
# legend2.AddEntry(histograms[9],'WW/WZ/ZZ'     ,'f')
# legend2.AddEntry(histograms[10],'Multijet'     ,'f')
# legend2.AddEntry(systLegendEntry, 'Uncert.','f')


# legendR1.AddEntry(histograms[-1], "Data", 'pe')
# legendR1.AddEntry(histograms[0],'t#bar{t}+#gamma','f')
# legendR1.AddEntry(histograms[1],'t#bar{t}+jets'  ,'f')
# legendR1.AddEntry(histograms[2],'t+#gamma'  ,'f')
# legendR1.AddEntry(histograms[3],'W+#gamma'       ,'f')
# legendR1.AddEntry(histograms[4],'Z+#gamma'       ,'f')
# legendR2.AddEntry(histograms[5],'Z+jets'         ,'f')
# legendR2.AddEntry(histograms[6],'W+jets'         ,'f')
# legendR2.AddEntry(histograms[7],'Single t'       ,'f')
# legendR2.AddEntry(histograms[8],'t#bar{t}+V'     ,'f')
# legendR2.AddEntry(histograms[9],'WW/WZ/ZZ'     ,'f')
# legendR2.AddEntry(histograms[10],'Multijet'     ,'f')
# legendR2.AddEntry(systLegendEntry, 'Uncert.','f')




stack = THStack()

for i in range(len(samples)-1):
    stack.Add(histograms[len(samples)-2-i])

stack.Draw("hist")

stack.GetYaxis().SetTitle("Events")

systBand = stack.GetStack().Last().Clone("errorBand")
systBand.SetFillColor(kGray+2)
systBand.SetFillStyle(3245)
systBand.SetMarkerSize(0)
systBand.Draw("same,e2")

maxVal  = max(histograms[-1].GetMaximum(),stack.GetMaximum())
minVal  = min(histograms[-1].GetMinimum(),stack.GetMinimum())

stack.SetMaximum(1.35*maxVal)

histograms[-1].Draw("e,x0,same")
if finalState=="Ele":
	_channelText = "e+jets"
if finalState=="Mu":
	_channelText ="#mu+jets"

CMS_lumi.channelText = _channelText
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True
CMS_lumi.CMS_lumi(canvas, 4, 11)
legend1.Draw()
legend2.Draw()
if runPresel:
    canvas.SaveAs("%s/JetBjetMult_Presel.pdf"%outputDir)
    canvas.SaveAs("%s/JetBjetMult_Presel.png"%outputDir)
else:
    canvas.SaveAs("%s/JetBjetMult_Phosel.pdf"%outputDir)
    canvas.SaveAs("%s/JetBjetMult_Phosel.png"%outputDir)
canvas.SetLogy(True)


stack.SetMaximum(10**(1.2*log10(maxVal)))
if runPresel:
    canvas.SaveAs("%s/JetBjetMult_Presel_log.pdf"%outputDir)
    canvas.SaveAs("%s/JetBjetMult_Presel_log.png"%outputDir)
else:
    canvas.SaveAs("%s/JetBjetMult_Phosel_log.pdf"%outputDir)
    canvas.SaveAs("%s/JetBjetMult_Phosel_log.png"%outputDir)
canvas.SetLogy(False)
stack.SetMaximum(1.35*maxVal)



ratio =histograms[-1].Clone("temp")

temp_stack = stack.GetStack().Last()
for q in range(temp_stack.GetNbinsX()):
       temp_stack.SetBinError(q,0)
ratio.Divide(temp_stack)
ratioSyst = systBand.Clone("ratioSystBand")
ratioSyst.Divide(temp_stack)

pad1.Clear()
pad2.Clear()

canvasRatio.cd()
#canvasRatio.SetLogy()
#canvasRatio.ResetDrawn()

pad1.Clear()
pad2.Clear()


pad1.cd()
#pad1.SetLogy()
stack.Draw('HIST')
systBand.Draw("same,e2")
#    pad1.Update()
y2 = pad1.GetY2()
stack.SetMinimum(10)
#    pad1.Update()
stack.GetXaxis().SetTitle('')

stack.SetTitle('')
stack.GetXaxis().SetLabelSize(0)
stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
histograms[-1].Draw('E,X0,SAME')
legendR1.Draw()
legendR2.Draw()
ratio.SetTitle('')

ratio.GetXaxis().SetLabelSize(0.05/(padRatio+padOverlap))
ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
ratio.GetXaxis().SetLabelOffset(.05)
maxRatio = ratio.GetMaximum()
if maxRatio > 1.8:
    ratio.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
elif maxRatio < 1:
    ratio.GetYaxis().SetRangeUser(0,1.2)
else:
    ratio.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)


ratio.GetYaxis().SetNdivisions(504)
#ratio.GetXaxis().SetTitle(plotInfo[0])
ratio.GetYaxis().SetTitle("Data/MC")

pad2.cd()
ratio.SetMarkerStyle(histograms[-1].GetMarkerStyle())
ratio.SetMarkerSize(histograms[-1].GetMarkerSize())
ratio.SetLineColor(histograms[-1].GetLineColor())
ratio.SetLineWidth(histograms[-1].GetLineWidth())

oneLine = TF1("oneline","1",-9e9,9e9)
oneLine.SetLineColor(kBlack)
oneLine.SetLineWidth(1)
oneLine.SetLineStyle(2)

ratio.Draw('e,x0')
ratioSyst.Draw("same,e2")
oneLine.Draw("same")

#    pad2.Update()
CMS_lumi.CMS_lumi(pad1, 4, 11)
#canvasRatio.Update()
#canvasRatio.RedrawAxis()
#canvasRatio.SetLogy()
if runPresel:
    canvasRatio.SaveAs("%s/JetBjetMult_Presel_ratio.pdf"%outputDir)
    canvasRatio.SaveAs("%s/JetBjetMult_Presel_ratio.png"%outputDir)
else:
    canvasRatio.SaveAs("%s/JetBjetMult_Phosel_ratio.pdf"%outputDir)
    canvasRatio.SaveAs("%s/JetBjetMult_Phosel_ratio.png"%outputDir)

stack.SetMaximum(10**(1.5*log10(maxVal)))
pad1.SetLogy()

if runPresel:
    canvasRatio.SaveAs("%s/JetBjetMult_Presel_ratio_log.pdf"%outputDir)
    canvasRatio.SaveAs("%s/JetBjetMult_Presel_ratio_log.png"%outputDir)
else:
    canvasRatio.SaveAs("%s/JetBjetMult_Phosel_ratio_log.pdf"%outputDir)
    canvasRatio.SaveAs("%s/JetBjetMult_Phosel_ratio_log.png"%outputDir)


