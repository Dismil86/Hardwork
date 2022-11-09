import os

# file = open('StudyPlan.txt', encoding='utf-8')
# print(file.read(10))# считывать файл(кол-во символов-объем памяти.которое необходимо прочитать)
# file.seek(0) # Перевод каретки в начальное положение.
# print(file.readline()) # Считывать строку файла
# s = file.readlines() # Создание списка из с трок файла
# for row in file: # обход файла по строкам и вывод этих строк
#     print(row)
# file.close() # закрытие файла
# file = open('StudyPlan.txt', 'a+', encoding='utf-8')
# file.write('Я изучаю  Python! Боль и слезы.\nНет личной жизни.\nПомогите!!!')
# print(file.close(),'закрываю файл')
# file = open('StudyPlan.txt', encoding='utf-8')
# print(file.read())
# file.seek(0)
# for row in file:
#     print(row)
# file.close
# print(file.read())
# file = open('StudyPlan.txt','w', encoding='utf-8') # Запись в файл
# file.write('hi\n')
# file.write('hello\n')
# file.write('world\n')
# # file.close()
# list_path = []
# a = os.walk("F:\Учебный материал\Python") # Функция walk Функция walk() возвращает объект-генератор,
# из которого получают кортежи. Каждый кортеж "описывает" очередной каталог из переданного в функцию дерева каталогов.
# Каждый кортеж состоит из трех элементов:
#
# Адрес очередного каталога в виде строки.
# Список имен подкаталогов первого уровня вложенности в данный каталог. Если вложенных каталогов нет, список будет пустым.
# Список имен файлов первого уровня вложенности в данный каталог. Если вложенных файлов нет, список будет пустым.
# print(a) # Функция walk вернуло объект генератор,извлечь данные из которого можно один раз!!!!
# for adress, dirs, files in a:
#     for name in files:
#         full = os.path.join(adress, name) # соединяем адресса файлов с их именами
#         list_path.append(full)# Добавляем в список адреса и имена файлов в виде строк
# print(list_path)
# file = open(r"F:\Учебный материал\Python\fileTest.txt", 'w') # открываем файл,поскольку открываем в режиме
#                                                              # "w" создаем его
# for x in list_path:
#     file.write(x + '\n') #Записываем в файл все стороки списка адресса и названия файлов
# file.close()


# Пример чтения из файла:
# with open("somefile.txt", "r") as f:
# f. read ()
# # Побайтное чтение
# f = open("file.txt", "r")
# f. read ( 1 О) # Читаем 1 О байтов
# Глава 15. Файловый ввод вывод
# f.read(lO} # Читаем следующие 10 байтов
# рrint("**Посимвольное чтение с кодировкой")
# txt = open("text.txt", "r", encoding='utf-8')
# print(txt.read(l))
# print(txt.read(2))
# print(txt.read(б))
# txt. close ()
# рrint("**Читает весь файл в переменную content ")
# txt = open("text.txt", "r", encoding='utf-8')
# content = txt.read()
# print(content)
# txt.close()
# рrint("**Построчное чтение файла ")
# txt.= open("text.txt", "r", encoding='utf-8')
# print (txt. readline ()) # Строка 1
# print(txt.readline()) # Строка 2
# txt.close()
# print·("** Читает файл в список ")
# txt = open("text.txt", "r", encoding='utf-8')
# lines = txt.readlines()
# print (lines)
# print(len(lines))
# for line in lines:
# print (line)
# txt .. close ()
#########################################################
# Далее рассмотрим пример записи в файл в текстовом и двоичном режимах:
# # Текстовый режим
# f = open("somefile.txt", "w", encoding="utf-8")
# f.write("String�)
# f. close ()
# # Двоичный режим
# f = open("somefile.txt", "wb", encoding="utf-8")
# f.write("String\r\n")
# f. close ()
# # Запись нескольких строк
# f = open("somefile.txt", "wb", encoding="utf-8").
# f.writelines{["Stringl\n", "String2"])
# f. flush () # Сбрасываем буфер на диск
# f. close()
################################################################
# filename = r'F:\Учебный материал\Python\fileTest1.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines() # читает файл построчно и сохраняет их в переменную lines(список)
# for line in lines:
#     print(line.rstrip()) # выводит список строк и удаляет пробелы в конце каждой строки

