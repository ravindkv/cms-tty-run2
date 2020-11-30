import os
import itertools
import json
from FitInputs import *

if not os.path.exists("./RateParams.json"):
    with open("RateParams.json", "w") as f:
        data = {}
        json.dump(data, f)

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

hists = []
#hists.append("phosel_noCut_ChIso") 
#hists.append("phosel_M3") 
#hists.append("presel_M3_0Pho") 
#hists.append("presel_MassDilep") 
hists.append("phosel_MassLepGamma")
for year, decay, channel in itertools.product(Year, Decay, Channel): 
    for h in hists:
        args = "-y %s -d %s -c %s --hist %s"%(year, decay, channel, h)
        runCmd("python performFit.py --isFD %s --isMassLepGamma"%args)
    for CR in ControlRegion:
        args = "-y %s -d %s -c %s --cr %s --hist %s"%(year, decay, channel, CR, h)
        runCmd("python performFit.py --isFD %s --isMassLepGamma"%args)
#python performFit.py --isFD --isT2W --isComb --combYear 2016 --combChannel Mu --combDecay Semilep
