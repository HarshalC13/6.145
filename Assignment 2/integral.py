const = 2
poly = [0, 0, 1/2]
integral = [const]
for i in range(len(poly)):
    integral.append(poly[i] / (i + 1))
print(integral)