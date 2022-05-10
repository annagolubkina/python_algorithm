"""2. Во втором массиве сохранить индексы четных элементов первого массива. """
import random

arr = [random.randint(0,20) for _ in range(10)]
# arr = [8, 3, 15, 6, 4, 2]
arr_new = []
for i, item in enumerate(arr):
    if item % 2 == 0:
        arr_new.append(i)
print(f'исходный массив:{arr}')
print(f'массив индексов четных элементов:{arr_new}')