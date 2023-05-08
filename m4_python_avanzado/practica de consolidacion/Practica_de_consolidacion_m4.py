class Vehiculo:
    def __init__(self,marca,modelo,numero_ruedas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas,velocidad,cilindrada) -> None:
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        super().__init__(marca, modelo, numero_ruedas)
        
    def __str__(self) -> str:
        tmp = super().__str__()
        return f"Datos del automovil => Marca: {self.marca}, Modelo: {self.modelo}, {self.numero_ruedas} Ruedas,{self.velocidad} km/hr, {self.cilindrada} cc"


    
def instanciar_vehiculos(n_vehiculos: int):
    v_array = []
    for _ in range(0,n_vehiculos):
        marca = input("Inserte la marca del automovil: ")
        modelo = input("Inserte el modelo del automovil: ")
        n_ruedas = input("Inserte el numero de ruedas del automovil: ")
        velocidad = int(input("Inserte la velocidad del automovil en km/hr: "))
        cilindraje = int(input("Inserte el cilindraje del automovil: "))
        
        instancia = Automovil(marca,modelo,n_ruedas,velocidad,cilindraje)
        v_array.append(instancia) 
    
    return v_array


def main():
    n_vehiculos = int(input("Cuantos Vehiculos desea insertar: "))
    vehiculo_instancias = instanciar_vehiculos(n_vehiculos)
    for i in vehiculo_instancias:
        print(i)
main()