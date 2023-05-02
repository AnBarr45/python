def funcionquehacealgo(l):
    n1,n2,n3 = l[0],l[1],l[2]
    return (n1 + n2 + n3 , n1 - (n2 + n3))

def main():
    n_list = [1,4,6]

    print(funcionquehacealgo(n_list))


main()