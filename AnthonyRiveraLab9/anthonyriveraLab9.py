import time
import requests
import urllib

print("Enter the URL, example(https://en.wikipedia.org/robots.txt)")
url = input()

# download url resource 
f = urllib.request.urlopen("http://www.nasonline.org")
myfile = f.read()

# Search for the keywords
# I have used the extra topic under review as sports
topics = ["sports", "research", "climate", "evolution", "cultural", "leadership"]
out = []

for topic in topics:
    out.append(text.count(topic))

print("Todays date is " + time.strftime("%d/%m/%Y"))
i = 0
for topic in topics:
    if out[i] > 0:
        print(topic + " appears " + str(out[i]) + " times.")
    i += 1
