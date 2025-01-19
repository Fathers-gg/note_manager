# 1. Создайте программу, которая выводит интерактивное текстовое меню, позволяющее пользователю выбирать действия.
# 2. Меню должно:
# Отображать список доступных действий.
# Выполнять выбранное пользователем действие, вызывая соответствующую функцию.
# Повторно показывать меню после завершения действия, пока пользователь не выберет выход.
# 3. Доступные действия:
# 1: Создать новую заметку (вызов функции create_note()).
# 2: Показать все заметки (вызов функции display_notes()).
# 3: Обновить заметку (вызов функции update_note()).
# 4: Удалить заметку (вызов функции delete_note()).
# 5: Найти заметки (вызов функции search_notes()).
# 6: Выйти из программы.
# 4. Обеспечьте обработку ошибок:
# Если пользователь вводит недопустимый номер действия, программа должна выводить сообщение об ошибке и повторно показывать меню.
# Убедитесь, что программа корректно завершает выполнение при выборе выхода.

from colorama import init, Fore, Back, Style

init(autoreset=True)
from create_note_function import create_note
from display_notes_function import display_notes
from update_note_function import update_note
from search_notes_function import search_notes


# Функция для удаления заметки
def delete_note(notes):
    if not notes:
        print(Back.RED + Style.BRIGHT + Fore.BLACK + "Нет заметок для удаления.")
        return

    display_notes(notes)  # Предполагается, что эта функция отображает все заметки
    try:
        note_index = int(input(Fore.BLUE + Back.LIGHTGREEN_EX + "Введите номер заметки для удаления: ")) - 1
        if note_index < 0 or note_index >= len(notes):
            print(Back.RED + Style.BRIGHT + Fore.BLACK + "Некорректный номер заметки.")
            return

        deleted_note = notes.pop(note_index)
        print(Fore.BLUE + Back.LIGHTGREEN_EX + f"Заметка '{deleted_note['Заголовок']}' удалена.")
    except ValueError:
        print(Back.RED + Style.BRIGHT + Fore.BLACK + "Ошибка: введите правильный номер заметки.")


if __name__ == '__main__':
    # Основной цикл программы
    notes = []  # Инициализация списка заметок
    while True:
        print(Fore.BLACK + Back.LIGHTWHITE_EX + Style.NORMAL + "Меню действий:\n1. Создать новую заметку\n2. Показать все заметки\n3. "
              "Обновить заметку\n4. Удалить заметку\n5. Найти заметки\n6. Выйти из программы")

        user_choice = input(Fore.BLACK + Back.LIGHTGREEN_EX + 'Введите необходимый пункт меню цифрой, например (1): ')

        if user_choice == '1':  # создание заметки
            note = create_note()
            notes.append(note)
            print(Fore.BLACK + Back.LIGHTGREEN_EX + "Заметка создана.")
        elif user_choice == '2':  # Отображение заметок
            display_notes(notes)
        elif user_choice == '3':  # Изменение заметки
            if not notes:
                print(Fore.BLACK + Back.LIGHTCYAN_EX + "Нет заметок для обновления.")
                continue
            display_notes(notes)
            try:
                note_index = int(input(Fore.BLACK + Back.LIGHTGREEN_EX + "Введите номер заметки для обновления: ")) - 1
                if note_index < 0 or note_index >= len(notes):
                    print(Back.RED + Style.BRIGHT + Fore.BLACK + "Некорректный номер заметки.")
                    continue

                update_note(notes[note_index])  # обновление заметки
            except ValueError:
                print(Back.RED + Style.BRIGHT + Fore.BLACK + "Ошибка: введите правильный номер заметки.")
        elif user_choice == '4':  # Удаление заметки
            delete_note(notes)
        elif user_choice == '5':  # Поиск заметок
            keyword = input(Fore.BLACK + Back.LIGHTGREEN_EX + "Введите ключевое слово для поиска: ")
            status = input(Fore.BLACK + Back.LIGHTGREEN_EX + "Введите статус для фильтрации (или оставьте пустым): ")
            search_notes(notes, keyword, status if status else None)
        elif user_choice == '6':  # Выход из программы
            print(Fore.BLUE + Back.LIGHTCYAN_EX + "Выход из программы.")
            break
        else:
            print(
                Back.RED + Style.BRIGHT + Fore.BLACK + "Некорректный ввод, пожалуйста, выберите пункт меню от 1 до 6.")
