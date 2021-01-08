
# PlotFromHist

* Here the plots containing overlay of data and stacked backgrounds
along with systematic and statistical uncertainty band are made
from the histograms produced from HistFromNtuple sub-package. The
ratio of data and total background is also plotted.

* We also need to make plots after the fit. The combine tool is
used for fitting. The root file containing histograms from the 
combine has slightly different directory structure. Hence we need
a seprate script to make post-fit plots.

* The basic inputs such as sample name, syst up/down, channel, year
are kept in a separate file. The empty histograms, TDRStyle, CMSLumi
are also kept separtely.

* Run the following for producing one pre-fit histogram
python makePreFitPlots.py --plot presel_Njet 

