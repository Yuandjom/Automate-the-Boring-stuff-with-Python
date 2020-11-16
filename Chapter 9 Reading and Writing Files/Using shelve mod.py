import shelve 
shelffile = shelve.open('mydata') #store in binary file 
cats =['Zophie ', 'Pooka', 'Simon']
shelffile['cats'] = cats #like dictionary key n value
shelffile.close() 
#shelve have key and value method 
#eg . shelffile.keys()
#eg . shelffile.values()