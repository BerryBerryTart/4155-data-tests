import re

def formatLine(line):
    date = r'([a-zA-z]{3}\s\d{2})'
    timestamp = r'(\d{2}\:\d{2}\:\d{2})'
    mac = r'(([a-f0-9]{2}:){5}[a-f0-9]{2})'
    deauthMAC = r'sta:\s(([a-f0-9]{2}:){5}[a-f0-9]{2})'
    ap = r'AP\s(?:\d{1,3}\.){3}\d{1,3}-(?:(?:[a-f0-9]{2}:){5}[a-f0-9]{2})-([^\s]+)'
    d_code = r'<(501105|501106|501080)>'
    a = []
    #here devices connect
    if (line.find('501100') != -1):
        #date
        str_date = re.search(date, line)
        if(str_date):
            a.append(str_date.group(1))
        #time
        str_time = re.search(timestamp, line)
        if(str_time):
            a.append(str_time.group(1))
        #code
        a.append('501100')
        #MAC
        str_mac = re.search(mac, line)
        if (str_mac):
            a.append(str_mac.group(1))
        #AP
        str_ap = re.search(ap, line)
        if (str_ap):
            a.append(formatAP(str_ap.group(1)))

    #deauth formating
    deauth_code = re.search(d_code, line)
    if(deauth_code):
        #date
        str_date = re.search(date, line)
        if(str_date):
            a.append(str_date.group(1))
        #time
        str_time = re.search(timestamp, line)
        if(str_time):
            a.append(str_time.group(1))
        #code
        a.append(deauth_code.group(1))
        #mac
        str_mac = re.search(deauthMAC, line)
        if (str_mac):
            a.append(str_mac.group(1))
        #ap
        str_ap = re.search(ap, line)
        if (str_ap):
            a.append(formatAP(str_ap.group(1)))

    #FORMAT CHECKER
    if(len(a) == 5):
        return '|'.join(a)
    else:
        return None

#cleans up the access point and removes any unecessary stuff
def formatAP(point):
    eol_check = r'(\d+)$'
    mid_check = r'(AP\d+)'
    point_mid_check = re.search(mid_check, point)
    if(point_mid_check):
        point = point.replace(point_mid_check.group(1) + '-', '')
    point_end_check = re.search(eol_check, point)
    if(point_end_check):
        point = point.replace('-' + point_end_check.group(1), '')
    return point
