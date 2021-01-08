
#HistFromNtuple/condor

* Basic information such as the name of channels, year of data-taking, name
of physics process, type of systematic uncertainties, control regions,
etc are specified in a file. This file is imported in multiple scripts

* The condor submission scripts (jdl files) are created containing all 
information about the jobs. These jdl files are created automatically
using a script

* One jdl file is submitted using the following command
    condor_submit jdl/submitJobs_2016SemiLepMu.jdl

* The condor jobs are run in remote machines. The log files are created
by condor in a local directory and the output files are transferred from
remote machine to the local directory

* After running multiple jobs, there will be thousands of output root 
files corresponding to various process, channels, systematics, etc 

* To check the failed or corrupted jobs, a script is in place. It 
compares the number of submitted and finished jobs. It also looks at the
size of output root files. If some files have a very small size, they are
most likely corrupted. In the end, this script creates a jdl file
containing failed/corrupted jobs. Which can be resubmitted again using
condor_submit
