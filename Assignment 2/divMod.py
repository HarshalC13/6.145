dividend = 56
divisor = 7
count = 0
if dividend == 0:
    print(0)
    print(0)
else:
    while dividend > 0 and dividend >= divisor:
        dividend = dividend - divisor
        count = count + 1
    print(count)
    print(dividend)