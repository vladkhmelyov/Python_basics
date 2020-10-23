
def num_line(nums_list):
    num_sum = 0
    for x in nums_list:
        num_sum = num_sum + x
    return num_sum


while True:
    user_line = input("Введите ряд чисел через пробел: ")
    if user_line[:] == 0:
        break
    num_list = list(map(int, user_line.split()))
    num_list = num_list + num_list
    print('Сумма введеных на данный момент чисел составляет: ', num_line(num_list))
