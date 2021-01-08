import json
from numpy import mean



def removekey(d, key):
    r = dict(d)
    del r[key]
    return r


def mergeMCStats(fName):
#    print fName
    jsonfile = open(fName,'r')
    data = json.load(jsonfile)
    
    newdata = dict(data)["params"]

    prop_binM3_control_impactR = []
    prop_binM3_control_impact = []
    prop_binM3_control_pull = []
    
    prop_binno_btag_impactR = []
    prop_binno_btag_impact = []
    prop_binno_btag_pull = []

    prop_binM3_impactR = []
    prop_binM3_impact = []
    prop_binM3_pull = []
    
    prop_binChHad_impactR = []
    prop_binChHad_impact = []
    prop_binChHad_pull = []

    for i in range(len(newdata)-1,-1,-1):
        value = newdata[i]
        if 'prop_binno_photon'in value["name"]:
            prop_binM3_control_impactR.append(value["impact_r"])
            prop_binM3_control_impact.append(value["r"])
            prop_binM3_control_pull.append(value["fit"])
    
            if 'prop_binno_photon_bin0' in value["name"]:
                value["name"] = "prop_binno_photon"
            else:
                del newdata[i]
    
        if 'prop_binno_btag'in value["name"]:
            prop_binno_btag_impactR.append(value["impact_r"])
            prop_binno_btag_impact.append(value["r"])
            prop_binno_btag_pull.append(value["fit"])
    
            if 'prop_binno_btag_bin0' in value["name"]:
                value["name"] = "prop_binno_btag"
            else:
                del newdata[i]
    
        elif 'prop_binM3'in value["name"]:
            prop_binM3_impactR.append(value["impact_r"])
            prop_binM3_impact.append(value["r"])
            prop_binM3_pull.append(value["fit"])
            if 'prop_binM3_bin0' in value["name"]:
                value["name"] = "prop_binM3"
            else:
                del newdata[i]
        elif 'prop_binChHad'in value["name"]:
            prop_binChHad_impactR.append(value["impact_r"])
            prop_binChHad_impact.append(value["r"])
            prop_binChHad_pull.append(value["fit"])
    
            if 'prop_binChHad_bin0' in value["name"]:
                value["name"] = "prop_binChHad"
            else:
                del newdata[i]
    
    
    for i in range(len(newdata)-1,-1,-1):
        value = newdata[i]
        if 'prop_binno_photon'in value["name"]:
            average = mean([x[1] for x in prop_binM3_control_impact])
            value["r"][1] = average
            value["r"][0] = average - sum([(x[0]-x[1])**2 for x in prop_binM3_control_impact])**0.5
            value["r"][2] = average + sum([(x[2]-x[1])**2 for x in prop_binM3_control_impact])**0.5
    
            value["fit"][0] = mean([x[0] for x in prop_binM3_control_pull])
            value["fit"][1] = mean([x[1] for x in prop_binM3_control_pull])
            value["fit"][2] = mean([x[2] for x in prop_binM3_control_pull])
    
            value["impact_r"] = sum([x**2 for x in prop_binM3_control_impactR])**0.5
    
        elif 'prop_binM3' in value["name"]:
            average = mean([x[1] for x in prop_binM3_impact])
            value["r"][1] = average
            value["r"][0] = average - sum([(x[0]-x[1])**2 for x in prop_binM3_impact])**0.5
            value["r"][2] = average + sum([(x[2]-x[1])**2 for x in prop_binM3_impact])**0.5
    
            value["fit"][0] = mean([x[0] for x in prop_binM3_pull])
            value["fit"][1] = mean([x[1] for x in prop_binM3_pull])
            value["fit"][2] = mean([x[2] for x in prop_binM3_pull])
    
            value["impact_r"] = sum([x**2 for x in prop_binM3_impactR])**0.5
    
    
        elif 'prop_binChHad' in value["name"]:
            average = mean([x[1] for x in prop_binChHad_impact])
            value["r"][1] = average
            value["r"][0] = average - sum([(x[0]-x[1])**2 for x in prop_binChHad_impact])**0.5
            value["r"][2] = average + sum([(x[2]-x[1])**2 for x in prop_binChHad_impact])**0.5
    
    
            value["fit"][0] = mean([x[0] for x in prop_binChHad_pull])
            value["fit"][1] = mean([x[1] for x in prop_binChHad_pull])
            value["fit"][2] = mean([x[2] for x in prop_binChHad_pull])
    
            value["impact_r"] = sum([x**2 for x in prop_binChHad_impactR])**0.5
    
    #print newdata
    data["params"] = newdata
    
    outfile = open(fName.replace('.json','_mergeStat.json'),"w")
    json.dump(data, outfile)


def systTable(_fileName):
    mergeMCStats(_fileName)

    _fileNameMerged = _fileName.replace('.json','_mergeStat.json')

    try:
        _file = open(_fileNameMerged,'r')
    except:
        print "bad file"
        return

    values = json.load(_file)

    paramName = json.load(open('nuisImpact.json','r'))
    #paramName = json.load(open('../parameterNames.json','r'))



    for v in values['POIs']:
        if v['name']=='r':
            r = v['fit'][1]


    systematics = []
    for v in values['params']:
        unc = (v['r'][0]-v['r'][1],v['r'][2]-v['r'][1])
    
        systematics.append([v['name'],v['impact_r'],max(unc), min(unc)])


    systematics.sort(key=lambda x: x[1], reverse=True)

    outputString = ""

    outputString += "\\begin{tabular}{| l | c | c | } \n"
    outputString += "\\hline \n"
    outputString += "Nuisance Parameter & Total uncertainty on r & Relative Uncertainty (\\%) \\\\  \n"
    outputString += "\\hline  \n"

    for syst in systematics:
        print syst[0], syst[1], syst[2], syst[3]
        #outputString += "%s     & %+.4f / %+.4f  & %.2f \\\\  \n"%( paramName[syst[0]],syst[2], syst[3], syst[1]/r*100)
        outputString += "%15s     & %+10.4f / %+10.4f  & %10.2f \\\\  \n"%(syst[0], syst[2], syst[3], syst[1]/r*100)
    outputString += "\\hline  \n"
    outputString += "\\end{tabular}  \n"

    return outputString

if __name__=="__main__":
    import sys
    try:
        fName = sys.argv[1]
    except:
        print 'Unknown file'
        sys.exit()

    print systTable(fName)
