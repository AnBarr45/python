class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza 
        self.edad= edad
        self.peso = peso 


def main():
    Caballo = Animal("Zeus","Pura Sangre",5,450)
    Leon = Animal("Boulder","Atlas",10,130)



main()