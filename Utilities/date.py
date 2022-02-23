'''A Tool To Find The Date Of Any Given Date'''

# Python program to Find day of the week for a given date
import datetime
import calendar

def findDay(date):
	Day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
	return (calendar.day_name[Day])


while True:
	try:
		date = input('Enter Date in form DD MM YYYY: ')
		print(findDay(date))
	except:
		print('No Date Available')
