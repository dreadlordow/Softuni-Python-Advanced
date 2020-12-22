from _collections import deque

food_quantity = int(input())
input_ints = list(map(int, input().split()))
queue = deque(input_ints)
print(max(queue))

while len(queue) > 0:
    if food_quantity >= queue[0]:
        order_executed = queue.popleft()
        food_quantity -= order_executed
    else:
        break
if len(queue) == 0:
    print(f'Orders complete')
else:
    to_print = []
    while len(queue) > 0:
        to_print.append(str(queue.popleft()))
    print(f"Orders left: {' '.join(to_print)} ")