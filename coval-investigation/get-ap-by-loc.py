import re
import glob
import os

def main():
    # use AP 'Colv5021'
    ap_pattern = r'(Colv5021)'

    #only capture assoc successful requests
    code_pattern = r'<(501100)>\s<NOTI>'

    #create target file to write to
    locationfile = open('../data/colvard-activity.txt', 'a')

    filearray = []

    for filename in glob.glob('../data/shards/*.txt'):
        filearray.append(filename)

    filearray.reverse()

    #use this as a file buffer because computers are dumb
    resultbuff = []

    for k in range(len(filearray)):
        currfile = open(filearray[k], 'r')

        print('Processing: ' + filearray[k])

        #find lines
        for line in currfile:
            #first search for target AP
            a = re.search(ap_pattern, line)
            if(a):
                #then search for if the proper code is there
                b = re.search(code_pattern, line)
                if (b):
                    #then add to buffer and pray to god
                    resultbuff.append(line)

        #reverse lines
        resultbuff.reverse()

        #add lines from buffer to file
        for el in resultbuff:
            locationfile.write(el)

        #reset buffer
        resultbuff = []

        #REMEBER TO CLOSE IT
        currfile.close()

    #close them bois
    currfile.close()
    locationfile.close()

if __name__ == '__main__':
    main()
