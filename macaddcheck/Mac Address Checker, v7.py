macuse = input()
f = open('macvendors.c', 'r')
line = f.readline()

if mac == line:
    print (line)
for line in f:
        if line.startswith("0"):
            mac = line.split()[0],
            mac2 = line.split()[1],
            print(mac, mac2)
