#!/usr/bin/env python

import calendar
from datetime import date
from time import strptime

# Function to validate DOB input
# validate_dob("1985", "November", "18")
def validate_dob(y, m, d):

	# Validating year
	try:
		if len(y) == 4 and not int(y) > date.today().year:	# Year length must be 4 digits and be in the past
			year = True
		else:
			year = False
	except ValueError:
		year = False

	# Validating month
	try:
		for n in calendar.month_name:	# Checking to see if user inputted month is in calendar
			if m == n:
				month = True
				break
		else:
			month = False
	except ValueError:
		month = False;

	# Validating day
	try:
		validDays = calendar.monthrange(int(y), strptime(m[0:3], "%b").tm_mon)	# Getting valid number of days for specified month/year from the calendar
		if int(d) > 0 and int(d) <= validDays[1]:	# Checking to see if user inputted day is valid
			day = True
		else:
			day = False
	except ValueError:
		day = False

	# Checking if year, month and date are all valid
	if True == year and True == month and True == day:
		return True
	else:
		return False
