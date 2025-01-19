# 1. Напишите программу, которая предоставляет пользователю возможность удалить заметку из списка заметок.
#
# 2. Заметки хранятся в виде списка словарей, каждый словарь представляет одну заметку.
#
# 3. Реализуйте функционал:
#
# Удаление заметки по имени пользователя.
# Удаление заметки по заголовку.
# 4. Программа должна:
#
# Запрашивать у пользователя критерий для удаления (например, имя пользователя или заголовок).
# Удалять все заметки, соответствующие введённому критерию.
# Если заметок для удаления не найдено, выводить соответствующее сообщение.
# После удаления оставлять остальные заметки в списке.
def display_notes(titles, user_notes, note_body, statuses, created_dates, issue_dates):
    if not titles:
        print("Нет доступных заметок.")
    else:
        print('Список заметок:')
        for title in titles:
            print("Имя: ", user_notes[title], '\n',
                  "Заголовок: ", title, '\n',
                  "Описание: ", note_body[title], '\n',
                  "Статус:", statuses[title], '\n',
                  "Дата создания:", created_dates[title], '\n',
                  "Дата дедлайна:", issue_dates[title], '\n')


def get_date(prompt):
    # This function should handle date input from the user.
    # For simplicity, we'll return the input directly, but you should add validation.
    return input(prompt)


def delete_note_by_title(titles, user_notes, note_body, statuses, created_dates, issue_dates):
    title_to_delete = input("Введите заголовок заметки для удаления: ")
    if title_to_delete in titles:
        titles.remove(title_to_delete)
        del user_notes[title_to_delete]
        del note_body[title_to_delete]
        del statuses[title_to_delete]
        del created_dates[title_to_delete]
        del issue_dates[title_to_delete]
    else:
        print("Заметка с таким заголовком не найдена.")


def delete_note_by_username(user_notes, titles, note_body, statuses, created_dates, issue_dates):
    username_to_delete = input("Введите имя пользователя для удаления заметки: ")
    titles_to_delete = [title for title in titles if user_notes[title] == username_to_delete]

    if titles_to_delete:
        for title in titles_to_delete:
            titles.remove(title)
            del user_notes[title]
            del note_body[title]
            del statuses[title]
            del created_dates[title]
            del issue_dates[title]
        print("Заметки успешно удалены.")
    else:
        print("Заметки для данного пользователя не найдены.")


def delete_note():
    stop_str = "стоп"
    user_notes = {}
    note_body = {}
    titles = []
    statuses = {}
    created_dates = {}
    issue_dates = {}
    note_counter = 1

    while True:
        username_input = input('Введите имя пользователя (или "стоп" для выхода): ')
        if username_input.lower() == stop_str:
            print('Выход')
            break
        user_input_head = input("Введите заголовок заметки: ")
        if user_input_head in titles:
            print("У вас уже есть такой заголовок, повторите ввод.")
            continue
        else:
            titles.append(user_input_head)

        user_input_1 = input("Введите заметку: ")
        note_body[user_input_head] = user_input_1

        status = 'в процессе'
        statuses[user_input_head] = status
        user_notes[user_input_head] = username_input

        print(f'Текущий статус заметки: "{status}"')

        print("Выберите новый статус заметки:")
        st_one = ['1', 'выполнено']
        st_two = ['2', 'в процессе']
        st_three = ['3', 'отложено']

        while True:
            user_input = input('(Статус заметки может быть: "выполнено", "в процессе", "отложено") Ваш выбор: ')
            if user_input in st_one:
                status = 'выполнено'
                print("Статус заметки успешно изменен на: Выполнено")
                break
            elif user_input in st_two:
                status = 'в процессе'
                print("Статус заметки успешно изменен на: В процессе")
                break
            elif user_input in st_three:
                status = 'отложено'
                print("Статус заметки успешно изменен на: Отложено")
                break
            else:
                print('Ошибка ввода, повторите ввод.')

        created_date = get_date('Введите дату создания заметки в формате "дд-мм-гггг": ')
        issue_date = get_date('Введите дату истечения заметки в формате "дд-мм-гггг": ')

        created_dates[user_input_head] = created_date
        issue_dates[user_input_head] = issue_date

        display_notes(titles, user_notes, note_body, statuses, created_dates, issue_dates)

        delete_choice = input("Хотите удалить заметку? (по заголовку(1)/по имени пользователя(2)/нет): ")
        head_1 = ['по заголовку', '1']
        name_delete = ['по имени пользователя', '2']
        if delete_choice.lower() in head_1:
            delete_note_by_title(titles, user_notes, note_body, statuses, created_dates, issue_dates)
        elif delete_choice.lower() in name_delete:
            delete_note_by_username(user_notes, titles, note_body, statuses, created_dates, issue_dates)

        print('Ваши заметки: ')
        display_notes(titles, user_notes, note_body, statuses, created_dates, issue_dates)


if __name__ == "__main__":
    delete_note()
