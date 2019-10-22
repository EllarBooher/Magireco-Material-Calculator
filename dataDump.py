import json
import csv
from collections import defaultdict

def build_dict(source_file):
    projects = defaultdict(dict)
    headers = ["Name","Level","100","551", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "401", "402", "403", "404", "405", "406", "407", "408", "501", "502", "503", "504", "505", "506", "552", "553", "554", "555", "556", "507", "557", "508", "509", "602", "603", "604", "605", "601", "606", "607", "608", "609", "610", "111", "112", "113", "211", "212", "213", "121", "122", "123", "221", "222", "223", "131", "132", "133", "231", "232", "233", "141", "142", "143", "241", "242", "243", "151", "152", "153", "251", "252", "253"]
    with open(source_file, 'r') as fp:
        reader = csv.DictReader(fp, fieldnames=headers, dialect='excel',skipinitialspace=True)
        i = 0
        for rowdict in reader:
            if None in rowdict:
	                del rowdict[None]
            name = rowdict.pop("Name")
            level = rowdict.pop("Level")
            rowdict = {k:int(v) for k,v in rowdict.items() if v != ""}
            projects[i] = {"Name":name}
            projects[i][level] = rowdict
            i+=1
    return dict(projects)

source_file = 'Data.csv'
oldDict = build_dict(source_file)
newDict = defaultdict(dict)

for j in range(0,910,9):
    for k in range(j+1,j+9,1):
        oldDict[k].pop("Name")  
    name = oldDict[j].pop("Name")
    newEntry = {"Name":name,"ID":'',"awakenLevel":{},"magiaLevel":{}}
    for i in range(0,5,1):
        newEntry["awakenLevel"].update(oldDict[j+i])
    for i in range(0,4,1):
        newEntry["magiaLevel"].update(oldDict[j+5+i])
    newDict[j/9] = newEntry
    
jsonfile = open('Data.json', 'w')
jsonfile.write('[\n')
for yaBaby in newDict:
    json.dump(newDict[yaBaby], jsonfile)
    jsonfile.write(',\n')
jsonfile.write(']')