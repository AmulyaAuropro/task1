from datetime import datetime
from datetime import date
import time

today = date.today()


def user_birthday():
    year = int(input('Enter your year of birth [YY] '))
    month = int(input('Enter your month of birth [MM] '))
    day = int(input('Enter your date of birth [DD] '))

    birthday = datetime(year, month, day)
    return birthday


def calculate_dates(birthday):
    today == date.fromtimestamp(time.time())
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return birthday
    else:
        return birthday

while True:
    try:
        bday = user_birthday()
        t = calculate_dates(bday)
        time_to_birthday = abs(t - today)
        days = str(time_to_birthday.days)
        print("Time to Birthday is :" + days + " days")
        hours = int(days)* 24
        print(f'{"Hours : "} {hours}')
        min = int(hours)* 60
        sec = int(min)* 60
        print(f'{"minutes : "} {min}')
        print(f'{"seconds : "} {sec}')
    except:
        print("invalid input, Enter only numbers")
    user_input = input("do you want to continue Y/exit")
    if(user_input) == 'exit':
        break
        
        
        
    OUTPUT:
          Enter your year of birth [YY] 2000
          Enter your month of birth [MM] 04
          Enter your date of birth [DD] 2
          Time to Birthday is :165 days
          Hours :  3960
          minutes :  237600
          seconds :  14256000
          do you want to continue Y/exity
          Enter your year of birth [YY] udhj
          invalid input, Enter only numbers
          do you want to continue Y/exit
