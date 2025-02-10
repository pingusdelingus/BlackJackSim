count = 0
for x in range(9):  # 0 to 8
    for y in range(9 - x):  # ensures y + x doesn't exceed 8
        for z in range(9 - x - y):  # ensures x + y + z doesn't exceed 8
            if 3 <= x + y + z <= 8:
                count += 1

print(count)
