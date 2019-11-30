import glob, os
import json

def main():
    filearray = []
    avg_dict = {}
    #get hour shards
    for filename in glob.glob('../data/data/*.json'):
        filearray.append(filename)

    # fields name, count, building

    for k in range(len(filearray)):
        timestamp = os.path.basename(filearray[k]).split('.')[0].split('--')[1]
        with open(filearray[k], 'r') as file:
            json_decoded = json.load(file)
            for el in json_decoded['aps']:
                if el['name'] in avg_dict:
                    avg_dict[el['name']].append({'time': timestamp, 'count': el['count']})
                else:
                    avg_dict[el['name']] = []
                    avg_dict[el['name']].append({'time': timestamp, 'count': el['count']})

    for k, v in avg_dict.items():
        with open('../data/raw_averages/' + k + '.json', 'w') as file:
            json.dump(v, file)

if __name__ == '__main__':
    main()