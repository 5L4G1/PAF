import Projectile as pr
A=pr.Projectile(0, 0, 100, 30, 0.01)
A.plot_trajectory_Euler(0.1)
A.plot_trajectory_Euler(0.01)
A.plot_trajectory_RungeKutta(0.01)
A.usporedba(0.01)