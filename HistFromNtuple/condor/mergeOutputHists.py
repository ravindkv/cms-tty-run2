
#//////////////////////////////////////////////////
#                                                 #
# Merge histo files into a single root file       #
#                                                 #
#//////////////////////////////////////////////////

import os
from optparse import OptionParser
from HistInputs import *

#-----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-d", "--decay", dest="ttbarDecayMode", default="SemiLep",type='str',
                     help="Specify which decay moded of ttbar SemiLep or DiLep? default is SemiLep")
(options, args) = parser.parse_args()
year = options.year
channel = options.channel
decay   = options.ttbarDecayMode

#-----------------------------------------
#Path of the I/O histrograms
#----------------------------------------
inHistSubDir = "Hists/%s/%s/%s"%(year, decay, channel)
inHistFullDir = "%s/%s"%(condorHistDir, inHistSubDir)
outHistSubDir = "Hists/%s/%s/%s/Merged"%(year, decay, channel)
outHistFullDir = "%s/%s"%(condorHistDir, outHistSubDir)
if not os.path.exists(outHistFullDir):
    os.makedirs(outHistFullDir)

#-----------------------------------------
#Merge histograms using hadd
#----------------------------------------
def runMe(command):
    print ""
    print "\033[01;32m"+ "Excecuting: "+ "\033[00m",  command
    print ""
    os.system(command)

if channel in ["mu", "Mu", "MU", "mU"]:
    for sampleMu in SampleListMu:
        runMe("hadd -f %s/%s.root %s/%s*.root"%(outHistFullDir, sampleMu, inHistFullDir, sampleMu))
else:
    for sampleEle in SampleListEle:
        runMe("hadd -k %s/%s.root %s/%s*.root"%(outHistFullDir, sampleEle, inHistFullDir, sampleEle))

runMe("mv %s/Data%s.root %s/Data.root"%(outHistFullDir, channel, outHistFullDir))
runMe("mv %s/QCD%s.root %s/QCD.root"%(outHistFullDir, channel, outHistFullDir))
runMe("hadd -k %s/AllInc.root %s/*.root "%(outHistFullDir,outHistFullDir))
print "-------------------------------------"
print "OUTPUT DIR: ", outHistFullDir
print "-------------------------------------"
print runMe(("du -h %s/*.root")%outHistFullDir)

