#the dot(.) matches with anything except the new line
#for matching the . we need to escape it using \.
# ^ is for start of the line
# $ is for the new line

# since the question asks for the new line only, the $ sign at last was enough to make it work

regex_pattern = r"^...\....\....\....$"	# Do not delete 'r'.
