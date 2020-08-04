
combine -M MultiDimFit -n   el_2016 datacard_M3ChIso_ele_2016.txt -s 314159 -t 5000 --expectSignal 1 --trackParameters PhoEff,Q2,PU,EleEff,BTagSF_b,lumi,BTagSF_l,MuEff,nonPromptSF --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file1.txt
combine -M MultiDimFit -n   mu_2016 datacard_M3ChIso_mu_2016.txt  -s 314159 -t 5000 --expectSignal 1 --trackParameters PhoEff,Q2,PU,EleEff,BTagSF_b,lumi,BTagSF_l,MuEff,nonPromptSF --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file2.txt 

combine -M MultiDimFit -n   el_2017 datacard_M3ChIso_ele_2017.txt -s 314159 -t 5000 --expectSignal 1 --trackParameters PhoEff,Q2,PU,EleEff,BTagSF_b,lumi,BTagSF_l,MuEff,nonPromptSF --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file3.txt 
combine -M MultiDimFit -n   mu_2017 datacard_M3ChIso_mu_2017.txt  -s 314159 -t 5000 --expectSignal 1 --trackParameters PhoEff,Q2,PU,EleEff,BTagSF_b,lumi,BTagSF_l,MuEff,nonPromptSF --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file4.txt 
combine -M MultiDimFit -n   el_2018 datacard_M3ChIso_ele_2018.txt -s 314159 -t 5000 --expectSignal 1 --trackParameters PhoEff,Q2,PU,EleEff,BTagSF_b,lumi,BTagSF_l,MuEff,nonPromptSF --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file5.txt 
combine -M MultiDimFit -n   mu_2018 datacard_M3ChIso_mu_2018.txt  -s 314159 -t 5000 --expectSignal 1 --trackParameters PhoEff,Q2,PU,EleEff,BTagSF_b,lumi,BTagSF_l,MuEff,nonPromptSF --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file6.txt 

wait

#while [ true ] ; do
#	read -t 60 -n 1
#	if [ $? = 0 ] ; then
#	echo "got all SFs ??? "
#	break;	
#	else
#	echo "waiting to finish the MultiDimFit."
#	fi
#done

#
##
text2workspace.py  datacard_M3ChIso_ele_2016.txt 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2016.root -m 125 -t -1 --expectSignal 1  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2016.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2016.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_ele_2016.json
plotImpacts.py -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016
##
##
text2workspace.py  datacard_M3ChIso_mu_2016.txt 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2016.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2016.root -m 125 -t -1 --expectSignal 1  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2016.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_mu_2016.json
plotImpacts.py -i impacts_toy_mu_2016.json -o impacts_toy_mu_2016
##
#####################
text2workspace.py  datacard_M3ChIso_ele_2017.txt 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2017.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2017.root -m 125 -t -1 --expectSignal 1  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2017.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_ele_2017.json
plotImpacts.py -i impacts_toy_ele_2017.json -o impacts_toy_ele_2017
##
##
text2workspace.py  datacard_M3ChIso_mu_2017.txt 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2017.root -m 125 -t -1 --expectSignal 1  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2017.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2017.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_mu_2017.json
plotImpacts.py -i impacts_toy_mu_2017.json -o impacts_toy_mu_2017
##
#######################
text2workspace.py  datacard_M3ChIso_ele_2018.txt 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2018.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2018.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2018.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_ele_2018.json
plotImpacts.py -i impacts_toy_ele_2018.json -o impacts_toy_ele_2018
##
##
text2workspace.py  datacard_M3ChIso_mu_2018.txt 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2018.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2018.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2018.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_mu_2018.json
plotImpacts.py -i impacts_toy_mu_2018.json -o impacts_toy_mu_2018
##
##


##
text2workspace.py  datacard_M3ChIso_ele_2016.txt 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2016.root -m 125   --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2016.root -m 125   --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_M3ChIso_ele_2016.root -m 125   -o impacts_data_ele_2016.json
plotImpacts.py -i impacts_data_ele_2016.json -o impacts_data_ele_2016
##
##
text2workspace.py  datacard_M3ChIso_mu_2016.txt 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2016.root -m 125  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2016.root -m 125  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_M3ChIso_mu_2016.root -m 125  -o impacts_data_mu_2016.json
plotImpacts.py -i impacts_data_mu_2016.json -o impacts_data_mu_2016
##
