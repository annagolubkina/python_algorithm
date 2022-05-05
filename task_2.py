"""Урок 2 задание 4. Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры."""

# Тесты выполнены на macOS-11.4-x86_64-i386-64bit
# Версия Python 3.8.2


from count_size import count_size

def var_sum(var_lst):
    summa = 0
    for i in var_lst:
        summa += count_size(i)
    print(f'Под переменные задействованно {summa} байт памяти, количество переменных {len(var_lst)}')

""" Вариант 1 """
def sum_series_1(n):
    a = 1
    summ = 0
    for _ in range(n):
        summ += a
        a /= -2
    # return summ
    return(var_sum([n, a, summ, _ ]))

sum_series_1(4)

""" Вариант 2 с рекурсией """

def sum_series_2(a, i, n, s): #a - перое число посл-ти, i -cчетчикб n- кол-во эл-в посл-ти s-суммы
    if i > n:
        return (var_sum([a, i, n, s]))
    else:
        if n == a:
            return a
        else:
            s += a
            a /= -2
        return sum_series_2(a, i + 1, n, s)
sum_series_2(1, 1, 4, 0)


""" Вариант 3 """
def sum_series_3(n):
    summ = 0
    for i in range(n):
        summ += 1 / pow(-2, i)
    # return summ
    return (var_sum([n, summ, i,]))

sum_series_3(4)

""" Вариант 4 """

def sum_series_4(n):
    summ = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    # return summ
    return (var_sum([n, summ]))

sum_series_4(4)

""" Самым оптимальным по выделенной памяти является вариант кода № 4 (52 байта памяти, так как использованы 2 переменные типов int и float). 
В вариант кода № 1 и № 2 объем выделенной памяти одинаков, так как количество и тип переменных  одинаковый.
При оптимизации варианта кода № 2 можно уменьшить количество переменных и получить меньший объем выделенной памяти 
В варианте кода №3 3 переменные (2 типа int  и 1 переменная float)."""