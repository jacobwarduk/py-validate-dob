py-validate-dob
===============

Python function to validate user inputted date of birth.

Example Usage
-------------
```
print validate_dob("1985", "November", "18")		# Returns True
print validate_dob("2017", "November", "18")		# Returns False
print validate_dob("2010", "NoMonth", "18")		# Returns False
print validate_dob("2010", "January", "39")		# Returns False
print validate_dob("2010", "January", "18")		# Returns True
```
