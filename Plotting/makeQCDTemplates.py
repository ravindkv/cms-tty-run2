from ROOT import *
import os
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                     help="Use 4j1t selection" )
parser.add_option("--Tight0b","--tight0b", dest="isTightSelection0b", default=False,action="store_true",
                     help="Use 4j0t selection" )
parser.add_option("--Loose","--loose", dest="isLooseSelection", default=False,action="store_true",
                     help="Use 2j0t selection" )
parser.add_option("--LooseCRe2g1","--looseCRe2g1", dest="isLooseCRe2g1Selection",default=False,action="store_true",
                  help="Use ==2j at least 1t control region selection")
parser.add_option("--LooseCR3g0","--looseCR3g0", dest="isLooseCR3g0Selection",default=False,action="store_true",
                  help="Use >=2j at least 1t control region selection")

parser.add_option("--LooseCRe3g1","--looseCRe3g1", dest="isLooseCRe3g1Selection",default=False,action="store_true",
                  help="Use 3j exactly 0t control region selection" )

#parser.add_option("-f","--file",dest="fileDir",default="histograms/mu/qcdhistsCR",
 #                    help="histogram file direcotry")

(options, args) = parser.parse_args()

finalState = options.channel
isTightSelection = options.isTightSelection
isTightSelection0b = options.isTightSelection0b
isLooseSelection = options.isLooseSelection
isLooseCR3g0Selection=options.isLooseCR3g0Selection
isLooseCRe2g1Selection = options.isLooseCRe2g1Selection
isLooseCRe3g1Selection = options.isLooseCRe3g1Selection
#_fileDir = options.fileDir
if finalState=="Mu":
	_fileDir="histograms/mu/qcdhistsCR"
	if isLooseCRe2g1Selection:
		_fileDir ="histograms/mu/qcdhistsCR_looseCRe2g1/"
	elif isLooseCR3g0Selection:
		_fileDir ="histograms/mu/qcdhistsCR_looseCRe3g0/"
	elif isLooseCRe3g1Selection:
                _fileDir ="histograms/mu/qcdhistsCR_looseCRe3g1/"
	elif isTightSelection:
		_fileDir ="histograms/mu/qcdhistsCR_tight/"
	elif isTightSelection0b:
                _fileDir ="histograms/mu/qcdhistsCR_tight0b/"
#	if "CR2" in sys.argv:
#		 _fileDir="histograms/mu/qcdhistsCR2"

elif finalState=="Ele":
	_fileDir="histograms/ele/qcdhistsCR"
	if isLooseCRe2g1Selection:
                _fileDir ="histograms/ele/qcdhistsCR_looseCRe2g1/"
	elif isLooseCR3g0Selection:
                _fileDir ="histograms/ele/qcdhistsCR_looseCRe3g0/"
        elif isLooseCRe3g1Selection:
                _fileDir ="histograms/ele/qcdhistsCR_looseCRe3g1/"
	elif isTightSelection:
		_fileDir ="histograms/ele/qcdhistsCR_tight/"
	elif isTightSelection0b:
                _fileDir ="histograms/ele/qcdhistsCR_tight0b/"
#	if "CR2" in sys.argv:
#		_fileDir="histograms/ele/qcdhistsCR2"
	

# if finalState=="Mu":
#     if isTightSelection:
#         _file  = TFile("histograms/mu/qcdhistsCR_Tight.root","update")
#     elif isTightSelection:
#         _file  = TFile("histograms/mu/qcdhistsCR_Loose.root","update")
#     else:
#         _file  = TFile("histograms/mu/qcdhistsCR.root","update")

# if finalState=="Ele":
#     if isTightSelection:
#         _file  = TFile("histograms/ele/qcdhistsCR_Tight.root","update")
#     elif isTightSelection:
#         _file  = TFile("histograms/ele/qcdhistsCR_Loose.root","update")
#     else:
#         _file  = TFile("histograms/ele/qcdhistsCR.root","update")



#if 'CR2' in sys.argv:
 #    _file  = TFile("histograms/mu/qcdhistsCR2.root","update")


from sampleInformation import *

stackList = sampleList[:-3]

_file = {}
print _fileDir
for sample in stackList:
#	print sample, "%s/%s.root"%(_fileDir,sample)
	_file[sample] = TFile("%s/%s.root"%(_fileDir,sample),"read")

if finalState=='Ele':
	sample = "DataEle"
	_file[sample] = TFile("%s/%s.root"%(_fileDir,sample),"read")
if finalState=='Mu':
	sample = "DataMu"
	_file[sample] = TFile("%s/%s.root"%(_fileDir,sample),"read")


gROOT.SetBatch(True)
keylist = _file["Data%s"%finalState].GetListOfKeys()
	

#keylist = gDirectory.GetListOfKeys()
keylist = _file["Data%s"%finalState].GetListOfKeys()	
#print keylist

histoList = {}
print stackList
for key in keylist:
    
    name = key.GetName()
    print name
    split = name.split('_')
    nameKey = split[0]
    if "Dilep" in nameKey:continue
#    print split, nameKey, split[1:-1]

    for n in split[1:-1]: nameKey += "_%s"%n

    hName = "%s_QCD_DD"%(nameKey)
#    print hName
   # histoList[nameKey] = key.ReadObj().Clone(hName)
    histoList[nameKey]= _file["Data%s"%finalState].Get("%s_%s"%(nameKey,"Data%s"%finalState))
    histoList[nameKey].SetNameTitle(hName,hName)

    for sample in stackList:
#	print "%s_%s"%(nameKey,sample)
        tempHist = _file[sample].Get("%s_%s"%(nameKey,sample))
	print _file[sample], "%s_%s"%(nameKey,sample)
	if nameKey=="presel_DilepMass":continue
	if "endcap" in nameKey:continue
        histoList[nameKey].Add(tempHist,-1)

outputFile = TFile("%s/QCD_DD.root"%_fileDir,"recreate")
print "output file:"," %s/QCD_DD.root"%(_fileDir)
for h in histoList:
    histoList[h].Write()

outputFile.Close()

