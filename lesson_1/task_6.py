# Начало
# Вывод "Введите номер буквы: "
# Ввод number
# ord_a = ord('a')
# ord_letter = ord_a + number
# letter = chr(ord_letter - 1)
# Вывод letter
# Конец

number = int(input("Номер буквы: "))
ord_a = ord('a')
ord_letter = ord_a + number
letter = chr(ord_letter - 1)
print(f'Letter: {letter}')
