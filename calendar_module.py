# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
import calendar

month, date, year = map(int, input().split())

print(calendar.day_name[calendar.weekday(year, month, date)].upper())