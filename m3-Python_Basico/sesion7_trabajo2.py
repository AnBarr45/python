



def main():
    l = [[1,2,3],[0,4,5],[4,0,1],[6,5,4]]

    for _,el in enumerate(l):
        if 0 == el[0]:
            continue
        elif 0 in el:
            el.pop(el.index(0))
        
        print(el)


main()