"""4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв."""

LOWER_A_CODE = ord('a')
LOWER_Z_CODE = ord('z')

k = input("Введите первый символ от 'a' до 'z': ")
j = input("Введите второй символ от 'a' до 'z': ")

code_k = ord(k)
code_j = ord(j)

if (code_k < code_j
        and LOWER_A_CODE <= code_k <= LOWER_Z_CODE
        and LOWER_A_CODE <= code_j <= LOWER_Z_CODE):
    poz_k = code_k - LOWER_A_CODE + 1
    poz_j = code_j - LOWER_A_CODE + 1
    print(f"Позиция '{k}' = {poz_k}, позиция '{j}' = {poz_j}, букв между ними: {poz_j - poz_k - 1}")
else:
    print("Неверный ввод")
