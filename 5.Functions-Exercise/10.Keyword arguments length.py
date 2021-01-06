def kwargs_length(**kwargs):
    return len(kwargs.keys())


dictionary = {'name': 'Peter', 'age': 25, 'ivan': 20}

print(kwargs_length(**dictionary))
