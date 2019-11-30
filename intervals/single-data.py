import requests, json
import glob

def main():
    headers = {'Content-type': 'application/json'}
    url = 'http://127.0.0.1:8000/average/'

    path = '../data/averages/'

    with open(path + 'Atki1COR3.json', 'r') as targetJson:
        r = requests.post(url=url , data=targetJson, headers=headers)
        print(r)

if __name__ == '__main__':
    main()

