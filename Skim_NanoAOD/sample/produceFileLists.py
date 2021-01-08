from NanoAOD_Gen_Samples import sampleList_2016, sampleList_2017, sampleList_2018
from getFilesFromDisk import getFileList_DAS, getFileList_EOS

f1 = open("NanoAOD_Gen_FileLists_cff.sh", "w")
f2 = open("NanoAOD_Gen_SplitJobs_cff.py", "w")
allJobs = 0
#for year in [2016,2017,2018]:
for year in [2016,2017,2018]:
    splitJobs = {}
    print '--------------------------'
    print  year 
    print  "nFiles\t  nJobs\t Samples"
    print '--------------------------'
    line = ""
    sampleList = eval("sampleList_%i"%year)
    jobs = 0
    for sampleName, sample in sampleList.items():
        line += '%s_FileList_%i="'%(sampleName,year)
        if '/store/user/' in sample:
            fileList = getFileList_EOS(sample)
            line += fileList
            line += '"\n\n'
        else:
            line += "xrootd "
            fileList = getFileList_DAS(sample)
            line += fileList 
            line += '"\n\n'
        nFiles = len(fileList.split(" "))
        nJob = 1
        if nFiles >= 5:
            nJob = int (nFiles/5)
        splitJobs[sampleName] = nJob
        jobs += nJob
        print("%i\t %i\t %s"%(nFiles, nJob, sampleName))
    f1.write(line.encode('ascii'))
    f2.write("Samples_%s = %s \n"%(str(year), str(splitJobs)))
    f2.write("AllJobs_%s = %s \n"%(str(year), str(jobs)))
    print '=================='
    print "AllJobs_%i = %i"%(year, jobs)
    print '=================='
    allJobs += jobs
f2.write("AllJobs_AllYears = %s \n"%str(allJobs))
 
