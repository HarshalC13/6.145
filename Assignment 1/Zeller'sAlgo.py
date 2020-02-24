year = 2017
month = 1  # 1=January, 2=February, ..., 12=December
day = 9
if month == 1 or month == 2:
    year1 = year - 1
    month1 = month + 12
else:
    year1 = year
    month1 = month
year_2 = year1 % 100
century = int(year1 / 100)
first_term = day
second_term = int(13 * (month1 + 1) / 5)
third_term = year_2
fourth_term = int(year_2 / 4)
fifth_term = int(century / 4)
sixth_term = 2 * century
w = (first_term + second_term + third_term + fourth_term + fifth_term - sixth_term) % 7
print(w)