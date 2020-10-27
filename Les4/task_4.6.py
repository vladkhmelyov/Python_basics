
from itertools import count
from itertools import cycle

for el in count(3):
    if el > 17:
        break
    else:
        print(el)
    # для вывода нечетных - использовать следующее
    # if el % 2 == 0:
    #     print(el)
    # elif el > 17:
    #     break

let = 0
for el in cycle("some_text"):
    if let > 10:
        break
    print(el)
    let += 1
