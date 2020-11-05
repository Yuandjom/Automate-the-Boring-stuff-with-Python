import re

haRegex = re.compile(r'(Ha){3,5}') #greedy matching 
mo = haRegex.search('He said "HaHaHaHaHa"')
print(mo.group())

haRegex = re.compile(r'(Ha){3,5}?') #non- greedy matching 
mo = haRegex.search('He said "HaHaHaHaHa"')
print(mo.group())