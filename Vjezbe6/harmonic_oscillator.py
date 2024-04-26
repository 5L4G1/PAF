import numpy as np
import matplotlib.pyplot as plt
class HarmonicOscillator:
    def __init__(self, m, k, x0, v0):
         self.m=m
         self.k=k
         self.x=x0
         self.v=v0
         self.pomak=[self.x]
         self.brzina=[self.v]
         self.akceleracija=[0]
         self.t=[0]
    def __reset(self):
        self.pomak=[self.x]
        self.brzina=[self.v]
        self.akceleracija=[0]
        self.t=[0]
    def __move(self, dt):
        self.a=-(self.k*self.x)/self.m
        self.akceleracija.append(self.a)
        self.v=self.v+self.a*dt
        self.brzina.append(self.v)
        self.x=self.x+self.v*dt
        self.pomak.append(self.x)
        self.t.append(self.t[-1]+dt)
    def plot_analiticko(self, t):
        omega=np.sqrt(self.k/self.m)
        vmax=omega*self.x
        amax=-omega*omega*self.x
        phiinitial=(np.pi)/2
        self.t=np.linspace(0, t, 10000)
        phaselist=[]
        for element in self.t:
            phaselist.append(omega*element+phiinitial)
        xlist=np.sin(phaselist)
        self.pomak=xlist*self.x
        self.brzina=vmax*np.cos(phaselist)
        self.akceleracija=amax*np.sin(phaselist)
        fig, axs=plt.subplots(3)
        axs[0].set_xlabel("t[s]")
        axs[0].set_ylabel("x[m]")
        axs[1].set_xlabel("t[s]")
        axs[1].set_ylabel("v[m/s]")
        axs[2].set_xlabel("t[s]")
        axs[2].set_ylabel("$a/[m/s^2]$")
        axs[0].plot(self.t, self.pomak)
        axs[1].plot(self.t, self.brzina)
        axs[2].plot(self.t, self.akceleracija)
        plt.show()
    def __analiticki_pomak(self, t):
        omega=np.sqrt(self.k/self.m)
        phiinitial=(np.pi)/2
        self.t=np.linspace(0, t, 10000)
        phaselist=[]
        for element in self.t:
            phaselist.append(omega*element+phiinitial)
        xlist=np.sin(phaselist)
        self.pomak=xlist*self.x
        return self.t, self.pomak
    def plot(self, t, dt):
        for i in range (1, round(t/dt)):
            self.__move(dt)
        fig, axs=plt.subplots(3)
        axs[0].set_xlabel("t[s]")
        axs[0].set_ylabel("x[m]")
        axs[1].set_xlabel("t[s]")
        axs[1].set_ylabel("v[m/s]")
        axs[2].set_xlabel("t[s]")
        axs[2].set_ylabel("$a/[m/s^2]$")
        axs[0].plot(self.t, self.pomak)
        axs[1].plot(self.t, self.brzina)
        axs[2].plot(self.t, self.akceleracija)
        plt.show()
    def usporedba_preciznosti(self, t, dt1, dt2, dt3):
        plt.xlabel("t[s]")
        plt.ylabel("x[m]")
        for i in range (1, round(t/dt1)):
            self.__move(dt1)
        plt.scatter(self.t, self.pomak, label="dt=0.1 s", color="green", s=12)
        self.__reset()
        for i in range (1, round(t/dt2)):
            self.__move(dt2)
        plt.scatter(self.t, self.pomak, label="dt=0.01 s", color="blue", s=5)
        self.__reset()
        for i in range (1, round(t/dt3)):
            self.__move(dt3)
        plt.scatter(self.t, self.pomak, label="dt=0.001 s", color="pink", s=1)
        self.__reset()
        self.__analiticki_pomak(t)
        plt.plot(self.t, self.pomak, label="analticko rjesenje", color="red", linewidth=4)
        plt.legend(loc="upper right")
        plt.show()
    def period(self, dt):
        self.__reset()
        C=-self.x
        while self.x>C:
            self.__move(dt)
        T=2*self.t[-1]
        return T