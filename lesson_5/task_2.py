# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#    При этом каждое число представляется как массив, элементы которого это цифры числа.
#    Например, пользователь ввёл A2 и C4F.
#    Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#    Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import random

NUMERALS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUM_DEC = { num : dec for dec, num in enumerate(NUMERALS) }

def summ(value1, value2, base):
    len1 = len(value1)
    len2 = len(value2)
    if len1 < len2:
        for _ in range(len1, len2):
            value1.insert(0, '0')
    else:
        for _ in range(len2, len1):
            value2.insert(0, '0')
    result = []
    mem = 0
    for i in range(len(value1) - 1, -1, -1):
        ii = NUM_DEC[value1[i]] + NUM_DEC[value2[i]] + mem
        result.insert(0, NUMERALS[ii % base])
        mem = ii // base
    if (mem != 0):
        result.insert(0, NUMERALS[mem])
    return [str(i) for i in result]


def mult(value1, value2, base):
    terms = []
    len1 = len(value1)
    len2 = len(value2)
    for i in range(len2 - 1, -1, -1):
        term = ['0'] * (len2 - i - 1)
        mem = 0
        for j in range(len1 - 1, -1, -1):
            ij = NUM_DEC[value2[i]] * NUM_DEC[value1[j]] + mem
            term.insert(0, NUMERALS[ij % base])
            mem = ij // base
        if (mem != 0):
            term.insert(0, NUMERALS[mem])
        terms.insert(0, term)
    result = ['0']
    for term in terms:
        result = summ(result, term, base)
    return result




# def base_n(num, b, numerals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#     return ((num == 0) and numerals[0]) or (base_n(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
#
# for i in range(50):
#     print(i, end=' ')
#     print(base_n(i, 16), end=' ')
#     print(int(base_n(i, 16), 16))



def test(iterations):
    def _base_n(num, b):
        return ((num == 0) and NUMERALS[0]) or (_base_n(num // b, b).lstrip(NUMERALS[0]) + NUMERALS[num % b])

    def _test(i, value1, value2):
        print(f'Test {i:5} ({value1:8}, {value2:8}):', end='')
        value1_ = list(_base_n(value1, 16))
        value2_ = list(_base_n(value2, 16))
        sum_ = summ(value1_, value2_, 16)
        mult_ = mult(value1_, value2_, 16)
        assert (value1 + value2 == int(''.join(sum_), 16))
        assert (value1 * value2 == int(''.join(mult_), 16))
        print(' OK')

    for i in range(1, iterations + 1):
        value1 = random.randint(0, 99)
        value2 = random.randint(0, 99)
        # if random.randint(0, 10) == 0:
        #     value1 = 0
        # if random.randint(0, 10) == 0:
        #     value2 = 0
        _test(i, value1, value2)
    print()


test(10000)

value1 = [ch.upper() for ch in list(input('Value1 = '))]
value2 = [ch.upper() for ch in list(input('Value2 = '))]

sum_ = summ(value1, value2, 16)
mult_ = mult(value1, value2, 16)

sum_str = ''.join(sum_)
mult_str = ''.join(mult_)

print()
print(f'Sum  = {sum_str}')
print(f'Mult = {mult_str}')
