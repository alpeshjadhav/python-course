import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

month_calendar = calendar.month(year, month)

print(month_calendar)
