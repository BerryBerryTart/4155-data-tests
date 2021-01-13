import multiprocessing
import re
from collections import Counter
import glob
import pickle
import os

def main():
    cnt = Counter()

    #get some things
    filenames = []
    for filename in glob.glob('../data/shards/*.txt'):
        filenames.append(filename)

    threadCount = 6

    #slice some things
    arr1 = filenames[::threadCount]
    arr2 = filenames[1::threadCount]
    arr3 = filenames[2::threadCount]
    arr4 = filenames[3::threadCount]
    arr5 = filenames[4::threadCount]
    arr6 = filenames[5::threadCount]

    #Can I speak to the manager???????????????
    with multiprocessing.Manager() as manager:

        return_dict = manager.dict()

        #create threads
        t1 = multiprocessing.Process(target=tCount, args=(arr1, 0, return_dict))
        t2 = multiprocessing.Process(target=tCount, args=(arr2, 1, return_dict))
        t3 = multiprocessing.Process(target=tCount, args=(arr3, 2, return_dict))
        t4 = multiprocessing.Process(target=tCount, args=(arr4, 3, return_dict))
        t5 = multiprocessing.Process(target=tCount, args=(arr5, 4, return_dict))
        t6 = multiprocessing.Process(target=tCount, args=(arr6, 5, return_dict))

        threads = [t1, t2, t3, t4, t5, t6]

        for thread in threads:
            thread.start()
            print('starting process: ' + thread.name)

        for thread in threads:
            thread.join()
            print('killing process: ' + thread.name)

        #enumerate the master counter
        for item in return_dict.values():
            cnt = cnt + item

    #preserve object state because this is so slow
    print("pickling the thing")
    aplist = open('../data/aplist', 'wb')
    pickle.dump(cnt, aplist)
    aplist.close()

def tCount(filenameList, procnum, return_dict):
    pattern = r'\|AP\s(EXT-.*?|.*?)-'
    code = '501100'
    # global cnt, lock

    apCounter = Counter()

    for filename in filenameList:
        with open(filename, 'r') as file:
            print('Processing: ' + filename)
            # lines = [next(file) for x in range(1000)]
            lines = file.readlines()
            for line in lines:
                if (code in line):
                    res = re.search(pattern, line)
                    if(res):
                        apCounter = apCounter + Counter([res.group(1)])

    #Put the shared object into the shared dictionary
    return_dict[procnum] = apCounter

if __name__ == '__main__':
    main()
