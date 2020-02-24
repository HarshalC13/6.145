def square(num):
    return num ** 2


def fourth_power(num):
    return square(square(num))


def perfect_square(num):
    root = num ** 0.5
    if root - int(root) == 0:
        return True
    else:
        return False
