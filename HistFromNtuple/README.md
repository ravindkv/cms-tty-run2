
#HistFromNtuple

* As the name suggests, in this directory, we have scripts to produce 
histograms from ntuples. The ntuples already contain all variables
associated with various physics objects such as an electron, muon, photon,
jets, and missing transverse energy.

* The histograms are initialized in a seprate file. A few other functions
are also defined in a separate file. The name of these files ends with "cff.py".
Finally, these files are imported inside the main file. 

* The main file is programmed so that it can produce one or multiple 
histograms for the different standard model process, decay modes, multiple
years of data-taking, etc. 

* For example, to produce histogram of jet multiplicity (NJet) of TTbar
process, for the year 2016, and muon channel, run the following:
    python makeHists13TeV.py -y 2016 -c Mu -s TTbar --plot presel_Njet 

* To produce multiple histograms, run the following:
    python makeHists13TeV.py -y 2016 -c Mu -s TTbar

* To run multiple jobs simultaneously, a condor setup is in place. Please
read the condor/README
