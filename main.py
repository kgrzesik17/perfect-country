import requests
import re

# ['Quality of Life Index', 'Purchasing Power Index', 'Safety Index', 'Health Care Index', 'Cost of Living Index', 'Property Price to Income Ratio', 'Traffic Commute Time Index', 'Pollution Index', 'Climate Index ']
weights = [0, 100, 100, 50, -50, 0, 0, 20, 20]  # weigths entered by user
max_values = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # max values used to standartize the values

r = requests.get('https://www.numbeo.com/quality-of-life/rankings_by_country.jsp')
r = r.text

countries = []  # countries with all the values
pairs = []

# add values to arrays
for i in range(3):
    a = r.split('<tr')[i + 3]
    b = a.split('<td style="text-align: right">')
    values = []  # QoL, purchasing power, etc.
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


#TODO: check if scales don't differ (e.g. logarythmic vs linear)

# standardize by using % of max values
for i in countries:
    for iterator, j in enumerate(i[1:]):
        if float(j) > float(max_values[iterator]):
            max_values[iterator] = j


# add everything together using weights
for i in countries:
    pair = [i[0], '']
    sum = 0
    iterator = 0

    for j in i[1::]:
        sum += float(j) * weights[iterator] / float(max_values[iterator])
        pair[1] = sum
        iterator += 1

    pairs.append(pair)

sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)





print(sorted_pairs)