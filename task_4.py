from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        # Перетворення дати народження на об'єкт datetime
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        # Отримуємо дату народження цього року
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже був цього року, обираємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Перевіряємо чи день народження випадає на наступні 7 днів
        delta = (birthday_this_year - today).days
        if 0 <= delta <= 7:
            # Переносимо привітання на понеділок, якщо день народження випав на вихідний
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            # Додаємо до списку привітань
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })
    
    return upcoming_birthdays

# Приклад
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

print(get_upcoming_birthdays(users))
