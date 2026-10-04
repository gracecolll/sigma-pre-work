import datetime
from datetime import date

date_entry = input("Enter a date in YYYY-MM-DD format: ")
year, month, day = map(int, date_entry.split("-"))
user_date = datetime.date(year, month, day)

current_date = date.today()
age = (current_date - user_date).days // 365
print(age)
