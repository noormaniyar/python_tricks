"""
    Did you know that you can get a calendar using Python?
    Python has a built-in module called calendar. We can import
    this module to print out the calendar. We can do a lot of things
    with calendar.
    Let`s say we want to see April 2022; we will use the month class
    of the calendar module and pass the year and month as
    arguments
"""

import calendar
month = calendar.month(2022, 4)
is_leap_year = calendar.isleap(2022)

print(month, '-------April 2022 calender------')
print(is_leap_year, '------is Leap Year----')
