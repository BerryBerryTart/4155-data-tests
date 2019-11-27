import requests, json
import glob

def main():
    headers = {'Content-type': 'application/json'}
    url = 'http://127.0.0.1:8000/timeslices/'

    path = '../data/data/'

    with open(path + '2019-08-16--14-45-00.json', 'r') as targetJson:
        r = requests.post(url=url , data=targetJson, headers=headers)
        print(r)

if __name__ == '__main__':
    main()

