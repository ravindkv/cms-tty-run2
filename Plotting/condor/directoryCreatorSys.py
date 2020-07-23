ControlRegion=["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]

#line =''
#for channel in ['ele', 'mu']:
#	for year in ["2016", "2017", "2018"]:
#		for cr in ControlRegion:
#			line+='eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s/ \n'%(year,channel,cr) 
#
#
#with open("nominalDirList.sh","w") as _file:
#    _file.write(line)
    
#systematics=["PU","Q2","Pdf","MuEff","EleEff","PhoEff","BTagSF_b","BTagSF_l"]    

systematics=["isr","fsr"]    

lineSyst ="eosmkdir='eos root://cmseos.fnal.gov mkdir' \n"
for channel in ['ele', 'mu']:
	for year in ["2016", "2017", "2018"]:
		for cr in ControlRegion:
			for syst in systematics:
				lineSyst+='$eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s_up_%s/ \n'%(year,channel,syst,cr) 
				lineSyst+='$eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s_down_%s/ \n'%(year,channel,syst,cr) 

with open("systematicsDirList_1.sh","w") as _file:
    _file.write(lineSyst)
    
    
  
