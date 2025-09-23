import requests
import re

# ['Quality of Life Index', 'Purchasing Power Index', 'Safety Index', 'Health Care Index', 'Cost of Living Index', 'Property Price to Income Ratio', 'Traffic Commute Time Index', 'Pollution Index', 'Climate Index ']
weights = [0, 100, 100, 50, -50, 0, 0, 20, 20]

r = requests.get('https://www.numbeo.com/quality-of-life/rankings_by_country.jsp')
r = r.text

countries = []
pairs = []

for i in range(20):
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
        pair[1] = sum  #TODO: make values follow the same standard (e.g. by making them percentage of the max value)
        iterator += 1

    pairs.append(pair)

sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

for i in sorted_pairs:
    print(i)