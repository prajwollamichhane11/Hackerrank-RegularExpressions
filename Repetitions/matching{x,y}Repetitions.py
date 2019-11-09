# Task
#
# You have a test string .
# Your task is to write a regex that will match  using the following conditions:
#
#  should begin with  or  digits.
# After that,  should have  or more letters (both lowercase and uppercase).
# Then  should end with up to  . symbol(s). You can end with  to  . symbol(s), inclusively.
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'	# Do not delete 'r'.
