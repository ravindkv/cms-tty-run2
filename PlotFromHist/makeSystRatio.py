import os
import itertools
import json
from PlotInputs import *

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

for year, decay, channel, sample in itertools.product(Year, Decay, Channel, SamplesSyst): 
    args = "-y %s -d %s -c %s -s %s"%(year, decay, channel, sample)
    #runCmd("python makeDCInc.py %s"%args)
    runCmd("python systRatioInc.py --hist phosel_noCut_ChIso %s"%args)
    runCmd("python systRatioInc.py --hist phosel_M3 %s"%args)
    runCmd("python systRatioInc.py --hist presel_M3_0Pho %s"%args)
    runCmd("python systRatioInc.py --hist phosel_MassLepGamma %s"%args)
    runCmd("python systRatioInc.py --hist presel_MassDilep %s"%args)
    print args
    '''
    for CR in ControlRegion:
        args = "-y %s -d %s -c %s -s %s --cr %s"%(year, decay, channel, sample, CR)
        print args
        #runCmd("python makeDCInc.py %s"%args)
        runCmd("python systRatioInc.py  --hist phosel_noCut_ChIso %s"%args)
        runCmd("python systRatioInc.py  --hist phosel_M3 %s"%args)
        runCmd("python systRatioInc.py  --hist presel_M3_0Pho %s"%args)
        runCmd("python systRatioInc.py  --hist phosel_MassLepGamma %s"%args)
        runCmd("python systRatioInc.py  --hist presel_MassDilep %s"%args)
    '''
