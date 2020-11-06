while True :
    print("Enter your age : ")
    age = input()
    try:
        age = int(age)
    except:
        print("Please use numeric digits!")
        continue
    if int(age) < 1 :
        print("Please print a positive number.")
        continue
    break

print(f'Your age is {age}')
