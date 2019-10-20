import re

def main():
    target = open('../data/faulty-aps.txt', 'a')

    count = 0
    iterations = 1000000

    with open('../data/wifilog.txt', 'r') as file:
        for line in file:
            line = fetchLine(line)
            if (line != None):
                target.write('{}'.format(line))
            #progress
            if ((count % iterations) == 0):
                print("Processed: " + str(count) + " lines")
            count = count + 1

    target.close()


def fetchLine(line):
    ap = r'-(\w*)-\w*-\w*$'
    faulty_code = r'(AP\d{3})'
    if (line.find('501100') != -1):
        str_ap = re.search(ap, line)
        if(str_ap):
            faulty_ap = re.search(faulty_code, str_ap.group(1))
            if (faulty_ap):
                return line
    return None

if __name__ == '__main__':
    main()
