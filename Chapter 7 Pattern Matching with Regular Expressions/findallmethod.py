import re 

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #has no group , (r'') the r means raw string 
mo = phoneRegex.findall('CELL: 415-444-9999 WORK : 212-555-9000')
print(mo) # no need gorup 
# return ['415-444-9999', '212-555-9000']
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #has groups 
mo = phoneRegex.findall('CELL: 415-444-9999 WORK : 212-555-9000')
print(mo)
#return [('415', '444-9999'), ('212', '555-9000')]