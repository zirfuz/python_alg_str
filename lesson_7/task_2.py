# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#    заданный случайными числами на промежутке [0; 50).
#    Выведите на экран исходный и отсортированный массивы.

import random

MIN = 0
MAX = 50
LEN = 20


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    a1 = merge_sort(array[:mid])
    a2 = merge_sort(array[mid:])
    ret = []
    i = j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            ret.append(a1[i])
            i += 1
        else:
            ret.append(a2[j])
            j += 1
    ret += a1[i:]
    ret += a2[j:]
    return ret


def test():
    array = [random.uniform(MIN, MAX - 1) for _ in range(LEN)]
    ar1 = array.copy()
    ar2 = array.copy()
    ar1 = merge_sort(ar1)
    ar2 = sorted(ar2)
    assert ar1 == ar2


def test_n(n):
    for i in range(n):
        test()
        print(f'Test {i + 1: 4} OK')


test_n(100)
print()

array = [random.uniform(MIN, MAX - 1) for _ in range(LEN)]
print(['%4.2f' % i for i in array])

array = merge_sort(array)
print(['%4.2f' % i for i in array])
