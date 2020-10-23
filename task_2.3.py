season = {1: 'Зима',
          2: 'Зима',
          3: 'Весна',
          4: 'Весна',
          5: 'Весна',
          6: 'Лето',
          7: 'Лето',
          8: 'Лето',
          9: 'Осень',
          10: 'Осень',
          11: 'Осень',
          12: 'Зима'}
month = int(input('Указать числовое значение календарного месяца '))
print(season.get(month))

# months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# season = int(input('Указать числовое значение календарного месяца '))
# if season == 1 or season == 2 or season == 12:
#     print('Зима')
# elif season == 3 or season == 4 or season == 5:
#     print('Весна')
# elif season == 6 or season == 7 or season == 8:
#     print('Лето')
# elif season == 9 or season == 10 or season == 11:
#     print('Осень')
# else:
#     print('Данные неверны')
