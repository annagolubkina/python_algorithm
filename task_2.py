"""В диапазоне натуральных чисел от 2 до 99 определить,сколько из них кратны каждому из чисел в диапазонеот 2 до 9."""
import cProfile
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

    return (div_two, div_three, div_four, div_five, div_six, div_seven, div_eight, div_nine)

# task_2 count_div_1(99)      1000 loops, best of 5: 24.1 usec per loop
# task_2 count_div_1(999)     1000 loops, best of 5: 258 usec per loop
# task_2 count_div_1(9999)    1000 loops, best of 5: 2.89 msec per loop
# task_2 count_div_1(99999)   1000 loops, best of 5: 28.9 msec per loop

# cProfile.run('count_div_1(9999)')       1    0.003    0.003    0.003    0.003 task_2.py:3(count_div_1)
# cProfile.run('count_div_1(99999)')      1    0.033    0.033    0.033    0.033 task_2.py:3(count_div_1)

min_div = 2
max_div = 9

def count_div_2(max_number):
    div_dict = dict()

    for div in range(min_div, max_div + 1):
        div_dict[div] = max_number // div

    return div_dict

# task_2 count_div_2(99)        1000 loops, best of 5: 825 nsec per loop
# task_2 count_div_2(999)       1000 loops, best of 5: 910 nsec per loop
# task_2 count_div_2(9999)      1000 loops, best of 5: 936 nsec per loop
# task_2 count_div_2(99999)     1000 loops, best of 5: 952 nsec per loop

# cProfile.run('count_div_2(9999)')   1    0.000    0.000    0.000    0.000 task_2.py:33(count_div_2)
# cProfile.run('count_div_2(99999)')  1    0.000    0.000    0.000    0.000 task_2.py:33(count_div_2)

def count_div_3(max_number):
    div_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(2, max_number + 1):

        if num % 2 == 0:
            div_dict[2] += 1

        if num % 3 == 0:
            div_dict[3] += 1

        if num % 4 == 0:
            div_dict[4] += 1

        if num % 5 == 0:
            div_dict[5] += 1

        if num % 6 == 0:
            div_dict[6] += 1

        if num % 7 == 0:
            div_dict[7] += 1

        if num % 8 == 0:
            div_dict[8] += 1

        if num % 9 == 0:
            div_dict[9] += 1

    return div_dict

# task_2 count_div_3(99)        1000 loops, best of 5: 36.2 usec per loop
# task_2 count_div_3(999)       1000 loops, best of 5: 381 usec per loop
# task_2 count_div_3(9999)      1000 loops, best of 5: 3.95 msec per loop
# task_2 count_div_3(99999)     1000 loops, best of 5: 40.8 msec per loop

# cProfile.run('count_div_3(999)')        1    0.000    0.000    0.000    0.000 task_2.py:49(count_div_3)
# cProfile.run('count_div_3(9999)')       1    0.004    0.004    0.004    0.004 task_2.py:49(count_div_3)

"""Первый и третий алгоритм работают приблизительно одинаково за O(n), 
так как за каждый запуск при увеличении количества элдемнтов в 10 раз, во только же раз увеличивается и время выполнения
Второй алгоритм обладает сложностью O(1), так как при увеличении количества элементов в 10 раз,
 время выполнения увеличивается незначительно"""