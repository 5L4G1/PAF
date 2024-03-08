import matplotlib.pyplot as plt
import numpy as np
def kosi_hitac(vstart, theta):
    #Početni uvjeti
    theta=np.deg2rad(theta)
    x=0
    y=0
    vx=vstart*np.cos(theta)
    vy=vstart*np.sin(theta)
    ax=0
    ay=-9.81
    horizontalno=[]
    vertikalno=[]
    #Štoperica
    vrijeme=np.linspace(0, 10, 100)
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
    print(vertikalno)
kosi_hitac(100, 60)
