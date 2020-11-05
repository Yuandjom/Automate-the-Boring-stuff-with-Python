import re 

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

#Matching newlines with the dot character 
noNewlineRegex = re.compile('.*',re.DOTALL)
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())