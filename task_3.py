head = ''
rev = ''

num = input('Введите натуральное число: ')

if num.startswith('0'):
    head = '0'
num = int(num)

while True:
    rev += str(num % 10)
    num //= 10

    if num == 0:
        break

print(f'Число обратное по порядку цифр= {rev + head}')
