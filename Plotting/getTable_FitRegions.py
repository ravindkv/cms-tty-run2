from ROOT import *
import os

import sys
from optparse import OptionParser

padRatio = 0.25
padOverlap = 0.15
padGap = 0.01
parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
		  help="Use 4j2t selection" )
parser.add_option("--LooseCR2e0","--looseCR2e0", dest="isLooseCR2e0Selection", default=False,action="store_true",
		  help="Use 2j exactly 0t control region selection" )
parser.add_option("--LooseCR3e0","--looseCR3e0", dest="isLooseCR3e0Selection", default=False,action="store_true",
		  help="Use 3j exactly 0t control region selection" )
parser.add_option("--LooseCR2g0","--looseCR2g0", dest="isLooseCR2g0Selection", default=False,action="store_true",
		  help="Use 2j at least 0t control region selection" )
parser.add_option("--LooseCR2g1","--looseCR2g1", dest="isLooseCR2g1Selection", default=False,action="store_true",
		  help="Use 2j at least 1t control region selection" )

(options, args) = parser.parse_args()
finalState = options.channel

isTightSelection = options.isTightSelection
isLooseCR2e0Selection = options.isLooseCR2e0Selection
isLooseCR2g0Selection = options.isLooseCR2g0Selection
isLooseCR2g1Selection = options.isLooseCR2g1Selection
isLooseCR3e0Selection = options.isLooseCR3e0Selection


print "Running on the %s channel"%(finalState)


if finalState=='Mu':
	channel = 'mu'
if finalState=='Ele':
	channel = 'ele'


_fileDir = "histograms/%s/hists/"%channel
if isTightSelection:      _fileDir  = "histograms/%s/hists_tight/"%channel
if isLooseCR2e0Selection: _fileDir  = "histograms/%s/hists_looseCR2e0/"%channel
if isLooseCR2g0Selection: _fileDir  = "histograms/%s/hists_looseCR2g0/"%channel
if isLooseCR2g1Selection: _fileDir  = "histograms/%s/hists_looseCR2g1/"%channel
if isLooseCR3e0Selection: _fileDir  = "histograms/%s/hists_looseCR3e0/"%channel





list_ = ['TTGamma', 'TTbar', 'TGJets','ST-tW','ST-tch','ST-sch', 'WGamma','ZGamma','WJets', 'ZJets', 'TTV', 'Diboson']
list_ = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WGamma','ZGamma','WJets', 'ZJets', 'TTV', 'Diboson']
#list_=["ZGamma"]
gROOT.SetBatch(True)

yield_ = {}
err_ = {}
sum_s = {}
err_s = {}

for l in list_:
	yield_[l] = []
	err_[l] = []
	sum_s[l] = 0
	err_s[l] = 0

for sample in list_:
	_file = TFile("%s/%s.root"%(_fileDir,sample),"read")
	hist=_file.Get("phosel_PhotonCategory_%s"%(sample))	
	for i in range(1,5):
                err = Double(0.0)
                err_[sample].append(err)            
        	yield_[sample].append(float(hist.IntegralAndError(i,i,err)))


for i in range(4):
	yield_['SingleTop'][i] += yield_['TGJets'][i]
	err_['SingleTop'][i] = (err_['SingleTop'][i]**2 + err_['TGJets'][i]**2)**0.5

list_.remove('TGJets')

_file = TFile("%s/Data%s.root"%(_fileDir,finalState),"read")
hist=_file.Get("phosel_M3_Data%s"%(finalState))
data = hist.Integral(-1,-1)

_file = TFile("%s/QCD_DD.root"%(_fileDir),"read")
hist=_file.Get("phosel_M3_QCD_DD")
yield_['QCD'] = [0,0,0,0]
err_['QCD'] = [0,0,0,0]
err = Double(0.0)
yield_['QCD'][3] = hist.IntegralAndError(-1,-1, err)
err_['QCD'][3] = err

sum

list_.append('QCD')

sum_=[]
total_=0
totalerr=0.0

error=0.
error= (totalerr)**.5
#for i in range(9):
#	total_+=sum_[i]

