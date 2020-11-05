
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

#Create a Regex for phone numbers
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?    #area code
(\s|-|\.)?    #separator 
(\d{3})    #first 3 digits 
(\s|-|\.)    #separator
(\d{4})    #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension
)''', re.VERBOSE)
#Create a Regex for email addresses
emailRegex = re.compile(r'''(
[a-zA-Z0-9.%_-]+ #username 
@ #@ symbol
[a-zA-Z0-9.-]+# domain name 
(\.[a-zA-Z]{2,4})# dot-something
)''', re.VERBOSE)
#Find matches in clipboard text.
text = str(pyperclip.paste())

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
allPhoneNumbers = []
for phonenumber in extractedPhone:
    allPhoneNumbers.append(phonenumber[0])
for Email in extractedEmail:
    allPhoneNumbers.append(Email[0])
#Copy results to the clipboard.
results = '\n'.join(allPhoneNumbers)
pyperclip.copy(results)