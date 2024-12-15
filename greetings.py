from datetime import datetime
username = 'имя пользователя'
print(username)
title = 'заголовок заметки '
print(title)
content= 'Описание заметки'
print(content)
status = 'статус заметки'
print(status)
created_date = datetime.now().strftime("%d-%m-%Y")#дата создания заметки
print("дата создания заметки ", created_date)
issue_date = datetime.now().strftime("%d-%m-%Y")#дата дедлайна
print("дата дедлайна", issue_date)

