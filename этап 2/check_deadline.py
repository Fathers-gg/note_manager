# 1. Напишите программу, которая:
# Сравнивает дату дедлайна заметки (issue_date) с текущей датой.
# Выводит соответствующее сообщение:
# Если дедлайн истёк, предупреждает пользователя.
# Если дедлайн не истёк, сообщает, сколько времени осталось до истечения срока.
# 2. Требования к функциональности:
#
# Получите текущую дату с помощью встроенной библиотеки Python (datetime).
# Проверьте, находится ли дедлайн в прошлом, настоящем или будущем.
# Реализуйте разницу в днях между текущей датой и дедлайном.
# 3. Программа должна корректно обрабатывать формат даты (например, "день-месяц-год")
# и информировать пользователя о неверном формате при вводе.
from datetime import datetime  # импортируем библиотеку


def deadline():
    date_now = datetime.now().date()  # переменная сегодняшней даты
    date_now = date_now.strftime('%d-%m-%Y')  # переводим в фомат дд-мм-гггг
    print("Сегодняшняя дата: ", date_now)

    while True:
        temp = input('Введите дату истечения заметки в формате "дд-мм-гггг" ')
        try:
            issue_date = datetime.strptime(temp, "%d-%m-%Y").date()  # дата истечения заметки в формате .date
        except ValueError:  # на случай неправильного ввода даты
            print("Некорректный формат даты. Попробуйте ещё раз.")
            continue
        date_now = datetime.now().date() # переводим обратно для вычисления разницы в датах
        diff = date_now - issue_date  # timedelta получилась, нужно рассчитать разницу только в днях
        days_dif = diff.days  # метод .days

        if days_dif > 0:
            expired_days = abs(days_dif)  # возвращаем модуль, чтоб не получилось отрицательных чисел
            if expired_days == 1:  # делаем адекватное окончание print дней/день
                print(f"Срок истек на {expired_days} день.")
            else:
                print(f" Срок истек на {expired_days} дней.")

        else:
            if issue_date == date_now:  # на случай если введена сегодняшняя дата
                print('Дедлайн сегодня!')
                break

            remaining_days = abs(days_dif)
            if remaining_days == 1:
                print(f"До истечения срока остался {remaining_days} день.")
            else:
                print(f"До истечения срока осталось {remaining_days} дней.")
        break


deadline()
