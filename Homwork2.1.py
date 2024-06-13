user_numbers = input('Введіть 4х-значне ціле число ')
number= int(user_numbers)
div_mod1=number//1000
div_mod2=(number%1000)//100
div_mod3=(number%100)//10
div_mod4=(number%10)
print(div_mod1)
print(div_mod2)
print(div_mod3)
print(div_mod4)