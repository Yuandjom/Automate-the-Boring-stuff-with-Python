import sys 

while True :
    print("Type exit to exit.")
    response = input()
    if response == 'exit':
        sys.exit()
    print("You have typed" + response +'.')