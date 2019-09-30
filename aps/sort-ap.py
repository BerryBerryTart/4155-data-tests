def main():
    target = open('../data/sorted-aps.txt', 'a')

    with open('../data/ap-list.txt', 'r') as file:
        head = file.readlines()

    head = sorted(head, key=lambda name : handleName(name))
    for el in head:
        target.write(el)

    target.close()

def handleName(name):
    res = name.split('-')
    if (res[0] == 'EXT'):
        return res[1]
    else:
        return name

if __name__ == '__main__':
    main()
