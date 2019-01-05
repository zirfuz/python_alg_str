# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#    Например, если введено число 3486, то надо вывести число 6843.

value = int(input('Value: '))
result = 0

while True:
    result = (result * 10) + (value % 10)
    value //= 10
    if value == 0:
        break

print(f'Result: {result}')
