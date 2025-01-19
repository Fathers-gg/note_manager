import yaml
import json

# Функция записи заметок в файл YAML
def save_notes_to_file(notes, filename):
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            # Записываем все заметки в формате YAML
            yaml.dump(notes, file, allow_unicode=True, default_flow_style=False)
        print(f"Заметки успешно сохранены в файл {filename}")
    except Exception as e:
        print(f'Ошибка при записи в файл YAML: {e}')

# Функция загрузки заметок из файла YAML обратно в код питон
def load_notes_from_file(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            notes = yaml.safe_load(file)  # Загружаем данные из файла и преобразуем их в Python-объект
            if notes is None:  # Если файл пустой, возвращаем пустой список
                return []
            return notes
    except yaml.YAMLError as e:
        print(f'Ошибка при чтении YAML: {e}')
        return []
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []

# Функция добавления новых заметок в существующий файл
def append_notes_to_file(notes, filename):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            yaml.dump(notes, file, allow_unicode=True, default_flow_style=False)
        print(f"Заметки успешно добавлены в файл {filename}")
    except yaml.YAMLError as e:
        print(f'Ошибка при записи в YAML: {e}')

# Функция записи заметок в файл JSON
def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print(f"Заметки успешно сохранены в файл {filename}")
    except Exception as e:
        print(f'Ошибка при записи в JSON: {e}')

# Пример заметок
notes = [
    {
        "Имя пользователя": "Алексей",
        "Заголовок": "Список покупок",
        "Описание": "Купить продукты",
        "Статус": "новая",
        "Дата создания": "27-11-2024",
        "Дедлайн": "30-11-2024"
    }
]

# Пример использования функций (все вызовы закомментированы для тестирования)
# 1
#save_notes_to_file(notes, 'filename.yaml')  # Вызов функции для записи в YAML
# 2
#append_notes_to_file(notes, 'filename.yaml')  # Вызов функции для добавления в YAML
#3
#save_notes_json(notes, 'filename.json')  # Вызов функции для записи в JSON

# 4 Пример Функции загрузки заметок из файла YAML обратно в код питон
# loaded_notes_yaml = load_notes_from_file('filename.yaml')  # Чтение из YAML файла
# print(loaded_notes_yaml)


