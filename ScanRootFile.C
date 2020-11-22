#include "TFile.h"
#include "TKey.h"
#include "TMacro.h"
//root -b -q "ScanRootFile.C(\"fileName.root\")"

void readDir(TDirectory *dir) {
    TDirectory *dirsav = gDirectory;
    gDirectory->pwd();
    TIter next(dir->GetListOfKeys());
    TKey *key;
    while ((key = (TKey*)next())){
        if (key->IsFolder()){
            dir->cd(key->GetName());
            //dir->ls();
            //dir->GetListOfKeys()->Print();
            TDirectory *subdir = gDirectory;
            readDir(subdir);
            dirsav->cd();
            continue;
        }
        else{
            if(TString(key->GetClassName())=="TH1F"){
                TH1F *h; gDirectory->GetObject(key->GetName(),h);
                printf("%15s %10.2d %10.2f %10.2f %10.4f\n", 
                        h->GetName(), h->GetNbinsX(), 
                        h->Integral(), h->GetEntries(),
                        float(h->Integral()/h->GetEntries()));
                for(int i = 1; i<h->GetNbinsX()+1; i++){
                    //printf("\t %5d %10.0f %10.0f\n", i, h->GetBinCenter(i), h->GetBinContent(i));
                }
            }
        }
    }
}

void readFile(TFile * file){
    TDirectory *dirsav = gDirectory;
    TIter next(file->GetListOfKeys());
    TKey *key;
    while ((key = (TKey*)next())){
        if (key->IsFolder()) {
            file->cd(key->GetName());
            TDirectory *subdir = gDirectory;
            readDir(subdir);
            dirsav->cd();
            continue;
        }
    }
}

void ScanRootFile(TString fileName){
    //TFile *f = new TFile(fileName);
    TFile *f = TFile::Open("root://cmsxrootd.fnal.gov/"+fileName);
    if (f->IsZombie()) {
        printf("The input root file is corrupted");
      return;
   }
   readFile(f);
}
