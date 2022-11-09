# print(f'Start modul module is {__nam__}'
import os
import time

spisok = []
for adress, dir, files in os.walk(r"F:\Учебный материал\Python"):  # выборка по адрессам, каталогам и файлам
    # в указанном каталоге
    for name in files:
        full = os.path.join(adress, name)
        if time.time() - os.path.getctime(full) < 604800:  # Условие: файлы созданные не позже недели назад(в секундах)
            spisok.append(full)

print(spisok)
file = open(r"F:\Учебный материал\Python\fileTest1.txt", 'w')  # создаем и открывам файл в path
for x in spisok:
    file.write(x + '\n')  # Записываем в файл все стороки списка адресса и названия файлов
file.close()
