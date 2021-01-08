GIT_COMMIT_FULL := "$(shell git log -1 --oneline)"
GIT_COMMIT := "$(shell git rev-parse HEAD)"
GIT_COMMIT_TIME := "$(shell git show -s --format=%ci $(GIT_COMMIT))"
GIT_BRANCH := "$(shell git rev-parse --abbrev-ref HEAD)"
GIT_STATUS := "$(shell git status -uno -s)"

all: src/EventTree_Skim.o src/EventPick_Skim.o makeSkim 

makeSkim:  src/EventPick_Skim.o src/EventTree_Skim.o  makeSkim.C
	g++ -o makeSkim `root-config --libs` -I `root-config --incdir` -std=c++17 src/EventTree_Skim.o src/EventPick_Skim.o makeSkim.C -DVERSION=\"$(GIT_COMMIT_FULL)\" -DBRANCH=\"$(GIT_BRANCH)\" -DSTATUS=\"$(GIT_STATUS)\" -DCOMMITTIME=\"$(GIT_COMMIT_TIME)\"

src/EventTree_Skim.o: src/EventTree_Skim.cpp interface/EventTree_Skim.h
	g++ -c -I `root-config --incdir` -std=c++17 src/EventTree_Skim.cpp -o src/EventTree_Skim.o

src/EventPick_Skim.o: src/EventPick_Skim.cpp interface/EventPick_Skim.h
	g++ -c -I `root-config --incdir` -std=c++17 src/EventPick_Skim.cpp -o src/EventPick_Skim.o 


clean:
	rm src/*.o 
