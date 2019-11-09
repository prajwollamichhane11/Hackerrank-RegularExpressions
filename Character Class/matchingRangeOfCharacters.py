# Task
#
# Write a RegEx that will match a string satisfying the following conditions:
# [a-z] = abc...z
# The string's length is >= 5. So donot use $ at last
# The first character must be a lowercase English alphabetic character.
# The second character must be a positive digit. Note that we consider zero to be neither positive nor negative.
# The third character must not be a lowercase English alphabetic character.
# The fourth character must not be an uppercase English alphabetic character.
# The fifth character must be an uppercase English alphabetic character.
# In the editor below, replace the blank (_________) with a RegEx pattern satisfying the criteria above. This is a RegEx-only challenge, so you are not required to write any additional code.

Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'	# Do not delete 'r'.
