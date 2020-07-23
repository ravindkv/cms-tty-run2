#!/bin/bash

channel=$1
year=$2
controlRegion=$3

if [ $channel == "DiEle" ]; then
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
    cd ${_CONDOR_SCRATCH_DIR}
    echo ${_CONDOR_SCRATCH_DIR}
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    xrdcp -f root://cmseos.fnal.gov//store/user/npoudyal/CMSSW_10_2_14.tgz .
    tar -xvf CMSSW_10_2_14.tgz
    cd CMSSW_10_2_14/src
    eval `scramv1 runtime -sh`
    cd ../..
    tar -xvf myHistograms.tar

fi

outputdir="root://cmseos.fnal.gov//store/user/npoudyal"

echo "Running python makeHistograms "
declare -a    SampleList=("TTGamma" "TTbar" "TGJets" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCD" "Data" )
declare -a SampleListEle=("TTGamma" "TTbar" "TGJets" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCDEle" "DataEle" )
declare -a  SampleListMu=("TTGamma" "TTbar" "TGJets" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCDMu" "DataMu" )
#declare -a SampleList=("TTbar")
#declare -a SampleListEle=("TTbar")
#declare -a SampleListMu=("TTbar")

for mysample in ${SampleList[@]}; do
	#python makeHistograms.py -c $channel -y $year --$controlRegion -s $mysample --makePlotsMEG
	python makeHistograms.py -c $channel -y $year --$controlRegion -s $mysample --dilepmassPlots 
	#python makeHistograms.py -c $channel -y $year --$controlRegion -s $mysample --plot presel_Njet
done
wait
#loop finishes
#make directory in eos first only if not exist there and then copy the file below
printf "Everything is done now copying all files to eos area"

if [ $channel == "DiEle" ]; then
	for mysample in ${SampleListEle[@]}; do
		echo "xrdcp -f histograms_$year/$mychannel/Dilep_hists_$controlRegion/$mysample.root $outputdir/histograms_$year/$mychannel/Dilep_hists_$controlRegion/"
		xrdcp -f histograms_$year/$mychannel/Dilep_hists_$controlRegion/$mysample.root $outputdir/histograms_$year/$mychannel/Dilep_hists_$controlRegion/
	done
else
	for mysample in ${SampleListMu[@]}; do
		echo "xrdcp -f histograms_$year/$mychannel/Dilep_hists_$controlRegion/$mysample.root $outputdir/histograms_$year/$mychannel/Dilep_hists_$controlRegion/"
		xrdcp -f histograms_$year/$mychannel/Dilep_hists_$controlRegion/$mysample.root $outputdir/histograms_$year/$mychannel/Dilep_hists_$controlRegion/
	done
fi

#wait 
printf "Done Histogramming at ";/bin/date


