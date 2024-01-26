'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from datetime import date, timedelta

def digit_sum(d):
    digit = sum(int(char) for char in str(d) if char.isdigit())
    return sum(int(char) for char in str(digit) if char.isdigit())

def find_dates_with_sum(target_sum, year):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    current_date = start_date
 
    while current_date <= end_date:
        if digit_sum(current_date) == target_sum:
            print(current_date)
        current_date += timedelta(days=1)

find_dates_with_sum(5, 2026)

