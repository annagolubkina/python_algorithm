"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда,
делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""

from random import randint


def find_median(array):
    temp_array = array.copy()
    median_position = len(temp_array) // 2 + 1
    for i in range(median_position - 1):
        temp_array.remove(min(temp_array))
        print(temp_array)
    return min(temp_array)


num_array = [randint(-100, 100) for _ in range(21)]
print(num_array)
print('-' * 95)

array_median = find_median(num_array)
print(f'Медиана= {array_median}')