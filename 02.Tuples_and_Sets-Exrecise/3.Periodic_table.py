n = int(input())
chem_set = set()
for _ in range(n):
    line = set(input().split())
    chem_set |= line

print('\n'.join(chem_set))