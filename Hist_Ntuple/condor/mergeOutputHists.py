
#//////////////////////////////////////////////////
#                                                 #
# Merge histo files into a single root file       #
#                                                 #
#//////////////////////////////////////////////////
#https://uscms.org/uscms_at_work/computing/LPC/usingEOSAtLPC.shtml#listFilesOnEOS
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
parser.add_option("-d", "--decay", dest="ttbarDecayMode", default="Semilep",type='str',
                     help="Specify which decay moded of ttbar Semilep or Dilep? default is Semilep")
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
runCmd("eos root://cmseos.fnal.gov mkdir -p %s"%outHistFullDir)

#-----------------------------------------
#Merge histograms using hadd
#----------------------------------------
def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

if channel in ["mu", "Mu", "MU", "mU"]:
    for sampleMu in SampleListMu:
        haddOut = "root://cmseos.fnal.gov/%s/%s.root"%(outHistFullDir, sampleMu)
        haddIn  = "`xrdfs root://cmseos.fnal.gov ls -u %s | grep \'%s_.*root\'`"%( inHistFullDir, sampleMu)
        runCmd("hadd -f %s %s"%(haddOut, haddIn))
else:
    for sampleEle in SampleListEle:
        haddOut = "root://cmseos.fnal.gov/%s/%s.root"%(outHistFullDir, sampleEle)
        haddIn  = "`xrdfs root://cmseos.fnal.gov ls -u %s | grep \'%s_.*root\'`"%( inHistFullDir, sampleEle)
        runCmd("hadd -f %s %s"%(haddOut, haddIn))

runCmd("eos root://cmseos.fnal.gov mv %s/Data%s.root %s/Data.root"%(outHistFullDir, channel, outHistFullDir))
runCmd("eos root://cmseos.fnal.gov mv %s/QCD%s.root %s/QCD.root"%(outHistFullDir, channel, outHistFullDir))
#Merge all histograms
haddOut = "root://cmseos.fnal.gov/%s/AllInc.root"%(outHistFullDir)
haddIn  = "`xrdfs root://cmseos.fnal.gov ls -u %s | grep \'.*root\'`"%(outHistFullDir)
runCmd("hadd -f %s %s"%(haddOut, haddIn))
print "-------------------------------------"
print "OUTPUT DIR: ", outHistFullDir
print "-------------------------------------"
print runCmd(("eos root://cmseos.fnal.gov find --size %s")%outHistFullDir)


