# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_f = open("task_5.5_text.txt", "a")
some_data = input("Введите набор чисел, разделенных пробелами: ")
sum_of_data = sum(int(i) for i in some_data.split())
my_f.write(some_data + '\n' + str(sum_of_data) + '\n')

my_f.close()
