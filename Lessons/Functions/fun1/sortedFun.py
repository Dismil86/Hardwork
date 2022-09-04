# from fileinput import filename
#
#
# def f(x):
#     return x % 10, x // 10 % 10
#
#
# def g(x):
#     return (x % 10)
#
#
# a = [4, -2, 45, -432, 64, -342, 215, -1, 4, 0, 744, 23, -345]
#
# b = ['zzz 75', 'ZZZ 290', 'aaa 290', 'eee 23','sss 899', 'DDD 111', 'www 899', 'BBB 777']
#
# # Аргументы key в сортировке
#
# print(1,sorted(a, key=abs))  # встроенная функция в качестве аргумента
#
# print(2,sorted(a, key=f))  # Собственная функция
# print(3,sorted(b))
# print(4,sorted(b, key=lambda x: int(x.split()[1])  )) # Сортировка по значению числа в строке
# print(5,sorted(b, key=lambda x: (int(x.split()[1]), x.split()[0])  )) # Теперь в аргументе функции Lambda x это кортэж
#                                                 # и теперь сортируем по двум элементам
# print(6,sorted(b, key=lambda x: (int(x.split()[1]), x.split()[0].lower()) )) # Сортрировка по числам и по буквам в стр.
#
# print(7,sorted(b, key=lambda x: (x.split()[0].lower(), int(x.split()[1])) )) # Сортировка по буквам в нижнем регистре
                                                           # и по числам

