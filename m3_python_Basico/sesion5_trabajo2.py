
palabra = "paralelepípedo"
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
pos = []
consonantes = []


for i,el in enumerate(palabra):
    if el in vocales:
        continue
    else:
        consonantes.append(el)
        pos.append(i)

for i,el in enumerate(consonantes):
    print(f"consonante {el} : posición {pos[i]}")