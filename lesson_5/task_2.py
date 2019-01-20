# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#    При этом каждое число представляется как массив, элементы которого это цифры числа.
#    Например, пользователь ввёл A2 и C4F.
#    Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#    Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


value1 = [ch.upper() for ch in list(input('Value1 = '))]
value2 = [ch.upper() for ch in list(input('Value2 = '))]

def sum_(value1, value2):
    len1 = len(value1)
    len2 = len(value2)
    if len1 < len2:
        for _ in range(len1, len2):
            value1.insert(0, '0')
    else:
        for _ in range(len2, len1):
            value2.insert(0, '0')
    value1.insert(0, '0')
    value2.insert(0, '0')
    result = [0] * len(value1)
    mem = 0;
    for i in range(len(value1) - 1, -1, -1):
        sum_i = int(value1[i]) + int(value2[i])
        result[i] = sum_i % 10
        result[i] += mem
        mem = sum_i // 10
    if result[0] == 0:
        result.pop(0)
    return [str(i) for i in result]


summ = sum_(value1, value2)
summ_str = ''.join(summ)
print(f'Sum: {summ_str}')
