poly = [0, 0, 1 / 2]
derv = []
for i in range(len(poly) - 1):
    derv.append((i + 1) * poly[i + 1])
print(derv)