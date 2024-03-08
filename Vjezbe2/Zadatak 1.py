import matplotlib.pyplot as plt
import numpy as np
def jednoliko_gibanje(F, m):
    #Početni uvjeti
    a=F/m
    v=0
    x=0
    pomak=[]
    brzina=[]
    akceleracija=[]

    #Štoperica
    vrijeme=np.linspace(0, 10, 100)
    dt=10/100
    for i in range (1, 101):
        v=v+a*dt
        brzina.append(v)
        x=x+v*dt
        pomak.append(x)
        akceleracija.append(a)

    #x-t graf
    plt.subplot(3, 1, 1)
    plt.xlabel("t(s)")
    plt.ylabel("x(m)")
    plt.plot(vrijeme, pomak)
    #v-t graf
    plt.subplot(3,1,2)
    plt.xlabel("t(s)")
    plt.ylabel("v(m/s)")
    plt.plot(vrijeme, brzina)
    #a-t graf
    plt.subplot(3,1,3)
    plt.xlabel("t(s)")
    plt.ylabel("$a(m/s^2)$")
    plt.plot(vrijeme, akceleracija)
    plt.show()
jednoliko_gibanje(10, 5)