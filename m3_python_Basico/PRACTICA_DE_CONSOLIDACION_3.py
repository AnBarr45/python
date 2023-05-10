def hacer_grandioso(lista):  
    for idx,nombre in enumerate(lista):
        lista[idx] = f"El gran {nombre}"
    

def imprimir_nombres(grupo, lista_nombres):
    print(f"\n{grupo}:")
    for nombre in lista_nombres:    
        print("-",nombre)

def main():
    l = ["Harry Houdini","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pele","Juanes"]
    magos = [l[0],l[2],l[5]]
    cientificos = [l[1],l[3],l[-3]] 
    otros = [l[4],l[-2],l[-1]]

    hacer_grandioso(magos)

    imprimir_nombres("Lista original",l)
    imprimir_nombres("Magos",magos)
    imprimir_nombres("Científicos",cientificos)
    imprimir_nombres("Restantes",otros)
    
main()