# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple, defaultdict

Profit = namedtuple('Profit', ['name', 'kvart1', 'kvart2', 'kvart3', 'kvart4'])
n = int(input('Сколько компаний: '))

profits = [Profit(input(f'Название {i} компании: '),
                  float(input('Прибыль за 1 квартал: ')),
                  float(input('Прибыль за 2 квартал: ')),
                  float(input('Прибыль за 3 квартал: ')),
                  float(input('Прибыль за 4 квартал: '))
                  ) for i in range(n)]

averages = defaultdict(float)
general_profit = 0
for company in profits:
    sum_income = sum([company[i] for i in range(1, 5)])
    general_profit += sum_income
    averages[company.name] = sum_income / 4
general_mean_profit = general_profit / (n * 4)

print(f'Общее среднее: {general_mean_profit}')
print(f'Выше среднего: {[key for key in averages.keys() if averages[key] > general_mean_profit]}')
print(f'Ниже среднего: {[key for key in averages.keys() if averages[key] < general_mean_profit]}')







