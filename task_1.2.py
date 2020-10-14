#  Пользователь вводит время в секундах.
#  Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#  Используйте форматирование строк.
time = int(input('Введите время в секундах '))
hour = (time // 3600)
minute = (time // 60) % 60
second: int = time % 60
if second < 10:
    second = '0' + str(second)
else:
    second = str(second)
if minute < 10:
    minute = '0' + str(minute)
else:
    minute = str(minute)
if hour < 10:
    hour = '0' + str(hour)
else:
    hour = str(hour)
print(hour + ':' + minute + ':' + second)
