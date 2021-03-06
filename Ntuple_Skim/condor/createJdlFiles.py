import itertools
import os
import sys

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("Ntuple_Skim/condor","Skim_NanoAOD/sample"))
from NanoAOD_Gen_SplitJobs_cff import Samples_2016, Samples_2017, Samples_2018 

if not os.path.exists("tmpSub/log"):
    os.makedirs("tmpSub/log")
condorLogDir = "log"
tarFile = "tmpSub/Ntuple_Skim.tar.gz"
if os.path.exists(tarFile):
	os.system("rm %s"%tarFile)
os.system("tar -zcvf %s ../../Ntuple_Skim --exclude condor"%tarFile)
os.system("cp runMakeNtuple.sh tmpSub/")
common_command = \
'Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
Transfer_Input_Files = Ntuple_Skim.tar.gz, runMakeNtuple.sh\n\
use_x509userproxy = true\n\
Output = %s/log_$(cluster)_$(process).stdout\n\
Error  = %s/log_$(cluster)_$(process).stderr\n\
Log    = %s/log_$(cluster)_$(process).condor\n\n'%(condorLogDir, condorLogDir, condorLogDir)

#----------------------------------------
#Create jdl files
#----------------------------------------
subFile = open('tmpSub/condorSubmit.sh','w')
for year in [2016,2017,2018]:
    sampleList = eval("Samples_%i"%year)
    jdlName = 'submitJobs_%s.jdl'%(year)
    jdlFile = open('tmpSub/%s'%jdlName,'w')
    jdlFile.write('Executable =  runMakeNtuple.sh \n')
    jdlFile.write(common_command)
    condorOutDir="/store/user/rverma/Output/cms-ttg-run2/Ntuple_Skim"
    os.system("eos root://cmseos.fnal.gov mkdir -p %s/%s"%(condorOutDir, year))
    jdlFile.write("X=$(step)+1\n")
    
    for sampleName, nJob in sampleList.items():
        if nJob==1:
            run_command =  'Arguments  = %s %s \nQueue 1\n\n' %(year, sampleName)
        else:
            run_command =  'Arguments  = %s %s $INT(X) %i\nQueue %i\n\n' %(year, sampleName, nJob, nJob)
	jdlFile.write(run_command)
    
	#print "condor_submit jdl/%s"%jdlFile
    subFile.write("condor_submit %s\n"%jdlName)
    jdlFile.close() 
subFile.close()
