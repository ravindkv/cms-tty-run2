#--------------------------
# 2016
#--------------------------
#MCType16='RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1'
MCType16='RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1'
MCType16_ext1=MCType16.replace('-v1','_ext1-v1')
MCType16_ext2=MCType16.replace('-v1','_ext2-v1')
MCType16_ext3=MCType16.replace('-v1','_ext3-v1')
MCType16_noPULabel = MCType16.replace('PUMoriond17_','')

MCType16_v2 = MCType16.replace('-v1','-v2')

DataType16='Nano1June2019-v1'
DataType16_ver2='_ver2-Nano1June2019_ver2-v1'

sampleList_2016 = {
'TTGamma_Dilepton'     : '/TTGamma_Dilept_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_Hadronic'   : '/TTGamma_Hadronic_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_SingleLept' : '/TTGamma_SingleLept_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',

'TTGamma_Dilepton_Pt100'  : '/TTGamma_Dilept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_Dilepton_Pt200' : '/TTGamma_Dilept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',

'TTGamma_SingleLept_Pt100' : '/TTGamma_SingleLept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_SingleLept_Pt200' : '/TTGamma_SingleLept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',

'TTGamma_Hadronic_Pt100' : '/TTGamma_Hadronic_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_Hadronic_Pt200' : '/TTGamma_Hadronic_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',

# 'TTGamma_Dilept_small'   : '/store/user/lpctop/TTGamma/NanoAOD/2016/Dilept',
# 'TTGamma_Hadronic_small' : '/store/user/lpctop/TTGamma/NanoAOD/2016/Had',
# 'TTGamma_SemiLept_small' : '/store/user/lpctop/TTGamma/NanoAOD/2016/SemiLept',

'TTGamma_Dilepton_TuneDown' : '/TTGamma_Dilept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_Dilepton_TuneUp'   : '/TTGamma_Dilept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_Dilepton_erdOn'    : '/TTGamma_Dilept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_Dilepton_CR2'      : '/TTGamma_Dilept_TuneCP5CR1_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_Dilepton_CR1'      : '/TTGamma_Dilept_TuneCP5CR2_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',


'TTGamma_SingleLept_TuneDown' : '/TTGamma_SingleLept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_SingleLept_TuneUp'   : '/TTGamma_SingleLept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_SingleLept_erdOn'    : '/TTGamma_SingleLept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_SingleLept_CR1'      : '/TTGamma_SingleLept_TuneCP5CR1_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',
'TTGamma_SingleLept_CR2'      : '/TTGamma_SingleLept_TuneCP5CR2_PSweights_13TeV-madgraph-pythia8/'+MCType16+'/NANOAODSIM',


'Data_SingleMu_b' : '/SingleMuon/Run2016B'+DataType16_ver2+'/NANOAOD',
'Data_SingleMu_c' : '/SingleMuon/Run2016C-'+DataType16+'/NANOAOD',
'Data_SingleMu_d' : '/SingleMuon/Run2016D-'+DataType16+'/NANOAOD',
'Data_SingleMu_e' : '/SingleMuon/Run2016E-'+DataType16+'/NANOAOD',
'Data_SingleMu_f' : '/SingleMuon/Run2016F-'+DataType16+'/NANOAOD',
'Data_SingleMu_g' : '/SingleMuon/Run2016G-'+DataType16+'/NANOAOD',
'Data_SingleMu_h' : '/SingleMuon/Run2016H-'+DataType16+'/NANOAOD',

'Data_SingleEle_b' : '/SingleElectron/Run2016B'+DataType16_ver2+'/NANOAOD',
'Data_SingleEle_c' : '/SingleElectron/Run2016C-'+DataType16+'/NANOAOD',
'Data_SingleEle_d' : '/SingleElectron/Run2016D-'+DataType16+'/NANOAOD',
'Data_SingleEle_e' : '/SingleElectron/Run2016E-'+DataType16+'/NANOAOD',
'Data_SingleEle_f' : '/SingleElectron/Run2016F-'+DataType16+'/NANOAOD',
'Data_SingleEle_g' : '/SingleElectron/Run2016G-'+DataType16+'/NANOAOD',
'Data_SingleEle_h' : '/SingleElectron/Run2016H-'+DataType16+'/NANOAOD',


'TTbarPowheg_Dilepton' : '/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Hadronic' : '/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Semilept' : '/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',


'W1jets'      : '/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'W2jets'      : '/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'W2jets_ext1' : '/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'W3jets'      : '/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'W3jets_ext1' : '/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'W4jets'      : '/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'W4jets_ext1' : '/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'W4jets_ext2' : '/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext2+'/NANOAODSIM',

'WJetsToQQ'   : '/WJetsToQQ_HT180_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',



'DYjetsM10to50' : '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'DYjetsM50_ext1' : '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'DYjetsM50_ext2' : '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext2+'/NANOAODSIM',


'ST_s_channel' : '/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/'+MCType16+'/NANOAODSIM',
'ST_t_channel' : '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'ST_tbar_channel' : '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'ST_tW_channel' : '/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'ST_tbarW_channel' : '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',


'TTWtoQQ' : '/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/'+MCType16+'/NANOAODSIM',
'TTWtoLNu_ext1' : '/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'TTWtoLNu_ext2' : '/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/'+MCType16_ext2+'/NANOAODSIM',
'TTZtoLL_ext1' : '/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'TTZtoLL_ext2' : '/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/'+MCType16_ext2+'/NANOAODSIM',
'TTZtoLL_ext3' : '/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/'+MCType16_ext3+'/NANOAODSIM',
'TTZtoLL_M1to10' : '/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_noPULabel+'/NANOAODSIM',
'TTZtoQQ'        : '/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/'+MCType16+'/NANOAODSIM',

'WW'      : '/WW_TuneCUETP8M1_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'WW_ext1' : '/WW_TuneCUETP8M1_13TeV-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'WZ'      : '/WZ_TuneCUETP8M1_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'WZ_ext1' : '/WZ_TuneCUETP8M1_13TeV-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'ZZ'      : '/ZZ_TuneCUETP8M1_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'ZZ_ext1' : '/ZZ_TuneCUETP8M1_13TeV-pythia8/'+MCType16_ext1+'/NANOAODSIM',

'WWTo1L1Nu2Q_amcatnlo' : '/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType16+'/NANOAODSIM',
'WWToLNuQQ_powheg' : '/WWToLNuQQ_13TeV-powheg/'+MCType16+'/NANOAODSIM',
'WWToLNuQQ_powheg_ext1' : '/WWToLNuQQ_13TeV-powheg/'+MCType16_ext1+'/NANOAODSIM',
'WWTo2L2Nu_powheg' : '/WWTo2L2Nu_13TeV-powheg/'+MCType16+'/NANOAODSIM',
'WWTo4Q_powheg' : '/WWTo4Q_13TeV-powheg/'+MCType16+'/NANOAODSIM',

'WZTo1L3Nu_amcatnlo' : '/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType16+'/NANOAODSIM',
'WZTo1L1Nu2Q_amcatnlo' : '/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType16+'/NANOAODSIM',
'WZTo2L2Q_amcatnlo' : '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType16+'/NANOAODSIM',
'WZTo3LNu_powheg' : '/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'WZTo3LNu_powheg_ext1' : '/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/'+MCType16_ext1+'/NANOAODSIM',

'ZZTo2L2Q_powheg' : '/ZZTo2L2Q_13TeV_powheg_pythia8/'+MCType16+'/NANOAODSIM',
'ZZTo2L2Nu_powheg' : '/ZZTo2L2Nu_13TeV_powheg_pythia8/'+MCType16+'/NANOAODSIM',
'ZZTo2L2Nu_powheg_ext1' : '/ZZTo2L2Nu_13TeV_powheg_pythia8_ext1/'+MCType16+'/NANOAODSIM',
'ZZTo2Q2Nu_amcatnlo' : '/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType16+'/NANOAODSIM',
'ZZTo2Q2Nu_powheg' : '/ZZTo2Q2Nu_13TeV_powheg_pythia8/'+MCType16+'/NANOAODSIM',
'ZZTo4L_powheg' : '/ZZTo4L_13TeV_powheg_pythia8/'+MCType16+'/NANOAODSIM',

'VVTo2L2Nu_amcatnlo' : '/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType16+'/NANOAODSIM',
'VVTo2L2Nu_amcatnlo_ext1' : '/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType16_ext1+'/NANOAODSIM',


'WGamma' : '/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'ZGamma_01J_5f_lowMass' : '/ZGToLLG_01J_5f_lowMLL_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/'+MCType16+'/NANOAODSIM',

'ZGamma_01J_LoosePt' : '/ZGToLLG_01J_LoosePtlPtg_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/'+MCType16+'/NANOAODSIM',

'ZGamma_01J_lowMLL_lowGPt': '/ZGToLLG_01J_5f_lowMLL_lowGPt_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType16+'/NANOAODSIM',

'TGJets' : '/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/'+MCType16+'/NANOAODSIM',
'TGJets_ext1' : '/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/'+MCType16_ext1+'/NANOAODSIM',


'GJets_HT40To100'      : '/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'GJets_HT40To100_ext1' : '/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'GJets_HT100To200'      : '/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'GJets_HT100To200_ext1' : '/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'GJets_HT200To400'      : '/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'GJets_HT200To400_ext1' : '/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'GJets_HT400To600'     : '/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'GJets_HT400To600_ext1' : '/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext1+'/NANOAODSIM',
'GJets_HT600ToInf'      : '/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'GJets_HT600ToInf_ext1' : '/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/'+MCType16_ext1+'/NANOAODSIM',


'QCD_Pt15to20_Mu'         : '/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt20to30_Mu'         : '/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt30to50_Mu'         : '/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt50to80_Mu'         : '/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt80to120_Mu'        : '/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt80to120_Mu_ext1'   : '/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt120to170_Mu'       : '/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt170to300_Mu'       : '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt170to300_Mu_ext1'  : '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt300to470_Mu'       : '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt300to470_Mu_ext1'  : '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt300to470_Mu_ext2'  : '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext2+'/NANOAODSIM',
'QCD_Pt470to600_Mu'       : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt470to600_Mu_ext1'  : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt470to600_Mu_ext2'  : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext2+'/NANOAODSIM',
'QCD_Pt600to800_Mu'       : '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt600to800_Mu_ext1'  : '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt800to1000_Mu'      : '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt800to1000_Mu_ext1' : '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt800to1000_Mu_ext2' : '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext2+'/NANOAODSIM',
'QCD_Pt1000toInf_Mu'      : '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt1000toInf_Mu_ext1' : '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',


'QCD_Pt20to30_Ele'        : '/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt30to50_Ele'        : '/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt30to50_Ele_ext1'   : '/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt50to80_Ele'        : '/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt50to80_Ele_ext1'   : '/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt80to120_Ele'       : '/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt80to120_Ele_ext1'  : '/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt120to170_Ele'      : '/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt120to170_Ele_ext1' : '/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16_ext1+'/NANOAODSIM',
'QCD_Pt170to300_Ele'      : '/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt300toInf_Ele'      : '/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/'+MCType16+'/NANOAODSIM',


}

