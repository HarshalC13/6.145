interest_rate = 1e-07
time = 0
if interest_rate == 0.0:
    print("NEVER")
else:
    while (1 + interest_rate) ** (time) < 2.0:
        time = time + 1
    print(time)