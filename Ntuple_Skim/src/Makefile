all: FactorizedJetCorrector.o JetCorrectorParameters.o SimpleJetCorrector.o JetCorrectionUncertainty.o JECvariation.o JetResolutionObject.o JetResolution.o

clean:
	rm FactorizedJetCorrector.o JetCorrectorParameters.o SimpleJetCorrector.o JetCorrectionUncertainty.o SimpleJetCorrectionUncertainty.o JECvariation.o

JECvariation.o: FactorizedJetCorrector.o JetCorrectorParameters.o SimpleJetCorrector.o JetCorrectionUncertainty.o JECvariation.cpp
	g++ -c `root-config --libs` -I`root-config --incdir` -std=c++17 JECvariation.cpp

JetResolution.o: JetResolution.h JetResolution.cc
	g++ -c `root-config --libs` -I`root-config --incdir` -std=c++17 -D STANDALONE JetResolution.cc 

JetResolutionObject.o: JetResolutionObject.cc JetResolutionObject.h
	g++ -c `root-config --libs` -I`root-config --incdir` -std=c++17 -D STANDALONE JERUtilities.h JetResolutionObject.cc 

FactorizedJetCorrector.o: FactorizedJetCorrector.cpp FactorizedJetCorrector.h JetCorrectorParameters.h SimpleJetCorrector.h Utilities.cc
	g++ -c `root-config --libs` -I`root-config --incdir` -std=c++17 FactorizedJetCorrector.cpp

JetCorrectorParameters.o: JetCorrectorParameters.cpp JetCorrectorParameters.h 
	g++ -c `root-config --libs` -I`root-config --incdir` -std=c++17 JetCorrectorParameters.cpp

SimpleJetCorrector.o: JetCorrectorParameters.cpp JetCorrectorParameters.h SimpleJetCorrector.h
	g++ -c `root-config --libs` -I`root-config --incdir` -std=c++17 SimpleJetCorrector.cpp 

JetCorrectionUncertainty.o: JetCorrectionUncertainty.cpp JetCorrectionUncertainty.h SimpleJetCorrectionUncertainty.cpp SimpleJetCorrectionUncertainty.h
	g++ -c `root-config --libs` -I`root-config --incdir` -std=c++17 JetCorrectionUncertainty.cpp SimpleJetCorrectionUncertainty.cpp 

