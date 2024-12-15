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
print(titles)
print("Введите описание заметки")
content = input() #Описание заметки

print("введите статус заметки, например 'активна'") #статус заметки
status = input()

created_date = datetime.now().strftime("%d-%m-%Y-%A")#дата создания заметки
print("дата создания заметки ", created_date)
issue_date = datetime.now().strftime("%d-%m-%Y-%A")#дата дедлайна
print("дата дедлайна", issue_date)

information_about_note=[username, content, status, created_date, issue_date,  titles,]
for item in information_about_note:
    print(item)