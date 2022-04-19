"""5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква"""
LOWER_A_CODE = ord('a')
LOWER_Z_CODE = ord('z')

c = int(input("Введите номер символа ('a'=1, 'z'=26): "))

c = c + LOWER_A_CODE - 1

if LOWER_A_CODE <= c <= LOWER_Z_CODE:
    print(f"Вы указали код символа {chr(c)}")
else:
    print("Неверный ввод")
