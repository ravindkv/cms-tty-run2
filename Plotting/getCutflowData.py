from ROOT import *

labels = ['Trigger \\& Good Vtx', '1 Muon', 'No Loose Muons', 'Electron Veto', '$>=1$ jet', '$>=2$ jets',  '$>=3$ jets', '$>=1$ b-tags', 'Photon']

SampleNames = ['Data','TTGamma','TTbar','ST t-ch','ST s-ch', 'ST tW', 'W+jets', 'Z+jets', 'W+gamma', 'Z+gamma', 'TTV']

files = {"Data":["Data_SingleMu_b_Cutflow.root",
                 "Data_SingleMu_c_Cutflow.root",
                 "Data_SingleMu_d_Cutflow.root",
                 "Data_SingleMu_e_Cutflow.root",
                 "Data_SingleMu_f_Cutflow.root",
                 "Data_SingleMu_g_Cutflow.root",
                 "Data_SingleMu_h_Cutflow.root"],
         "TTGamma":["TTGamma_Dilepton_Cutflow.root",
                    "TTGamma_Hadronic_Cutflow.root",
                    "TTGamma_SingleLeptFromT_Cutflow.root",
                    "TTGamma_SingleLeptFromTbar_Cutflow.root"],
         "TTbar":["TTbarPowheg_Cutflow.root"],
         "ST t-ch":["ST_t-channel_Cutflow.root",
                    "ST_tbar-channel_Cutflow.root"],
         "ST s-ch":["ST_s-channel_Cutflow.root"],
         "ST tW":["ST_tW-channel_Cutflow.root",
                  "ST_tbarW-channel_Cutflow.root"],
         "TTV":["TTWtoLNu_Cutflow.root",
                "TTWtoQQ_Cutflow.root",
                "TTZtoLL_Cutflow.root"],
         "W+jets":["W1jets_Cutflow.root",
                   "W2jets_Cutflow.root",
                   "W3jets_Cutflow.root",
                   "W4jets_Cutflow.root"],
         "Z+jets":["DYjetsM10to50_Cutflow.root",
                   "DYjetsM50_Cutflow.root"],
         "W+gamma":["WGamma_Cutflow.root"],
         "Z+gamma":["ZGamma_Cutflow.root"],
         }


Cutflows ={}
Cutflows["Total"] = [0]*10
for sample in SampleNames:
    fileList = files[sample]
    Cutflows[sample] = [0]*10
    print sample
    for _fileName in fileList:
        _file = TFile.Open("root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_Cutflows/%s"%_fileName,"read")

#        print _fileName

        cutflow_mu = _file.Get("cut_flow_weight_mu")
        j = 0
        for i in range(2,16):
            if not i in [10,12,13,14]:
                Cutflows[sample][j] = Cutflows[sample][j] + cutflow_mu.GetBinContent(i)
                if not sample =="Data": Cutflows["Total"][j] = Cutflows["Total"][j] + cutflow_mu.GetBinContent(i)
                j += 1

print Cutflows


print "\\resizebox{\\textwidth}{!}{"
print "\\begin{tabular}{l | c c c c c c c c | c}"
print "\\hline"
print "Sample ",
for l in labels:
    print "& %s "%l,
print "\\\\"

print "\\hline"
sample = "TTGamma"
print "%s "%sample,
data = Cutflows[sample]
for x in data[1:]:
    print "& %.1f "%x,
print "\\\\"

print "\\hline"
for sample in SampleNames[2:]:
    print "%s "%sample,
    data = Cutflows[sample]
    for x in data[1:]:
        print "& %.1f "%x,

    print "\\\\"

print "\\hline"
sample = "Total"
print "%s "%sample,
data = Cutflows[sample]
for x in data[1:]:
    print "& %.1f "%x,
print "\\\\"

print "\\hline"
sample = "Data"
print "%s "%sample,
data = Cutflows[sample]
for x in data[1:]:
    print "& %i "%x,
print "\\\\"
print "\\hline"

print "Data/MC",
data = Cutflows["Data"]
total = Cutflows["Total"]
for x,y in zip(data[1:],total[1:]):
    print "& %.3f "%(x/y),
print "\\\\"
print "\\hline"



print "\\end{tabular} }"
