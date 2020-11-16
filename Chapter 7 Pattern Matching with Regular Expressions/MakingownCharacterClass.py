import re 

vowelRegex = re.compile(r'[aeiouAEIOU]') #trying to match the letter and return list of letters found 
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo) #['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

vowelRegex = re.compile(r'[^aeiouAEIOU]') # ^ means character not inside
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

#Matching newlines with the dot character 
noNewlineRegex = re.compile('.*',re.DOTALL) #.* means match everything
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())