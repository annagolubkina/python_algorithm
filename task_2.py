num = int(input('Введите натуральное число:'))
i = 0
j = 0
while True:
    if num % 10 % 2:
        j += 1
    else:
        i += 1
    num //= 10
    if not num:
        break
print(f'В веденном числе четных чисел {i}, нечетных чисел {j}')


