import re 

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #has no group 
mo = phoneRegex.findall('CELL: 415-444-9999 WORK : 212-555-9000')
print(mo) # no need gorup 

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #has groups 
mo = phoneRegex.findall('CELL: 415-444-9999 WORK : 212-555-9000')
print(mo)