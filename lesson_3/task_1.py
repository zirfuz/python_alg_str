# 1. В диапазоне натуральных чисел от 2 до 99 определить,
#    сколько из них кратны любому из чисел в диапазоне от 2 до 9.

import random

rng = range(2, 9 + 1)
counter = 0

for i in range(2, 99 + 1):
    for j in rng:
        if i % j == 0:
            counter += 1
            break

print(f'Result: {counter}')
