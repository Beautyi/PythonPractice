#向数据库中添加一条记录
#第一个参数为数据库字典
def addRecord(dbdict):
    name = input("Please input name:\n")
    if name not in dbdict:
        address = input("Please input address:\n")
        phone_number = input("Please input phone_number:\n")
        dbdict[name] = {"address":address, "phone_number":phone_number}
    else:
        print("{} has already in database!".format(name))



#更新记录
#第一个参数为数据库字典
def updateRecord(dbdict):
    name = input("Please input name:\n")
    if name in dbdict:
        address = input("Please input address:\n")
        phone_number = input("Please input phone_number:\n")
        dbdict[name] = {"address":address, "phone_number":phone_number}
    else:
        print("{} is not in database!".format(name))


#删除记录
#第一个参数为数据库字典
def deleteRecord(dbdict):
        name = input("Please input name:\n")
        if name in dbdict:
            del dbdict[name]
        else:
            print(name + " is not in database!")   


#查询记录详细信息
#第一个参数为数据库字典
def queryRecord(dbdict):
    name = input("Please input name:\n")
    if name in dbdict:
        print(dbdict[name])
    else:
        print(name + " is not in database!")   


#查询所有记录
#第一个参数为数据库字典
def queryAllRecord(dbdict):
    print("{} people in the database!".format(len(dbdict)))
    for key, value in dbdict.items():
        print("name: {}, address : {}, phone_number : {}".format(key, value['address'], value['phone_number']))

        
database = {}
while True:
    cmd = input("Please input command:\n")
    if cmd == "add":
        addRecord(database)
    elif cmd == "update":
        updateRecord(database)
    elif cmd == "delete":
        deleteRecord(database)
    elif cmd == "query":
        queryRecord(database)
    elif cmd == "query all":
        queryAllRecord(database)
    elif cmd == "quit":
        break  
    else:
        print("Unknown command")


