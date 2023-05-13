# ################################## PARTE 1 #################################### #
class Vehiculo:
    def __init__(self, marca: str, modelo: str, num_ruedas: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def __str__(self) -> str:
        return f"|Marca: {self.marca}| Modelo: {self.modelo} | {self.num_ruedas} Ruedas |"
    
    
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

class Carga(Automovil):
    def __init__(self,*args, peso: int, **kwargs) -> None: 
        super().__init__(*args, **kwargs)
        self.peso_carga = peso
    def __str__(self) -> str:
        return super().__str__() + f" {self.peso_carga} kgs |"
    
class Bicicleta(Vehiculo):      
    def __init__(self, *args, **kwargs) -> None: 
        super().__init__(*args,**kwargs)
    def __str__(self) -> str:
        return super().__str__()
    
class Urbana(Bicicleta):

    def __init__(self, *args, **kwargs) -> None: 
        super().__init__(*args,**kwargs)
    def __str__(self) -> str:
        return super().__str__()
    
class Carrera(Bicicleta):
    def __init__(self, *args, **kwargs) -> None: 
        super().__init__(*args, **kwargs)
    def __str__(self) -> str:
        return super().__str__()
    
class Motocicleta(Bicicleta):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def __str__(self) -> str:
        return super().__str__()