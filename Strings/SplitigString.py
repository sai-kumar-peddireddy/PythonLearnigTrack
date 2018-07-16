"""
Mon Jul 16 06:13:33 IST 2018
source :https://www.tutorialspoint.com/python3/string_split.htm
The split() method returns a list of all the words in the string, using str as the separator
(splits on all whitespace if left unspecified), optionally limiting the number of splits to num
"""
text = "cat|dog|elephant|zoo|monkey|cat|dog|dog"

print(text.split('|', 2))  # it splits the given string based on the argument we are given by default it is space
print(text.split('|'))
