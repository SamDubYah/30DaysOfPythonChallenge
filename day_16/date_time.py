#! /usr/bin/env python3

from datetime import datetime, date, timedelta



# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp

print(f'{day}/{month}/{year}, {hour}:{minute}')


# 1. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
now = now.strftime("%m/%d/%Y, %H:%M:%S")

print(now)

# 1. Today is 5 December, 2019. Change this time string to time.
today_string = "5 December, 2019"
today_object = datetime.strptime(today_string, "%d %B, %Y")

print(today_object)

# 1. Calculate the time difference between now and new year.
today = date.today()
new_year = date(year=today.year+1, month=1, day=1)
time_to_new_year = new_year - today


# 1. Calculate the time difference between 1 January 1970 and now.
now = datetime.now()
then = datetime(1970, 1, 1)
time_since_then = now - then

print(now)
print(then)
print(time_since_then)


# 1. Think, what can you use the datetime module for? Examples:
#    - Time series analysis
#    - To get a timestamp of any activities in an application
#    - Adding posts on a blog 