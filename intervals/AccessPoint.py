from functools import total_ordering

@total_ordering
class AccessPoint():
    def __init__(self, name):
        self.name = name
        self.connected = []

    def __len__(self):
        return len(self.connected)

    def __str__(self):
        return "Connected: " + str(len(self.connected))

    def __repr__(self):
        return "Connected: " + str(len(self.connected))

    def __gt__(self, ap2):
        return len(self) > len(ap2)

    def __lt__(self, ap2):
        return len(self) < len(ap2)

    def __eq__(self, ap2):
        return len(self) == len(ap2)

    def process(self, code, mac):
        if(code == '501105' or code == '501106' or code == '501080'):
            if mac in self.connected:
                self.connected.remove(mac)
        elif(code == '501100'):
            if mac not in self.connected:
                self.connected.append(mac)
