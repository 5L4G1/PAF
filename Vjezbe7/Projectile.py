import numpy as np
import matplotlib.pyplot as plt
def sgn(number):
        if number<0:
            return int(-1)
        elif number==0:
            return int(0)
        else:
            return int(1)
class Projectile:
    def __init__(self, x, y, v0, theta, air_resist):
        self.x=x
        self.y=y
        self.theta=np.deg2rad(theta)
        self.vx=v0*np.cos(self.theta)
        self.vy=v0*np.sin(self.theta)
        self.horizontalno=[self.x]
        self.visina=[self.y]
        self.t=[0]
        self.friction=air_resist
    def __move(self, dt):
        ax=-self.friction
        ay=-9.81+sgn(self.vy)*self.friction
        self.vx=self.vx+ax*dt
        self.x=self.x+self.vx*dt
        self.horizontalno.append(self.x)
        self.vy=self.vy+ay*dt
        self.y=self.y+self.vy*dt
        self.visina.append(self.y)
        self.t.append(self.t[-1]+dt)
    def plot_trajectory_Euler(self, dt):
        while self.y>=0:
            self.__move(dt)
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.plot(self.horizontalno, self.visina)
        plt.show()
    def __Runge_Kutta(self, dt):
        ax=-self.friction
        ay=-9.81+sgn(self.vy)*self.friction
        k1vx=ax*dt*(self.vx)**2
        k1x=self.vx*dt
        k2vx=ax*dt*(self.vx+k1vx/2)**2
        k2x=(self.vx+k1vx/2)*dt
        k3vx=ax*dt*(self.vx+k2vx/2)**2
        k3x=(self.vx+k2vx/2)*dt
        k4vx=ax*dt*(self.vx+k3vx/2)**2
        k4x=(self.vx+k3vx/2)*dt
        self.vx=self.vx+(1/6)*(k1vx+2*k2vx+2*k3vx+k4vx)
        self.x=self.x+(1/6)*(k1x+2*k2x+2*k3x+k4x)

        k1vy=ay*dt*(self.vy)**2
        k1y=self.vy*dt
        k2vy=ay*dt*(self.vy+k1vy/2)**2
        k2y=(self.vy+k1vy/2)*dt
        k3vy=ay*dt*(self.vy+k2vy/2)**2
        k3y=(self.vy+k2vy/2)*dt
        k4vy=ay*dt*(self.vy+k3vy/2)**2
        k4y=(self.vy+k3vy/2)*dt
        self.vy=self.vy+(1/6)*(k1vy+2*k2vy+2*k3vy+k4vy)
        self.y=self.y+(1/6)*(k1y+2*k2y+2*k3y+k4y)
    def plot_trajectory_RungeKutta(self, dt):
        while self.y>=0:
            self.__Runge_Kutta(dt)
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.plot(self.horizontalno, self.visina)
        plt.show()
    def __reset(self):
        self.x=0
        self.y=0
        self.t=[0]
        self.horizontalno=[self.x]
        self.visina=[self.y]
    def usporedba(self, dt):
        while self.y>=0:
            self.__move(dt)
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.plot(self.horizontalno, self.visina, label="Euler", color="red", linewidth=3)
        while self.y>=0:
            self.__Runge_Kutta(dt)
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.plot(self.horizontalno, self.visina, label="Runge-Kutta", color="green", linewidth=2)
        plt.legend(loc="upper right")
        plt.show()