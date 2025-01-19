# 1. Напишите функцию update_note(), которая:
# Принимает заметку (словарь) в качестве аргумента.
# Позволяет пользователю выбрать, какое поле заметки нужно обновить.
# Запрашивает новое значение для выбранного поля.
# Обновляет указанное поле заметки.
# 2. Реализуйте следующий функционал:
# Покажите пользователю все поля заметки, которые можно обновить:
# username
# title
# content
# status
# issue_date
# Запросите у пользователя выбор поля для обновления.
# Если пользователь вводит некорректное имя поля, сообщите об ошибке и повторите запрос.
# Обновите поле с новым значением, введённым пользователем.
# Верните обновлённый словарь заметки.
# 3. Обеспечьте проверку корректности формата для issue_date (например, "день-месяц-год").
from create_note_function import create_note  # импорт функции запроса заметки
from datetime import datetime  # импорт библиотеки datetime


# функция проверки даты
def date_exp():
    while True:
        new_f = input('Введите новое значение для поля "Дата истечения" в формате дд-мм-гггг: ')
        try:
            # Проверка формата даты
            datetime.strptime(new_f, '%d-%m-%Y')
            return new_f
        except ValueError:
            print('Неверный формат даты. Пожалуйста, используйте дд-мм-гггг.')


# функция изменения статуса
def status_change():
    while True:
        status = input('Выберите статус заметки "Выполнено(1)", "В процессе(2)", "Отложено(3):" ')
        if status == '1':
            return 'выполнено'

        elif status == '2':
            return 'в процессе'

        elif status == '3':
            return 'отложено'

        else:
            print('Ошибка ввода, повторите ввод.')


# функция изменения полей
def update_note(note):
    fields = ["Имя пользователя", "Заголовок", "Содержание", "Статус", "Дата истечения"]
    print('Выберите поле для обновления')
    for index, field in enumerate(fields, start=1):
        print(f"{index}. {field}")

    while True:
        try:
            select_index = int(input("Введите номер поля для изменения: ")) - 1

            if 0 <= select_index < len(fields):
                field_to_update = fields[select_index]

                if field_to_update == "Статус":
                    new_f = status_change()
                elif field_to_update == "Дата истечения":
                    new_f = date_exp()
                else:
                    new_f = input(f'Введите новое значение для поля "{field_to_update}": ')

                # Обновляем значение в словаре
                note[field_to_update] = new_f
                print(f"Поле '{field_to_update}' обновлено на '{new_f}'")
                break
            else:
                print("Некорректный номер поля. Пожалуйста, попробуйте снова.")
        except ValueError:
            print("Ошибка: введите число.")

    return note


if __name__ == '__main__':
    # функция итогового вывода
    def update_create_function():
        # Вызываем функцию create_note, чтобы создать новую заметку
        note = create_note()
        print("Созданная заметка:", note)

        # Теперь можем обновить заметку, вызывая функцию update_note
        updated_note = update_note(note)
        print("Обновленная заметка:", updated_note)


    # Вызов функции
    update_create_function()
