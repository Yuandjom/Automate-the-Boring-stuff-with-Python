while True :
    print("Who are you?")
    name = input()
    if name != "joe":
        continue
    print("Hello joe . What is the password? ")
    password = input()
    if password == "swordfish":
        break
print("acess granted")