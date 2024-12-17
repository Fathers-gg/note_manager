status = input('Введите статус заметки ')
print(status)

new_status = '' # задаем пустую переменную
st_yes = 'да' # задаем переменную для ответа да
st_no = 'нет' # задаем переменную для ответа нет

while True:
    user_input = input('Желаете сменить статус вашей заметки? Да/Нет ')
    if user_input == st_no: # если ввод пользователя нет, то выводим старый статус
        print(status)
        break # остановка цикла
    elif user_input != st_yes and user_input != st_no: # иначе если не да и не нет, вывод ошибки
        print('Ошибка ввода')
    else:
        temp_status = input('Введите новый статус заметки ') # иначе ответ был да, запрашиваем новый статус
        new_status_2 = temp_status
        print(new_status_2) # и выводим на экран