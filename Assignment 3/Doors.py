# doors start out locked so False
def ndoors(num):
    doors = []
    for i in range(1, num + 1):
        doors.append([i, False])

    for i in range(0, num):
        for j in range(0, num):
            if doors[j][0] % (i + 1) == 0:
                doors[j][1] = not doors[j][1]
            else:
                pass

    open = []
    for i in range(0, num):
        if doors[i][1]:
            open.append(doors[i][0])
        else:
            pass
    print(open)
ndoors(400)
