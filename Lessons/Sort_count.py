# Сортировка подсчётом( counting sort ) — алгоритм сортировки, в котором используется диапазон чисел сортируемого массива
# (списка) для подсчёта совпадающих элементов. Применение сортировки подсчётом целесообразно лишь тогда,
# когда сортируемые числа имеют диапазон возможных значений,
# который достаточно мал по сравнению с сортируемым множеством.
#
# Идея сортировки: подсчитываем сколько раз в массиве встречается каждое значение и
# заполняем массив подсчитанными элементами в соответствующих количествах.
a = [2,2,3,5,2,4,2,7,8,3,1,0,9,7,1,4,]
count = [0] * 10
for i in a:
    count[i] += 1
print(count) # Подсчет колличества элеметов коллекции и вывод подчета в список
for i in range(10):
    if count[i] > 0:
        print((str(i) + ' ') * count[i],end="") # отображение элементов коллекции умноженное на их колличетво в списке

s = "abc83kl jfkj shihr3-p=9==-=-l;']=--?JJ3-o0]]03401>:{}"
letters = [0] * 26
for i in s.lower():
    if i >= 'a' and i <= 'z':  #  Отбор из строки только букв латиницы
        nomer = ord(i) - 97
        letters[nomer] += 1

for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97) * letters[i],end='')



