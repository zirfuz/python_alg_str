# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#    При этом каждое число представляется как массив, элементы которого это цифры числа.
#    Например, пользователь ввёл A2 и C4F.
#    Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#    Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


value1 = [ch.upper() for ch in list(input('Value1 = '))]
value2 = [ch.upper() for ch in list(input('Value2 = '))]


def summ(value1, value2):
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
        sum_i = int(value1[i]) + int(value2[i])
        result.insert(0, sum_i % 10 + mem)
        mem = sum_i // 10
    if (mem != 0):
        result.insert(0, mem)
    return [str(i) for i in result]


def mult(value1, value2):
    terms = []
    len1 = len(value1)
    len2 = len(value2)
    for i in range(len2 - 1, -1, -1):
        term = ['0'] * (len2 - i - 1)
        mem = 0
        for j in range(len1 - 1, -1, -1):
            ij = int(value2[i]) * int(value1[j]) + mem
            term.insert(0, ij % 10)
            mem = ij // 10
        if (mem != 0):
            term.insert(0, mem)
        terms.insert(0, term)
    result = ['0']
    for term in terms:
        result = summ(result, term)
    return result


print()

sum_ = summ(value1, value2)
sum_str = ''.join(sum_)
print(f'Sum =  {sum_str}')

mult_ = mult(value1, value2)
mult_str = ''.join(mult_)
print(f'Mult = {mult_str}')
