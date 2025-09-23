import requests
import re

r = requests.get('https://www.numbeo.com/quality-of-life/rankings_by_country.jsp')
r = r.text

a = r.split('<tr')[2]

b = a.split('<th><div style="font-size: 90%;">')

c = []

for i in b:
    # c.append(re.sub(r'<.+>', '', i))
    i = (re.sub(r'<.+>', '', i))
    i = i.replace("\n", "")
    i = i.replace("\t", "")
    i = i.replace(">", "")
    if i:
        c.append(i)

print(c)