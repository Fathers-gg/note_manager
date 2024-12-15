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

print("введите статус заметки") #статус заметки
status = input()

created_date = datetime.now().strftime("%d-%m-%Y")#дата создания заметки
print("дата создания заметки ", created_date)
issue_date = datetime.now().strftime("%d-%m-%Y")#дата дедлайна
print("дата дедлайна", issue_date)