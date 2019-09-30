import re

def main():
    pattern = r'<(501105)>'
    sampleFile = open('501105.txt', 'a')

    with open('../data/wifi-1000.txt', 'r') as file:
        for line in file:
            a = re.search(pattern, line)
            if (a):
                sampleFile.write(line)


if __name__ == '__main__':
    main()
