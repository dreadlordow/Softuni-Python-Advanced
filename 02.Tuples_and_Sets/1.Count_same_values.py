d= {}

numbers = map(float,input().split())

for number in numbers:
    if number not in d:
        d[number] = 0
    d[number] += 1

for number, occurance_count in d.items():
    print(f'{number} - {occurance_count} times')
