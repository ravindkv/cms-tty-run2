import os
import itertools
import json
from PlotInputs import *

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)
for year, channel, sample in itertools.product(Year, Channel, SamplesSyst): 
    args = "-y %s -c %s -s %s"%(year, channel, sample)
    runCmd("python systRatioInc.py -d Semilep --hist phosel_noCut_ChIso %s"%args)
    runCmd("python systRatioInc.py -d Semilep --hist phosel_M3 %s"%args)
    runCmd("python systRatioInc.py -d Semilep --hist presel_M3_0Pho %s"%args)
    runCmd("python systRatioInc.py -d Semilep --hist phosel_MassLepGamma --cr tight_a4j_e0b %s"%args)
    runCmd("python systRatioInc.py -d Dilep   --hist presel_MassDilep %s"%args)
for year, decay, channel in itertools.product(Year, Decay, Channel): 
    inputArg = "SystRatio_%s_%s_%s"%(year, decay, channel)
    outputArg= "All_%s"%inputArg
    runCmd("pdfunite %s*.pdf %s.pdf"%(inputArg, outputArg))

'''
for year, decay, channel, sample in itertools.product(Year, Decay, Channel, SamplesSyst): 
    args = "-y %s -d %s -c %s -s %s"%(year, decay, channel, sample)
    #runCmd("python systRatioInc.py  --hist phosel_noCut_ChIso %s"%args)
    runCmd("python systRatioInc.py  --hist phosel_M3 %s"%args)
    runCmd("python systRatioInc.py  --hist presel_M3_0Pho %s"%args)
    #runCmd("python systRatioInc.py  --hist phosel_MassLepGamma --cr tight_a4j_e0b %s"%args)
    #runCmd("python systRatioInc.py -hist presel_MassDilep %s"%args)

for year, decay, channel in itertools.product(Year, Decay, Channel): 
    inputArg = "SystRatio_%s_%s_%s"%(year, decay, channel)
    outputArg= "All_%s"%inputArg
    runCmd("pdfunite %s*.pdf %s.pdf"%(inputArg, outputArg))
for year, decay, channel, sample in itertools.product(Year, Decay, Channel, SamplesSyst): 
    args = "-y %s -d %s -c %s -s %s"%(year, decay, channel, sample)
    #runCmd("python systRatioInc.py --hist phosel_noCut_ChIso %s"%args)
    #runCmd("python systRatioInc.py --hist phosel_M3 %s"%args)
    #runCmd("python systRatioInc.py --hist presel_M3_0Pho %s"%args)
    #runCmd("python systRatioInc.py --hist phosel_MassLepGamma %s"%args)
    runCmd("python systRatioInc.py --hist presel_MassDilep %s"%args)
    print args
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
