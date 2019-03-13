database = {}
while True:
    cmd = input("Please input command:\n")
    
    if cmd == "add":
        name = input("Please input name:\n")
        if name not in database:
            address = input("Please input address:\n")
            phone_number = input("Please input phone_number:\n")
            database[name] = {"address":address, "phone_number":phone_number}
        else:
            print("{} has already in database!".format(name))

    elif cmd == "update":
        name = input("Please input name:\n")
        if name in database:
            address = input("Please input address:\n")
            phone_number = input("Please input phone_number:\n")
            database[name] = {"address":address, "phone_number":phone_number}
        else:
            print("{} is not in database!".format(name))

    elif cmd == "delete":
        name = input("Please input name:\n")
        if name in database:
            del database[name]
        else:
            print(name + " is not in database!")   
 
    elif cmd == "query":
        name = input("Please input name:\n")
        if name in database:
            print(database[name])
        else:
            print(name + " is not in database!")   

    elif cmd == "query all":
        print("{} people in the database!".format(len(database)))
        for key, value in database.items():
            print("name: {}, address : {}, phone_number : {}".format(key, value['address'], value['phone_number']))

    elif cmd == "quit":
        break
        
    else:
        print("Unknown command")
        
