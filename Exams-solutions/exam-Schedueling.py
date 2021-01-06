from sys import maxsize
from _collections import deque
cycles = [int(x) for x in input().split(', ')]
task_to_see = int(input())

total_cycles = 0

while True:
    minimum = cycles.index(min(cycles))
    total_cycles += cycles[minimum]
    if minimum == task_to_see:
        break
    cycles[minimum]  = maxsize
print(total_cycles)