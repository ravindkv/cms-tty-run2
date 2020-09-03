import os
import itertools
import json
from FitInputs import *

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

hists = []
hists.append("phosel_noCut_ChIso") 
hists.append("phosel_M3") 
hists.append("presel_M3") 
hists.append("presel_MassDilep") 
hists.append("phosel_MassLepGammma")
for year, decay, channel in itertools.product(Year, Decay, Channel): 
    for h in hists:
        args = "-y %s -d %s -c %s --hist %s"%(year, decay, channel, h)
        runCmd("python performFit.py --isT2W %s"%args)
    for CR in ControlRegion:
        args = "-y %s -d %s -c %s --cr %s --hist %s"%(year, decay, channel, CR, h)
        runCmd("python performFit.py --isT2W %s"%args)
