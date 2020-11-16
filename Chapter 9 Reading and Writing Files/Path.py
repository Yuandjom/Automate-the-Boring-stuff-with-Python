import os 
from pathlib import Path
print(os.getcwd())
print(Path.cwd()) #getting the current working directory
os.chdir('C:\\Users')
print(Path.cwd())
print(Path.home())
print(os.getcwd()) #getting the current working directory
os.chdir(r'C:\Users\ziyan\OneDrive\Desktop\Trying to test out bro') #making a new folder
print(os.getcwd())
currentpath = os.getcwd()
print(os.path.basename(currentpath)) #base name is the end of the file ; Trying to test out bro
print(os.path.dirname(currentpath)) #C:\Users\ziyan\OneDrive\Desktop\