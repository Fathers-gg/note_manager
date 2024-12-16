from datetime import datetime
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