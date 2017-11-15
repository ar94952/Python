import urllib
import requests

link = "http://www.nasonline.org"

f = urllib.request.urlopen(link)
myfile = f.read()

topics = ["sports", "research", "climate", "evolution", "cultural", "leadership"]
out = []



for topic in topics:
    out.append(myfile.count(topic))

print("Todays date is " + time.strftime("%d/%m/%Y"))
i = 0
for topic in topics:
    if out[i] > 0:
        print(topic + " appears " + str(out[i]) + " times.")
    i += 1