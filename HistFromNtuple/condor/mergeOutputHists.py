
#//////////////////////////////////////////////////
#                                                 #
# Merge histo files into a single root file       #
#                                                 #
#//////////////////////////////////////////////////

import os
from optparse import OptionParser
from BasicInputs import *

#-----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
(options, args) = parser.parse_args()
year = options.year
channel = options.channel

#-----------------------------------------
#Path of the I/O histrograms
#----------------------------------------
histMainDir = "/home/rverma/t3store/TTGammaSemiLep13TeV"
inHistSubDir = "Histograms/%s/SemiLep/%s"%(year, channel)
inHistFullDir = "%s/%s"%(histMainDir, inHistSubDir)
outHistSubDir = "Histograms/%s/SemiLep/%s/Merged"%(year, channel)
outHistFullDir = "%s/%s"%(histMainDir, outHistSubDir)
if not os.path.exists(outHistFullDir):
    os.makedirs(outHistFullDir)

#-----------------------------------------
#Merge histograms using hadd
#----------------------------------------
def execme(command):
    print ""
    print "\033[01;32m"+ "Excecuting: "+ "\033[00m",  command
    print ""
    os.system(command)

if channel in ["mu", "Mu", "MU", "mU"]:
    for sampleMu in SampleListMu:
        execme("hadd -f %s/%s.root %s/%s*.root"%(outHistFullDir, sampleMu, inHistFullDir, sampleMu))
else:
    for sampleEle in SampleListEle:
        execme("hadd -k %s/%s.root %s/%s*.root"%(outHistFullDir, sampleEle, inHistFullDir, sampleEle))

print "-------------------------------------"
print "OUTPUT DIR: ", outHistFullDir
print "-------------------------------------"
print execme(("du -h %s/*.root")%outHistFullDir)
