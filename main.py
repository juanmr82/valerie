import os
from datetime import date
import calendar


def write_email(date):
    """So I am assuming you are using Outlook, which is the most corporate tool ever. And one of the worst ones"""
    try:
        if os.name == 'nt':
            import win32com.client as win32
            outlook = win32.Dispatch('outlook.application')
            if outlook is None:
                return -1
            mail = outlook.CreateItem(0)
            mail.To = "juanmr82@gmail.com"
            mail.Subject = f"Our date on {date}"
            mail.HtmlBody = f"Juan, lets meet on {date} in Munich"
            mail.Display(True)
        else:
            return -1
    except:
        return -1

    return 0


def say_hi_to_valerie():
    today_weekday = date.today().weekday()
    print(f'Hello valerie, hope you are having a fantastic, {calendar.day_name[today_weekday]}')


def ask_for_a_date():
    """Don't be too needy just because she is cool and pretty"""
    print('Would you like to go out in a date sometime soon?\nLooking forward meeting you')


def display_calendar():
    """You are in Germany, so show her a calendar so she chooses a date. Girls here love that"""
    year = date.today().year
    month = date.today().month
    day = date.today().day
    if (31 - day) <= 6:
        month += 1

    print(f"Which date would you like to meet?:\n{calendar.month(year, month)}")


def input_date():
    """I am not proud of this, but since I am doing this on a coffee break, well, it ain't that bad"""
    date_date = input("Please enter the day DD/MM/YY Format: ")
    year, month, day = map(int, date_date.split('/'))
    if (24 < year < 1) or (12 < month < 1) or (30 < day < 1):
        return 1
    else:
        print("Preparing Outlook email")
        email_result = write_email(date_date)
        if email_result != 0:
            print("Please let Juan know on Telegram, since apparently you are too cool for Outlook\n")


if __name__ == '__main__':
    say_hi_to_valerie()
    ask_for_a_date()
    display_calendar()
    input_date()
