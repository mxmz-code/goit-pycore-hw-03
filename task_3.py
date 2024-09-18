import re

def normalize_phone(phone_number):
    # Видалення всіх непотрібних символів
    cleaned = re.sub(r'\D', '', phone_number)
    
    # Якщо номер починається з '380', додаємо тільки '+'
    if cleaned.startswith('380'):
        return '+' + cleaned
    # Якщо номер без коду країни, додаємо '+38'
    elif len(cleaned) == 10:
        return '+38' + cleaned
    # Якщо номер починається з '+', залишаємо його
    return '+' + cleaned if phone_number.startswith('+') else cleaned

# Приклад
raw_numbers = [
    "067\t123 4567", "(095) 234-5678\n", "+380 44 123 4567", "380501234567",
    "+38(050)123-32-34", "0503451234", "(050)8889900", "38050-111-22-22", "38050 111 22 11"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери:", sanitized_numbers)
