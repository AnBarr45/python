# ################################## PARTE 1 #################################### #
class Vehiculo:
    def __init__(self,marca, modelo, num_ruedas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

class Automovil(Vehiculo):
    def __init__(self,*args,**kwargs) -> None:
        self.velocidad = int(input("-Inserte la velocidad del automovil en km/hr: "))
        self.cilindrada = int(input("-Inserte el cilindraje del automovil: "))
        
        super(Automovil,self).__init__(*args,**kwargs)
        
    def __str__(self) -> str:
        return f"|Marca: {self.marca}| Modelo: {self.modelo} | {self.num_ruedas} Ruedas | {self.velocidad} km/hr | {self.cilindrada} cc|"
        
# ################################## PARTE 2 #################################### #
class Particular(Automovil):
    def __init__(self,num_puestos,*args,**kwargs) -> None:
        self.num_puestos = num_puestos
        super(Particular,self).__init__(*args,**kwargs)

class Carga(Automovil):
    def __init__(self,peso_carga,*args,**kwargs) -> None:
        self.peso_carga = peso_carga
        super(Carga,self).__init__(*args,**kwargs)

class Bicicleta(Vehiculo):   
    def __init__(self,*args,**kwargs) -> None:
        super(Bicicleta,self).__init__(*args,**kwargs)
        
class Urbana(Bicicleta):
    def __init__(self,*args,**kwargs) -> None:
        super(Urbana,self).__init__(*args,**kwargs)

class Carrera(Bicicleta):
    def __init__(self,*args,**kwargs) -> None:
        super(Carrera,self).__init__(*args,**kwargs)

class Motocicleta(Bicicleta):
    def __init__(self,*args,**kwargs) -> None:
        super(Motocicleta,self).__init__(*args,**kwargs)