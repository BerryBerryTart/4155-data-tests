import pickle

def main():
    file = open('aplist', 'rb')
    data = pickle.load(file)
    file.close()

    with open('ap-list.txt', 'a') as file:
        for k, v in data.items():
            file.write('{}: {}\n'.format(k,v))

if __name__ == '__main__':
    main()