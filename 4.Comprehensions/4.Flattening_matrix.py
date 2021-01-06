matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
print([item for sublist in matrix for item in sublist])