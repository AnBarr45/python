from pt2 import *

def parte3():
    vehiculos = parte2(1)
    for vh in vehiculos:
        vh.guardar_datos_csv(".\\vehiculos.csv")
        
    print("############################## PARTE 3 ################################### \n") 
    Vehiculo.leer_datos_csv(".\\vehiculos.csv")