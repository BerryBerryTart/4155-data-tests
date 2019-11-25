import re
import pprint
import json
import glob

def main():
    aplist = {}
    filearray = []

    for filename in glob.glob('../data/hours/*.txt'):
        filearray.append(filename)

    for k in range(len(filearray)):
        with open(filearray[k]) as source:
            print('Processing: ' + filearray[k].split('\\')[-1])
            for line in source:
                fullap = line.split('|')[4].strip('\n')
                result = filterPoint(fullap)
                if result not in aplist:
                    aplist[result] = []
                    aplist[result].append(fullap)
                else:
                    if fullap not in aplist[result]:
                        aplist[result].append(fullap)

    # pp = pprint.PrettyPrinter(indent=2, width=90, compact=True)
    with open('../data/json/buildings.json', 'w') as targetJson:
        json.dump(aplist, targetJson, sort_keys=True, indent=4)

def filterPoint(ap):
    #captures points with room numbers
    pattern = r'([a-zA-Z]+)\d'
    #captures the rest
    pattern2 = r'([a-zA-Z]+)-'

    result = ap.replace('EXT-', '')
    apSearch = re.search(pattern, result)
    if (apSearch):
        result = apSearch.group(1)
    apSearch2 = re.search(pattern2, result)
    if (apSearch2):
        result = apSearch2.group(1)

    return result

if __name__ == '__main__':
    main()