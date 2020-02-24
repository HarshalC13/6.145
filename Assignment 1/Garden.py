pi = 3.14
side_length = 30
spacing = 0.6
flower_depth = 5
gravel_depth = 3

o_rad = side_length / 4
i_rad = o_rad

smaller_circle_gravel = (i_rad ** 2) * pi  # area of perfect circle
smaller_square = (side_length / 2) ** 2  # area of inner square
small_flower = (smaller_square - smaller_circle_gravel) / 4  # area of one smaller flowerbed

semicircles_gravel = (o_rad ** 2) * pi * 2  # area of the two semicircles
large_flower = ((side_length ** 2) - semicircles_gravel - smaller_square) / 4  # area of one larger flowerbed

plants_smallbed = int(small_flower / (spacing ** 2))
plants_largebed = int(large_flower / (spacing ** 2))
total_plants = int(4 * (plants_largebed + plants_smallbed))

vol_soil_smallbed = small_flower * flower_depth / 27  # convert to cubic yards by dividing by 27
vol_soil_largebed = large_flower * flower_depth / 27
total_soil = 4 * vol_soil_largebed + 4 * vol_soil_smallbed

vol_gravel_smallbed = smaller_circle_gravel * gravel_depth / 27  # convert to cubic yards by dividing by 27
vol_gravel_largebed = semicircles_gravel * gravel_depth / 27
total_gravel = vol_gravel_largebed + vol_gravel_smallbed

print(plants_smallbed)
print(plants_largebed)
print(total_plants)
print(vol_soil_smallbed)
print(vol_soil_largebed)
print(total_soil)
print(total_gravel)