#mac= input ("Input your partial mac address" )
f = open('macvendors.c', 'r')
line = f.readline()
for line in f:
        if line.startswith("0"):
            mac = line.split()[0]
            print(mac)
