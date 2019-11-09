# w{3} : It will match the character w exactly 3  times.
# [xyz]{5} : It will match the string of length  consisting of characters {x, y, z}. For example it will match xxxxx, xxxyy and xyxyz.
# \d{4} : It will match any digit exactly 4 times.
#
# Task
#
# You have a test string .
# Your task is to write a regex that will match  using the following conditions:
#
#  must be of length equal to 45.
# The first 40 characters should consist of letters(both lowercase and uppercase), or of even digits.
# The last 5 characters should consist of odd digits or whitespace characters.
Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'	# Do not delete 'r'.
