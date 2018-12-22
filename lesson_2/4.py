# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#    Количество элементов (n) вводится с клавиатуры.

def sum_rec(n, x = 1):
    if n == 1:
        return 1
    x /= -2
    return sum_rec(n - 1, x) + x

n = int(input("n = "))
result_rec = sum_rec(n)
print(f'ResultRec:  {result_rec}')



# - Test -
def sum_loop(n):
    ret = 0
    x = 1
    for i in range(n):
        ret += x
        x /= -2
    return ret

result_loop = sum_loop(n)
print(f'ResultLoop: {result_loop}')
