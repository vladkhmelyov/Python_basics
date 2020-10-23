rating = [8, 1, 6, 4, 9, 8]
user_rat = int(input('Введите новое значение '))
rating.append(user_rat)
rev = sorted(rating, reverse = True)
print(rev)
