import glob, os
import datetime
import json
from statistics import mean
from math import floor
import multiprocessing

def main():
    #get some things
    filenames = []
    for filename in glob.glob('../data/raw_averages/*.json'):
        filenames.append(filename)

    core_Count = 6
    process_arr = []
    for k in range(0, core_Count):
        process_arr.append(multiprocessing.Process(target=processAverages, args=(filenames[k::core_Count],) ))

    for process in process_arr:
        process.start()
        print('Starting Process: ' + process.name)

    for process in process_arr:
        process.join()
        print('Ending Process: ' + process.name)

def processAverages(filenames):
    for filename in filenames:
        with open(filename, 'r') as file:
            json_decoded = json.load(file)

        ap_name = os.path.basename(filename).split('.')[0]

        mindelta = datetime.timedelta(minutes = 15)
        hourdelta = datetime.timedelta(hours = 1)
        start_time = datetime.datetime(2019, 1, 1, 0, 0, 0)
        end_time = start_time + hourdelta

        buffer = []
        result = {'name': ap_name, 'averages' : []}

        #It's 24 * 4 = 96 to accomodate for the 15 minute intervals
        for k in range(0, 97):
            stringTime = getStringTime(start_time)
            count = next((item for item in json_decoded if item['time'] == stringTime), None)
            if start_time >= end_time:
                if len(buffer) == 0:
                    result['averages'].append({'hour' : (start_time - hourdelta).strftime('%H'),
                        'count': 0})
                else:
                    result['averages'].append({'hour' : (start_time - hourdelta).strftime('%H'),
                        'count': floor(mean(buffer))})
                    # result[(start_time - hourdelta).strftime('%H')] = floor(mean(buffer))
                buffer = []
                end_time = end_time + hourdelta
            if count:
                buffer.append(count['count'])
            start_time = start_time + mindelta
        with open('../data/averages/' + ap_name + '.json', 'w') as file:
            json.dump(result, file)

def getStringTime(time):
    return time.strftime('%H-%M-%S')

if __name__ == '__main__':
    main()