# Начало
# Ввод c1
# Ввод c2
#
# pos1 = ord(c1) - ord('a')
# pos2 = ord(c2) - ord('a')
#
# Если pos1 == pos2
# то letters = 0
# иначе
#     Если pos1 < pos2
#     то letters = pos2 - pos1 - 1
#     иначе letters = pos1 - pos2 - 1
#
# Вывод letters
# Конец

c1 = input("Letter1 = ")
c2 = input("Letter2 = ")

pos1 = ord(c1) - ord('a')
pos2 = ord(c2) - ord('a')

if pos1 == pos2:
    letters = 0
else:
    if pos1 < pos2:
        letters = pos2 - pos1 - 1
    else:
        letters = pos1 - pos2 - 1

print(f"Letters between Letter1 and Letter2: {letters}")
