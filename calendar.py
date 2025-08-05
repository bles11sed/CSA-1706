import calendar

year = int(input("enter year (e.g. 2025): "))
month = int(input("enter month (1-12): "))

cal_text = calendar.month(year, month)

print(f"\nhere is the calendar for {calendar.month_name[month]} {year}:\n")
print(cal_text)
