from datetime import date, timedelta, datetime, time

#substract 5 days from current
#dt = date.today() - timedelta(5)
#print('Current Date :',date.today())
#print('5 days before Current Date :',dt)

#today yesterday tomorrow
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)

#microseconds
dtt = datetime.datetime.today().replace(microsecond=0)
print()
print(dtt)
print()

#date difference in seconds

