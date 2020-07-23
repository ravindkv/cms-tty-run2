ControlRegion=["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]
SampleListEle=["TTGamma", "TTbar", "TGJets", "WJets", "ZJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","QCDEle" ,"GJets" ,"DataEle" ]
SampleListMu= ["TTGamma", "TTbar" ,"TGJets" ,"WJets", "ZJets" ,"WGamma" ,"ZGamma","Diboson", "SingleTop", "TTV" ,"QCDMu", "GJets" ,"DataMu" ]

cfile = open('condor_makeHistograms_nominal.jdl','w')
common_command = \
'Executable =  makeHistograms_condor_nominal.sh \n\
Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
Transfer_Input_Files = myHistograms.tar, makeHistograms_condor_nominal.sh\n\
use_x509userproxy = true \n\
Output = condor_Dec5/log$(cluster)_$(process).stdout\n\
Error  = condor_Dec5/log$(cluster)_$(process).stderr\n\
Log    = condor_Dec5/log$(cluster)_$(process).condor\n\n'
cfile.write(common_command)

for year in ["2016", "2017", "2018"]:
    for cr in ControlRegion:
            run_commandEle =  \
            'arguments  = Ele %s %s \n\
queue 1\n\n' %(year, cr)
            cfile.write(run_commandEle)
            run_commandMu =  \
            'arguments  = Mu %s %s \n\
queue 1\n\n' %(year, cr)
            cfile.write(run_commandMu)
            
            
