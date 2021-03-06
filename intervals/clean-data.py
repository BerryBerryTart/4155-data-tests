import formatLine

def main():
    target = open('../data/clean/reversed-data.txt', 'a')

    count = 1
    writeCount = 0
    iterations = 100000

    with open('../data/wifilog.txt', 'r') as file:
        for line in file:
            line = formatLine.formatLine(line)
            if (line != None):
                target.write('{}\n'.format(line))
                writeCount = writeCount + 1
            #progress
            if ((count % iterations) == 0):
                print("Processed: " + str(count) + " lines")
            count = count + 1

    target.close()
    print("Wrote: " + str(writeCount) + " lines")

if __name__ == '__main__':
    main()
