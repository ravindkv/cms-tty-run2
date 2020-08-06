import itertools
import os
from BasicInputs_cff import *

common_command = \
'Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
use_x509userproxy = true\n\
Output = log/log_$(cluster)_$(process).stdout\n\
Error  = log/log_$(cluster)_$(process).stderr\n\
Log    = log/log_$(cluster)_$(process).condor\n\n'

#----------------------------------------
#Create jdl files
#----------------------------------------
for year, channel in itertools.product(Year, Channel):
    jdlFile = open('jdl/submitJobs_%s%s.jdl'%(year, channel),'w')
    jdlFile.write('Executable =  remoteRun.sh \n')
    jdlFile.write(common_command)
    if channel=="Mu": Samples = SampleListEle
    else: Samples = SampleListMu
    
    #Create for Base, Signal region
    for sample in Samples:
        run_command =  \
		'arguments  = %s %s %s \n\
queue 1\n\n' %(year, channel, sample)
	jdlFile.write(run_command)
    
    #Create for Base, Control region
    for sample, cr in itertools.product(Samples, ControlRegion):
        run_command =  \
		'arguments  = %s %s %s %s \n\
queue 1\n\n' %(year, channel, sample, cr)
	jdlFile.write(run_command)
	
    #Create for Syst, Signal region
    for sample, syst, level in itertools.product(Samples, Systematics, SystLevel):
        run_command =  \
		'arguments  = %s %s %s %s %s \n\
queue 1\n\n' %(year, channel, sample, syst, level)
        if not sample in ["DataMu", "DataEle", "QCD_DD"]:
            jdlFile.write(run_command)
    
    #Create for Syst, Control region
    for sample, syst, level, cr in itertools.product(Samples, Systematics, SystLevel, ControlRegion):
        run_command =  \
		'arguments  = %s %s %s %s %s %s \n\
queue 1\n\n' %(year, channel, sample, syst, level, cr)
        if not sample in ["DataMu", "DataEle", "QCD_DD"]:
            jdlFile.write(run_command)
    jdlFile.close() 
