import AccessPoint as AP
import operator
import json
from datetime import datetime, timedelta
import glob
from blacklist import BLACKLIST

# LINE STRUCTURE
# DATE | TIME | CODE | MAC | AP
# Sep 16|00:00:00|501080|30:57:14:7c:17:dc|EXT-Band101

def main():
    apdict = {}
    filearray = []

    #Time resolution
    minute_limit = 15

    #get hour shards
    for filename in glob.glob('../data/hours/*.txt'):
        filearray.append(filename)

    for k in range(len(filearray)):
        with open(filearray[k], 'r') as file:
            lines = file.readlines()

        #initialise the beast
        start_time = getDateTime(lines[0])
        end_time = start_time + timedelta(minutes = minute_limit)

        for line in lines:
            curr_time=getDateTime(line)
            line = line.split('|')
            code = str(line[2].strip('\n'))
            mac = line[3].strip('\n')
            ap = line[4].strip('\n')

            if(curr_time < end_time):
                if ap in apdict:
                    apdict[ap].process(code, mac)
                else:
                    apdict[ap] = AP.AccessPoint(ap)
                    apdict[ap].process(code, mac)
            else:
                #if times are equal, move to new timeframe
                dumpJsonData(apdict, end_time)
                start_time = end_time
                end_time = start_time + timedelta(minutes = minute_limit)
                #reset everything
                apdict = {}
                if ap in apdict:
                    apdict[ap].process(code, mac)
                else:
                    apdict[ap] = AP.AccessPoint(ap)
                    apdict[ap].process(code, mac)
        #dump the last
        dumpJsonData(apdict, end_time)

def getDateTime(line):
    MONTH_ARRAY = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Sep', 'Aug', 'Oct', 'Nov', 'Dec']
    firstLine = line.split('|')

    year = 2019
    month = firstLine[0].split(' ')[0]
    month = MONTH_ARRAY.index(month) + 1
    day = int(firstLine[0].split(' ')[1])
    hour = int(firstLine[1].split(':')[0])
    min = int(firstLine[1].split(':')[1])

    return datetime(year, month, day, hour, min)

def dumpJsonData(apdict, end_time):
    ### REFACTOR TO INCLUDE ALL ZERO ACTIVITY POINTS ###
    inactive = []
    #Get APs with no activity / Buildings that don't matter
    for ap, count in apdict.items():
        if (len(apdict[ap]) == 0):
            inactive.append(ap)
        elif (apdict[ap].building in BLACKLIST):
            inactive.append(ap)

    #Clean up
    for el in inactive:
        apdict.pop(el)

    #sort
    sortedap = sorted(apdict.items(), key=operator.itemgetter(1), reverse=True)

    #export to json
    dataArray = []
    filename = end_time.strftime('%Y-%m-%d--%H-%M-%S')
    jsondate = end_time.strftime('%Y-%m-%d %H:%M:%S')

    print('DUMPING DATA FOR ' + str(jsondate))

    with open('../data/data/{}.json'.format(filename), 'w') as targetJson:
        for k in range(len(sortedap)):
            dataArray.append({'name': sortedap[k][0], 'count': len(sortedap[k][1]), 'building': sortedap[k][1].building})
        datadict = {'datetime': jsondate, 'aps': dataArray}
        json.dump(datadict, targetJson)

if __name__ == '__main__':
    main()
