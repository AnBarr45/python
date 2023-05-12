# ################################## PARTE 1 #################################### #
class Vehiculo:
    def __init__(self,marca, modelo, num_ruedas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def __str__(self) -> str:
        return f"|Marca: {self.marca}| Modelo: {self.modelo} | {self.num_ruedas} Ruedas |"
    
    
class Automovil(Vehiculo):
    def __init__(self,marca,modelo,num_ruedas,velocidad, cilindrada ) -> None:
        super().__init__(marca,modelo,num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
        
    def __str__(self) -> str:
        return super().__str__() + f" {self.velocidad} km/hr | {self.cilindrada} cc|"
        
# ################################## PARTE 2 #################################### #
class Particular(Automovil):
    def __init__(self,num_puestos,*args,**kwargs) -> None:
        self.num_puestos = num_puestos
        super(Particular,self).__init__(*args,**kwargs)
        
    def __str__(self) -> str:
        return super().__str__() + f" {self.num_puestos} |"

class Carga(Automovil):
    def __init__(self,peso_carga,*args,**kwargs) -> None:
        self.peso_carga = peso_carga
        super(Carga,self).__init__(*args,**kwargs)

    def __str__(self) -> str:
        return super().__str__() + f" {self.peso_carga} |"
    
class Bicicleta(Vehiculo):   
    def __init__(self,*args,**kwargs) -> None:
        super(Bicicleta,self).__init__(*args,**kwargs)
        
    def __str__(self) -> str:
        return super().__str__()
    
class Urbana(Bicicleta):
    def __init__(self,*args,**kwargs) -> None:
        super(Urbana,self).__init__(*args,**kwargs)
    def __str__(self) -> str:
        return super().__str__()
    
class Carrera(Bicicleta):
    def __init__(self,*args,**kwargs) -> None:
        super(Carrera,self).__init__(*args,**kwargs)
    def __str__(self) -> str:
        return super().__str__()
    
class Motocicleta(Bicicleta):
    def __init__(self,*args,**kwargs) -> None:
        super(Motocicleta,self).__init__(*args,**kwargs)
    def __str__(self) -> str:
        return super().__str__()