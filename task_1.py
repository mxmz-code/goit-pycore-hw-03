from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Перетворення рядка дати у об'єкт datetime
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # Отримання поточної дати
        today = datetime.today().date()
        # Різниця між поточною датою і введеною датою
        delta = today - input_date
        # Повернення кількості днів
        return delta.days
    except ValueError:
        # Якщо дата у невірному форматі
        return "Невірний формат дати"

# Приклад
print(get_days_from_today("2021-10-09"))
