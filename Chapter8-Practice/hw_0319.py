#改写database 把增删改查的逻辑分别写到函数中去
database = {}
while True:
    cmd = input("Please input command:\n")

    if cmd == "add" or cmd == "update":
        def add_name():
            """让用户增加或者修改名字"""
            mg_add_name = input("Please input name:\n")
            print(mg_add_name)


        add_name()

        def add_address():
            mg_add_address = input("Please input address:\n")
            print(mg_add_address)


        add_address()

        def add_phone_number():
            mg_add__phone_number = input("Please input phone_number:\n")
            print(mg_add__phone_number)


        add_phone_number()

        database[add_name] = {"address": add_address(), "phone_number": add_phone_number()}

    elif cmd == "delete":
        def delete_name():
            mg_delete_name = input("Please input name:\n")
            print(mg_delete_name)


        delete_name()

        if str(delete_name()) not in database:
            print("Sorry, " + str(delete_name()) + " cannot be found,please try again.")
        else:
            del database[delete_name()]
    elif cmd == "query":
        def query_name():
            mg_query_name = input("Please input name:\n")
            print(mg_query_name)


        query_name()

        print(database[query_name()])

    elif cmd == "quit":
        break
    else:
        print("Unknown command")
