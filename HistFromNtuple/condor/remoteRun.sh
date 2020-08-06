#!/bin/bash

#Take input arguments as an array
myArray=( "$@" )
#Array: Size=$#, an element=$1, all element = $@

printf "Start Running Histogramming at ";/bin/date
printf "Worker node hostname ";/bin/hostname
echo "---------------------------------------------"

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
    echo "Running Interactively" ; 
else
    echo "Running In Batch"
    echo ${_CONDOR_SCRATCH_DIR}
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    cd /home/rverma/t3store/TTGammaSemiLep13TeV/CMSSW_10_2_5/src/TTGamma/HistFromNtuple/
    #-------------------
    #For LPC
    #-------------------
    #cmsrel CMSSW_10_2_5
    #cd CMSSW_10_2_5/src
    #eval `scramv1 runtime -sh`
    #cp -r /home/rverma/t3store/TTGammaSemiLep13TeV/CMSSW_10_2_5/src/TTGamma/HistFromNtuple/ .
    #cd HistFromNtuple
fi

#Run for Base, Signal region
echo $@
if [ $# -eq 3 ] 
then
    python makeHists13TeV.py -y $1 -c $2 -s $3 --plot presel_Njet

#Run for Base, Control region
elif [ $# -eq 4 ] 
then
    python makeHists13TeV.py -y $1 -c $2 -s $3 -cr $4 --plot presel_Njet

#Run for Syst, Signal region
elif [ $# -eq 5 ] 
then
    python makeHists13TeV.py -y $1 -c $2 -s $3 --syst $4 --level $5 --plot presel_Njet

#Run for Syst, Control region
elif [ $# -eq 6 ] 
then
    python makeHists13TeV.py -y $1 -c $2 -s $3 --syst $4 --level $5 --cr $6 --plot presel_Njet

#For over/under flow of arguments
else
    echo "The number of command line areguments should be >=3 and <=6"
fi
printf "Done Histogramming at ";/bin/date
