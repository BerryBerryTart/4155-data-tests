import formatLine

def main():
    target = open('../data/hours/reversed-data.txt', 'a')

    count = 0

    with open('../data/wifilog.txt', 'r') as file:
        for line in file:
            line = formatLine.formatLine(line)
            if (line != None):
                target.write('{}\n'.format(line))
                count = count + 1

    target.close()
    print("Wrote: " + str(count) + " lines")

if __name__ == '__main__':
    main()
