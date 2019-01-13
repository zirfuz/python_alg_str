# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...

import timeit


def sum_rec(n, x=1):
    if n == 1:
        return 1
    x /= -2
    return sum_rec(n - 1, x) + x


def sum_loop(n):
    ret = 0
    x = 1
    for i in range(n):
        ret += x
        x /= -2
    return ret


def test_sum(n):
    lst = [None, 1, -0.5, 0.25, -0.125, 0.0625, -0.03125]
    if n < len(lst):
        sum_ = sum(lst[1:n + 1])
        assert sum_ == sum_rec(n)
        assert sum_ == sum_loop(n)
    else:
        diff = abs(sum_rec(n) - sum_loop(n))
        assert diff < 0.1 ** 10
    print(f'Test {n} OK')


def test_sums(n):
    for i in range(1, n):
        test_sum(i)


test_sums(500)

file_sum_rec = open('sum_rec.txt', 'w')
file_sum_loop = open('sum_loop.txt', 'w')

for n in range(1, 500):
    print(timeit.timeit('sum_rec(n)', setup="from __main__ import sum_rec, n", number=100), file=file_sum_rec)
    print(timeit.timeit('sum_loop(n)', setup="from __main__ import sum_loop, n", number=100), file=file_sum_loop)
