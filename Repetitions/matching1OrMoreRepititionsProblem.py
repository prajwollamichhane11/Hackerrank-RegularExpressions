# w+ : It will match the character w  or more times.
# [xyz]+ : It will match the character x, y or z  or more times.
# \d+ : It will match any digit  or more times.
#
# Task
#
# You have a test string .
# Your task is to write a regex that will match  using the following conditions:
#
#  should begin with  or more digits.
# After that,  should have  or more uppercase letters.
#  should end with  or more lowercase letters.
Regex_Pattern = r'^[\d]+[A-Z]+[a-z]+$'	# Do not delete 'r'.
