# When programm starts, it should print:
import datetime
date_now = datetime.datetime.now()

# Current time (full)
print(date_now.strftime("%c"))
# Current year 
print(date_now.strftime("%Y"))
# Current month as text
print(date_now.strftime("%B"))
# Current month as number
print(date_now.strftime("%m"))
# Current day of year (1-365)
print(date_now.strftime("%j"))
# Current day of month (1-31)
print(date_now.strftime("%d"))
# Current day of weekend as number
print(date_now.strftime("%u"))
# Current day of weekend as text
print(date_now.strftime("%A"))
# Current time: hour/minute/second
print(date_now.strftime("%X"))