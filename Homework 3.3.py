value_list = [1, 2, 3, 4, 5]
midpoint = len(value_list) / 2
print(midpoint)
if midpoint % 2 == 0:
    midpoint = len(value_list) // 2
    first_half = value_list[:midpoint]
    second_half = value_list[midpoint:]
    print(f'{value_list} => [{first_half}, {second_half}]')
else:
    midpoint = len(value_list) // 2 +1
    first_half = value_list[:midpoint]
    second_half = value_list[midpoint:]
    print(f'{value_list} => [{first_half}, {second_half}]')