numbers = [int(x) for x in input().split()]
negative = list(filter(lambda x: x < 0, numbers))
positive = list(filter(lambda x: x > 0, numbers))
print(f'{sum(negative)}')
print(f'{sum(positive)}')

if abs(sum(negative)) > sum(positive):
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')