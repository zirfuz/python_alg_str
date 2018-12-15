# Начало
# Ввод("a = ")
# Ввод("b = ")
# Ввод("c = ")
#
# Если (a == b) или (a == c) или (b == c)
# то Вывод("Решения нет")
# иначе
#     Если (a < b < c) or (a > b > c)
#     то mid = b
#     иначе
#         Если (b < a < c) or (b > a > c)
#         то mid = a
#         иначе mid = c
#
#     Вывод mid
# Конец


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if (a == b) or (a == c) or (b == c):
    print("Решения нет")
else:
    if (a < b < c) or (a > b > c):
        mid = b
    else:
        if (b < a < c) or (b > a > c):
            mid = a
        else:
            mid = c

    print(f"Mid: {mid}")
