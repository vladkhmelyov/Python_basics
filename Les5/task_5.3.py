# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

my_f = open("task_5.3_text.txt", "r")
people = []
for el in my_f:
    people.append(el.split())
print(people)
count = len(people)
for el in people:
    if float(el[1]) < 20000:
        print(el[0], 'получает менее 20 тыс.руб')
sallary = []
for elem in people:
    sallary.append(float(elem[1]))
mid = sum(sallary) // count
print('Средняя з.п. составляет ', mid)
my_f.close()
