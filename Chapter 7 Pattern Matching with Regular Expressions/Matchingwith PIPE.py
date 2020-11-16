import re 

heroRegex= re.compile(r'Batman|Tina Fey') # | means or 
mo1 = heroRegex.search('Batman and Tina Fey')

print(mo1.group())

batRegex = re.compile(r'Bat(wo)?man') #optional matching 
batRegex = re.compile(r'Bat(wo)*man') #0 or more times
batRegex = re.compile(r'Bat(wo)+man') # one or more times

