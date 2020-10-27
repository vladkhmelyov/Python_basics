
import random

some_list = [i for i in range(0, 21)]
res_list = random.choices(some_list, k=30)
print("30 случайных из some_list ", res_list)
new_list = []
for i in res_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
