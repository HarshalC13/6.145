def dictmap(d, f):
    for i in d:
        d[i] = f(d[i])
