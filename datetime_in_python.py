"""
    The below code demonstrates how you can get the current time
    using the datetimeQ module. The strftimeQ method formats
    time for the desired output. This code breaks down how you can
    use the datetime module with the strftimeQ method to get a
    formatted string of time in hours, minutes, and seconds format.
"""

from datetime import datetime
from datetime import date

time_now = datetime.now().strftime('%H:%M:%S')
today_date = date.today()


print(f'The time now is {time_now}')
print(f'Today is {today_date}')