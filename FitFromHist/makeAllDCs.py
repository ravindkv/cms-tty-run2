import os
import itertools
import json
from FitInputs import *

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

for year, decay, channel, isCount in itertools.product(Year, Decay, Channel, CountBased): 
    args = "-y %s -d %s -c %s %s"%(year, decay, channel, isCount)
    #runCmd("python makeDCInc.py %s"%args)
    runCmd("python makeDCCat.py --isChIsoM3      --hist phosel_noCut_ChIso %s"%args)
    runCmd("python makeDCCat.py --isChIsoM3      --hist phosel_M3 %s"%args)
    runCmd("python makeDCCat.py --is0PhoM3       --hist presel_M3_0Pho %s"%args)
    runCmd("python makeDCCat.py --isMassLepGamma --hist phosel_MassLepGamma %s"%args)
    runCmd("python makeDCCat.py --isMassDilep    --hist presel_MassDilep %s"%args)
    print args
    for CR in ControlRegion:
        args = "-y %s -d %s -c %s %s --cr %s"%(year, decay, channel, isCount, CR)
        print args
        #runCmd("python makeDCInc.py %s"%args)
        runCmd("python makeDCCat.py --isChIsoM3      --hist phosel_noCut_ChIso %s"%args)
        runCmd("python makeDCCat.py --isChIsoM3      --hist phosel_M3 %s"%args)
        runCmd("python makeDCCat.py --is0PhoM3       --hist presel_M3_0Pho %s"%args)
        runCmd("python makeDCCat.py --isMassLepGamma --hist phosel_MassLepGamma %s"%args)
        runCmd("python makeDCCat.py --isMassDilep    --hist presel_MassDilep %s"%args)
