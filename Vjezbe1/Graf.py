import matplotlib.pyplot as plt
def tocke(a, b, n, g):
    T1=a.split(",")
    T2=b.split(",")
    xpoint=(T1[0], T2[0])
    ypoint=(T1[1], T2[1])
    plt.plot(xpoint, ypoint)
    plt.title(n)
    if g==1:
        plt.show()
    else:
        plt.savefig("graf.pdf")
A=input("Unesi prvu točku (x1, y1): ")
B=input("Unesi drugu točku (x2, y2): ")
G=int(input("1 ako želiš sliku na ekranu, bilo što drugo ako želiš pdf: "))
N=input("Naslov grafa: ")
tocke(A, B, N, G)