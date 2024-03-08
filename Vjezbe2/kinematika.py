import matplotlib.pyplot as plt
import numpy as np
def jednoliko_gibanje(F, m, t):
    #Početni uvjeti
    a=F/m
    v=0
    x=0
    pomak=[]
    brzina=[]
    akceleracija=[]

    #Štoperica
    vrijeme=np.linspace(0, t, 100)
    dt=t/100
    for i in range (1, 101):
        v=v+a*dt
        brzina.append(v)
        x=x+v*dt+(a/2)*(dt**2)
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

def kosi_hitac(vstart, theta, x0, y0, t):
        #Početni uvjeti
    theta=np.deg2rad(theta)
    x=x0
    y=y0
    vx=vstart*np.cos(theta)
    vy=vstart*np.sin(theta)
    ax=0
    ay=-9.81
    horizontalno=[]
    vertikalno=[]
    #Štoperica
    vrijeme=np.linspace(0, t, 100)
    dt=10/100
    for i in range (1, 101):
        vy=vy+ay*dt
        x=x+vx*dt
        horizontalno.append(x)
        y=y+vy*dt
        vertikalno.append(y)
    #x-y graf
    plt.subplot(3, 1, 1)
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.plot(horizontalno, vertikalno)
    #x-t graf
    plt.subplot(3, 1, 2)
    plt.xlabel("t(s)")
    plt.ylabel("x(m)")
    plt.plot(vrijeme, horizontalno)
    #y-t graf
    plt.subplot(3, 1, 3)
    plt.xlabel("t(s)")
    plt.ylabel("y(m)")
    plt.plot(vrijeme, vertikalno)
    plt.show()

