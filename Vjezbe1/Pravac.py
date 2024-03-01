def tocke(a, b):
    T1=a.split(",")
    T2=b.split(",")
    k=(int(T2[1])-int(T1[1]))/(int(T2[0])-int(T1[0]))
    l=-k*int(T1[0])+int(T1[0])
    print("y={}x+{}".format(k,l))
A=input("Unesi prvu točku (x1, y1): ")
B=input("Unesi drugu točku (x2, y2): ")
tocke(A, B)