# NOTE
* There is an issue of segmentation violation while creating datacards
using CombineHarvester class in the lattest (2 April 2020) repository:
https://github.com/cms-analysis/CombineHarvester/tree/2782a7c0d69707083c4210a80843585c95b936c6

* Kindly use the older (15th June 2018) package :
https://github.com/cms-analysis/CombineHarvester/tree/cfa42837cb82605a57c6af121979a4289a685c4a/CombinePdfs
https://github.com/cms-analysis/CombineHarvester/tree/cfa42837cb82605a57c6af121979a4289a685c4a/CombineTools

* There are a few compilation erorrs with the older package when using CMSS_10_2_13 and lattet:
https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit

* To fix these, copy CombineTools/bin/* from NEW to Older package 
