import os
import itertools
from optparse import OptionParser
from BasicInputs import *

#-----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
(options, args) = parser.parse_args()
year = options.year
channel = options.channel

#-----------------------------------------
#Path of the output histrograms
#----------------------------------------
inHistMainDir = "/home/rverma/t3store/TTGammaSemiLep13TeV"
inHistSubDir = "Histograms/%s/SemiLep/%s"%(year, channel)
inHistFullDir = "%s/%s"%(inHistMainDir, inHistSubDir)

resubmitBase = {}
if channel in ["Mu", "mu", "MU", "mU"]:
    for sample, syst, level, in itertools.product(SampleListMu, Systematics, SystLevel):
        fileFullPath = "%s/%s_%s%s_SignalRegion.root"%(inHistFullDir, sample, syst, level)
        if not os.path.exists(fileFullPath):
            print "%s does not exist"%fileFullPath

for sample, syst in itertools.product(SampleListMu, Systematics):
    if syst=="Base":
        cmd = "python makeHists13TeV.py -s %s --syst %s --plot presel_Njet &"%(sample, syst)
        print cmd
        os.system(cmd)
    else:
	for level in SystLevel:
	    cmd = "python makeHists13TeV.py -s %s --syst %s --level %s --plot presel_Njet &"%(sample, syst, level)
            print cmd
            os.system(cmd)

common_command = \
'Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
use_x509userproxy = true\n\
Output = log/log$(cluster)_$(process).stdout\n\
Error  = log/log$(cluster)_$(process).stderr\n\
Log    = log/log$(cluster)_$(process).condor\n\n'

#----------------------------------------
#Create jdl file for base
#----------------------------------------
if not os.path.exists("jdl"):
    os.makedirs("jdl")
fileBase = open('jdl/submitBase.jdl','w')
fileBase.write('Executable =  remoteRunBase.sh \n')
fileBase.write(common_command)
for year, sample, cr in itertools.product(Year, SampleListEle, ControlRegion):
	run_commandEle =  \
	'arguments  = %s Ele %s %s \n\
queue 1\n\n' %(year, sample, cr)
	fileBase.write(run_commandEle)
for year, sample, cr in itertools.product(Year, SampleListMu, ControlRegion):
	run_commandMu =  \
	'arguments  = %s Mu %s %s \n\
queue 1\n\n' %(year, sample, cr)
	fileBase.write(run_commandMu)
fileBase.close() 

#----------------------------------------
#Create jdl files for systematics
#----------------------------------------
for syst in Systematics:
	fileSyst = open('jdl/submitSyst_%s.jdl'%syst,'w')
	fileSyst.write('Executable =  remoteRunSyst.sh \n')
	fileSyst.write(common_command)
	for year, sample, level, cr in itertools.product(Year, SampleListEle, SystLevel, ControlRegion):
		run_commandEle =  \
		'arguments  = %s Ele %s %s %s %s \n\
queue 1\n\n' %(year, sample, syst, level, cr)
		if not sample=="DataEle":
			fileSyst.write(run_commandEle)
	for (year, sample, level, cr) in zip(Year, SampleListMu, SystLevel, ControlRegion):
		run_commandMu =  \
		'arguments  = %s Mu %s %s %s %s \n\
queue 1\n\n' %(year, sample, syst, level, cr)
		if not sample=="DataMu":
			fileSyst.write(run_commandMu)
	fileSyst.close() 
