# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#    При этом каждое число представляется как массив, элементы которого это цифры числа.
#    Например, пользователь ввёл A2 и C4F.
#    Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#    Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
import random

NUMERALS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUM_DEC = {num: dec for dec, num in enumerate(NUMERALS)}

def summ(value1, value2, base):
    value1 = deque(value1)
    value2 = deque(value2)
    result = deque()
    mem = 0
    while value1 or value2:
        num1 = value1.pop() if value1 else '0'
        num2 = value2.pop() if value2 else '0'
        ii = NUM_DEC[num1] + NUM_DEC[num2] + mem
        result.appendleft(NUMERALS[ii % base])
        mem = ii // base
    if (mem != 0):
        result.appendleft(NUMERALS[mem])
    return [str(i) for i in result]


def mult(value1, value2, base):
    terms = deque()
    len1 = len(value1)
    len2 = len(value2)
    for i in range(len2 - 1, -1, -1):
        term = deque(['0'] * (len2 - i - 1))
        mem = 0
        for j in range(len1 - 1, -1, -1):
            ij = NUM_DEC[value2[i]] * NUM_DEC[value1[j]] + mem
            term.appendleft(NUMERALS[ij % base])
            mem = ij // base
        if (mem != 0):
            term.appendleft(NUMERALS[mem])
        terms.appendleft(term)
    result = ['0']
    for term in terms:
        result = summ(result, term, base)
    return result


def test(iterations, base):
    def _base_n(num, b):
        return ((num == 0) and NUMERALS[0]) or (_base_n(num // b, b).lstrip(NUMERALS[0]) + NUMERALS[num % b])

    def _test(i, value1, value2):
        print(f'Test {i:5} ({value1:8}, {value2:8}):', end='')
        value1_ = list(_base_n(value1, base))
        value2_ = list(_base_n(value2, base))
        sum_ = summ(value1_, value2_, base)
        mult_ = mult(value1_, value2_, base)
        assert (value1 + value2 == int(''.join(sum_), base))
        assert (value1 * value2 == int(''.join(mult_), base))
        print(' OK')

    for i in range(1, iterations + 1):
        value1 = random.randint(0, 999999)
        value2 = random.randint(0, 999999)
        if random.randint(0, 10) == 0:
            value1 = 0
        if random.randint(0, 10) == 0:
            value2 = 0
        _test(i, value1, value2)
    print()


test(1000, 13)

value1 = [ch.upper() for ch in list(input('Value1 = '))]
value2 = [ch.upper() for ch in list(input('Value2 = '))]

sum_ = summ(value1, value2, 16)
mult_ = mult(value1, value2, 16)

sum_str = ''.join(sum_)
mult_str = ''.join(mult_)

print()
print(f'Sum  = {sum_str}')
print(f'Mult = {mult_str}')