genuine_=0
genuineerr=0.
misID_=0
misIDerr=0.
HadPho_=0
HadPhoerr=0.
HadFake_=0
HadFakeerr=0.
for sample in list_:
	genuine_+=yield_[sample][0]
        misID_+=yield_[sample][1]
        HadPho_+=yield_[sample][2]
        HadFake_+=yield_[sample][3]
        genuineerr+=(err_[sample][0])**2
        misIDerr+=(err_[sample][1])**2
        HadPhoerr+=(err_[sample][2])**2
        HadFakeerr+=(err_[sample][3])**2

genuine_error=genuineerr**0.5
misID_error=misIDerr**0.5
HadPho_error=HadPhoerr**0.5
HadFake_error=HadFakeerr**0.5

process_list ={"TTGamma":["TTGamma"],
	       "TTbar":  ["TTbar"],
	       "VGamma":["ZGamma", "WGamma"],
	       "VJets":["WJets", "ZJets"],
#	       "SingleTop":["SingleTop"],
	       "Other":[ "TTV", "Diboson","QCD","SingleTop"],
	       }	


prompt ={}
prompt_err ={}
nonprompt = {}
nonprompt_err = {}

totalPrompt = 0.
totalPromptErr = 0.

totalNonPrompt = 0.
totalNonPromptErr = 0.


for process in process_list:
	prompt[process] = 0.
	prompt_err[process] = 0.
	nonprompt[process] = 0.
	nonprompt_err[process] = 0.
	for sample in process_list[process]:
		prompt[process] += yield_[sample][0] + yield_[sample][1]
		prompt_err[process] += err_[sample][0]**2 + err_[sample][1]**2

		nonprompt[process] += yield_[sample][2] + yield_[sample][3]
		nonprompt_err[process] += err_[sample][2]**2 + err_[sample][3]**2

	totalPrompt += prompt[process]
	totalPromptErr += prompt_err[process]
	totalNonPrompt += nonprompt[process]
	totalNonPromptErr += nonprompt_err[process]

	sum_s[process] = prompt[process] + nonprompt[process]
	err_s[process] = prompt_err[process] + nonprompt_err[process]

	prompt_err[process] = prompt_err[process]**0.5
	nonprompt_err[process] = nonprompt_err[process]**0.5
	err_s[process] = err_s[process]**0.5

for sample in process_list:
	total_+=sum_s[sample]
	totalerr+= err_s[sample]**2


totalPromptErr = totalPromptErr**0.5
totalNonPromptErr = totalNonPromptErr**0.5
totalerr = totalerr **0.5

process_list = ["TTGamma", "TTbar", "VGamma","Other"]

process_latexNames = {"TTGamma":r"$t\bar{t}$+$\gamma$",
		      "TTbar":r"$t\bar{t}$",
		      "VGamma":r"$V\gamma",
		      "SingleTop":r"$Single top$",
		      "VJets":r"$VJets$",
		      "Other":r"$Other$",
		      }
print
print
print

table=''
table +=  '\\begin{tabular}{l | c c  } \n'
table +=  '\\hline\n'
table +=  'Sample & Prompt & Hadronic/Nonprompt \\\\ \n'
table +=  '\\hline\n'
for sample in process_list:
	table += '%s & $%.1f \pm %.1f$   & $%.1f \\pm %.1f$  \\\\ \n' % (process_latexNames[sample], prompt[sample], prompt_err[sample], nonprompt[sample], nonprompt_err[sample])

table += '\\end{tabular} \n'

table = table.replace("$0.0 \pm 0.0$","---")

print table
print
print
print
table=''
table +=  '\\begin{tabular}{l | c c | c } \n'
table +=  '\\hline\n'
table +=  'Sample & Prompt & Hadronic/Nonprompt & Total \\\\ \n'
table +=  '\\hline\n'
for sample in process_list:
	table += '%s & $%.1f \pm %.1f$  & $%.1f \\pm %.1f$ & $%.1f \\pm %.1f$  \\\\ \n' % (process_latexNames[sample], prompt[sample], prompt_err[sample], nonprompt[sample], nonprompt_err[sample], sum_s[sample], err_s[sample])

table += '\\hline \n'
table += "MC Totals & $%.1f \\pm %.1f$ & $%.1f \\pm %.1f$ & $%.1f \\pm %.1f$ &\\\\ \n" %(totalPrompt,totalPromptErr, totalNonPrompt, totalNonPromptErr, total_, error)
table += "Data & --- & --- & $%.1f$ &\\\\ \n" %(data)
table += '\\hline \n'
table += '\\end{tabular} \n'

table = table.replace("$0.0 \pm 0.0$","---")

print table


