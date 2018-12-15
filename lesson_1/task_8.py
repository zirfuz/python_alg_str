# Начало
# Ввод year
# Если year % 400 == 0
# то leap = True
# иначе
#     Если year % 100 == 0
#     то leap = False
#     иначе leap = year % 4 == 0
# Если leap
# то Вывод("Високосный")
# иначе Вывод("Невисокосный")
# Конец

year = int(input("Year: "))

if year % 400 == 0:
    leap = True
else:
    if year % 100 == 0:
        leap = False
    else:
        leap = year % 4 == 0

if leap:
    print("Високосный")
else:
    print("Невисокосный")
