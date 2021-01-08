import ROOT
import sys
# python scanRootFile.py fileName.root

fileName = sys.argv[-1]
def readDir(mydir,level):
    level = level +1
    print "Directory level: %s"%level
    ROOT.gDirectory.pwd()
    keys = ROOT.TIter(mydir.GetListOfKeys())
    #print mydir.GetListOfKeys().Print()
    for key in keys:
        if key.IsFolder():
            mydir.cd(key.GetName())
            #mydir.ls()
            #mydir.GetListOfKeys().Print()
            subdir = ROOT.gDirectory
            readDir(subdir,level)
        else:
            dataType=key.GetClassName()
            if dataType=="TH1F":
                h = key.ReadObj()
                hName = h.GetName()
                hInt = round(h.Integral(),2)
                hEnt = round(h.GetEntries(),2)
                hWt  = round(h.Integral()/h.GetEntries(),4)
                print "%15s %10s %15s %5s"%(
                        str(hName), str(hInt), 
                        str(hEnt),str(hWt))

f = ROOT.TFile(fileName)
if f.IsZombie():
    print "Input file %s is corrupted"%fileName
    sys.exit()
else:
    readDir(f,0)
