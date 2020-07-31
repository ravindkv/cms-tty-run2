#!/bin/bash

year=$1
channel=$2
sample=$3
systX=$4
levelX=$5
controlRegion=$6


if [ $channel == "Ele" ]; then
	mychannel="ele"
else
	mychannel="mu"

fi

printf "Start Running Histogramming at ";/bin/date
printf "Worker node hostname ";/bin/hostname
echo "---------------------------------------------"

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
    echo "Running Interactively" ; 
else
    echo "Running In Batch"
    echo ${_CONDOR_SCRATCH_DIR}
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    #cd /uscms/home/rverma/work/ttgamma/CMSSW_10_2_5/src/TTGamma/Plotting/
    cd /home/rverma/t3store/TTGammaSemiLep13TeV/CMSSW_10_2_5/src/TTGamma/Plotting/
    eval `scramv1 runtime -sh`
fi

echo "Running python makeHistograms "
#python makeHistograms13TeV.py -y $year -c $channel -s $sample --syst $systX --level $levelX --$controlRegion 
python makeHistograms13TeV.py -y $year -c $channel -s $sample --syst $systX --level $levelX --$controlRegion --plot presel_Njet
printf "Done Histogramming at ";/bin/date
