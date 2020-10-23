
def max_sum(arg_1, arg_2, arg_3):
    """
    Сумма двух больших аргументов
    """
    min_arg = min(arg_1, arg_2, arg_3)
    return arg_1 + arg_2 + arg_3 - min_arg


print(max_sum(10, 20, 30))
