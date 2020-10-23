
def degree(x, y):
    """
    Возведение в степень
    """
    # return pow(x, y)

    return x ** y

    # i = 1  # текущая / исходная степень
    # result = 1
    # while i <= y:
    #     result *= x
    #     i += 1
    # return result # не для отрицательной степени


print(degree(8, 2))
