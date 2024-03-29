def suma(N):
    Result=5
    for i in range(0, N):
        Result=Result+(1/3)
    for j in range(0, N):
        Result=Result-(1/3)
    print(Result)
suma(200)
suma(2000)
suma(20000)
#Rezultati se razlikuju zbog toga što je konačni rezultat prve petlje u svakom zadatku različit decimalni broj koji nema isti binarni zapis.