# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
#    заданный случайными числами на промежутке [-100; 100).
#    Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
#    По возможности доработайте алгоритм (сделайте его умнее).

import random

MIN = -100
MAX = 100
LEN = 20


def bubble_sort_rev(array):
    len_ar = len(array)
    for i in range(len_ar - 1):
        for j in range(i + 1, len_ar):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]


def test():
    array = [random.randint(MIN, MAX - 1) for _ in range(LEN)]
    ar1 = array.copy()
    ar2 = array.copy()
    bubble_sort_rev(ar1)
    ar2 = sorted(ar2, reverse=True)
    assert ar1 == ar2


def test_n(n):
    for i in range(n):
        test()
        print(f'Test {i + 1: 4} OK')


test_n(100)
print()

array = [random.randint(MIN, MAX - 1) for _ in range(LEN)]
print('Array:  ', end='')
print(array)

bubble_sort_rev(array)
print('Sorted: ', end='')
print(array)
