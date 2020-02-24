p_d = 5
sq_cells = p_d ** 2
cir_cells = 0
unit_from_center = p_d // 2
distances = []
for i in range(-unit_from_center, unit_from_center + 1, 1):
    for j in range(-unit_from_center, unit_from_center + 1, 1):
        x = i ** 2
        y = j ** 2
        distances.append((x + y) ** 0.5)
for k in range(len(distances)):
    if distances[k] <= p_d / 2:
        cir_cells = cir_cells + 1
    else:
        cir_cells = cir_cells
Approx = 4 * cir_cells / sq_cells
print(Approx)