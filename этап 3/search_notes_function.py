# Описание задания
# 1. Напишите функцию search_notes(notes, keyword=None, status=None), которая:
# Принимает список заметок (notes), ключевое слово (keyword) и/или статус (status) в качестве аргументов.
# Возвращает список заметок, которые соответствуют заданным критериям поиска.
# 2. Реализуйте следующий функционал:
# Поиск по ключевым словам:
# Заметки отбираются, если заданное ключевое слово встречается в любом из полей:
# title, content, или username.
# Поиск по статусу:
# Заметки отбираются, если их поле status совпадает с указанным.
# Если указаны оба параметра (keyword и status), выполняйте поиск с учётом обоих условий.
# Программа должна выводить найденные заметки в удобном формате. Если заметки не найдены, выведите сообщение:
# Заметки, соответствующие запросу, не найдены.
# 3. Обеспечьте обработку пустого списка заметок.
# Функция для поиска заметок
# Импорт необходимых функций
import datetime

#Функция создания заметки
from create_note_function import create_note
# отображение заметок
from display_notes_function import display_notes
# функция поиска
def search_notes(notes, keyword=None, status=None):
    # Функция поиска заметок
    found_notes = []
    if not notes:
        print("Список заметок пуст.")
        return []

    for note in notes:
        keyword_match = keyword is None or keyword.lower() in note.get("Заголовок", "").lower() or \
                        keyword.lower() in note.get("Содержание", "").lower() or \
                        keyword.lower() in note.get("Имя пользователя", "").lower()

        status_match = status is None or note.get("Статус") == status

        if keyword_match and status_match:
            found_notes.append(note)

    if found_notes:
        display_notes(found_notes)
    else:
        print("Заметки, соответствующие запросу, не найдены.")

if __name__ == '__main__':
    def search():
        # Работа с заметками в общем
        notes = []
        while True:
            new_note = create_note()# Создаем заметки
            if new_note is None:  # Проверяем на отсутствие
                print("Выход из программы.")
                break
            notes.append(new_note) # Добавляем заметку в список
            print("Заметка добавлена.")
            display_notes(notes)  # Отображаем добавленную заметку

            while True:
                keyword = input("Введите ключевое слово для поиска (или пустая строка для выхода): ").lower()
                if not keyword:
                    break
                status = input("Введите статус для поиска (или пустая строка для выхода): ").lower()
                search_notes(notes, keyword, status)


    search()
