from vehiculo import Automovil

def parte1() -> None:
    marcas = ["Toyota","Fiat","Ford"]
    modelos = ["Yaris","Palio"]
    ruedas = [4,4,4]
    v = [120,95,125]
    cc = [800,1200,1500]
    lista_autos = [] 
    
    for i in range(0,3):
        print(f"\nIngrese los datos del vehiculo {i} => ")
        print(f"Inserte la marca: {marcas[i]}")
        print(f"Inserte el modelo: {modelos[i]}")
        print(f"Inserte el numero de ruedas: {ruedas[i]}")
        print(f"Inserte la velocidad en km/h: {v[i]}")
        print(f"Inserte el cilindraje en cc: {cc[i]}")
        
        obj = Automovil(marcas[i],modelos[i],ruedas[i],velocidad=v[i],cilindrada=cc[i])
        lista_autos.append(obj)
        
    print("\nImprimiendo por pantalla los vehiculos: \n")
    
    for i in range(0,3):
        print(f"Datos del vehiculo {i + 1}: ", end="")
        print(lista_autos[i], "\n")
