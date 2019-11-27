import requests, json
import glob

def main():
    headers = {'Content-type': 'application/json'}
    url = 'http://127.0.0.1:8000/timeslices/'
    filearray = []

    for filename in glob.glob('../data/data/*.json'):
        filearray.append(filename)

    for k in range(len(filearray)):
        with open(filearray[k], 'r') as targetJson:
            r = requests.post(url=url , data=targetJson, headers=headers)
            print(r)

if __name__ == '__main__':
    main()

