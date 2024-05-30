import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def vector_value(e):
    A=e[0]**2
    B=e[1]**2
    V=np.sqrt(A+B)
    return V
class Objekt:
    def __init__(self, m, v, r, Sustav_instance):
        self.m=m
        self.v=np.array((0, v))
        self.r=np.array((r, 0))
        self.px=[r]
        self.py=[0]
        self.Sustav_instance=Sustav_instance
        self.Sustav_instance.objectlist.append(self)
    def move(self, dt):
        G=6.67408*(10**-11)
        M=0
        vec_cm_i=np.array((0, 0))
        vec_cm_s=np.array((0, 0))
        for element in self.Sustav_instance.objectlist:
            if element != self:
                M=M+element.m
                vec_cm_i=element.m * element.r
                vec_cm_s=vec_cm_s+vec_cm_i
        vec_cm=vec_cm_s/M
        a1 = (-(G * M) / (vector_value(vec_cm - self.r))**3) * (self.r-vec_cm)
        self.v = self.v + a1 * dt
        self.r = self.r + self.v * dt
        self.px.append(self.r[0])
        self.py.append(self.r[1])
                
class Sustav:
    def __init__(self):
        self.objectlist=[]
    def add(self, m, v, r):
        new_object=Objekt(m, v, r, self)
        return new_object
    def pokreni(self):
        for i in range(1, 1001):
            for element in self.objectlist:    
                element.move(24*3600)

#Dodajemo Sunce, planete i komet u sustav
SMVZK=Sustav()
Sunce=SMVZK.add(1.989e30, 0, 0)
Merkur=SMVZK.add(3.3e23, 47400, 57.9e9)
Venera=SMVZK.add(4.87e24, 35000, 108.2e9)
Zemlja=SMVZK.add(5.97e24, 29800, 149.6e9)
Mars=SMVZK.add(6.4e23, 24100, 228e9)
Komet=SMVZK.add(1e14, 20000, 6.2e11)
Novi_komet=SMVZK.add(6e14, 25000, 1.8e11)

#Pokrećemo simulaciju sustava za 1000 dana
SMVZK.pokreni()

#Animiramo gibanje dobivenih pomaka
fig, ax=plt.subplots()
ax.set(xlim=([-1e12, 1e12]), ylim=([-1e12, 1e12]))
ln1=ax.plot(Merkur.px[0], Merkur.py[0], color="grey")[0]
ln2=ax.plot(Venera.px[0], Venera.py[0], color="orange")[0]
ln3=ax.plot(Zemlja.px[0], Zemlja.py[0], color="blue")[0]
ln4=ax.plot(Mars.px[0], Mars.py[0], color="red")[0]
ln5=ax.plot(Komet.px[0], Komet.py[0], color="cyan")[0]
ln6=ax.plot(Novi_komet.px[0], Novi_komet.py[0], color="purple")[0]
def update(frame):
    x1=Merkur.px[:frame]
    y1=Merkur.py[:frame]
    ln1.set_xdata(x1[:frame])
    ln1.set_ydata(y1[:frame])

    x2=Venera.px[:frame]
    y2=Venera.py[:frame]
    ln2.set_xdata(x2[:frame])
    ln2.set_ydata(y2[:frame])

    x3=Zemlja.px[:frame]
    y3=Zemlja.py[:frame]
    ln3.set_xdata(x3[:frame])
    ln3.set_ydata(y3[:frame])

    x4=Mars.px[:frame]
    y4=Mars.py[:frame]
    ln4.set_xdata(x4[:frame])
    ln4.set_ydata(y4[:frame])

    x5=Komet.px[:frame]
    y5=Komet.py[:frame]
    ln5.set_xdata(x5[:frame])
    ln5.set_ydata(y5[:frame])

    x6=Novi_komet.px[:frame]
    y6=Novi_komet.py[:frame]
    ln6.set_xdata(x6[:frame])
    ln6.set_ydata(y6[:frame])

    return (ln1, ln2, ln3, ln4, ln5, ln6)

ani=FuncAnimation(fig=fig, func=update, frames=3000, interval=10)

#Sunce postavljamo u ishodište sustava kao mirujuće jednostavnosti radi
plt.scatter([0], [0], color="yellow", s=20)
plt.show()