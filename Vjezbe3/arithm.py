import numpy as np
def aritmeticka_sredina(a, b, c, d, e, f, g, h ,i, j):
   Sum=(a+b+c+d+e+f+g+h+i+j)
   Avg=Sum/10
   print("Aritmetička sredina=", Avg)

def standardna_devijacija(a, b, c, d, e, f, g, h ,i, j):
    Sum=(a+b+c+d+e+f+g+h+i+j)
    Avg=Sum/10
    L=np.array([a, b, c, d, e, f, g, h ,i, j])
    Alpha=0
    Beta=0
    Sigma=0
    for n in L:
      Alpha=Alpha+(n-Avg)**2
    Beta=Alpha/90
    Sigma=np.sqrt(Beta)
    print("Standardna devijacija iznosi:", Sigma)
      