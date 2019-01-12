# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN = 1
MAX = 10
F_WIDTH = 2


def print_array(array):
    for item in array:
        print(f'{item:>{F_WIDTH}}', end=' ')
    print()


array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print_array(array)

min_index = max_index = 0
for i, item in enumerate(array):
    if item < array[min_index]:
        min_index = i
    elif item >= array[max_index]:
        max_index = i

array[min_index], array[max_index] = array[max_index], array[min_index]
print_array(array)
