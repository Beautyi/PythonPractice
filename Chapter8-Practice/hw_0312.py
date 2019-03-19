database = {}
while True:
    cmd = input("Please input command:\n")

    if cmd == "add" or cmd == "update":
        name = input("Please input name:\n")
        address = input("Please input address:\n")

        phone_number = input("Please input phone_number:\n")
        database[name] = {"address": address, "phone_number": phone_number}
    elif cmd == "delete":
        name = input("Please input name:\n")
        if str(name) not in database:
            print("Sorry, " + str(name) + " cannot be found,please try again.")
        else:
            del database[name]
    elif cmd == "query":
        name = input("Please input name:\n")
        print(database[name])
    elif cmd == "quit":
        break
    else:
        print("Unknown command")
