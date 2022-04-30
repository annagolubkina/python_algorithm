"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
 Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
  Проанализировать скорость и сложность алгоритмов"""
import cProfile


""" Вариант 1. c решетом Эратосфена."""
def sieve_1(n):

    num = 10
    sieve = [i for i in range(num)]
    sieve[1] = 0
    res_lst = []

    while len(res_lst) < n:

        for i in range(2, len(sieve)):

            if sieve[i] != 0:

                j = i + i

                while j < len(sieve):
                    sieve[j] = 0
                    j += i

        res_lst = [i for i in sieve if i != 0]
        add_arr = [i for i in range(num, 2*num)]
        num *= 2
        sieve = sieve + add_arr

    return res_lst [n-1]

# task_4.sieve_1(10)        100 loops, best of 5: 20.2 usec per loop
# task_4.sieve_1(100)       100 loops, best of 5: 403 usec per loop
# task_4.sieve_1(1000)      100 loops, best of 5: 7.61 msec per loop

# cProfile.run('sieve_1(100)')        1    0.000    0.000    0.001    0.001 task_4.py:8(sieve_1)
# cProfile.run('sieve_1(1000)')       1    0.008    0.008    0.012    0.012 task_4.py:8(sieve_1)
# cProfile.run('sieve_1(10000)')      1    0.154    0.154    0.218    0.218 task_4.py:8(sieve_1)

def sieve_2(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number

# task_4.sieve_2(10)        100 loops, best of 5: 4.42 usec per loop
# task_4.sieve_2(100)       100 loops, best of 5: 232 usec per loop
# task_4.sieve_2(1000)       100 loops, best of 5: 23.6 msec per loop

# cProfile.run('sieve_2(100)')    1    0.000    0.000    0.000    0.000 task_4.py:22(sieve_2)
# cProfile.run('sieve_2(1000)')   1    0.026    0.026    0.026    0.026 task_4.py:22(sieve_2)
# cProfile.run('sieve_2(10000)')  1    2.690    2.690    2.691    2.691 task_4.py:22(sieve_2)

""" Сложность второго алгоритма близка к O(n**2), второй алгоритм схож по времени выполнения с первым. 
 Однако при возрастании n алготрим с использованием решета Эрастофена, начинает показывать лучшие результаты: 
  скорость выполнения становится меньше в 3 раза"""