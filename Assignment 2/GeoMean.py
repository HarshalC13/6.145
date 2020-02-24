numbers = [2, 7, 3, 9, 13]
length = len(numbers)
product = 1
if length == 0:
    print(None)
else:
    for i in numbers:
        product = product * i
    print(product ** (1 / length))