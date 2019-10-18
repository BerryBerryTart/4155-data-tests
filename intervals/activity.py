import AccessPoint as AP
import operator

def main():
    apdict = {}
    with open('../data/hours/00-hour.txt', 'r') as file:
        lines = file.readlines()

    # LINE STRUCTURE
    # DATE | TIME | CODE | MAC | AP

    for line in lines:
        line = line.split('|')
        time = line[1]
        code = str(line[2].strip('\n'))
        mac = line[3].strip('\n')
        ap = line[4].strip('\n')

        if ap in apdict:
            apdict[ap].process(code, mac)
        else:
            apdict[ap] = AP.AccessPoint(ap)
            apdict[ap].process(code, mac)

    inactive = []
    #Get APs with no activity
    for ap, count in apdict.items():
        if (len(apdict[ap]) == 0):
            inactive.append(ap)

    #Clean up
    for el in inactive:
        apdict.pop(el)

    #sort
    # sortedap = sorted(apdict.items(), key=operator.itemgetter(1), reverse=True)
    # print(sortedap)
    sortedap = sorted(apdict.items())
    for k in range(10):
        print(sortedap[k])


if __name__ == '__main__':
    main()
