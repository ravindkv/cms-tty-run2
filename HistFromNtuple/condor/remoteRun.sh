#!/bin/bash

#Take input arguments as an array
myArray=( "$@" )
#Array: Size=$#, an element=$1, all element = $@

printf "Start Running Histogramming at ";/bin/date
printf "Worker node hostname ";/bin/hostname

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
    echo "Running Interactively" ; 
else
    echo "Running In Batch"
    echo ${_CONDOR_SCRATCH_DIR}
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    scramv1 project CMSSW CMSSW_10_2_14
    cd CMSSW_10_2_14/src
    eval `scramv1 runtime -sh`
	cd ../..
	tar --strip-components=1 -zxvf HistFromNtuple.tar.gz
fi

#Run for Base, Signal region
echo "All arguements: "$@
echo "Number of arguements: "$#
if [ $# -eq 4 ] 
then
    python makeHists.py -y $1 -d $2 -c $3 -s $4 --fitHist

#Run for Base, Control region
elif [ $# -eq 5 ] 
then
    python makeHists.py -y $1 -d $2 -c $3 -s $4 --cr $5 --fitHist

#Run for Syst, Signal region
elif [ $# -eq 6 ] 
then
    python makeHists.py -y $1 -d $2 -c $3 -s $4 --syst $5 --level $6 --fitHist

#Run for Syst, Control region
elif [ $# -eq 7 ] 
then
    python makeHists.py -y $1 -d $2 -c $3 -s $4 --syst $5 --level $6 --cr $7 --fitHist

#For over/under flow of arguments
else
    echo "The number of command line areguments should be >=4 and <=7"
fi
printf "Done Histogramming at ";/bin/date

#---------------------------------------------
#Copy the ouput root files
#---------------------------------------------
printf "Copying output files ..."
condorOutDir=/store/user/rverma/OutputTTGamma
eos root://cmseos.fnal.gov mkdir -p $condorOutDir/Hists/$1/$2/$3/
xrdcp -rf hists/$1/$2/$3/*.root root://cmseos.fnal.gov/$condorOutDir/Hists/$1/$2/$3/ 
printf "Done ";/bin/date
