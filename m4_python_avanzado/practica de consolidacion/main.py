import vehiculo

def main():
    obj1 = vehiculo.Vehiculo("marca","modelo",4)
    obj2 = vehiculo.Automovil("marca","modelo",4,velocidad=123,cilindrada=456)
    obj3 = vehiculo.Particular("marca","modelo",4,velocidad=123,cilindrada=456, num_puestos=1)
    obj4 = vehiculo.Carga("marca","modelo",4,velocidad=123,cilindrada=456, peso=7)
    obj5 = vehiculo.Bicicleta("marca","modelo",1)
    obj6 = vehiculo.Urbana("marca","modelo",1)
    obj7 = vehiculo.Motocicleta("marca","modelo",2)
    
    
    print(f"\nDatos del vehiculo => {1}:\n{obj1}")
    print(f"\nDatos del vehiculo => {2}:\n{obj2}")
    print(f"\nDatos del vehiculo => {3}:\n{obj3}")
    print(f"\nDatos del vehiculo => {4}:\n{obj4}")
    print(f"\nDatos del vehiculo => {5}:\n{obj5}")
    print(f"\nDatos del vehiculo => {6}:\n{obj6}")
    print(f"\nDatos del vehiculo => {7}:\n{obj7}")
        
main()