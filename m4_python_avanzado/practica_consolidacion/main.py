from vehiculo import *
import csv
from pt1 import *
from pt2 import *

def main():
    parte1()
    vehiculos = parte2()
    
    # for vh in vehiculos:
    #     vh.guardar_datos_csv("m4_python_avanzado\\practica_consolidacion\\vehiculos.csv")
    
    Vehiculo.leer_datos_csv("m4_python_avanzado\\practica_consolidacion\\vehiculos.csv")

main()