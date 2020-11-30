import os
import itertools
from optparse import OptionParser
from HistInputs import *

#----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("--isCheck","--isCheck", dest="checkStatus",action="store_true",default=False, help="Check the status of histograms produced by condor jobs" )
parser.add_option("--isMerge","--isMerge", dest="mergeHistos",action="store_true",default=False, help="merge histograms produced by condor jobs" )
parser.add_option("--isCat","--isCat", dest="catHistos",action="store_true",default=False, help="categorise histograms produced by condor jobs" )
(options, args) = parser.parse_args()
isCheck = options.checkStatus
isMerge = options.mergeHistos
isCat = options.catHistos


def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

if isCheck:
    for year, decay, channel in itertools.product(Year, Decay, Channel): 
        args = "-y %s -d %s -c %s"%(year, decay, channel)
        runCmd("python checkJobStatus.py  %s "%args)

if isMerge:
    for year, decay, channel in itertools.product(Year, Decay, Channel): 
        args = "-y %s -d %s -c %s"%(year, decay, channel)
        runCmd("python mergeOutputHists.py  %s "%args)

if isCat:
    for year, decay, channel, isCount in itertools.product(Year, Decay, Channel, CountBased): 
        if isCount=="":
            outDir = "%s/Hists/%s/%s/%s/Merged/ShapeBased"%(condorHistDir, year, decay, channel)
        else:
            outDir = "%s/Hists/%s/%s/%s/Merged/CountBased"%(condorHistDir, year, decay, channel)
        runCmd("eos root://cmseos.fnal.gov mkdir -p %s"%outDir)
        args = "-y %s -d %s -c %s %s"%(year, decay, channel, isCount)
        runCmd("python categorizeHist.py %s --hist phosel_noCut_ChIso"%args)
        runCmd("python categorizeHist.py %s --hist phosel_M3"%args)
        runCmd("python categorizeHist.py %s --hist presel_M3_0Pho --is0PhoM3"%args)
        runCmd("python categorizeHist.py %s --hist phosel_MassLepGamma --isMassLepGamma"%args)
        runCmd("python categorizeHist.py %s --hist presel_MassDilep --isMassDilep"%args)
        print args
        for CR in ControlRegion:
            args = "-y %s -d %s -c %s %s --cr %s"%(year, decay, channel, isCount, CR)
            runCmd("python categorizeHist.py %s --hist phosel_noCut_ChIso"%args)
            runCmd("python categorizeHist.py %s --hist phosel_M3"%args)
            runCmd("python categorizeHist.py %s --hist presel_M3_0Pho --is0PhoM3"%args)
            runCmd("python categorizeHist.py %s --hist phosel_MassLepGamma --isMassLepGamma"%args)
            runCmd("python categorizeHist.py %s --hist presel_MassDilep --isMassDilep"%args)

        runCmd("xrdcp AllCat*.root root://cmseos.fnal.gov/%s"%(outDir))
        runCmd("rm AllCat*.root")
