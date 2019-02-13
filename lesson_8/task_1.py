# 1. Определение количества различных подстрок с использованием хэш-функции.
#    Пусть дана строка S, состоящая только из маленьких латинских букв.
#    Требуется найти количество различных подстрок в этой строке.

class HashSet:
    def __init__(self, lst_size=10):
        self._size = 0
        self._lst = [[] for _ in range(lst_size)]

    def _hash(self, value):
        letter = 26
        index = 0
        for i, char in enumerate(value):
            index += (ord(char) - ord('a') + 1) * letter ** i
        return index % len(self._lst)

    def __contains__(self, value):
        index = self._hash(value)
        return value in self._lst[index]

    def insert(self, value):
        index = self._hash(value)
        lst = self._lst[index]
        if value not in lst:
            lst.append(value)
            self._size += 1

    @property
    def size(self):
        return self._size;


def count_sub(string):
    set_ = HashSet()
    len_str = len(string)
    for i in range(len_str):
        for j in range(i + 1, len_str + 1):
            if i == 0 and j == len_str:
                continue
            set_.insert(string[i: j])
    return set_.size


string = 'papapa_aaaa'
result = count_sub(string)
print(f'{string}: {result}')
