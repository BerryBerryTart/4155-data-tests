import requests, json
import glob

def main():
    headers = {'Content-type': 'application/json'}
    url = 'http://127.0.0.1:8000/average/'
    filearray = []
    faulty = []

    for filename in glob.glob('../data/averages/*.json'):
        filearray.append(filename)

    for k in range(len(filearray)):
        with open(filearray[k], 'r') as targetJson:
            print(filearray[k])
            try:
                r = requests.post(url=url , data=targetJson, headers=headers, timeout=3)
            except:
                faulty.append(filearray[k])
            print(r)
    print(faulty)

if __name__ == '__main__':
    main()

