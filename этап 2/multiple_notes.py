# 1. Напишите программу, которая позволяет пользователю:
# Создавать несколько заметок, каждая из которых хранится в виде словаря.
# Добавлять заметки в список для их упорядоченного хранения.
# 2. Реализуйте следующий функционал:
# Создание заметки: Пользователь вводит данные заметки (имя, заголовок, описание, статус,
# дату создания, дедлайн).
# Сохранение заметки: Каждая заметка сохраняется как словарь внутри списка.
# Отображение заметок: Программа выводит список всех созданных заметок с понятным форматированием.
# 3. Особенности:
# Реализуйте цикл, который позволяет пользователю добавлять любое количество заметок.
# Предусмотрите возможность завершения ввода новых заметок (например, с помощью команды "стоп").
from datetime import datetime


def multiple():
    def deadline():
        date_now = datetime.now().date()  # переменная сегодняшней даты
        print("Сегодняшняя дата: ", date_now.strftime("%d-%m-%Y"))

        while True:
            temp = input('Введите дату истечения заметки в формате "дд-мм-гггг": ')
            try:
                issue_date = datetime.strptime(temp, "%d-%m-%Y").date()
            except ValueError:
                print("Некорректный формат даты. Попробуйте ещё раз.")
                continue

            diff = issue_date - date_now
            days_dif = diff.days

            if days_dif < 0:
                expired_days = abs(days_dif)
                if expired_days == 1:
                    print(f"Срок истек на {expired_days} день.")
                else:
                    print(f"Срок истек на {expired_days} дней.")
            elif days_dif == 0:
                print('Дедлайн сегодня!')
                break
            else:
                remaining_days = days_dif
                if remaining_days == 1:
                    print(f"До истечения срока остался {remaining_days} день.")
                else:
                    print(f"До истечения срока осталось {remaining_days} дней.")
            break

        print(f"Дата истечения: {issue_date.strftime('%d-%m-%Y')}")  # Отображение даты
        return issue_date  # Возвращаем дату истечения ##
# блок с датами
    return deadline  # Возвращаем функцию deadline для использования в title


def change_status(note_title, notes):
    print("Текущий статус заметки:", notes[note_title]['status'])
    print("Выберите новый статус заметки:")
    print("1. Выполнено")
    print("2. В процессе")
    print("3. Отложено")

    while True:
        user_input_status = input('Ваш выбор (1, 2, 3): ')
        if user_input_status == '1':
            notes[note_title]['status'] = 'выполнено'
            print("Статус заметки успешно изменен на: Выполнено")
            break
        elif user_input_status == '2':
            notes[note_title]['status'] = 'в процессе'
            print("Статус заметки успешно изменен на: В процессе")
            break
        elif user_input_status == '3':
            notes[note_title]['status'] = 'отложено'
            print("Статус заметки успешно изменен на: Отложено")
            break
        else:
            print('Ошибка ввода, повторите ввод.')
# блок для статуса

def title():
    user_name = input('Введите имя пользователя: ')
    stop_str = "стоп"
    notes = {}
    deadline_function = multiple()  # Получаем функцию deadline

    while True:
        user_title = input("Введите заголовок заметки или 'стоп': ")
        if user_title.lower() == stop_str or user_title == "":
            break

        if user_title in notes:
            print("Заголовок уже есть. Пожалуйста, введите другой заголовок.")
            continue

        user_content = input("Введите заметку: ")
        if user_content.strip() == "":
            print("Заметка не может быть пустой. Пожалуйста, введите содержимое заметки.")
            continue

        deadline_date = deadline_function()  # Получаем дату дедлайна
        notes[user_title] = {
            "content": user_content,
            "user": user_name,
            "status": "новая",
            "deadline": deadline_date  # Добавляем дату дедлайна
        }

        change_status(user_title, notes)

    print('Заметки:')  # Вывод заметок
    for title, note in notes.items():
        formatted_deadline = note['deadline'].strftime('%d-%m-%Y')
        print(
            f"- {title}: \n{note['content']} \nСтатус: {note['status']} \nДата дедлайна: {formatted_deadline}")
# Основная функция

# Запуск программы
if __name__ == "__main__":
    title()
