#!/bin/bash
mkdir -p log
condor_submit  jdl/submitBase.jdl
#sys
#condor_submit  jdl/submitSyst_PU.jdl
#condor_submit  jdl/submitSyst_MuEff.jdl
#condor_submit  jdl/submitSyst_PhoEff.jdl
#condor_submit  jdl/submitSyst_BTagSF_b.jdl
#condor_submit  jdl/submitSyst_BTagSF_l.jdl
#condor_submit  jdl/submitSyst_EleEff.jdl
#condor_submit  jdl/submitSyst_Q2.jdl
#condor_submit  jdl/submitSyst_Pdf.jdl
#condor_submit  jdl/submitSyst_isr.jdl
#condor_submit  jdl/submitSyst_fsr.jdl
