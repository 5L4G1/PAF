import numpy as np
import matplotlib.pyplot as plt
class Cestica_u_polju:
    def __init__(self, m, q):
        self.m=m
        self.q=q
    def Lorentz_force(self):
        p=np.array((0, 0, 0))
        v=np.array((0.1, 0.1, 0.1))
        B=np.array((0, 0, 1))
        E=np.array((0, 0, 0))
        a=(self.q/self.m)*(E+np.cross(v, B))
        dt=0.01
        X=[]
        Y=[]
        Z=[]
        for i in range(1, 10000):
            v=v+a*dt
            p=p+v*dt
            a=(self.q/self.m)*(E+np.cross(v, B))
            X.append(p[0])
            Y.append(p[1])
            Z.append(p[2])
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(X, Y, Z)
        plt.show()

e=Cestica_u_polju(1, -1)
p=Cestica_u_polju(1, 1)
e.Lorentz_force()
p.Lorentz_force()

   
       