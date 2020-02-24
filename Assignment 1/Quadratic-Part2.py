a = 0
b = -7.165539291395731
c = -10.232818719422397
if a == 0:
    x = -c / b
    print(x)
else:
    quad_formula1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    quad_formula2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    print(quad_formula1)
    print(quad_formula2)