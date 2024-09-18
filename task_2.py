import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000) or not (min_num <= quantity <= max_num):
        return []

    # Генерація унікальних чисел
    lottery_numbers = random.sample(range(min_num, max_num + 1), quantity)
    # Повернення відсортованого списку
    return sorted(lottery_numbers)

# Приклад
print(get_numbers_ticket(1, 49, 6))
