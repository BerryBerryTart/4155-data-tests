import glob

def main():
    with open('../data/hours/reversed-data.txt', 'r') as file:
        head = [next(file) for x in range(10)]

    for el in head:
        print(el)


if __name__ == '__main__':
    main()
