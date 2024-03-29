#1

        from datetime import datetime
        
        def get_days_from_today(date):
            
            input_date = datetime.strptime(date, "%Y-%m-%d").date()
        
            current_date = datetime.now().date()
            
            difference = input_date - current_date
            
            return difference.days
        
        print(get_days_from_today("2021-10-09"))
        
        
#2
        
        import random
        
        def get_numbers_ticket(min_val, max_val, quantity):
            if min_val < 1 or max_val > 1000 or min_val > max_val or quantity < 1 or quantity > (max_val - min_val + 1):
                return []
        
            numbers_list = sorted(random.sample(range(min_val, max_val + 1), quantity))
            
            return numbers_list
        
        lottery_numbers = get_numbers_ticket(1, 49, 6)
        print("Your lottery numbers:", lottery_numbers)

        
        
#3
        
        from datetime import datetime, timedelta
        
        users = [
            {"name": "John Doe", "birthday": "1985.01.23"},
            {"name": "Jane Smith", "birthday": "1990.01.27"},
            {"name": "Jane Smith1", "birthday": "1990.03.05"},
        ]
        #first function
        prepared_users = []
        for user in users:
            try:
                birthday = datetime.strptime(user["birthday"], '%Y,%m,%d').date()
                prepared_users.append({"name": user['name'], 'birthday': birthday})
            except ValueError:
                print(f"некоректна дата народження для користувача {user['name']}")
        
        print(prepared_users)
        
        #second function
        def find_next_weekday(d, weekday: int):
            #функція для знаходження наступного дня тижня після заданої дати
        
            days_ahad = weekday - d.weekday()
            if days_ahad <= 0:
               days_ahad += 7
            return d + timedelta(days = days_ahead)
        
        days = 7
        datetime.today().date()
        upcoming_birthdays = []
        
        for user in prepared_users:
            birthday_this_year = user['birthday'].replace(year=today.year)
        
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
            if 0 <= (birthday_this_year - today).days <= days:
                if birthday_this_year.weekday >= 5:
                    birthday_this_year = find_next_weekday(birthday_this_year, 0)
        
            congratulation_data_str = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date":congratulation_data_str
            })
        
        print(upcoming_birthdays)
