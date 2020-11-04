#! python3  
# bulletPointAdder .py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard.
# how to run the code below 
#Make a .txt file
#Make a bunch of lists items and save it
#Now copy your lists items
#Open your terminal with the path file and run your PointAdder.py
#Return or open another .txt file and paste, you should get your list with a * on each line
import pyperclip
text = pyperclip.paste()

#TODO : Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n' .join(lines)
pyperclip.copy(text)