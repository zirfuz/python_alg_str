# 5. В массиве найти максимальный отрицательный элемент.
#    Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN = -9
MAX = 9

array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(array)

max_neg_i = None
for i, item in enumerate(array):
    if item < 0 and (max_neg_i is None or item > array[max_neg_i]):
        max_neg_i = i

max_neg = None if max_neg_i is None else array[max_neg_i]
print(f'MaxNeg: array[{max_neg_i}] = {max_neg}')
