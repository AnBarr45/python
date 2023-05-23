from vehiculo import Automovil

def parte1():
    lista_autos = [] 
    for i in range(0,3):
        print(f"\nIngrese los datos del vehiculo {i} => ")
        marca = input("Inserte la marca: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el numero de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        obj = Automovil(marca,modelo,nro_ruedas,velocidad=velocidad,cilindrada=cilindrada)
        lista_autos.append(obj)
        
    print("\nImprimiendo por pantalla los vehiculos: \n")
    
    for i in range(0,3):
        print(f"Datos del vehiculo {i + 1}: ", end="")
        print(lista_autos[i], "\n")
