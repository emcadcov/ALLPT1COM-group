#Big list of mac addresses here
#

print ("Content-Type: text/html\n")

import urllib.request as urllib2
import json
import codecs

url = "http://macvendors.co/api/"
mac_address =str( input ("Enter a partial mac address here:   "))

request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
response = urllib2.urlopen( request )
reader = codecs.getreader("utf-8")
obj = json.load(reader(response))

print (obj['result']['company']);

print (obj['result']['address']);
