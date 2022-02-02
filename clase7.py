userToSearch = input("Enter name to be searched")

mylist = [{"nombre": "Lari", "edad": 19, "profesion": "programadora", "main-linea-lol": "Mid"}, {"nombre": "Leo", "edad": 22, "profesion": "Developer", "main-linea-lol": "Mid"}, {"nombre": "Gaston", "edad": 22, "profesion": "Cocinero", "main-linea-lol": "Supp"}, {"nombre": "Yahia", "edad": 21, "profesion": "Programador", "main-linea-lol": "Mid"}]
print(mylist)

for item in mylist:
    
    if str.lower(item["nombre"]) == userToSearch:
        print("I found you, " + item["nombre"])
        exit()

    else:
        print(item["nombre"])



#elif "nombre" != "Lari":
    #print(item)#


    #if "nombre" == "Lari"
    #print("hello")#
