from vehiculo import *
def pt1():
    lista_autos = [] 
    for i in range(1,4):
        print(f"\nIngrese los datos del vehiculo {i} => ")
        marca = input("Inserte la marca del vehiculo: ")
        modelo = input("Inserte el modelo del vehiculo: ")
        nro_ruedas = int(input("Inserte el numero de ruedas del vehiculo: "))
        velocidad = int(input("Inserte la velocidad del vehiculo: "))
        cilindrada = int(input("Inserte la cilindrada del vehiculo: "))
        obj = Automovil(marca,modelo,nro_ruedas,velocidad=velocidad,cilindrada=cilindrada)
        lista_autos.append(obj)
        
    print("Imprimiendo por pantalla los vehiculos: ")
    
    for i in range(0,3):
        print(f"\nDatos del vehiculo {i + 1}")
        print(lista_autos[i])

def pt2():
    vehiculo_base = Vehiculo("marca","modelo",4) 
    auto_base = Automovil("marca","modelo",4,velocidad=100,cilindrada=800)
    auto_particular = Particular("Ford","Fiesta",4,velocidad=180,cilindrada=500,num_puestos=5)
    auto_carga = Carga("Daft Trucks","G 38",10,velocidad=120,cilindrada=1_000,peso=20_000)
    bicicleta = Bicicleta("Shimano","MT Ranger",2, tipo="Carrera")
    motocicleta = Motocicleta("BMW","F800s",2,tipo="Deportiva",motor="2T",cuadro="Doble Viga",nro_radios=21)
    print(vehiculo_base)
    print(auto_base)
    print(auto_particular)
    print(auto_carga)
    print(bicicleta)
    print(motocicleta)
    print(f"\nMotocicleta es instancia con relacion a Vehiculo?: {isinstance(motocicleta,Vehiculo)}")
    print(f"Motocicleta es instancia con relacion a Automovil?: {isinstance(motocicleta,Automovil)}")
    print(f"Motocicleta es instancia con relacion a Vehiculo Particular?: {isinstance(motocicleta,Particular)}")
    print(f"Motocicleta es instancia con relacion a Vehiculo de Carga?: {isinstance(motocicleta,Carga)}")
    print(f"Motocicleta es instancia con relacion a Bicicleta?: {isinstance(motocicleta,Bicicleta)}")
    print(f"Motocicleta es instancia con relacion a Motocicleta?: {isinstance(motocicleta,Motocicleta)}")


def main():
    # pt1()
    pt2()
    
main()