#ifndef OVERLAP_H
#define OVERLAP_H

#include"EventTree.h"
#include<iostream>
#include<cstdlib>
#include <math.h>
#include <algorithm>
#include <tuple>

#include "Utils.h"

std::vector<double> minGenDr(int myInd, const EventTree* tree, std::vector<int> ignorePID = std::vector<int>());

bool overlapRemoval(EventTree* tree, double Et_cut, double Eta_cut, double dR_cut, bool verbose);
bool overlapRemoval_2To3(EventTree* tree, double Et_cut, double Eta_cut, double dR_cut, bool verbose);
bool overlapRemovalTT(EventTree* tree, bool verbose);
bool overlapRemovalZJets(EventTree* tree, bool verbose=false);
bool overlapRemovalWJets(EventTree* tree, bool verbose=false);
bool overlapRemoval_Tchannel(EventTree* tree);

#endif
