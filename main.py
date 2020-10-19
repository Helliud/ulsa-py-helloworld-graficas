from User import User

print("Hola")

variable1 = 'si'
print(variable1)

num = 1
print(num)

if (1 < 0):
    print("Es menor")
else:
    print("Es mayor")
    
vector1 = ["Joel", "Eliud", "Ana", "La otra Ana", "Pancho", "Karen", "Pablito"]
print(vector1[0])

movies = ["The warriors", "Amores Perros", "Emojis", "Toy Story", "Rattatouille", "Robert Pattison te odio"]
print(movies)

for m in movies:
    m = m + " (Clasificacion: R)"
    print(m)

    def showName():
        print('nombre perron: Jesus')

user1 = User("Pancho", 40, "waifuhunter@gmail.com")
print(user1.name)
user1.getInfo()

showName()