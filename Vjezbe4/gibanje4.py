import particle as part
A=part.particle(0, 0, 100, 45)
A.range(0.1)
print(A.x)
print(A.range_analytic())
#Rješenje odstupa od analitičkog za ~0,009%
A.plot_trajectory(0.1)