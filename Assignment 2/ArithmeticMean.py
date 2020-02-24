numbers = []
length = len(numbers)
total = 0
if length == 0:
    print(None)
else:
    for i in numbers:
        total = total + i
    print(total / length)