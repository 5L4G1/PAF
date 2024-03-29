import arithm as ar
import numpy as np
ar.aritmeticka_sredina(2, 2, 2, 2, 2, 0, 0, 0, 0, 0)
ar.standardna_devijacija(2, 2, 2, 2, 2, 0, 0, 0, 0, 0)

Arg=np.array([2, 2, 2, 2, 2, 0, 0, 0, 0, 0])
M=np.mean(Arg)
SD=np.std(Arg)
print(M)
print(SD)
print(SD/np.sqrt(9))

