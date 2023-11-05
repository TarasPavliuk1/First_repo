from datetime import date, datetime, timedelta
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
    if not users:
        return {}

    for user in users:
        name = user.get("name")  # Отримуємо ім'я з словника user
        birthdate = user.get("birthday").replace(year=today.year)  # Отримуємо дату народження з словника user
        if birthdate < today:
            birthdate = birthdate.replace(year=today.year + 1)
    
        # Визначаємо день тижня для дня народження користувача
        birthday_day_of_week = birthdate.weekday()
        # Розраховуємо різницю між поточним днем тижня і днем народження
        days_until_birthday = (birthdate - today).days
        # Якщо день народження вже в цьому тижні, додаємо користувача до відповідного дня
        if days_until_birthday < 5 :
            day_name = list(birthdays_per_week.keys())[birthday_day_of_week]
            birthdays_per_week[day_name].append(user['name'])

        if days_until_birthday < 7:
            if birthday_day_of_week == 6 or birthday_day_of_week == 0:
                birthdays_per_week['Monday'].append(user['name'])
  

    new_birtdays_per_week = {}

    for day, users in birthdays_per_week.items():
        if users:
            new_birtdays_per_week[day] = users
            

    return new_birtdays_per_week

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")