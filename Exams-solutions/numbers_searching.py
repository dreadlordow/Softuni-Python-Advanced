def numbers_searching(*args):
    numbers = args
    duplicate_numbers = []
    min_number = min(numbers)
    max_number = max(numbers)
    for number in numbers:
        number_occurance = 0
        for num in numbers:
            if number == num:
                number_occurance += 1
                if number_occurance == 2:
                    duplicate_numbers.append(number)
                    break

        missing = max_number - 1
        while True:
            is_missing_found = False
            for n in numbers:
                if n == missing:
                    missing -= 1
                    is_missing_found = True
                    break
            if not is_missing_found:
                break
    res = [missing]
    res.append(list(sorted(set(duplicate_numbers))))
    return res


