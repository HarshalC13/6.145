kwh_used = 1000
bill = 0
if (kwh_used <= 500):
    bill = 1.2 * (kwh_used * 0.41)
    print(bill)
elif (kwh_used <= 1500 and kwh_used > 500):
    lowest_rate = 500 * 0.41
    second_rate = (kwh_used - 500) * 0.75
    bill = 1.2 * (lowest_rate + second_rate)
    print(bill)
elif (kwh_used <= 2500 and kwh_used > 1500):
    lowest_rate = 500 * 0.41
    second_rate = 1000 * 0.75
    third_rate = (kwh_used - 1500) * 1.28
    bill = 1.2 * (lowest_rate + second_rate + third_rate)
    print(bill)
else:
    lowest_rate = 500 * 0.41
    second_rate = 1000 * 0.75
    third_rate = 1000 * 1.28
    fourth_rate = (kwh_used - 2500) * 1.77
    bill = 1.2 * (lowest_rate + second_rate + third_rate + fourth_rate)
    print(bill)