def main():
    filenum = 1
    count = 0
    isFileOpen = True

    with open('../data/wifilog.txt', 'r') as logs:
        #define file path
        path = '../data/shards/wifi-shard-{}.txt'.format(filenum)

        #open (or create) file path in append mode
        file = open(path, 'a')

        for line in logs:
            #check if limit is reached and then close file
            if (count >= 250000):
                isFileOpen = False
                file.close()

            #handle creation of new file and reset flags / counters
            if (isFileOpen == False):
                filenum = filenum + 1
                path = '../data/shards/wifi-shard-{}.txt'.format(filenum)
                file = open(path, 'a')
                count = 0
                isFileOpen = True

            #else write to file
            file.write(line)

            #increase counter too
            count = count + 1

    #close file anyway JUST to be safe
    file.close()

if __name__ == '__main__':
    main()
