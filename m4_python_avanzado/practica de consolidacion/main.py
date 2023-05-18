from vehiculo import *
def pt1():
    lista_autos = [] 
    for i in range(1,4):
        print(f"Ingrese los datos del vehiculo {i} => ")
        marca = input("Inserte la marca del vehiculo: ")
        modelo = input("Inserte la modelo del vehiculo: ")
        nro_ruedas = int(input("Inserte el numero de ruedas del vehiculo: "))
        velocidad = int(input("Inserte la velocidad del vehiculo: "))
        cilindrada = int(input("Inserte la cilindrada del vehiculo: "))
        obj = Automovil(marca,modelo,nro_ruedas,velocidad=velocidad,cilindrada=cilindrada)
        lista_autos.append(obj)
        
    for i in range(0,3):
        print(f"Datos del vehiculo {i + 1}")
        print(lista_autos[i])

def pt2():
    
    vehiculo_base = Vehiculo("marca","modelo",4) 
    auto_base = Automovil("marca","modelo",4,velocidad=100,cilindrada=800)
    auto_particular = Particular("Ford","Fiesta",4,velocidad=180,cilindrada=500,num_puestos=5)
    auto_carga = Carga("Daft Trucks","G 38",10,velocidad=120,cilindrada=1_000,peso=20_000)
    bicicleta = Bicicleta("Shimano","MT Ranger",2, tipo="Carrera")
    motocicleta = Motocicleta("BMW","F800s",2,tipo="Deportiva",nro_radios=1,motor="2T",cuadro="Doble Viga")
    print(vehiculo_base)
    print(auto_base)
    print(auto_particular)
    print(auto_carga)
    print(bicicleta)
    print(motocicleta)


def main():
    pt1()
    
    
main()