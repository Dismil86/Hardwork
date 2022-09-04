# Основные моменты:
# 1) все компсы и генэксп работают по принципу
# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# читается это слева направо, что важно когда циклов больше 1.
# 2) принцип работы операций у листкомпс и генэксп одинаков, синтаксически различаются скобками
# 3) компсы (листкомпс, сеткомпс, дикткомпс) в результате своей работы формируют соответствующую коллекцию и занимают
# память
# 4) переменные созданные внутри компсов или генэкспа недоступны извне
# 5) генэксп вернет объект, а не коллекцию! при создании объекта он проверит источник, что может быть критично,
# если это какая то функция. Если источник не валидный то ошибка упадет при создании генератора,
# а не при попытке получить значение
# 6) генэксп ленивый, то есть ничего не делает и не занимает память пока не потребуется значение.
# Сгенерировав значение снова засыпает пока опять не попросят новое.
# 7) генэксп одноразовый, при исчерпании начинает бросать исключение, которое мы не увидим,
# если используем генератор в цикле for
# 8) генэксп может потенциально генерировать бесконечные последовательности,
# но он ничего не знает о порядке элементов или о их количестве (нет len)
import pprint
print(f'Start modul module is {__name__}')
import random
n = 4
m = 6
a = [random.randint(1,9) for i in range(m)]
 # генератор случайных m = 5 элементов списка в пределах от 1 до 10
 # print(a)
b = [[random.randint(1, 9) for i in range(m)] for j in range(n)]
 # в качестве элемента списка создаем список из n = 4 случайных элементов от 1 до 10 в колличестве m = 5 раз.
# for i in b:  # перебераем каждый элемент списка
#     print(i)
# c = [b[i][j] for i in range(m) for j in range(n) if i == j]
# d = [b[i][1] for i in range(n)]
# g = [b[1][j] for j in range(m)]
# print(c,'find diagonal')
# print(d,'find column')
# print(g,'find string')
# a = ['hello', 'world']
# b = [i[::-1] for i in a]
# print(a)
# print(b)
# print(a)
# s = [int(i) for i in iter(input,'')]  # Ввод чисел от пользователя
# x = list(map(int,input().split()))
# print(s,x)
# # for i in range(int(input())):  # Генератор ввода пользователем
# #     print(i)
#
# text = "hello world"
# words = [word.capitalize() for word in text.split()] #Создаем новый список из строки,разделяя строку на отдельнгые слова
# print(words)
# letters = [letter for word in text.split() for letter in word if letter > 'o'] # Двойный цикл для обращение элементов
#                                                                              #строк в словаре
# print(letters)
#
# uniq_letters = {letter for word in text.split() for letter in word if letter > 'e'} # генератор множества
# print(uniq_letters)
#
# if __name__ == '__main__':
#     matrix = [list(range(x, x + 4)) for x in range(4)] # генератор матрицы
#     pprint.pprint(matrix, indent=1, width=15)

#
# print("Введите список игроков,через запятую, короторые выходят в стартовом составе по окончании введите 'q' : ")
# words = [word for word in iter(input,'q')]
# print(words)