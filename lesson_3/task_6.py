# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#    Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN = 1
MAX = 10

array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(array)

min_index = max_index = 0

for i, item in enumerate(array):
    if item < array[min_index]:
        min_index = i
    elif item >= array[max_index]:
        max_index = i

sum_ = 0
i1, i2 = (min_index, max_index) if (min_index < max_index) else (max_index, min_index)

for i in range(i1 + 1, i2):
    sum_ += array[i]

print(f'Sum(a[{i1}]..a[{i2}]) = {sum_}')
