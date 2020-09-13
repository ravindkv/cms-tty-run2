#include "TFile.h"
#include "TKey.h"
#include "TMacro.h"
//root -b -q "ScanRootFile.C(\"fileName.root\")"

void readDir(TDirectory *dir) {
    TDirectory *dirsav = gDirectory;
    cout<<"\n"<<endl;
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
                printf("%20s %15.2f %15.2f %10.4f\n", 
                        key->GetName(), h->Integral(), h->GetEntries(),
                        float(h->Integral()/h->GetEntries()));
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

void scanRootFile(TString fileName){
    TFile *f = new TFile(fileName);
    if (f->IsZombie()) {
        printf("The input root file is corrupted");
      return;
   }
   readFile(f);
}
