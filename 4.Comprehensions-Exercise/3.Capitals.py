countries = [country for country in input().split(', ')]
cities = [city for city in input().split(', ')]
d = ({pair[0]: pair[1] for pair in zip(countries, cities)})
for k,v in d.items():
    print(f'{k} -> {v}')