#--------------------------
# 2017
#--------------------------
#MCType17 = 'RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1'
MCType17 = 'RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1'
MCType17_pmx = MCType17.replace('102X','new_pmx_102X')
MCType17_v2 = MCType17.replace('-v1','-v2')
MCType17_ext1 = MCType17.replace('-v1','_ext1-v1')
MCType17_ext2 = MCType17.replace('-v1','_ext2-v1')
MCType17_RECOSIM = MCType17.replace('PU2017','PU2017RECOSIMstep')
MCType17_RECOSIM_ext1 = MCType17_RECOSIM.replace('-v1','_ext1-v1')
MCType17_oddTTZ = 'RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_v7_102X_mc2017_realistic_v7-v1'
                 
MCType17_oddWW = 'RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1'

DataType17='Nano1June2019-v1'

sampleList_2017 = {
'TTGamma_Dilepton'     : '/TTGamma_Dilept_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_Hadronic'   : '/TTGamma_Hadronic_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_SingleLept' : '/TTGamma_SingleLept_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM', 

'TTGamma_Dilepton_Pt100' : '/TTGamma_Dilept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_Dilepton_Pt200' : '/TTGamma_Dilept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',

'TTGamma_SingleLept_Pt100' : '/TTGamma_SingleLept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_SingleLept_Pt200' : '/TTGamma_SingleLept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',

'TTGamma_Hadronic_Pt100' : '/TTGamma_Hadronic_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_Hadronic_Pt200' : '/TTGamma_Hadronic_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',

# 'TTGamma_Dilepton_small'   : '/store/user/lpctop/TTGamma/NanoAOD/2017/Dilept',
# 'TTGamma_Hadronic_small' : '/store/user/lpctop/TTGamma/NanoAOD/2017/Had',
# 'TTGamma_SemiLept_small' : '/store/user/lpctop/TTGamma/NanoAOD/2017/SemiLept',

'TTGamma_Dilepton_TuneDown' : '/TTGamma_Dilept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_Dilepton_TuneUp'   : '/TTGamma_Dilept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_Dilepton_erdOn'    : '/TTGamma_Dilept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_Dilepton_CR1'      : '/TTGamma_Dilept_TuneCP5CR1_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_Dilepton_CR2'      : '/TTGamma_Dilept_TuneCP5CR2_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',



'TTGamma_SingleLept_TuneDown' : '/TTGamma_SingleLept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_SingleLept_TuneUp'   : '/TTGamma_SingleLept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_SingleLept_erdOn'    : '/TTGamma_SingleLept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_SingleLept_CR1'      : '/TTGamma_SingleLept_TuneCP5CR1_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',
'TTGamma_SingleLept_CR2'      : '/TTGamma_SingleLept_TuneCP5CR2_PSweights_13TeV-madgraph-pythia8/'+MCType17+'/NANOAODSIM',


'Data_SingleMu_b' : '/SingleMuon/Run2017B-'+DataType17+'/NANOAOD',
'Data_SingleMu_c' : '/SingleMuon/Run2017C-'+DataType17+'/NANOAOD',
'Data_SingleMu_d' : '/SingleMuon/Run2017D-'+DataType17+'/NANOAOD',
'Data_SingleMu_e' : '/SingleMuon/Run2017E-'+DataType17+'/NANOAOD',
'Data_SingleMu_f' : '/SingleMuon/Run2017F-'+DataType17+'/NANOAOD',

'Data_SingleEle_b' : '/SingleElectron/Run2017B-'+DataType17+'/NANOAOD',
'Data_SingleEle_c' : '/SingleElectron/Run2017C-'+DataType17+'/NANOAOD',
'Data_SingleEle_d' : '/SingleElectron/Run2017D-'+DataType17+'/NANOAOD',
'Data_SingleEle_e' : '/SingleElectron/Run2017E-'+DataType17+'/NANOAOD',
'Data_SingleEle_f' : '/SingleElectron/Run2017F-'+DataType17+'/NANOAOD',


'TTbarPowheg_Dilepton' : '/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17_pmx+'/NANOAODSIM',
'TTbarPowheg_Hadronic' : '/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17_pmx+'/NANOAODSIM',
'TTbarPowheg_Semilept' : '/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',


'W1jets'      : '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',
'W2jets'      : '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',
'W3jets'      : '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17_v2+'/NANOAODSIM',
'W4jets'      : '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17_pmx+'/NANOAODSIM',

'DYjetsM10to50'      : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17_v2+'/NANOAODSIM',
'DYjetsM10to50_ext1' : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17_ext1+'/NANOAODSIM',

'DYjetsM50_ext1' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17_RECOSIM+'/NANOAODSIM',
'DYjetsM50_ext2' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17_RECOSIM_ext1+'/NANOAODSIM',



'ST_s_channel'     : '/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/'+MCType17_pmx+'/NANOAODSIM',
'ST_t_channel'     : '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'ST_tbar_channel'  : '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'ST_tW_channel'    : '/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17_pmx+'/NANOAODSIM',
'ST_tbarW_channel' : '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',



'TTWtoQQ'       : '/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/'+MCType17+'/NANOAODSIM',
'TTWtoLNu' : '/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/'+MCType17_oddWW+'/NANOAODSIM',
'TTZtoLL'  : '/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/'+MCType17+'/NANOAODSIM',
'TTZtoLL_M1to10' : '/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType17_oddTTZ+'/NANOAODSIM',
'TTZtoQQ'        : '/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType17+'/NANOAODSIM',
'TTZtoQQ_ext1'   : '/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType17_ext1+'/NANOAODSIM',


'WW'      : '/WW_TuneCP5_13TeV-pythia8/'+MCType17+'/NANOAODSIM',
'WZ'      : '/WZ_TuneCP5_13TeV-pythia8/'+MCType17+'/NANOAODSIM',
'ZZ'      : '/ZZ_TuneCP5_13TeV-pythia8/'+MCType17_v2+'/NANOAODSIM',

'WWTo1L1Nu2Q_amcatnlo' : '/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType17_oddWW+'/NANOAODSIM',
'WWToLNuQQ_powheg' : '/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17_ext1+'/NANOAODSIM',
'WWTo2L2Nu_powheg' : '/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17_ext1+'/NANOAODSIM',
'WWTo4Q_powheg' : '/WWTo4Q_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType17_ext1+'/NANOAODSIM',

'WZTo1L3Nu_amcatnlo' : '/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/'+MCType17+'/NANOAODSIM',
'WZTo1L1Nu2Q_amcatnlo' : '/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType17+'/NANOAODSIM',
'WZTo2L2Q_amcatnlo' : '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType17+'/NANOAODSIM',
'WZTo3LNu_powheg' : '/WZTo3LNu_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',

'ZZTo2L2Q_amcatnlo' : '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType17+'/NANOAODSIM',
'ZZTo2L2Nu_powheg' : '/ZZTo2L2Nu_13TeV_powheg_pythia8/'+MCType17+'/NANOAODSIM',
'ZZTo2Q2Nu_amcatnlo' : '/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType17+'/NANOAODSIM',
'ZZTo4L_powheg' : '/ZZTo4L_13TeV_powheg_pythia8/'+MCType17+'/NANOAODSIM',
'ZZTo4L_powheg_ext1' : '/ZZTo4L_13TeV_powheg_pythia8/'+MCType17_ext1+'/NANOAODSIM',
'ZZTo4L_powheg_ext2' : '/ZZTo4L_13TeV_powheg_pythia8/'+MCType17_ext2+'/NANOAODSIM',

'VVTo2L2Nu_amcatnlo' : '/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType17+'/NANOAODSIM',

'WGamma' : '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',
'ZGamma_01J_5f_lowMass' : '/ZGToLLG_01J_5f_lowMLL_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType17+'/NANOAODSIM',

'ZGamma_01J_LoosePt' : '/ZGToLLG_01J_LoosePtlPtg_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType17+'/NANOAODSIM',

'ZGamma_01J_lowMLL_lowGPt': '/ZGToLLG_01J_5f_lowMLL_lowGPt_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType17+'/NANOAODSIM',

'TGJets' : '/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/'+MCType17+'/NANOAODSIM',

'GJets_HT40To100'       : '/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',
'GJets_HT100To200'      : '/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',
'GJets_HT200To400'      : '/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17_pmx+'/NANOAODSIM',
'GJets_HT400To600'      : '/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',
'GJets_HT600ToInf'      : '/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',

'QCD_Pt20to30_Mu'         : '/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',

'QCD_Pt30to50_Mu'         : '/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',

'QCD_Pt50to80_Mu'         : '/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt80to120_Mu'        : '/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt120to170_Mu'       : '/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt170to300_Mu'       : '/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt300to470_Mu'       : '/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt470to600_Mu'       : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt600to800_Mu'       : '/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt800to1000_Mu'      : '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt1000toInf_Mu'      : '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',

'QCD_Pt20to30_Ele'        : '/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt30to50_Ele'        : '/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt50to80_Ele'        : '/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt80to120_Ele'       : '/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt120to170_Ele'      : '/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt170to300_Ele'      : '/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt300toInf_Ele'      : '/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',

}


