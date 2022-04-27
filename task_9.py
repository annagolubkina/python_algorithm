"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
import random
m = 5
n = 4
a = []
min_list = []

for i in range(n):
    b = []
    for j in range(m):
        n = random.randint(-10, 10)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

for j in range(m):
    min_el = a[0][j]
    for i in range(n):
        if a[i][j] < min_el:
            min_el = a[i][j]
    min_list.append(min_el)

max_el  = min_list[0]
for idx in range(0, len(min_list)):
    if min_list[idx] > max_el:
            max_el = min_list[idx+1]

print(f'минимальные элементы столбцов матрицы:  {min_list}')
print(f'максимальный среди минимальных:  {max_el}')

