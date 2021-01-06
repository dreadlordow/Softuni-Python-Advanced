from itertools import permutations, chain, product

numbers = list(input().split(', '))
n = len(numbers)
permutation = product('-+', repeat=n)

for perm in permutation:
    expr = ''.join(chain(*zip(perm, numbers)))
    res = eval(expr)
    print(f'{expr}={res}')