# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#    Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
#    которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
#    Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

import random
import statistics

MIN = 0
MAX = 10
LEN = 2001


def median(array):
    def _median(array, idx):
        if len(array) == 1:
            return array[0]
        ar1, ar2, ar3 = [], [], []
        pvt = len(array) // 2
        for i in range(len(array)):
            ari = array[i]
            if ari < array[pvt]:
                ar1.append(ari)
            elif ari == array[pvt]:
                ar2.append(ari)
            else:
                ar3.append(ari)

        if len(ar1) > idx:
            return _median(ar1, idx)
        elif len(ar1) + len(ar2) > idx:
            return ar2[0]
        return _median(ar3, idx - len(ar1) - len(ar2))

    return _median(array, len(array) // 2)


def test():
    array = [random.randint(MIN, MAX) for _ in range(LEN)]

    a1 = median(array)
    a2 = statistics.median(array)
    assert median(array) == statistics.median(array)


def test_n(n):
    for i in range(n):
        test()
        print(f'Test {i + 1: 4} OK')


test_n(100)
print()

array = [random.randint(MIN, MAX - 1) for _ in range(LEN)]
print(array)

print(median(array))
