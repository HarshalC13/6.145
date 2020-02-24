px = 1
py = 2
a = 3
b = 4
c = 5
normal = ((a ** 2) + (b ** 2)) ** 0.5
dot = (a * px) + (b * py) + (c)
distance = abs(dot) / normal
print(distance)