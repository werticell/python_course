def pascal_triangle():
i = 1
last_array = [1]
yield 1
while True:
    current_array = []
    for y in range(0, i + 1):
        if y == 0 or y == i:
            current_array.append(1)
        else:
            current_array.append(last_array[y - 1] + last_array[y])
    for values in current_array:
        yield values
    last_array = current_array
    i += 1
