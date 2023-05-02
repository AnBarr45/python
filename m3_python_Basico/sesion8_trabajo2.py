
def main():
    l = [[1,2,3],[0,4,5],[4,0,1],[6,5,4]]
    claves = "ABCD"
    mi_dict = {k:v for k,v in zip(claves,l)}

    for _,el in enumerate(l):
        if 0 == el[0]:
            continue
        elif 0 in el:
            el.pop(el.index(0))
        
        print(el)
    for k in mi_dict:
        print(f"{k}:{mi_dict.get(k)}")

main()