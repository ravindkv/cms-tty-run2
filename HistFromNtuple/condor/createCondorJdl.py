import itertools
import os
Year 	      =	["2016", "2017", "2018"]
SampleList    =	["TTGamma", "TTbar", "TGJets", "WJets", "ZJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","GJets"]
SampleListEle = SampleList + ["QCDEle", "DataEle"]
SampleListMu  = SampleList + ["QCDMu", "DataMu"]
Systematics   =	["PU","MuEff","PhoEff","BTagSF_b","BTagSF_l","EleEff","Q2","Pdf","isr","fsr"]
SystLevel     = ["up", "down"]
ControlRegion = ["tight"]
#ControlRegion=["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]

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
for (year, sample, cr) in zip(Year, SampleListMu,  ControlRegion):
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
		fileSyst.write(run_commandEle)
	for (year, sample, level, cr) in zip(Year, SampleListMu, SystLevel, ControlRegion):
		run_commandMu =  \
		'arguments  = %s Mu %s %s %s %s \n\
queue 1\n\n' %(year, sample, syst, level, cr)
		fileSyst.write(run_commandMu)
	fileSyst.close() 
