import calculus as calc
import numpy as np
import matplotlib.pyplot as plt
#Koraci
X1=np.linspace(1, 10, 10)
X2=np.linspace(1, 10, 100)
X3=np.linspace(1, 10, 1000)
X4=np.linspace(1, 10, 10000)
X5=np.linspace(1, 10, 100000)

#Derivacija sin(x) u rasponu 1-10 za 100, 1000 i 10000 ponavljanja
Y1=calc.derivacija("sin(x)", 1, 10, 10)
Y2=calc.derivacija("sin(x)", 1, 10, 100)
Y3=calc.derivacija("sin(x)", 1, 10, 1000)
Y4=calc.derivacija("sin(x)", 1, 10, 10000)
Y5=calc.derivacija("sin(x)", 1, 10, 100000)

#Integracija sin(x) u rasponu 1-10 za 5, 10, 20, 30, i 40 ponavljanja
Y6=calc.integracija_trapezna("sin(x)", 1, 10, 10)
Y7=calc.integracija_trapezna("sin(x)", 1, 10, 100)
Y8=calc.integracija_trapezna("sin(x)", 1, 10, 1000)
Y9=calc.integracija_trapezna("sin(x)", 1, 10, 10000)
Y10=calc.integracija_trapezna("sin(x)", 1, 10, 100000)
Xint=[5, 10, 20, 30, 40]
Yint=[Y6, Y7, Y8, Y9, Y10]

#Grafovi
fig, axs=plt.subplots(2)
axs[0].set_title("Derivacija")
axs[1].set_title("Integracija")
axs[1].set_xlabel("koraci")
axs[1].set_ylabel("rezultat")
axs[1].set_ylim([-2, 2])


axs[0].plot(X1, Y1, label="10 koraka")
axs[0].plot(X2, Y2, label="100 koraka")
axs[0].plot(X3, Y3, label="1000 koraka")
axs[0].plot(X4, Y4, label="10000 koraka")
axs[0].plot(X5, Y5, label="100000 koraka")
axs[0].legend()

axs[1].scatter(Xint, Yint)
plt.show()
