"""Урок 3 задача 1
В диапазоне натуральных чисел от 2 до 99 определить,сколько из них кратны каждому из чисел в диапазонеот 2 до 9."""

# Тесты выполнены на macOS-11.4-x86_64-i386-64bit
# Версия Python 3.8.2
from count_size import count_size

def var_sum(var_lst):
    summa = 0
    for i in var_lst:
        summa += count_size(i)
    print(f'Под переменные задействованно {summa} байт памяти, количество переменных {len(var_lst)}')


def count_div_1(n):
    arr = list(range(2, n + 1))

    div_two = div_three = div_four = div_five = div_six = div_seven = div_eight = div_nine = 0

    for item in arr:
        if not item % 2:
            div_two += 1
        if not item % 3:
            div_three += 1
        if not item % 4:
            div_four += 1
        if not item % 5:
            div_five += 1
        if not item % 6:
            div_six += 1
        if not item % 7:
            div_seven += 1
        if not item % 8:
            div_eight += 1
        if not item % 9:
            div_nine += 1

    # return (div_two, div_three, div_four, div_five, div_six, div_seven, div_eight, div_nine)
    return var_sum([div_two, div_three, div_four, div_five, div_six, div_seven, div_eight, div_nine, arr, item, n])

count_div_1(99)

min_div = 2
max_div = 9

def count_div_2(max_number):
    div_dict = dict()

    for div in range(min_div, max_div + 1):
        div_dict[div] = max_number // div

    # return div_dict
    return var_sum([div, div_dict, max_number])
count_div_2(99)

"""Данный вариант оптимизирован и отличен от кода, что представлен в ДЗ 4 """
def count_div_3(max_number):
    div_dict = dict()

    for div in range(min_div, max_div + 1):
        div_dict[div] = 0

        for num in range(2, max_number + 1):

            if num % div == 0:
                div_dict[div] += 1
    # return div_dict
    return var_sum([div, div_dict, max_number,num])
count_div_3(99)

""" Самым оптимальным по выделенной памяти является вариант кода № 2 (864 байта памяти,
так как использованы 2 переменные типa  int и словарь). 
В варианте кода № 3 объем выделенной памяти  отличен от варианта № 2 на 28 байт,
ввиду использования еще одной переменной типа int.
Вариант кода № 1 требует наибольший объем выделяемой памяти (3864 байта) за счет большого количества переменных
"""

