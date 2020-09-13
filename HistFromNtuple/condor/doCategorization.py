import os
from HistInputs import *
import itertools

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

for year, decay, channel in itertools.product(Year, Decay, Channel): 
    args = "-y %s -d %s -c %s"%(year, decay, channel)
    runCmd("python categorizeHist.py %s --hist phosel_M3"%args)
    runCmd("python categorizeHist.py %s --hist phosel_noCut_ChIso"%args)
    runCmd("python categorizeHist.py %s --hist presel_M3_0Pho --is0PhoM3"%args)
    runCmd("python categorizeHist.py %s --hist phosel_MassLepGamma --isMassLepGamma"%args)
    runCmd("python categorizeHist.py %s --hist presel_MassDilep --isMassDilep"%args)
    for CR in ControlRegion:
        args = "-y %s -d %s -c %s --cr %s"%(year, decay, channel, CR)
        runCmd("python categorizeHist.py %s --hist phosel_M3"%args)
        runCmd("python categorizeHist.py %s --hist phosel_noCut_ChIso"%args)
        runCmd("python categorizeHist.py %s --hist presel_M3_0Pho --is0PhoM3"%args)
        runCmd("python categorizeHist.py %s --hist phosel_MassLepGamma --isMassLepGamma"%args)
        runCmd("python categorizeHist.py %s --hist presel_MassDilep --isMassDilep"%args)
