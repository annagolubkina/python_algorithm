"""Урок 2 задание 4. Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры."""
import cProfile

""" Вариант 1 """
def sum_series_1(n):
    a = 1
    summ = 0
    for _ in range(n):
        summ += a
        a /= -2
    return summ
# task_1.sum_series_1(3)       1000 loops, best of 5: 477 nsec per loop
# task_1.sum_series_1(30)      1000 loops, best of 5: 2.12 usec per loop
# task_1.sum_series_1(300)     1000 loops, best of 5: 17.8 usec per loop
# task_1.sum_series_1(3000)    1000 loops, best of 5: 198 usec per loop

# cProfile.run('sum_series_1(30000)')   1    0.002    0.002    0.002    0.002 task_1.py:6(sum_series_1)
# cProfile.run('sum_series_1(300000)')  1    0.021    0.021    0.021    0.021 task_1.py:6(sum_series_1)



""" Вариант 2 с рекурсией """

def sum_series_2(a, i, n, s): #a - перое число посл-ти, i -cчетчикб n- кол-во эл-в посл-ти s-сумма
    if i > n:
        return s
    else:
        if n == a:
            return a
        else:
            s += a
            a /= -2
        return sum_series_2(a, i + 1, n, s)
# task_1.sum_series_2(1,1,3,0)      1000 loops, best of 5: 697 nsec per loop
# task_1.sum_series_2(1,1,30,0)     1000 loops, best of 5: 6.38 usec per loop
# task_1.sum_series_2(1,1,300,0)    1000 loops, best of 5: 67.1 usec per loop
# task_1.sum_series_2(1,1,990,0)    1000 loops, best of 5: 261 usec per loop  макс. возможное кол-во эл-в из-за переполнения стека

# cProfile.run('sum_series_2(1,1,300,0)')     301/1    0.000    0.000    0.000    0.000 task_1.py:25(sum_series_2)
# cProfile.run('sum_series_2(1,1,990,0)')     991/1    0.001    0.000    0.001    0.001 task_1.py:25(sum_series_2)



""" Вариант 3 """
def sum_series_3(n):
    summ = 0
    for i in range(n):
        summ += 1 / pow(-2, i)
    return summ
# task_1.sum_series_3(3)        1000 loops, best of 5: 913 nsec per loop
# task_1.sum_series_3(30)       1000 loops, best of 5: 9.52 usec per loop
# task_1.sum_series_3(300)      1000 loops, best of 5: 168 usec per loop
# task_1.sum_series_3(3000)     1000 loops, best of 5: 4.46 msec per loop

#cProfile.run('sum_series_3(3000)')      1    0.001    0.001    0.005    0.005 task_1.py:47(sum_series_3)
#cProfile.run('sum_series_3(30000)')     1    0.007    0.007    1.066    1.066 task_1.py:47(sum_series_3)

""" Вариант 4 """

def sum_series_4(n):
    summ = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    return summ
# task_1.sum_series_4(3)        1000 loops, best of 5: 281 nsec per loop
# task_1.sum_series_4(30)       1000 loops, best of 5: 309 nsec per loop
# task_1.sum_series_4(300)      1000 loops, best of 5: 318 nsec per loop
# task_1.sum_series_4(3000)     1000 loops, best of 5: 336 nsec per loop

#cProfile.run('sum_series_4(30000)')     1    0.000    0.000    0.000    0.000 task_1.py:62(sum_series_4)
#cProfile.run('sum_series_4(300000)')    1    0.000    0.000    0.000    0.000 task_1.py:62(sum_series_4)

"""Алгоритм с рекурскией оказался медленее изначального варианта,
 худший результат показал алгорим с использованием функции pow. Все алгоритмы имееют линейную сложность.
Алгоритм с перемнной оказался быстрее моего начального варианта, 
 и можно сказать что он имеет практически незначительную линейную сложность
 (думаю здесь связь с лишними переменными, которые  в последнем варинате отуствуют """