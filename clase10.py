from unittest import result

def login (username, password):

    users = [{"username": "Maria", "password": "123maria"}, {"username": "Pepe", "password": "123pepe"}, {"username": "Juan", "password": "123juan"}]
    print(users) 

    for item in users:

        if (item["username"]) == username:
            if (item["password"] == password):
                print("congrats you are logged in")
            else: 
                print("wrong password")

username = input("Enter your username")
password = input("Enter your password")

loginExec = login(username, password)

def search_engine(userTosearch):
    
    
    
    users = [{"username": "Maria", "password": "123maria"}, {"username": "Pepe", "password": "123pepe"}, {"username": "Juan", "password": "123juan"}]
    print(users)

    for item in users:
    
        if str.lower(item["username"]) == userToSearch:
            print("I found you, " + item["username"])
            exit()

        else:
            print(item["username"])
            
userToSearch = input("Enter name to be searched")
searchExec = search_engine(userToSearch)


