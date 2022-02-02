username = input("Enter your username")
password = input("Enter your password")

users = [{"username": "Maria", "password": "123maria"}, {"username": "Pepe", "password": "123pepe"}, {"username": "Juan", "password": "123juan"}]
print(users) 

for item in users:

    if (item["username"]) == username:
        if (item["password"] == password):
            print("congrats you are logged in")
        else: 
            print("wrong password")

userToSearch = input("Enter name to be searched")

mylist = [{"nombre": "Lari", "edad": 19, "profesion": "programadora", "main-linea-lol": "Mid"}, {"nombre": "Leo", "edad": 22, "profesion": "Developer", "main-linea-lol": "Mid"}, {"nombre": "Gaston", "edad": 22, "profesion": "Cocinero", "main-linea-lol": "Supp"}, {"nombre": "Yahia", "edad": 21, "profesion": "Programador", "main-linea-lol": "Mid"}]
print(mylist)

for item in users:
    
    if str.lower(item["username"]) == userToSearch:
        print("I found you, " + item["nombre"])
        exit()

    else:
        print(item["username"])


# if users == login:
#print username + password