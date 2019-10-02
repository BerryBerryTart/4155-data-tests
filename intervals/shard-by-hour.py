
def main():
    with open('../data/hours/reversed-data.txt', 'r') as file:
        lines = reversed(file.readlines())

    currentHour = 0
    file = open('../data/hours/{:02d}-hour.txt'.format(currentHour), 'a')
    print('Processing Hour: ' + str(currentHour))
    #here's where the magic happens
    #also please don't crash please I beg you
    for line in lines:
        hour = line.split('|')[0].split(' ')[2].split(':')[0]
        if(currentHour == int(hour)):
            file.write(line)
        else:
            file.close()
            currentHour = currentHour + 1
            file = open('../data/hours/{:02d}-hour.txt'.format(currentHour), 'a')
            print('Processing Hour: ' + str(currentHour))
            file.write(line)

    #ensure it's really closed
    file.close()

if __name__ == '__main__':
    main()
