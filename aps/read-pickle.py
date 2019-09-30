import pickle

def main():

    file = open('../data/aplist', 'rb')
    data = pickle.load(file)
    file.close()

    print(len(data))

if __name__ == '__main__':
    main()
