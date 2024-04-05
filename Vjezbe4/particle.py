import numpy as np
import matplotlib.pyplot as plt
class particle:
    def __init__(self, x, y, v0, theta):
        self.x=x
        self.y=y
        self.v0=v0
        self.theta=np.deg2rad(theta)
        self.vx=self.v0*np.cos(self.theta)
        self.vy=self.v0*np.sin(self.theta)
        self.xput=[self.x]
        self.yput=[self.y]
        self.t=[0]
    def reset(self):
        self.x=0
        self.y=0
        self.v0=0
        self.theta=0
        self.vx=0
        self.vy=0
        self.xput=[]
        self.yput=[]
        self.t=[0]
    def __move(self, dt):
        a=-9.81
        self.vy=self.vy+a*dt
        self.x=self.x+self.vx*dt
        self.xput.append(self.x)
        self.y=self.y+self.vy*dt
        self.yput.append(self.y)
        self.t.append(self.t[-1]+dt)
    def range(self, dt):
        while self.y>=0:
            self.__move(dt)
        return self.x
    def range_analytic(self):
        T=(2*self.vy)/9.8
        self.x=self.vx*T
        return abs(self.x)
    def plot_trajectory(self, dt):
        while self.y>=0:
            self.__move(dt)
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.plot(self.xput, self.yput)
        plt.show()