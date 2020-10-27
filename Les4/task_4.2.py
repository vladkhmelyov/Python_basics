
import random

some_list = [i for i in range(0, 21)]
res_list = random.choices(some_list, k=30)
# print("30 случайных из some_list ", res_list)
result =[]
for item in range(1, len(res_list)): #цикл ходит по индексу
    if res_list[item] > res_list[item - 1]:
        result.append(res_list[item])
print(result)
