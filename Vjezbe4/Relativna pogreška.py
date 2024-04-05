import numpy as np
import matplotlib.pyplot as plt
import particle as part
A=part.particle(0, 0, 10, 60)
t=np.linspace(0.001, 0.1, 1000)
Greske=[]
for dt in t:
    A.range(dt)
    error=(abs(A.range_analytic()-A.x))
    Greske.append(error)
plt.title("Relativna pogreška")
plt.xlabel("dt[s]")
plt.ylabel("relativna greška[%]")
plt.plot(t, Greske, "b")
plt.show()

