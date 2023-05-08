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

    
