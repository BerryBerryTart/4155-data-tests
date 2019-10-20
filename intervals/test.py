import formatLine

def main():
    with open('../data/wifilog.txt', 'r') as file:
        head = [next(file) for x in range(100)]

    for line in head:
        line = formatLine.formatLine(line)
        if (line != None):
            print(line)


if __name__ == '__main__':
    main()
