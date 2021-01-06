def best_list_pureness(lst, K):
    rotations = 0
    best_rotation = 0
    best_pureness = 0
    for i in range(K+1):
        current_pureness = 0
        for idx in range(len(lst)):
            current_pureness += (lst[idx] * idx)
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = rotations
        last = lst.pop()
        lst.insert(0, last)
        rotations += 1
    return f'Best pureness {best_pureness} after {best_rotation} rotations'


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)



