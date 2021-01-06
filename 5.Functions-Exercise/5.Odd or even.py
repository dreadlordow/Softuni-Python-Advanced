command = input()
numbers = [int(x) for x in input().split()]
if command == 'Odd':
    odd = filter(lambda x: x % 2 != 0, numbers)
    print(sum(odd)*len(numbers))
else:
    even = filter(lambda x: x % 2 == 0, numbers)
    print(sum(even)*len(numbers))