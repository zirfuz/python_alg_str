# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

ROWS = 3
COLUMNS = 5

MIN = 1
MAX = 10
F_WIDTH = 2

matrix = [[random.randint(MIN, MAX) for _ in range(COLUMNS)] for _ in range(ROWS)]

for row in matrix:
    for item in row:
        print(f'{item:>{F_WIDTH}}', end=' ')
    print()

print()

max_min = None

for column in range(COLUMNS):
    min_ = matrix[0][column]
    for row in range(1, ROWS):
        item = matrix[row][column]
        if item < min_:
            min_ = item
    print(f'{min_:>{F_WIDTH}}', end=' ')
    if max_min is None or min_ > max_min:
        max_min = min_

print()
print(f'MaxMin: {max_min}')
