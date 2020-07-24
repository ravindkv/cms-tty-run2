#!/bin/bash

channel=$1
year=$2
controlRegion=$3
systX=$4
levelX=$5


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
declare -a    SampleList=("TTGamma" "TTbar" "TGJets" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCD" "Data" )
declare -a SampleListEle=("TTGamma" "TTbar" "TGJets" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCDEle" "DataEle" )
declare -a  SampleListMu=("TTGamma" "TTbar" "TGJets" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCDMu" "DataMu" )
#declare -a SampleList=("TTbar")
#declare -a SampleListEle=("TTbar")
#declare -a SampleListMu=("TTbar")
for mysample in ${SampleList[@]}; do
	#python makeHistograms.py -c $channel -y $year --$controlRegion -s $mysample --syst $systX --level $levelX --makePlotsMEG
	python makeHistograms.py -c $channel -y $year --$controlRegion -s $mysample --syst $systX --level $levelX --makePlotsForSF
	#python makeHistograms.py -c $channel -y $year --$controlRegion -s $mysample --syst $systX --level $levelX --plot phosel_MET
done
printf "Done Histogramming at ";/bin/date
