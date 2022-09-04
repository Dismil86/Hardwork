import gettext
# s = 'hello'
# n = len(s)
# a = s[:int((n + 1) / 2)]#Деление строки пополам,если нечетная то большая часть строки
# b = s[int((n + 1) / 2):n]# Вторая часть строки
# print(a)
# print(b)
# print(f'{b + a}')

# s = input()
# print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])
# print(help(str),sep='/n')

# s = ['hello,', 'world']  # Объединение строк в одну
# print(''.join([s[0], s[1]]))
from gettext import find

# a = "Hello, World!"
# b = a.find(' '[:])  # Поиск индекса первого найденного введенного символа в строке(" ") str.find(sub[, start[, end]])
# print(b)
# print(a[b + 1:], a[:b])
# s = input() # Проверяет вхождение в список подстроки вывод его индекса с левой стороны или справой
# n = s.count('f')
# if  n == 1:
#      print(s.find('f'))
# if n > 1:
#     print(s.find('f'),s.rfind('f'))
###############################################################################
# Ввод данных от пользователя:
# print(*reversed([input() for _ in range(3)]), sep='\n')# Создание списка и распаковка в обратном порядке эл-ов списка
# print('\n'.join([input() for i in '123'][::-1]))# присоединение "\n" к каждому вводу строки списка в обратном порядке
# print(*[input() for _ in range(3)][::-1], sep='\n') # распаковка элементов списка в обратном направлении
s = [int(i) for i in input().split()]
print(f"{sum(s)} / {len(s)} = ")
