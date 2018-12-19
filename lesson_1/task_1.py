# Начало
# Вывод("Введите трёхзначное число")
# Ввод(Число)
#
# a = value // 100
# b = value // 10 % 10
# c = value % 10
#
# sum = a + b + c
# product = a * b * c
#
# Вывод("Sum = ", sum)
# Вывод("Product = ", product)
# Конец

value = int(input(('Введите трёхзначное число: ')))

a = value // 100
b = value // 10 % 10
c = value % 10

sum = a + b + c
product = a * b * c

print(f'Sum = {sum}')
print(f'Product = {product}')
