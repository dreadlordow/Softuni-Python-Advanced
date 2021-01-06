from _collections import deque

customers = deque([int(x) for x in input().split(', ')])
list_of_taxis = [int(x) for x in input().split(', ')]
total_time = 0
are_driven = True
while len(customers) > 0 :
    if len(list_of_taxis) > 0:
        current_customer = customers.popleft()
        current_driver = list_of_taxis.pop()
    else:
        print(f'Not all customers were driven to their destinations')
        print(f'Customers left: {", ".join([str(x) for x in customers])}')
        are_driven = False
        break
    if current_customer <= current_driver:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)
if are_driven:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')

