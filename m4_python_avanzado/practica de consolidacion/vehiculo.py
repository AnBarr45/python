import csv
# ################################## PARTE 1 #################################### #
class Vehiculo:
    def __init__(self, marca: str, modelo: str, num_ruedas: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas
    def __str__(self) -> str:
        return f"| Marca: {self.marca} | Modelo: {self.modelo} | {self.num_ruedas} Ruedas |"
    
    def guardar_datos_csv(self,archivo_destino):
        archivo = open(archivo_destino, "w")
        datos = [(self.__class__, self.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()
    def leer_datos_csv(self,archivo):
        vehiculos = []
        archivo = open(archivo, "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            vehiculos.append(vehiculo)
        archivo.close()
        return vehiculos
##########################################################
class Automovil(Vehiculo):
    def __init__(self,*args, velocidad: int, cilindrada: int) -> None:
        super().__init__(*args)   
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self) -> str:
        return super().__str__() + f" {self.velocidad} km/hr | {self.cilindrada} cc |"
# ################################## PARTE 2 #################################### #
class Particular(Automovil):
    def __init__(self, *args, num_puestos: int , **kwargs) -> None:
        self.num_puestos = num_puestos
        super().__init__(*args, **kwargs)
        
    def __str__(self) -> str:
        return super().__str__() + f" {self.num_puestos} Puestos |"
##########################################################
class Carga(Automovil):
    def __init__(self,*args, peso: int, **kwargs) -> None: 
        super().__init__(*args, **kwargs)
        self.peso_carga = peso
    def __str__(self) -> str:
        return super().__str__() + f" {self.peso_carga} kgs |"
##########################################################
class Bicicleta(Vehiculo):      
    def __init__(self, *args,tipo: str, **kwargs) -> None: 
        self.tipo = tipo # Urbana o Carrera
        super().__init__(*args,**kwargs)
    def __str__(self) -> str:
        return super().__str__() + f" Tipo: {self.tipo} |"
##########################################################
class Motocicleta(Bicicleta):
    def __init__(self, *args, nro_radios: int, cuadro: str, motor: str, **kwargs) -> None:
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
        super().__init__(*args, **kwargs)
    def __str__(self) -> str:
        return super().__str__() +f" Motor: {self.motor} | Cuadro: {self.cuadro} | Nro Radios: {self.nro_radios} |"