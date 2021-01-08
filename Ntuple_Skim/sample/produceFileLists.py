import os
import sys
import subprocess

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("RecoNtuple_Skim/sample","Skim_NanoAOD/sample"))
from NanoAOD_Gen_SplitJobs_cff import Samples_2016, Samples_2017, Samples_2018

eosDir = '/store/user/rverma/Output/cms-hcs-run2/Skim_NanoAOD'
skimFiles = open('Skim_NanoAOD_FileLists_cff.sh','w')
#for year in [2016]:
for year in [2016,2017,2018]:
    print  "------------: %s :-----------"%year 
    print  "Sub\t  Done\t Diff\t Sample"
    missingJobs = {}
    line = ""
    sampleList = eval("Samples_%i"%year)
    skimFiles.write("eosDirSkim=root://cmseos.fnal.gov/%s\n"%eosDir)
    for sampleName, nJob in sampleList.items():
        line += '%s_FileList_%i="'%(sampleName,year)
        extraArgs = "%s_Skim_NanoAOD*.root"%sampleName
        fileList = subprocess.Popen('eos root://cmseos.fnal.gov/ ls %s/%i/%s'%(eosDir, year, extraArgs),shell=True,stdout=subprocess.PIPE).communicate()[0].split('\n')
        fileList.remove("")
        nFiles = len(fileList)
        joinList = ' '.join(["$eosDirSkim/%i/%s"%(year, str(y).split("/")[-1]) for y in fileList])
        line += joinList
        line += '"\n\n'
        print("%i\t %i\t %i\t %s"%(nJob, nFiles, nJob-nFiles, sampleName))
        if nFiles is not nJob:
            missingJobs[sampleName] = nJob -nFiles
    skimFiles.write(line.encode('ascii'))
    print "Missing jobs:", missingJobs
skimFiles.close()

