text = "hello world"
words = [word.capitalize() for word in text.split()]
print(1,words)
letters = [letter for word in text.split() for letter in word if letter > 'o'] # Двойный цикл для обращение элементов
                                                                               # строк в словаре
print(2,letters)


uniq_letters = {letter for word in text.split() for letter in word if letter > 'e'}
print(3,'set',uniq_letters)
alphabet = {letter  for index, letter in enumerate('letterinwordifletter',10)}
print(4,alphabet)
alphabet = {index: letter for index, letter in enumerate('aetterinwordifletter',1)}
print(5,'dict',alphabet)
print(6,{value: key for key,value in alphabet.items()})

posives_gen = (e for e in range(100000) if e > 0) # Генератор создает объект данных. К которому при необходимости
                                                   # можно обратиться

if __name__ == '__main__':
    #for e in posives_gen:
    print(7,posives_gen)

