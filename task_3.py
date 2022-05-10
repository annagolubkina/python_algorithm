"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

arr = [random.randint(-5,5) for _ in range(10)]
print(arr)
min_el = 0
max_el = 0
for i, item in enumerate(arr):
    if item < min_el:
        min_el = item
        min_idx = i
    else:
        if item > max_el:
            max_el = item
            max_idx = i
arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]
print(f'минимальный элемент {min_el} с индексом {min_idx}')
print(f'максимальный элемент {max_el} с индексом {max_idx}')
print(f'Массив со сменой мест минимального и максимального элементов {arr}')