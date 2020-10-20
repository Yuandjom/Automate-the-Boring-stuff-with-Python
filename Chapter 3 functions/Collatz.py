def collatz():
    try:
        number = int(input("Input an integer value.\n"))
        while number != 1:
            if number % 2 == 0 :
                number = int(number /2 )
                print(number)            
            elif number % 2 == 1:
                number = int(3 * number + 1 )
                print(number)
        
    except ValueError:
        print("Please input only integer values.")


collatz()