# 0-1. Изучение Python: откройте пустой файл в текстовом редакторе и напишите несколько
# строк текста о возможностях Python. Каждая строка должна начинаться с фразы: «In Python
# you can…» Сохраните файл под именем learning_python.txt в каталоге, использованном для
# примеров этой главы. Напишите программу, которая читает файл и выводит текст три раза:
# с чтением всего файла, с перебором строк объекта файла и с сохранением строк в списке
# с последующим выводом списка вне блока with
#
# file = 'StudyPlan.txt'
# text = open(file, encoding='utf-8')
# for line in text:
#     print(line.rstrip())
# for line in content.split('\n'):
#     print(line)
# rows = content.split('\n')
# for row in rows:
#     print(row)


# with open(file, encoding='utf-8') as f:
#      content = f.read()
#      print(content)  # отображение содержимого файла целиком
# with open(file, encoding='utf-8') as f:
#      lines = f.readlines() # сохранение в список построчное чтение файла
#      for line in lines:
#          print(2,line.rstrip()) # вывод цикла(пероборки) строк списка
#
# print(lines) # вывод переменной списка сохраненных строк

# ################################################################################################
# 10-2. Изучение C: метод replace() может использоваться для замены любого слова в строке
# другим словом. В следующем примере слово ‘dog’ заменяется словом ‘cat’:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Прочитайте каждую строку из только что созданного файла learning_python.txt и замените
# слово Python названием другого языка, например C. Выведите каждую измененную строку
# на экран.
# with open(file, encoding= 'utf-8') as f:
#     text_string = f.readlines()
#     for line in text_string:
#         ch_lines = line.replace('Python', 'OOP')
#         print(ch_lines.rstrip())
#########################################################################################
# 10-3. Гость: напишите программу, которая запрашивает у пользователя его имя. Введенный
# ответ сохраняется в файле с именем guest.txt.


# with open('guest_book.txt', 'a+') as qb:
#     guest_list = input().split('  ')
#     for guest in guest_list:
#         qb.write(guest + '\n')

#########################################################################################
# 0-4. Гостевая книга: напишите цикл while, который в цикле запрашивает у пользователей
# имена. При вводе каждого имени выведите на экран приветствие и добавьте строку с сообщением в файл
# с именем guest_book.txt. Проследите за тем, чтобы каждое сообщение размещалось в отдельной строке файла.


# print("Составим список гостей ")
# print("Для завершения составления списка гостей введите 'ok' ")
# guest_list = []
# while True:
#     name = input("Приглашения получат: ")
#     if name == 'ok':
#         break
#     else:
#         print(f'Welcome, Dear {name}, on our website!!!!')
#         guest_list.append(name)
# with open('guest_book.txt', 'a') as qb:
#     for guest in guest_list:
#         qb.write(guest + '\n')
################################################################################
# 10-5. Опрос: напишите цикл while, в котором программа спрашивает у пользователя,
# почему ему нравится программировать. Каждый раз, когда пользователь вводит очередную
# причину, сохраните текст его ответа в файле

# print("Расскажите, почему вам нравитcя  программировать: ")
# print("По окончании нажмите введите 'ok' ")
# answer = []
# end = True
# while end:
#     text = input("Мне нравится программировать, потому что:  ")
#     if text == 'end':
#         end = False
#     else:
#         answer.append(text)
# with open('guest_book.txt', 'a', encoding='utf-8') as qb:
#     for motive in answer:
#         qb.write(motive + '\n')


#######################################################################################
# Открытие файла и запись в файл с помощью функции print
# s = 'I love Spartak Moscow. I was born redwhait!'
# with open('StudyPlan.txt','wt') as f:
#     print(s, file =f)
# Открытие, чтение файла и сохрание его в переменную
text = open('D:\ProgrammProjects\LearnPython\Hardwork\Lessons\guest_book.txt')
#######################################################################
print(iter(text) is text)
next(text)

