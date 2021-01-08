#ifndef EVENTPICK_H
#define EVENTPICK_H

#include<vector>
#include<string>
#include<set>
#include<iostream>
#include<TH1F.h>
#include<TH1D.h>

#include"EventTree_Skim.h"

class EventPick{
public:
	EventPick(std::string titleIn);
	~EventPick();
	
	void process_event(EventTree* inp_tree);

	std::string title;
	
	bool saveCutflows;

	std::string year;

	int printEvent;

	// cuts as parameters, to modify easily
	double MET_cut;
	bool no_trigger;

	int Nlep_eq;
	
	int Njet_ge;
	int NBjet_ge;
	int SkimNjet_ge;
	int SkimNBjet_ge;

	bool ZeroBExclusive;

	int Jet_Pt_cut_1;
	int Jet_Pt_cut_2;
	int Jet_Pt_cut_3;	
	int Nele_eq;
	int Nmu_eq;
	int NEleVeto_le;
	
	int Npho_ge;
	int NlooseMuVeto_le;
	int NlooseEleVeto_le;
	int NmediumEleVeto_le;
	
	bool skimEle;
	bool skimMu;

	// variables showing passing or failing selections
	bool passSkim;
	bool passPresel_ele; // passed preselection
	bool passAll_ele; // single flag: event passed all cuts: preselection + photon
	bool passPresel_mu; // passed preselection
	bool passAll_mu; // single flag: event passed all cuts: preselection + photon
	bool passFirstcut; // pass the sync cut	
	// histograms
	TH1D* cutFlow_mu;
	TH1D* cutFlowWeight_mu;
	TH1D* cutFlow_ele;
	TH1D* cutFlowWeight_ele;


private:
	EventTree* tree;
	
	//	void clear_vectors();
	void set_cutflow_labels_mu(TH1D* hist);
	void set_cutflow_labels_ele(TH1D* hist);
};

#endif
