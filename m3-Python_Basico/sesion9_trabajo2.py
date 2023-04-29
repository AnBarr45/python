def suma(n1,n2):
     return n1 + n2
def resta(n1,n2):
    return n1 - n2
def multiplicacion(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
def aritmetica(n1,n2):
    return (suma(n1,n2),resta(n1,n2),multiplicacion(n1,n2),division(n1,n2))

def main():
    num1,num2 = 56,14 
    claves = ["Suma","Resta","Multiplicación","División"]
    mi_dict = {k:v for k,v in zip(claves,aritmetica(num1,num2))}

    #decomentar para ver el resultado 
    #print(mi_dict)


main()