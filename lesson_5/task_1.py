# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
#    для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования
#    предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import defaultdict, deque, namedtuple

QUARTERS = 4


def avg(col):
    if not col:
        return 0
    sum = 0
    for value in col:
        sum += value
    return sum / len(col)


Company = namedtuple('Company', 'name, quarter_profits')

companies = deque()

count = int(input('Количество предприятий: '))
print()

avg_profit = 0.0
for i in range(count):
    print(f'Предприятие {i + 1}:')
    name = input('  Имя: ')
    print('  Прибыль:')
    quarter_profits = tuple([float(input(f'    {j + 1}-й квартал: ')) for j in range(QUARTERS)])
    company = Company(name, quarter_profits)
    companies.append(company)
    avg_profit += quarter_profits[0]
    avg_profit += quarter_profits[1]
    avg_profit += quarter_profits[2]
    avg_profit += quarter_profits[3]
    print()

avg_profit /= count
print(f'Средняя прибыль: {avg_profit}\n')

greater = defaultdict(float)
less = defaultdict(float)

for company in companies:
    qrt_prfs = company.quarter_profits
    total_profit = qrt_prfs[0] + qrt_prfs[1] + qrt_prfs[2] + qrt_prfs[3]
    if total_profit > avg_profit:
        greater[company] = total_profit
    elif total_profit < avg_profit:
        less[company] = total_profit

print('Больше среднего:')
for company, total_profit in greater.items():
    print(f'  {company.name:10}: {total_profit:10.1f}')

print()

print('Меньше среднего:')
for company, total_profit in less.items():
    print(f'  {company.name:10}: {total_profit:10.1f}')
