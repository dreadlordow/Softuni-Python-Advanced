nums = [int(num) for num in input().split(', ')]
pos = [num for num in nums if num >= 0]
neg = [num for num in nums if num < 0]
even = [num for num in nums if num % 2 ==0]
odd = [num for num in nums if num % 2 !=0]

print(f'Positive: {", ".join([str(x) for x in pos])}')
print(f'Negative: {", ".join([str(x) for x in neg])}')
print(f'Even: {", ".join([str(x) for x in even])}')
print(f'Odd: {", ".join([str(x) for x in odd])}')