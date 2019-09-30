import threading
import re
from collections import Counter
import glob
import pickle
import os



def main():
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

    #create threads
    t1 = threading.Thread(target=tCount, args=(arr1,))
    t2 = threading.Thread(target=tCount, args=(arr2,))
    t3 = threading.Thread(target=tCount, args=(arr3,))
    t4 = threading.Thread(target=tCount, args=(arr4,))
    t5 = threading.Thread(target=tCount, args=(arr5,))
    t6 = threading.Thread(target=tCount, args=(arr6,))

    threads = [t1, t2, t3, t4, t5, t6]

    for thread in threads:
        thread.start()
        print('starting thread: ' + thread.name)

    for thread in threads:
        thread.join()
        print('killing thread: ' + thread.name)

    #preserve object state because god damn this is slow
    print("pickling the thing")
    aplist = open('../data/aplist', 'wb')
    pickle.dump(cnt, aplist)
    aplist.close()

def tCount(filenameList):
    pattern = r'\|AP\s(EXT-.*?|.*?)-'
    code = '501100'
    global cnt, lock

    #Thanks Dak
    jeffrey = Counter()

    for filename in filenameList:
        with open(filename, 'r') as file:
            print('Processing: ' + filename)
            # lines = [next(file) for x in range(1000)]
            lines = file.readlines()
            for line in lines:
                if (code in line):
                    res = re.search(pattern, line)
                    if(res):
                        jeffrey = jeffrey + Counter([res.group(1)])

    #JEFFREY SUBMITS HIMSELF TO THE GLOBAL GOD
    with lock:
        cnt = cnt + jeffrey

if __name__ == '__main__':
    cnt = Counter()
    lock = threading.Lock()
    main()
