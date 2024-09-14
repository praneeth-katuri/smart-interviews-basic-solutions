'''
Given 2 unique dates, print the number of days between the 2 given dates.


Input Format

The first and only line of input contains 2 dates separated by space.


Output Format

Print the number of days.


Constraints

The given dates are valid dates between the years 1971 and 2100.


Example

Input

2000-01-16 1999-12-30

Output

17


Explanation

Self Explanatory
'''

date1, date2 = input().split()

y1, m1, d1 = map(int, date1.split('-'))
y2, m2, d2 = map(int, date2.split('-'))

def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_months(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28

def total_days(year, month, day):
    total = 0
    for y in range(1971, year):
        total += 365 + (1 if leap_year(y) else 0)
    
    for m in range(1, month):
        total += days_in_months(year, m)
    
    total += day
    return total

total_days1 = total_days(y1, m1, d1)
total_days2 = total_days(y2, m2, d2)

diff = abs(total_days1 - total_days2)
print(diff)