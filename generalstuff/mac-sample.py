import re

def main():
    mac = r'([a-fA-F0-9:]{17}|[a-fA-F0-9]{12}):'

    sampleFile = open('../data/sample-singleton-connection.txt', 'a')

    with open('../data/wifi-1000.txt', 'r') as file:
        for line in file:
            a = re.search(mac, str(line))
            if (a and a.group(1) == '90:cd:b6:2b:6e:48'):
                sampleFile.write(line)

    sampleFile.close()

if __name__ == '__main__':
    main()
