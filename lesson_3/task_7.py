# 7. В одномерном массиве целых чисел определить два наименьших элемента.
#    Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 5
MIN = 1
MAX = 10

array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(array)

min1 = array[0]
min2 = array[1]

for i in range(2, len(array)):
    if min1 > min2:
        min1, min2 = min2, min1
    item = array[i]
    if item < min2:
        min2 = min1
        min1 = item

if min1 > min2:
    min1, min2 = min2, min1

print(f'Min1: {min1}')
print(f'Min2: {min2}')
