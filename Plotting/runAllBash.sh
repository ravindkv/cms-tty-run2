# ./runAllBash.sh fileName
# fileName will be parsed as an argument to python
# The & is used to run each of the command in background
file=$1
python $file  TTGamma   &
python $file  TTbar     &
python $file  TGJets    &
python $file  WJets     &
python $file  ZJets     &
python $file  WGamma    &
python $file  ZGamma    &
python $file  Diboson   &
python $file  SingleTop &
python $file  TTV       &
python $file  GJets     &
python $file  QCD       &
python $file  Data      &
