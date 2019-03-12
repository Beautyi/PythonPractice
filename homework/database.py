database = {}
while True:
    cmd = input("Please input command:\n")
    
    if cmd == "add" or cmd == "update":
        name = input("Please input name:\n")
        address = input("Please input address:\n")
        phone_number = input("Please input phone_number:\n")
        database[name] = {"address":address, "phone_number":phone_number}

    elif cmd == "delete":
        name = input("Please input name:\n")
        del database[name]    
 
    elif cmd == "query":
        name = input("Please input name:\n")
        print(database[name])

    elif cmd == "quit":
        break
        
    else:
        print("Unknown command")
        
        
'''
Please input command:
ddd
Unknown command
Please input command:
add
Please input name:
tony
Please input address:
beijing
Please input phone_number:
123456
Please input command:
add
Please input name:
jack
Please input address:
shanghai
Please input phone_number:
987654
Please input command:
query
Please input name:
tony
{'address': 'beijing', 'phone_number': '123456'}
Please input command:
delete
Please input name:
tony
Please input command:
update
Please input name:
jack
Please input address:
hangzhou
Please input phone_number:
5555
Please input command:
query
Please input name:
jack
{'address': 'hangzhou', 'phone_number': '5555'}
Please input command:
quit

'''
