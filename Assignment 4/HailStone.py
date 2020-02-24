out = []


def hailstone_sequence(a_0):
    if a_0 == 1:
        out.append(1)
        return out
    elif a_0 % 2 == 0:
        out.append(a_0)
        operation = a_0 / 2
    elif a_0 % 2 == 1:
        out.append(a_0)
        operation = 3 * a_0 + 1
    a_0 = operation
    return hailstone_sequence(a_0)
