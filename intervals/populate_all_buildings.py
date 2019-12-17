from blacklist import BLACKLIST
import json
import pickle

def main():
    masterArray = []
    with open('../data/json/buildings.json', 'r') as file:
        data = json.load(file)

    for el in data:
        if el not in BLACKLIST:
            masterArray = masterArray + data[el]

    with open('masterArray', 'wb') as outFile:
        pickle.dump(masterArray, outFile)


if __name__ == '__main__':
    main()