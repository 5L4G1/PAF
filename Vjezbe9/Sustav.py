import numpy as np
import matplotlib.pyplot as plt
G=6.67408*(10**-11)
def vector_value(e):
    A=e[0]**2
    B=e[1]**2
    V=np.sqrt(A+B)
    return V
class Sustav: 
    def __init__(self, m1, m2, r1, r2, v1, v2):
        self.m1=m1
        self.m2=m2
        self.r1=np.array((r1, 0))
        self.r2=np.array((r2, 0))
        self.v1=np.array((0, v1))
        self.v2=v2
        self.p1x=[r1]
        self.p1y=[0]
        self.p2x=[r2]
        self.p2y=[0]
    def __move(self, dt):
        a1=-G*(self.m2/(vector_value(self.r1-self.r2))**3)*(self.r1-self.r2)
        self.v1=self.v1+a1*dt
        self.r1=self.r1+self.v1*dt
        self.p1x.append(self.r1[0])
        self.p1y.append(self.r1[1])
        a2=-G*(self.m1/(vector_value(self.r2-self.r1))**3)*(self.r2-self.r1)
        self.v2=self.v2+a2*dt
        self.r2=self.r2+self.v2*dt
        self.p2x.append(self.r2[0])
        self.p2y.append(self.r2[1])
    def plot_orbit(self, t):
        for i in range(0, round(t)):
            self.__move(3600*24)
        plt.plot(self.p1x, self.p1y, color="blue")
        plt.scatter(self.p2x, self.p2y, color="yellow")
        plt.xlim(-1.7*(10**11), 1.7*(10**11))
        plt.ylim(-1.7*(10**11), 1.7*(10**11))
        plt.show()