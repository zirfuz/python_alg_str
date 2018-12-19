# Начало
#
# Ввод границ целого случайного числа ai, bi
# ri = random(ai, bi)
# Вывод ri
#
# Ввод границ целого вещественного числа af, bf
# rf = random(af, bf)
# Вывод rf
#
# Ввод границ случайного символа ai, bi
# rc = random(ac, bc)
# Вывод rc
#
# Конец

import random

print("Границы целого случайного числа:")
ai = int(input("A = "))
bi = int(input("B = "))
ri = random.randint(ai, bi)
print(f"Random int: {ri}\n")

print("Границы вещественного случайного числа:")
af = float(input("A = "))
bf = float(input("B = "))
rf = random.uniform(af, bf)
print(f"Random float: {rf}\n")

print("Границы случайной буквы (lower case):")
ac = ord(input("A = "))
bc = ord(input("B = "))
rc = random.randint(ac, bc)
rc = chr(rc)
print(f"Random letter: {rc}")
