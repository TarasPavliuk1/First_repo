from datetime import date, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = date.today()
    
    # Визначаємо день тижня для поточної дати (понеділок - 0, вівторок - 1, ..., неділя - 6)
    current_day_of_week = today.weekday()
    
    # Створюємо словник для зберігання днів народжень на тиждень вперед
    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }
    
    # Проходимося по користувачам і додаємо їх до відповідних днів
    for user in users:
        user_birthday = user['birthday']
        
        # Визначаємо день тижня для дня народження користувача
        birthday_day_of_week = user_birthday.weekday()
        
        # Розраховуємо різницю між поточним днем тижня і днем народження
        days_until_birthday = current_day_of_week - birthday_day_of_week
        
        # Якщо день народження вже в цьому тижні, додаємо користувача до відповідного дня
        if days_until_birthday < 5 :
            day_name = list(birthdays_per_week.keys())[days_until_birthday]
            birthdays_per_week[day_name].append(user['name'])
        # Якщо день народження в наступному тижні, додаємо користувача до відповідного дня наступного тижня
        else:
            day_name = list(birthdays_per_week.keys())[days_until_birthday - 5]
            birthdays_per_week[day_name].append(user['name'])
    
    # Переносимо вихідні дні на понеділок
    if current_day_of_week > 4:
        for i in range(current_day_of_week, 7):
            day_name = list(birthdays_per_week.keys())[i - 5]
            birthdays_per_week['Monday'].extend(birthdays_per_week[day_name])
            birthdays_per_week[day_name] = []
  
    
    return birthdays_per_week

# Приклад використання:
users = [
    {"name": "Bill Gates", "birthday": date(2023, 10, 28)},
    {"name": "Jan", "birthday": date(2023, 11, 6)},  # понеділок
    {"name": "Kim", "birthday": date(2023, 11, 2)}, # четверг
]

result = get_birthdays_per_week(users)
print(result)

# Не розумію чому Monday': ['Kim'] якщо має бути 'Wednesday'
# і чого 'Thursday': ['Jan']  якщо має бути 'Monday'