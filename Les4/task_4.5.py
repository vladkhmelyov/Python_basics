
from functools import reduce

some_list = [i for i in range(100, 1001) if i % 2 == 0]
print(some_list)
print(reduce(lambda x, y: x * y, some_list))
