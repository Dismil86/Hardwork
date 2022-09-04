text = "hello world"
words = [word.capitalize() for word in text.split()]
print(words)
letters = [letter for word in text.split() for letter in word if letter > 'o'] # Двойный цикл для обращение элементов
                                                                               # строк в словаре
print(letters)


uniq_letters = {letter for word in text.split() for letter in word if letter > 'e'}
print('set',uniq_letters)
#alphabet = {letter  for index, letter in enumerate('letterinwordifletter',10)}
#print(alphabet)
alphabet = {index: letter for index, letter in enumerate('aetterinwordifletter',1)}
print('dict',alphabet)
print({value: key for key,value in alphabet.items()})

posives_gen = (e for e in range(100000) if e > 0) # Генератор создает объект данных. К которому при необходимости
                                                   # можно обратиться

if __name__ == '__main__':
    #for e in posives_gen:
    print(posives_gen)

