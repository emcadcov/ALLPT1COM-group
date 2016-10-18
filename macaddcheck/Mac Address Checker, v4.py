#mac=input ("Input your partial mac address")
f = open('macvendors.c', 'r')
line = f.readline()
for line in f:
    if not line.startswith("#"):
        print   ( line )

