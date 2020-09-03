import os
import itertools
import json
from FitInputs import *

with open("DataCards.json", "w") as f:
    data = {}
    json.dump(data, f)

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

for year, decay, channel in itertools.product(Year, Decay, Channel): 
    args = "-y %s -d %s -c %s"%(year, decay, channel)
    #runCmd("python makeDCInc.py %s"%args)
    runCmd("python makeDCCat.py --isChIsoM3      --hist phosel_noCut_ChIso %s"%args)
    runCmd("python makeDCCat.py --isChIsoM3      --hist phosel_M3 %s"%args)
    runCmd("python makeDCCat.py --is0PhoM3       --hist presel_M3 %s"%args)
    runCmd("python makeDCCat.py --isMassDilep    --hist presel_MassDilep %s"%args)
    runCmd("python makeDCCat.py --isMassLepGamma --hist phosel_MassLepGammma %s"%args)
    for CR in ControlRegion:
        args = "-y %s -d %s -c %s --cr %s"%(year, decay, channel, CR)
        #runCmd("python makeDCInc.py %s"%args)
        runCmd("python makeDCCat.py --isChIsoM3      --hist phosel_noCut_ChIso %s"%args)
        runCmd("python makeDCCat.py --isChIsoM3      --hist phosel_M3 %s"%args)
        runCmd("python makeDCCat.py --is0PhoM3       --hist presel_M3 %s"%args)
        runCmd("python makeDCCat.py --isMassDilep    --hist presel_MassDilep %s"%args)
        runCmd("python makeDCCat.py --isMassLepGamma --hist phosel_MassLepGammma %s"%args)
