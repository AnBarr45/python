class Seleccion_Futbol:
    def __init__(self, id, nombre, apellidos, edad) -> None:
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad


    def concentrarse(self):
        ...

    def viajar(self):
        ...

class Futbolista(Seleccion_Futbol):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion) -> None:
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion

    def jugar_partido(self):
        ...
    def entrenar(self):
        ...



class Entrenador(Seleccion_Futbol):
    def __init__(self, id, nombre, apellidos, edad,id_federacion) -> None:
        super().__init__(id, nombre, apellidos, edad)
        self.id_federacion = id_federacion
    def dirigir_partido(self):
        ...
    def dirigir_entrenamiento(self):
        ...


class Masajista(Seleccion_Futbol):
    def __init__(self, id, nombre, apellidos, edad,titulacion,annos_exp) -> None:
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.annos_exp = annos_exp
    def dar_masajes(self):
        ...