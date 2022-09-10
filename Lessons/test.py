# info = "We couldn't verify your mother's maiden name."
# intro = "Here is important information about your account security."
# first_name = 'Joffrey'
# greeting = 'Hello' + ',' + ' '  + first_name + '!'
# print(greeting)
# print(intro,info,sep='\n')
# #
# # first_name = 'Joffrey'
# # greeting = 'Hello'
# #
# # print(greeting + ", " + first_name + "!")
# # # => Hello, Joffrey!
# one = 'Naharis'
# two = 'Mormont'
# three = 'Sand'
# print(f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}')

# text = open('StudyPlan.txt',encoding='utf-8').read()
# print(text)
# text.encode('utf-16')
# print(f'{111:x}')

# def f():
#     return 5
#     return 10
# text = 'python'

# def trip_and_repeat(text,offset=2,repetitions=2):
#     new_text = f'{text[offset:] * repetitions}'
#     print(new_text)
#
# def string_or_not(text):
#
#     print(isinstance(text,str) and 'yes' or 'no')
# string_or_not(text)

# x = int(input())
# y = int(input())
# print(x % 7 == 0 and y % 7 == 0)
# print((x and y) % 7 == 0)
# def even_or_odd(number):
#   return 'Even' if number % 2 == 0 else 'Odd'
# print(even_or_odd(45))
#####################################################################################################
#                                   Кодировка Unicode
# print(bytes((66,97,127,255)))
# line = '4rthпро'.encode('utf-8')# Кодирует тип - строку в тип bytes
# print(line)
# print(b'4rth\xd0\xbf\xd1\x80\xd0\xbe'.hex())# метод преобразует тип bytes в 16-ичные числа
# print(int('d0bfd180d0be', base=16))# Здесь 'd0' обозначает байт с заданным значением'
# print(int('d0', base=16)) # Здесь 'd0' обозначает обозначает символ Юникод с заданным значением кодовой точки
############################################################################################

# print(__import__('binascii').unhexlify(b'd09bd0b5d0b220d09dd0b8d0bad0bed0bbd0b0d0b'
#                                        b'5d0b2d0b8d18720d0a2d0bed0bbd181d182d0bed0b'
#                                        b'920d0bdd0b0d0bfd0b8d181d0b0d0bb2022d092d0be'
#                                        b'd0b9d0bdd0b020d0b820d0bcd0b8d18022').decode('utf-8'))
# x = 'Лев Николаевич Толстой написал "Война и мир"'
# print(x.encode('utf8'))
########################################################################

    
        