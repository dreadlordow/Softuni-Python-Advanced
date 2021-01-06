from itertools import combinations

people = input().split(', ')
n = int(input())

for combination in combinations(people, n):
    print(', '.join(combination))
