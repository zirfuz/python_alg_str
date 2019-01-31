# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#    Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#    Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
#    Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

import sys
import random


class PersistentLocals(object):
    def __init__(self, func):
        self._locals = {}
        self.func = func

    def __call__(self, *args, **kwargs):
        def tracer(frame, event, arg):
            if event == 'return':
                self._locals = frame.f_locals.copy()

        sys.setprofile(tracer)
        try:
            res = self.func(*args, **kwargs)
        finally:
            sys.setprofile(None)
        return res

    def clear_locals(self):
        self._locals = {}

    @property
    def locals(self):
        return self._locals

    def print_mem(self):
        print('=' * 20)
        _vars = {}
        for key in self.locals:
            _vars[key] = self._mem_size(self._locals[key])
        total = sum(_vars.values())
        print(f'TOTAL: {total}\n')
        for var, sz in _vars.items():
            print(f'{var}: {sz}')
        print()

    def _mem_size(self, x):
        total = sys.getsizeof(x)

        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in locals.items():
                    total += self._mem_size(key)
                    total += self._mem_size(value)
            elif not isinstance(x, str):
                for item in x:
                    total += self._mem_size(item)
        return total


SIZE = 200
MIN = 1
MAX = 10

ARRAY = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(ARRAY)
print()


@PersistentLocals
def f1():
    min1 = ARRAY[0]
    min2 = ARRAY[1]

    for i in range(2, len(ARRAY)):
        if min1 > min2:
            min1, min2 = min2, min1
        item = ARRAY[i]
        if item < min2:
            min2 = min1
            min1 = item

    if min1 > min2:
        min1, min2 = min2, min1

    return min1, min2


@PersistentLocals
def f2():
    array = ARRAY.copy()
    min1 = min(array)
    array.remove(min1)
    min2 = min(array)
    return min1, min2


@PersistentLocals
def f3():
    min1_i = ARRAY.index(min(ARRAY))
    min2 = float('inf')
    for i in range(len(ARRAY)):
        value = ARRAY[i]
        if i != min1_i and value < min2:
            min2 = value
    return ARRAY[min1_i], min2


r1 = f1()
r2 = f2()
r3 = f3()

assert (r1 == r2 == r3)

f1.print_mem()
f2.print_mem()
f3.print_mem()


# Выводы:
# Алгоритмы f1 и f3 потребляют заметно меньше памяти чем f2.
# f1 и f3 дают похожие результаты употребления памяти.
# На примере из двух элементов (например ARRAY = [1, 2] f1 может употребить почти в 2 раза меньше памяти, чем f3.
# На некоторых примерах (например ARRAY = [1, 2, 3]) f3 может употребить чуть меньше памяти, чем f1.
# `array = ARRAY.copy()` потребляет существенное количество памяти.
