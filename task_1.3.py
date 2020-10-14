# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
number = int(input('Введите натуральное число '))
while number >= 10:
    print('Введите число менее 10')
    number = int(input('Введите число: '))
else:
    dual = int(str(number) + str(number))
    triple = int(str(number) + str(number) + str(number))
    total = number + dual + triple
    print('Сумма', number, '+', dual, '+', triple, 'равна', total)
