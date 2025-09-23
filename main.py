import requests
import re

r = requests.get('https://www.numbeo.com/quality-of-life/rankings_by_country.jsp')
r = r.text

a = r.split('<tr')[3]
b = a.split('<td style="text-align: right">')
c = []

for i in b:
    print(i)
    # c.append(re.sub(r'<.+>', '', i))
    i = (re.sub(r'<.+>', '', i))
    i = re.sub("[^0-9\.]", "", i)
    c.append(i)

del c[0]

print(c)