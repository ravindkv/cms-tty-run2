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
    scramv1 project CMSSW CMSSW_10_2_5
    cd CMSSW_10_2_5/src
    eval `scramv1 runtime -sh`
    #-------------------
    #For TIFR
    #-------------------
    cp -rf /home/rverma/t3store/TTGammaSemiLep13TeV/Code/CMSSW_10_2_5/src/TTGamma/HistFromNtuple/ .
    #-------------------
    #For LPC
    #-------------------
    #xrdcp -f root://cmseos.fnal.gov//store/user/npoudyal/CMSSW_10_2_14.tgz .
    cd HistFromNtuple
fi

#Run for Base, Signal region
echo "All arguements: "$@
echo "Number of arguements: "$#
if [ $# -eq 4 ] 
then
    python makeHists.py -y $1 -d $2 -c $3 -s $4 

#Run for Base, Control region
elif [ $# -eq 5 ] 
then
    python makeHists.py -y $1 -d $2 -c $3 -s $4 --cr $5 

#Run for Syst, Signal region
elif [ $# -eq 6 ] 
then
    python makeHists.py -y $1 -d $2 -c $3 -s $4 --syst $5 --level $6

#Run for Syst, Control region
elif [ $# -eq 7 ] 
then
    python makeHists.py -y $1 -d $2 -c $3 -s $4 --syst $5 --level $6 --cr $7

#For over/under flow of arguments
else
    echo "The number of command line areguments should be >=4 and <=7"
fi
printf "Done Histogramming at ";/bin/date

#---------------------------------------------
#Copy the ouput root files
#---------------------------------------------
printf "Copying output files ..."
condorOutDir=/home/rverma/t3store/TTGammaSemiLep13TeV/Output
cp -rf hists/$1/$2/$3/* $condorOutDir/Hists/$1/$2/$3/ 
printf "Done ";/bin/date
cd ${_CONDOR_SCRATCH_DIR}
rm -rf CMSSW_10_2_5
