
def division(arg_1, arg_2):
    """
    Функция деления
    arg_1 - делимое
    arg_2 - делитель
    """
    if arg_2 == 0:
        return "Дление на 0 невозможно"
    else:
        return arg_1 / arg_2


devd = int(input("Введите делимое "))
devr = int(input("Введите делитель "))
print(division(devd, devr))
