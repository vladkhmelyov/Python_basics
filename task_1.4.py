# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции
number = int(input('Введите число '))
maximal = number % 10
number = number // 10
while number > 0:
    if number % 10 > maximal:
        maximal = number % 10
    number = number // 10
print('Наибольшая цифра в числе', maximal)
