import numpy as np
import matplotlib.pyplot as plt
M=np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
phi=np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])
P=0
Mphi=[]
Xsqr=[]
for i in range (0, 6):
    P=(M[i])*(phi[i])
    Mphi.append(P)
    R=(phi[i])**2
    Xsqr.append(R)
def AVG(list):
    U=sum(list)
    D=len(list)
    Avg=U/D
    return Avg
anum=AVG(Mphi)
aden=AVG(Xsqr)
k=anum/aden
plt.xlabel("$\\varphi [rad]$")
plt.ylabel("M [Nm]")
plt.scatter(phi, M, label="data")
plt.plot(phi, k*phi, label="fit")
plt.legend(loc="upper left")
plt.title("y={}x".format(k))
plt.show()
snum=AVG(M**2)
sden=AVG(phi**2)
frac=snum/sden
alpha=(1/6)*(frac-(k**2))
sigma=np.sqrt(alpha)
print("Modul torzije iznosi {} +/- {}".format(k, sigma))
