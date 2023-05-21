from vehiculo import *
import csv
def pt1():
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

def pt2():
    vehiculo_base = Vehiculo("marca","modelo",4) 
    auto_base = Automovil("marca","modelo",4,velocidad=100,cilindrada=800)
    auto_particular = Particular("Ford","Fiesta",4,velocidad=180,cilindrada=500,num_puestos=5)
    auto_carga = Carga("Daft Trucks","G 38",10,velocidad=120,cilindrada=1_000,peso=20_000)
    bicicleta = Bicicleta("Shimano","MT Ranger",2, tipo="Carrera")
    motocicleta = Motocicleta("BMW","F800s",2,tipo="Deportiva",motor="2T",cuadro="Doble Viga",nro_radios=21)
    
    objetos = [vehiculo_base,auto_base,auto_particular,auto_carga,bicicleta,motocicleta]
    clases = [Vehiculo,Automovil,Particular,Carga,Bicicleta,Motocicleta]
    
    for obj in objetos:
        print(obj)
        
    for cls in clases:
        print(f"\nMotocicleta es instancia con relacion a {cls.__name__}?: {isinstance(motocicleta,cls)}")



def main():
    # pt1()
    # pt2()
    ...
    
main()