#--------------------------
# 2018
#--------------------------
#MCType18='RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1'
MCType18='RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1'
MCType18_ext1 = MCType18.replace('-v1','_ext1-v1')
MCType18_ext2 = MCType18.replace('-v1','_ext2-v1')
MCType18_ext3 = MCType18.replace('-v1','_ext3-v1')
MCType18_4cores5k = MCType18.replace('102X','4cores5k_102X')
MCType18_v3 = MCType18.replace('-v1','-v3')

DataType18='Nano1June2019-v1'

sampleList_2018 = {
'TTGamma_Dilepton'     : '/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_Hadronic'   : '/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_SingleLept' : '/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',

'TTGamma_Dilepton_Pt100' : '/TTGamma_Dilept_ptGamma100-200_TuneCP5_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_Dilepton_Pt200' : '/TTGamma_Dilept_ptGamma200inf_TuneCP5_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',

'TTGamma_SingleLept_Pt100' : '/TTGamma_SingleLept_ptGamma100-200_TuneCP5_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_SingleLept_Pt200' : '/TTGamma_SingleLept_ptGamma200inf_TuneCP5_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',

'TTGamma_Hadronic_Pt100' : '/TTGamma_Hadronic_ptGamma100-200_TuneCP5_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_Hadronic_Pt200' : '/TTGamma_Hadronic_ptGamma200inf_TuneCP5_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',

# 'TTGamma_Dilepton_small'   : '/store/user/lpctop/TTGamma/NanoAOD/2018/Dilept',
# 'TTGamma_Hadronic_small' : '/store/user/lpctop/TTGamma/NanoAOD/2018/Had',
# 'TTGamma_SemiLept_small' : '/store/user/lpctop/TTGamma/NanoAOD/2018/SemiLept',

'TTGamma_Dilepton_TuneDown' : '/TTGamma_Dilept_TuneCP5Down_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_Dilepton_TuneUp'   : '/TTGamma_Dilept_TuneCP5Up_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_Dilepton_erdOn'    : '/TTGamma_Dilept_TuneCP5_erdON_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_Dilepton_CR1'      : '/TTGamma_Dilept_TuneCP5CR1_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_Dilepton_CR2'      : '/TTGamma_Dilept_TuneCP5CR2_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',


'TTGamma_SingleLept_TuneDown' : '/TTGamma_SingleLept_TuneCP5Down_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_SingleLept_TuneUp'   : '/TTGamma_SingleLept_TuneCP5Up_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_SingleLept_erdOn'    : '/TTGamma_SingleLept_TuneCP5_erdON_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_SingleLept_CR1'      : '/TTGamma_SingleLept_TuneCP5CR1_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',
'TTGamma_SingleLept_CR2'      : '/TTGamma_SingleLept_TuneCP5CR2_13TeV-madgraph-pythia8/'+MCType18+'/NANOAODSIM',


'Data_SingleMu_a' : '/SingleMuon/Run2018A-'+DataType18+'/NANOAOD',
'Data_SingleMu_b' : '/SingleMuon/Run2018B-'+DataType18+'/NANOAOD',
'Data_SingleMu_c' : '/SingleMuon/Run2018C-'+DataType18+'/NANOAOD',
'Data_SingleMu_d' : '/SingleMuon/Run2018D-'+DataType18+'/NANOAOD',

'Data_SingleEle_a' : '/EGamma/Run2018A-'+DataType18+'/NANOAOD',
'Data_SingleEle_b' : '/EGamma/Run2018B-'+DataType18+'/NANOAOD',
'Data_SingleEle_c' : '/EGamma/Run2018C-'+DataType18+'/NANOAOD',
'Data_SingleEle_d' : '/EGamma/Run2018D-'+DataType18+'/NANOAOD',


'TTbarPowheg_Dilepton' : '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Hadronic' : '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/'+MCType18_v3+'/NANOAODSIM',
'TTbarPowheg_Semilept' : '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',


'W1jets'      : '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'W2jets'      : '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'W3jets'      : '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'W4jets'      : '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',

'DYjetsM10to50'  : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'DYjetsM10to50_ext1'  : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18_ext1+'/NANOAODSIM',
'DYjetsM50'      : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',


'ST_s_channel'     : '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/'+MCType18_ext1+'/NANOAODSIM',
'ST_t_channel'     : '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/'+MCType18+'/NANOAODSIM',
'ST_tbar_channel'  : '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/'+MCType18+'/NANOAODSIM',
'ST_tW_channel'    : '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/'+MCType18_ext1+'/NANOAODSIM',
'ST_tbarW_channel' : '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/'+MCType18_ext1+'/NANOAODSIM',


'TTWtoQQ'  : '/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/'+MCType18+'/NANOAODSIM',
'TTWtoLNu' : '/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/'+MCType18_ext1+'/NANOAODSIM',
'TTZtoLL'  : '/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType18_ext1+'/NANOAODSIM',
'TTZtoLL_M1to10' : '/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType18+'/NANOAODSIM',
'TTZtoQQ' : '/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType18+'/NANOAODSIM',
'TTZtoQQ_ext1' : '/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType18_ext1+'/NANOAODSIM',

'WW'      : '/WW_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'WZ'      : '/WZ_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'ZZ'      : '/ZZ_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',

'WWTo1L1Nu2Q_amcatnlo' : '/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType18+'/NANOAODSIM',
'WWToLNuQQ_powheg' : '/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'WWTo2L2Nu_powheg' : '/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'WWTo4Q_powheg' : '/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',

'WZTo1L3Nu_amcatnlo' : '/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType18+'/NANOAODSIM',
'WZTo1L1Nu2Q_amcatnlo' : '/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType18+'/NANOAODSIM',
'WZTo2L2Q_amcatnlo' : '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType18+'/NANOAODSIM',
'WZTo3LNu_powheg' : '/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/'+MCType18_ext1+'/NANOAODSIM',
'WZTo3LNu_amcatnlo' : '/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType18+'/NANOAODSIM',
'WZTo3LNu_amcatnlo_ext1' : '/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType18_ext1+'/NANOAODSIM',

'ZZTo2L2Q_amcatnlo' : '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType18+'/NANOAODSIM',
'ZZTo2L2Nu_powheg_ext1' : '/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/'+MCType18_ext1+'/NANOAODSIM',
'ZZTo2L2Nu_powheg_ext2' : '/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/'+MCType18_ext2+'/NANOAODSIM',
'ZZTo2Q2Nu_amcatnlo' : '/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType18+'/NANOAODSIM',
'ZZTo4L_powheg_ext1' : '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/'+MCType18_ext1+'/NANOAODSIM',
'ZZTo4L_powheg_ext2' : '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/'+MCType18_ext2+'/NANOAODSIM',
'ZZTo4L_amcatnlo' : '/ZZTo4L_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType18+'/NANOAODSIM',

'VVTo2L2Nu_amcatnlo' : '/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType18+'/NANOAODSIM',

'WGamma' : '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'ZGamma_01J_5f_lowMass' : '/ZGToLLG_01J_5f_lowMLL_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType18+'/NANOAODSIM',

'ZGamma_01J_LoosePt' : '/ZGToLLG_01J_LoosePtlPtg_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType18+'/NANOAODSIM',

'ZGamma_01J_lowMLL_lowGPt': '/ZGToLLG_01J_5f_lowMLL_lowGPt_TuneCP5_13TeV-amcatnloFXFX-pythia8/'+MCType18+'/NANOAODSIM',

'TGJets' : '/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/'+MCType18+'/NANOAODSIM',


'GJets_HT40To100'       : '/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'GJets_HT100To200'      : '/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18_4cores5k+'/NANOAODSIM',
'GJets_HT200To400'      : '/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'GJets_HT400To600'      : '/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'GJets_HT600ToInf'      : '/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18_ext1+'/NANOAODSIM',


'QCD_Pt20to30_Mu'         : '/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt30to50_Mu'         : '/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt50to80_Mu'         : '/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt80to120_Mu'        : '/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt80to120_Mu_ext1'   : '/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18_ext1+'/NANOAODSIM',
'QCD_Pt120to170_Mu'       : '/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt120to170_Mu_ext1'  : '/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18_ext1+'/NANOAODSIM',
'QCD_Pt170to300_Mu'       : '/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt300to470_Mu'       : '/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt300to470_Mu_ext3'  : '/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18_ext3+'/NANOAODSIM',
'QCD_Pt470to600_Mu'       : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt470to600_Mu_ext1'  : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18_ext1+'/NANOAODSIM',
'QCD_Pt600to800_Mu'       : '/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt800to1000_Mu'      : '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18_ext3+'/NANOAODSIM',
'QCD_Pt1000toInf_Mu'      : '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',

'QCD_Pt20to30_Ele'        : '/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt30to50_Ele'        : '/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18_ext1+'/NANOAODSIM',
'QCD_Pt50to80_Ele'        : '/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt80to120_Ele'       : '/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt120to170_Ele'      : '/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt170to300_Ele'      : '/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt300toInf_Ele'      : '/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18+'/NANOAODSIM',

}
