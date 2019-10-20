import AccessPoint as AP
import operator
import json

def main():
    apdict = {}
    with open('../data/hours/00-hour.txt', 'r') as file:
        lines = file.readlines()

    # LINE STRUCTURE
    # DATE | TIME | CODE | MAC | AP

    for line in lines:
        line = line.split('|')
        time = line[1]
        code = str(line[2].strip('\n'))
        mac = line[3].strip('\n')
        ap = line[4].strip('\n')

        minute_limit = 15
        if(int(time.split(':')[1]) <= minute_limit):
            if ap in apdict:
                apdict[ap].process(code, mac)
            else:
                apdict[ap] = AP.AccessPoint(ap)
                apdict[ap].process(code, mac)
        else:
            break

    inactive = []
    #Get APs with no activity
    for ap, count in apdict.items():
        if (len(apdict[ap]) == 0):
            inactive.append(ap)

    #Clean up
    for el in inactive:
        apdict.pop(el)

    #sort
    sortedap = sorted(apdict.items(), key=operator.itemgetter(1), reverse=True)
    # print(sortedap)
    # sortedap = sorted(apdict.items())
    # for k in range(10):
    #     print(sortedap[k])

    dataArray = []
    #export to json
    with open('../data/json/example.json', 'w') as targetJson:
        for k in range(len(sortedap)):
            dataArray.append({'AP_Name': sortedap[k][0], 'Count': len(sortedap[k][1])})

        json.dump(dataArray, targetJson)

if __name__ == '__main__':
    main()
