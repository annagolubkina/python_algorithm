"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать."""
import random

arr = [random.randint(-5,5) for _ in range(10)]
print(arr)
min_el = 0
max_el = 0
sum = 0
for i, item in enumerate(arr):
    if item < min_el:
        min_el = item
        min_idx = i
    else:
        if item > max_el:
            max_el = item
            max_idx = i
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx
for i, item in enumerate(arr[(min_idx+1):max_idx]):
        sum = sum + item
print(f'индекс минимального элемента= {min_idx},индекс максимального элемента= {max_idx}')
print(f'Сумма элементов находящихся между минимальным и максимальным элементами = {sum}')
