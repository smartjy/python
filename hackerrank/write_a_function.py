
def is_leap(year):
    if 1999 <= (10**5):
        return (year % 400 == 0 or year % 100 != 0) and year % 4 == 0



year = int(input())
print(is_leap(year))

# year = int(input())
#
# print(year / 100)
# print(year / 400)
# print(year / 4)