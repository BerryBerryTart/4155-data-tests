import pickle

def main():

    file = open('../data/aplist', 'rb')
    data = pickle.load(file)
    file.close()

    target = open('../data/frequency.txt', 'a')

    req = sorted(data.items(), key=lambda item : item[1], reverse=True)
    for el in req:
        target.write('{}: {}\n'.format(el[0], el[1]))

    target.close()

if __name__ == '__main__':
    main()
