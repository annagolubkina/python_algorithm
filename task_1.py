"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

import random
import cProfile
from random import shuffle


def lesson_bubble(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  
        n += 1
    return array

# Мой вариант

def my_bubble(num_array):
    n = 1
    array_1 = []
    array_2 = []
    avg_num = sum(num_array) / len(num_array)

    for num in num_array:
        if num >= avg_num:
            array_2.append(num)
        else:
            array_1.append(num)

    while n < (len(array_1) - 1):
        for i in range(len(array_1) - n):
            if array_1[i] > array_1[i + 1]:
                array_1[i], array_1[i + 1] = array_1[i + 1], array_1[i]
            if array_2[i] > array_2[i + 1]:
                array_2[i], array_2[i + 1] = array_2[i + 1], array_2[i]
        n += 1

    return array_1 + array_2



array = [num for num in range(-100, 100)]
shuffle(array)
print(array)




# print(lesson_bubble(array))
# cProfile.run('lesson_bubble(array)')


# print(my_bubble(array))

cProfile.run('my_bubble(array)')

"""
Вариант функции разобраный на лекции: 

    403 function calls in 0.002 seconds
 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.003    0.003    0.003    0.003 task_1.py:11(lesson_bubble)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      399    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
"task_1.lesson_bubble([-28, 67, 55, 53, -17, 20, 78, 77, -40, 60, 79, 28, -13, -91, 57, -44, 29, 56, 37, 91, -41, 1, 66, 
62, -19, -73, -22, -15, -20, 26, -45, 93, -36, -27, -70, 46, 83, 89, 95, -85, -75, 96, -18, 0, 75, -87, -1, 41, 81, 10, 
-88, 49, 25, -39, -86, 74, -72, -34, -92, 12, 59, -94, -5, -97, 52, -37, -25, 99, 70, 23, -42, 43, 97, -6, -68, 73, -10,
32, 45, -57, -80, 9, -95, -65, -82, -98, -76, -77, 13, 71, 80, -81, 63, 85, 17, -21, 30, 68, 2, -54, -56, 87, -9, 38, 
47, 82, -48, -47, 48, -3, -30, 61, 5, 51, 50, 11, -29, -66, -4, -11, -23, 92, -64, 54, 27, -93, 6, 33, 4, -55, -96,
24, 44, -2, 18, -83, -61, -49, 21, -31, 98, -43, -63, 36, -89, -50, -84, 84, -99, 86, 14, 90, -46, 22, 31, 58, 34, -69, 
35, -58, -33, -32, 8, -71, -78, 65, -35, 42, -52, -90, 64, 72, -51, -67, -14, 16, 88, -16, -26, 39, -59, -7, -8, -12, 
76, 3, -60, 7, -62, -53, -24, 94, 40, -100, -79, -74, 69, 19, -38, 15])"
1000 loops, best of 5: 2.85 msec per loop

 Мой вариант    
 
    
 403 function calls in 0.001 seconds
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_1.py:22(my_bubble)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      198    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
      200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 
"task_1.my_bubble([-28, 67, 55, 53, -17, 20, 78, 77, -40, 60, 79, 28, -13, -91, 57, -44, 29, 56, 37, 91, 
-41, 1, 66, 62, -19, -73, -22, -15, -20, 26, -45, 93, -36, -27, -70, 46, 83, 89, 95, -85, -75, 96, -18, 0, 75, -87, -1, 
41, 81, 10, -88, 49, 25, -39, -86, 74, -72, -34, -92, 12, 59, -94, -5, -97, 52, -37, -25, 99, 70, 23, -42, 43, 97, -6, 
-68, 73, -10, 32, 45, -57, -80, 9, -95, -65, -82, -98, -76, -77, 13, 71, 80, -81, 63, 85, 17, -21, 30, 68, 2, -54, -56, 
87, -9, 38, 47, 82, -48, -47, 48, -3, -30, 61, 5, 51, 50, 11, -29, -66, -4, -11, -23, 92, -64, 54, 27, -93, 6, 33, 4,
-55, -96, 24, 44, -2, 18, -83, -61, -49, 21, -31, 98, -43, -63, 36, -89, -50, -84, 84, -99, 86, 14, 90, -46, 22, 31, 
58, 34, -69, 35, -58, -33, -32, 8, -71, -78, 65, -35, 42, -52, -90, 64, 72, -51, -67, -14, 16, 88, -16, -26, 39, -59, 
-7, -8, -12, 76, 3, -60, 7, -62, -53, -24, 94, 40, -100, -79, -74, 69, 19, -38, 15])"
1000 loops, best of 5: 1.4 msec per loop
 """
"""Проведенный анализ показывает, что по сравнению с сортировкой пузырьком lesson_bubble (реализованной на лекции),
предложенный мной оптимизированный вариант показывает результат в 2 раза быстрее """