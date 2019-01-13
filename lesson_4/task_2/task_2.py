# Написать два алгоритма нахождения i-го по счёту простого числа.
#   Без использования «Решета Эратосфена»;
#   Используя алгоритм «Решето Эратосфена»

import timeit


# Алгоритм 1 (Без решета Эратосфена)
def prime(i):
    def _is_prime(value):
        for i in range(2, (value // 2) + 1):
            if value % i == 0:
                return False
        return True

    value = 1
    while i > -1:
        value += 1
        if _is_prime(value):
            i -= 1
    return value


# Алгоритм 2 (С решетом Эратосфена)
class Sieve:
    def __init__(self, size):
        self._sieve = [i for i in range(size)]
        self._sieve[1] = 0

        for i in range(2, size):
            if self._sieve[i] != 0:
                j = i + i
                while j < size:
                    self._sieve[j] = 0
                    j += i

        self._sieve = [i for i in self._sieve if i != 0]

    def get(self, i):
        return self._sieve[i]


# Инициализация (Решето Эратосфена)
sieve = Sieve(10000)


# Test
def test_prime(i):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    if i < len(lst):
        assert lst[i] == prime(i)
        assert lst[i] == sieve.get(i)
    else:
        assert prime(i) == sieve.get(i)
    print(f'Test {i} OK')


# Test 0..n
def test_primes(n):
    for i in range(0, n):
        test_prime(i)


# Test
test_primes(200)


# Файлы для замеров timeit
file_not_sieve = open('not_sieve.txt', 'w')
file_sieve = open('sieve.txt', 'w')

# Вывод замеров timeit в файлы
for i in range(1, 150):
    print(timeit.timeit('prime(i)', setup="from __main__ import prime, i", number=100), file=file_not_sieve)
    print(timeit.timeit('sieve.get(i)', setup="from __main__ import Sieve, sieve, i", number=100), file=file_sieve)
