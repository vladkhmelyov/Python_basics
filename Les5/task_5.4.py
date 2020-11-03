# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_f = open("task_5.4_text.txt", "r")
out_f = open("task_5.4_textN.txt", "w")
numCount = []
for el in my_f:
    numCount.append(el.split())

for el in numCount:
    val, sp, nmb = el[:]
    value = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }
    # space = {
    #     '-': '-'
    # }
    # numbers = {
    #     '1': '1',
    #     '2': '2',
    #     '3': '3',
    #     '4': '4'
    # }
    result = f"{value[val]} {sp} {nmb}"
    print(result)
    out_f.writelines(result)

out_f.close()
my_f.close()
