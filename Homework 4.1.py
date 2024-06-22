value_list = [0, 11, 12, 0, 13, 45, 25, 0, 0, 5, 3, 0]
for item in value_list:
    if item == 0:
        value_list.remove(item)
        value_list.append(item)
print(value_list)
