# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print('2017 leap :', is_leap(2017))
print('2018 leap :', is_leap(2018))
print('2019 leap :', is_leap(2019))
print('2020 leap :', is_leap(2020))
print('')
print('2017 month 2 :', days_in_month(2017, 2))
print('2018 month 2 :', days_in_month(2018, 2))
print('2019 month 2 :', days_in_month(2019, 2))
print('2020 month 2 :', days_in_month(2020, 2))