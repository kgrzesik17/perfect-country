import requests
import re

weights = [0, 1, 0, 0, 0, 0, 0, 0, 0]

r = requests.get('https://www.numbeo.com/quality-of-life/rankings_by_country.jsp')
r = r.text

countries = []

for i in range(3):
    a = r.split('<tr')[i + 3]
    b = a.split('<td style="text-align: right">')
    values = []
    country_name = ''

    for i in b:
        i = (re.sub(r'<.+>', '', i))
        i = re.sub("[^0-9\.]", "", i)
        values.append(i)

    country = a.split('<td class="cityOrCountryInIndicesTable">')

    for i in country:
        country_name = (re.sub(r'<.+>', '', i))

    country_name = country_name.split()

    values[0] = country_name[0]

    countries.append(values)

for i in countries:
    pair = [i[0], '']
    sum = 0
    iterator = 0

    for j in i[1::]:
        sum += float(j) * weights[iterator]
        pair[1] = sum
        iterator += 1   

    print(pair)