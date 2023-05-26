from pt1 import *
from pt2 import *
from pt3 import *

def main():
    print("Que parte desea ejecutar? (pt1, pt2 o pt3):")
    pt = int(input("numero:"))
    
    
    if pt == 1: parte1()
    elif pt == 2: parte2()
    elif pt == 3: parte3()
    else:
        exit("el numero debe ser 1, 2 o 3")
main()