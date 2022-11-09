from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path


def pdf_to_mp3(file_path='test_pdf', language='en'):
    # Проверяем явл-ся ли указанный путь путь к файлу и это файл PDF формата :
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # выводим сообщение о имение фала который обрабатывается
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Proccessing...')
        # открываем указанный PDF файл в режиие байтового чтения
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            # преоброзуем  каждую страницу файла в строку и сохраняем и все строки в список строк
            pages = [page.extract_text() for page in pdf.pages]
        # соединяем весь список строк в одну строку
        text = ''.join(pages)
        # Удаляем лишние пробелы после каждой строки
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}ru.mp3')

        return f'[+] {file_name}.mp3 saved successfully!\n...Have a good day!...'
    else:
        return 'File not exists, check the file path!'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input(" Choose a language. for example 'en' or 'ru' : ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
