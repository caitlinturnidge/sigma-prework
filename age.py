from datetime import date

def get_user_date():
    user_birth_date = input("What is your date of birth? (dd-mm-yyyy) ")
    user_birth_year = ""
    user_birth_month = ""
    user_birth_day = ""
    for i in range(6,10):
        user_birth_year += user_birth_date[i]
    for i in range(3,5):
        user_birth_month += user_birth_date[i]
    for i in range(2):
        user_birth_day += user_birth_date[i] 

    birth_date = date(int(user_birth_year), int(user_birth_month), int(user_birth_day))
    return birth_date

def calculate_age(birth_date, current_date):
    age = current_date.year - birth_date.year
    if (current_date.month < birth_date.month):
        age = age - 1
    if (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age = age - 1
    print("Your age is:", age)  

current_date = date.today()
birth_date = get_user_date()
calculate_age(birth_date, current_date)
