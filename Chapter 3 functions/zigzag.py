import time , sys 
indent = 0 #how many spaces to indent 
indentIncreasing = True 

try :
    while True : #the main loop
        print(" "* indent, end='')
        print("********")
        time.sleep(0.1)

        if indentIncreasing:
            #increase the number of spaces 
            indent += 1 
            if indent == 20:
                indentIncreasing = False
        
        else:
            #decrease the number of spaces 
            indent -= 1 
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
