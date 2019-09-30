import re
from collections import Counter
import glob
import pickle

def main():
    cnt = Counter()
    for filename in glob.glob('../data/shards/*.txt'):
        print('Processing: ' + filename)
        codes = re.findall(r'<(\d{6})>', open(filename).read())
        cnt = cnt + Counter(codes)

    #preserve object state because god damn this is slow
    outfile = open('code-count', 'wb')
    pickle.dump(cnt, outfile)
    outfile.close()


if __name__ == '__main__':
    main()
