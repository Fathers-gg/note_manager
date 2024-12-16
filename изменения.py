from datetime import datetime
username = input('Введите имя пользователя ' ) #имя пользователя
content='' #присваиваю переменной пустую строку
titles=''#присваиваю переменной пустую строку
def main(): #открывается блок кода для заголовков и тел заметок
    stop_str = "конец" # задаем переменную для того, что бы остановить цикл при ее вводе
    titles = [] #создаеи пустой список для добавления заголовков заметок

    while True: # тут начинается цикл "пока истина"
        user_input = input("Введите заголовок заметки или 'конец' ")  # запрос на ввод заголовка или стоп-слова
        if user_input == stop_str: # если пользователь ввел стоп слово тогда
            break # остановка цикла

        titles.append(user_input)  # Добавляем заголовок в список с помощью метода .append

        user_input_body = input("Введите заметку ") # далее идет запрос тела заметки
        content=user_input_body # далее данные введенные пользователем присваиваются переменной content

    for i in range(len(titles)): # отбирает каждый элемент списка titles на экран
        print([titles[i]]) # и выводит его

# Запуск основной функции
if __name__ == "__main__": # переменная __name__ и == дает нам понять что это не импортируемый модуль,
    # а должен выполняться сам блок mine(). если переменная name это main то выполнять main()
    main()

status = input("введите статус заметки, например 'активна' ") #запрос статуса заметки



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

information_about_note=[[username],  [titles], [content], [status], [created_date], [issue_date], ] # собираем в список все
# что выше и печатаем пока содержимое списка не кончится
for item in information_about_note:
    print(item)