from datetime import datetime

print('Введите имя пользователя')
username = input() #имя пользователя

print("Введите заголовок заметки 1")
title_1 = input() #заголовок заметки
print("Введите заголовок заметки 2")
title_2 = input() #заголовок заметки
print("Введите заголовок заметки 3")
title_3 = input() #заголовок заметки
titles=[title_1, title_2, title_3]

print("Введите описание заметки")
content = input() #Описание заметки

print("введите статус заметки, например 'активна'") #статус заметки
status = input()



while True:
    temp = input('Введите дату в формате "дд-мм-гггг" ')
    try:
        form_date = datetime.strptime(temp, "%d-%m-%Y").date() #дата создания заметки
    except ValueError:
        print("Некорректный формат даты. Попробуйте ещё раз.")
    else:
        # Преобразуем дату в формат "дд-мм"
        created_date = form_date.strftime("%d-%m")
        print("Дата создания заметки:", created_date)
        break

temp= input('Введите дату в формате "дд-мм-гггг" ')
try:
    form_date = datetime.strptime(temp, "%d-%m-%Y").date()  #дата истечения заметки
except ValueError:
    print("Некорректный формат даты. Попробуйте ещё раз.")
else:
    # Преобразуем дату в формат "дд-мм"
    issue_date = form_date.strftime("%d-%m")
    print("Дата истечения заметки:", issue_date)


information_about_note={
    "username": username,
    "title_1": title_1,
    "title_2": title_2,
    "title_3": title_3,
    "content": content,
    "status": status,
    "created_date": created_date,
    "issue_date": issue_date
}

for key, value in information_about_note.items():
    print(key + ": " + str(value))
