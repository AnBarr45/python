import clases

def instanciar_vehiculo(i: int):
    print(f"\nDatos del automovil {i + 1}")
    marca = input("-Inserte la marca del automovil: ")
    modelo = input("-Inserte el modelo del automovil: ")
    n_ruedas = input("-Inserte el numero de ruedas del automovil: ")
    velocidad = int(input("-Inserte la velocidad del automovil en km/hr: "))
    cilindraje = int(input("-Inserte el cilindraje del automovil: "))
    
    instancia = clases.Automovil(marca,modelo,n_ruedas,velocidad,cilindraje)
        
    
    return instancia


def main():
    n_vehiculos = int(input("Cuantos Vehiculos desea insertar: " ))
    tmp_array = []
    for i in range(0,n_vehiculos):
        v = instanciar_vehiculo(i + 1)
        tmp_array.append(v)
        
    for idx in range(0,len(tmp_array)):
        print(f"\nDatos del automovil {idx} => {tmp_array[idx]}")




main()