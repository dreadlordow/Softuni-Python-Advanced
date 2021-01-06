def age_assignment(*args, **kwargs):
    d = {}
    for k,v in kwargs.items():
        for arg in args:
            if arg.startswith(k):
                d[arg] = v
    return d

print(age_assignment("Peter", "George", G=20, P=19))
