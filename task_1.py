"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple


Companies = namedtuple('Companies', 'name quarter_1 quarter_2 quarter_3 quarter_4 year')

companies_n = int(input('Введите количество предприятий для анализа: '))
enterprises = [0 for _ in range(companies_n)]
profit_sum = 0
less_avg = []
more_avg = []

for i in range(companies_n):
    name = input(f'Введите название {i+1}-го предприятия: ')
    quarters = [float(j) for j in input('Введите через пробел прибыль в каждом квартале: ').split()]

    year = 0
    for quarter in quarters:
        year += quarter

    profit_sum += year
    enterprises[i] = Companies(name, *quarters, year)
    # print(enterprises[i])

profit_average = profit_sum / companies_n


for i in range(companies_n):

    if enterprises[i].year < profit_average:
            less_avg.append(enterprises[i])

    elif enterprises[i].year > profit_average:
            more_avg.append(enterprises[i])

print(f'\nсредняя годовая прибыль по предприятиям: {profit_average: .2f}')

print(f'предприятия, чья прибыль меньше {profit_average: .2f}:')

for company in less_avg:
    print(f'предприятие "{company.name}" с прибылью {company.year: .2f}')

print(f'\nпредприятия, чья прибыль больше {profit_average: .2f}:')

for company in more_avg:
        print(f'предприятие "{company.name}" с прибылью {company.year: .2f}')