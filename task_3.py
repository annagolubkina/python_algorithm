"""5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве."""
import random
import cProfile

def arr_max_min_1(lst_len):
    my_list = [random.randint(-1000, -800) for _ in range(lst_len)]
    neg_list = []


    for i, item in enumerate(my_list):
        if item < 0:
            neg_list.append(item)

    max_el = neg_list[0]
    for idx in range(1, len(neg_list)):
        if neg_list[idx] > max_el:
            max_el = neg_list[idx]
    return max_el

# task_3.arr_max_min_1(10)      1000 loops, best of 5: 8.97 usec per loop
# task_3.arr_max_min_1(100)     1000 loops, best of 5: 81.9 usec per loop
# task_3.arr_max_min_1(1000)    1000 loops, best of 5: 846 usec per loop
# task_3.arr_max_min_1(10000)   1000 loops, best of 5: 9.04 msec per loop

# cProfile.run('arr_max_min_1(10000)')        1    0.002    0.002    0.015    0.015 task_3.py:6(arr_max_min_1)
# cProfile.run('arr_max_min_1(100000)')       1    0.018    0.018    0.147    0.147 task_3.py:6(arr_max_min_1)

"""Второй вариант"""
def arr_max_min_2(lst_len):
    array = [random.randint(-1000, -800) for _ in range(lst_len)]
    SIZE = len(array)
    i = 0
    index = -1

    while i < SIZE:
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        return array[index]

# task_3.arr_max_min_2(10)      1000 loops, best of 5: 9.05 usec per loop
# task_3.arr_max_min_2(100)     1000 loops, best of 5: 82.8 usec per loop
# task_3.arr_max_min_2(1000)    1000 loops, best of 5: 825 usec per loop
# task_3.arr_max_min_2(10000)   1000 loops, best of 5: 8.64 msec per loop

#cProfile.run('arr_max_min_2(10000)')        1    0.002    0.002    0.015    0.015 task_3.py:26(arr_max_min_2)
#cProfile.run('arr_max_min_2(100000)')       1    0.017    0.017    0.140    0.140 task_3.py:26(arr_max_min_2)

# # Третий вариант
def arr_max_min_3(lst_len):
    array = [random.randint(-1000, -800) for _ in range(lst_len)]
    num = float('-inf')
    index = -1

    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i

    if index != -1:
        return num


#cProfile.run('arr_max_min_3(10000)')        1    0.001    0.001    0.014    0.014 task_3.py:51(arr_max_min_3)
#cProfile.run('arr_max_min_3(100000)')       1    0.008    0.008    0.136    0.136 task_3.py:51(arr_max_min_3)

# task_3.arr_max_min_3(10)      1000 loops, best of 5: 8.2 usec per loop
# task_3.arr_max_min_3(100)     1000 loops, best of 5: 75.7 usec per loop
# task_3.arr_max_min_3(1000)    1000 loops, best of 5: 790 usec per loop
# task_3.arr_max_min_3(10000)   1000 loops, best of 5: 8.12 msec per loop"""

""""Основное время выполнения занимает генерация списка с генерацией чисел
Все алгоритмы дают схожие результаты. Возможно время выполненеия можно сократить, 
если вынести генерацию массива в отдельную фунцию"""