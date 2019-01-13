# Написать два алгоритма нахождения i-го по счёту простого числа.
#   Без использования «Решета Эратосфена»;
#   Используя алгоритм «Решето Эратосфена»

def is_prime(value):
    for i in range(2, value - 1):
        if value % i == 0:
            return False
    return True


def prime(i):
    value = 1
    while i > -1:
        value += 1
        if is_prime(value):
            i -= 1
    return value



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


sieve = Sieve(1000)


def test_prime(i):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    if i < len(lst):
        assert lst[i] == prime(i)
        assert lst[i] == sieve.get(i)
    else:
        assert prime(i) == sieve.get(i)
    print(f'Test {i} OK')


def test_primes(n):
    for i in range(n):
        test_prime(i)


test_primes(100)
