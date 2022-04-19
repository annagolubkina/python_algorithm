"""3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ."""

"a. cлучайное целое число"

from random import randint, uniform


data_in = input("Введите тип данных i(nteger)|f(loat)|c(haracters): ")
a = input("Введите начальное значение: ")
b = input("Введите конечное значение: ")

if data_in == 'i':
    r = randint(int(a), int(b))
elif data_in == 'f':
    r = uniform(float(a), float(b))
elif data_in == 'c':
    r = chr(randint(ord(a), ord(b)))
else:
    r = f"Неизвестный тип данных '{data_in}'"

print(f"Случайное значение в диапазоне от {a} до {b} = {r}")
