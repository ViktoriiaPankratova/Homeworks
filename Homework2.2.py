user_numbers = input('Введіть 5ти-значне ціле число ')
number= int(user_numbers)
div_mod0=number//10000
div_mod1=(number%10000)//1000
div_mod2=(number%1000)//100
div_mod3=(number%100)//10
div_mod4=(number%10)
print(div_mod4, div_mod3, div_mod2, div_mod1, div_mod0)