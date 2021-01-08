file=$1
echo $file
root -b "/uscms_data/d3/rverma/CMSSW_10_2_13/src/TTGamma/ScanRootFile.C(\"$file\")" -q
