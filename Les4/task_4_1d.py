#if __name__ == "__name__":

def salary(argA, argB, argC):
    """
    Расчет зарплаты
    """
    return (argA * argB) + argC


workHour = int(input("количество часов: "))
rate = int(input("ставка: "))
extra = int(input("премия: "))
print("Итоговая зарплата: ", salary(workHour, rate, extra))
