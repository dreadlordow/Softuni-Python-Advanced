n = int(input())
even_set = set()
odd_set = set()

for i in range(1, n + 1):
    name = input()
    summed = sum([ord(x) for x in name]) // i
    if summed % 2 == 0:
        even_set.add(summed)
    else:
        odd_set.add(summed)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if odd_sum > even_sum:
    difference_values = odd_set.difference(even_set)
    print(', '.join([str(x) for x in difference_values]))
elif even_sum > odd_sum:
    sym_values = odd_set.symmetric_difference(even_set)
    print(', '.join([str(x) for x in sym_values]))
else:
    union_values = odd_set.union(even_set)
    print(', '.join([str(x) for x in union_values]))