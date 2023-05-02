class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza 
        self.edad= edad
        self.peso = peso 

    def comer(self):
        ...
      
    def caminar(self):
        ...
            
    def dormir(self):
        ...

def main():
    perro = Animal("Brando",3,"San Bernardo",30)
    gato = Animal("Roll",4,"Persa",3)

    print(type(perro))
    print(type(gato))

main()