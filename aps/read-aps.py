import pickle

def main():

    file = open('../data/aplist', 'rb')
    data = pickle.load(file)
    file.close()

    print(data.most_common(20))

if __name__ == '__main__':
    main()
