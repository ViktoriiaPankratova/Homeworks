value_list1 = [12, 3, 4, 10]
value_list2 = []
value_list3 = [1]
if len(value_list1)>1:
    last_element1 = value_list1[-1]
    remaining_list1 = value_list1[:-1]
    reversed_list1 = [last_element1] + remaining_list1
    print(f'{value_list1} => {reversed_list1}')
else:
    print(f'{value_list1} => {value_list1}')
if len(value_list2)>1:
    last_element2 = value_list2[-1]
    remaining_list2 = value_list2[:-1]
    reversed_list2 = [last_element2] + remaining_list2
    print(f'{value_list2} => {reversed_list2}')
else:
    print(f'{value_list2} => {value_list2}')
if len(value_list3)>1:
    last_element3 = value_list3[-1]
    remaining_list3 = value_list3[:-1]
    reversed_list3 = [last_element3] + remaining_list3
    print(f'{value_list3} => {reversed_list3}')
else:
    print(f'{value_list3} => {value_list3}')
