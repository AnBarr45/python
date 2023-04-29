def positivo_o_negativo(n):
    if n < 0:
        return "negativo"
    return "positivo"

def num_check(n: int) -> str:
    r = positivo_o_negativo(n)
    if n == 0:
        return "El número es cero"
    if n % 2 == 0:
         return f"El número es par y {r} "
    return f"El número es impar y {r}"
     

def main():
    n = int(input("Elija un número: "))
    print(num_check(n))

main()