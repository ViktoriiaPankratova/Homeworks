user_number1 = float(input('Введіть 1-ше число '))
user_operation = input('Введіть дію (+, /, -, *)')
user_number2 = float(input('Введіть 2-ге число '))
if user_operation == '+':
    result = user_number1 + user_number2
elif user_operation == '-':
    result = user_number1 + user_number2
elif user_operation == '*':
    result = user_number1 + user_number2
elif user_operation == '/' and user_number2 !=0:
    result = user_number1 / user_number2

print(f"{user_number1} {user_operation} {user_number2} = {result}")






