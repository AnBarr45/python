from vehiculo import *

def main():
    vehiculo_base = Vehiculo("marca","modelo",4) 
    auto_base = Automovil("marca","modelo",4,velocidad=100,cilindrada=800)
    auto_particular = Particular("Ford","Fiesta",4,velocidad=180,cilindrada=500,num_puestos=5)
    auto_carga = Carga("Daft Trucks","G 38",10,velocidad=120,cilindrada=1_000,peso=20_000)
    bicicleta = Bicicleta("Shimano","MT Ranger",2, tipo="Carrera")
    motocicleta = Motocicleta("BMW","F800s",2,tipo="Deportiva",nro_radios=1,motor="2T",cuadro="Doble Viga")
    
main()