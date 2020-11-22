a = [
    ['a', 'a1', 'b1  b2  b3  b4  b5', 'c', 'd', 'e', 'f']
]
data_by_serial_number = []
for i in a:
    data_serial_numbers = i[2].strip().split('  ')
    if len(data_serial_numbers) > 0:
        for serial_number in data_serial_numbers:
            i[2] = serial_number
            print([j for j in i])
            data_by_serial_number.append([j for j in i])
    else:
        data_by_serial_number.append(i)
        print(i)
print(data_by_serial_number)
