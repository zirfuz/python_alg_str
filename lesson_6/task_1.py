# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#    Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#    Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
#    Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

import sys


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
        print('=' * 20)

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


@PersistentLocals
def f():
    a = 1
    b = [1, 2]


f()
f.print_mem()
