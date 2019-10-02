
def main():
    a = 'Sep 16 00:59:59 | 501100 | 14:c2:13:cc:3b:74 | StuU140'
    hour = a.split('|')[0].split(' ')[2].split(':')[0]
    print(int(hour))


if __name__ == '__main__':
    main()
