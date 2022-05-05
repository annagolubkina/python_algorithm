"""Урок 3 задача 5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве."""

# Тесты выполнены на macOS-11.4-x86_64-i386-64bit
# Версия Python 3.8.2

import random
import sys
from count_size import count_size

def var_sum(var_lst):
    summa = 0
    for i in var_lst:
        summa += count_size(i)
    print(f'Под переменные задействованно {summa} байт памяти, количество переменных {len(var_lst)}')


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
    # return max_el
    return var_sum([lst_len, my_list, neg_list, i, item, max_el, idx])
arr_max_min_1(10)


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
        # return array[index]
        return var_sum([lst_len, array, SIZE, i, index])
arr_max_min_2(10)

#  Третий вариант
def arr_max_min_3(lst_len):
    array = [random.randint(-1000, -800) for _ in range(lst_len)]
    num = float('-inf')
    index = -1

    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i

    if index != -1:
        num = num
    return var_sum([lst_len, array, num, i, item, index])
arr_max_min_3(10)

""" Самым оптимальным по выделенной памяти является вариант кода № 2 (576 байт памяти, 
так как использован 1 список- array и 4 переменные типа int )). 
Вариант кода №3 отличается от варианта кода № 1, добавлением еще одной переменной типа int 
и соответсвенно увеличением выделенной памяти на 28 байт
В варианте кода № 1 выделено больше всего памяти (1068 байт),
так как использовано 2 списка my_list и neg_list, остальные 5 переменных типа int .
"""

