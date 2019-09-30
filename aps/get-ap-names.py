import re
from collections import Counter
import glob
import pickle
import os

def main():
    pattern = r'\|AP\s(EXT-.*?|.*?)-'
    code = '501100'
    cnt = Counter()
    # for filename in glob.glob('../shards/*.txt'):
    #     print('Processing: ' + filename)
    with open('../data/wifi-1000.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if (code in line):
                res = re.search(pattern, line)
                if(res):
                    cnt = cnt + Counter([res.group(1)])

    #preserve object state because god damn this is slow
    aplist = open('../data/aplist', 'wb')
    pickle.dump(cnt, aplist)
    aplist.close()


if __name__ == '__main__':
    main()
