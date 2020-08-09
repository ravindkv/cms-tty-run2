import itertools
import os
from BasicInputs_cff import *

if not os.path.exists("jdl"):
    os.makedirs("jdl")
condorLogDir = "%s/Log"%(condorHistDir)
if not os.path.exists(condorLogDir):
    os.makedirs(condorLogDir)

common_command = \
'Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
use_x509userproxy = true\n\
Output = %s/log_$(cluster)_$(process).stdout\n\
Error  = %s/log_$(cluster)_$(process).stderr\n\
Log    = %s/log_$(cluster)_$(process).condor\n\n'%(condorLogDir, condorLogDir, condorLogDir)

#----------------------------------------
#Create jdl files
#----------------------------------------
for year, decay, channel in itertools.product(Year, Decay, Channel):
    condorOutDir = "%s/Hists/%s/%s/%s"%(condorHistDir, year, decay, channel)
    if not os.path.exists(condorOutDir):
        os.makedirs(condorOutDir)
    jdlFile = open('jdl/submitJobs_%s%s%s.jdl'%(year, decay, channel),'w')
    jdlFile.write('Executable =  remoteRun.sh \n')
    jdlFile.write(common_command)
    if channel=="Mu": Samples = SampleListMu
    else: Samples = SampleListEle
    
    #Create for Base, Signal region
    for sample in Samples:
        run_command =  \
		'arguments  = %s %s %s %s \n\
queue 1\n\n' %(year, decay, channel, sample)
	jdlFile.write(run_command)
    
    #Create for Base, Control region
    for sample, cr in itertools.product(Samples, ControlRegion):
        run_command =  \
		'arguments  = %s %s %s %s %s \n\
queue 1\n\n' %(year, decay, channel, sample, cr)
	jdlFile.write(run_command)
	
    #Create for Syst, Signal region
    for sample, syst, level in itertools.product(Samples, Systematics, SystLevel):
        run_command =  \
		'arguments  = %s %s %s %s %s %s \n\
queue 1\n\n' %(year, decay, channel, sample, syst, level)
        if not sample in ["DataMu", "DataEle", "QCD_DD"]:
            jdlFile.write(run_command)
    
    #Create for Syst, Control region
    for sample, syst, level, cr in itertools.product(Samples, Systematics, SystLevel, ControlRegion):
        run_command =  \
		'arguments  = %s %s %s %s %s %s %s \n\
queue 1\n\n' %(year, decay, channel, sample, syst, level, cr)
        if not sample in ["DataMu", "DataEle", "QCD_DD"]:
            jdlFile.write(run_command)
    jdlFile.close() 
