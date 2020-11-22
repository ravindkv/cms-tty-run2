import os
from HistInputs import *
import itertools

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

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
