import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the system of equations
def system(y, x):
    dydx = [y[1]*y[0]**2, y[1]/x - y[0]*y[1]**2]
    return dydx

# Initial conditions
y0 = [1, 1] # Example initial values for y and z
x = np.linspace(1, 5, 100)  # Range of x values

# Solve the system
sol = odeint(system, y0, x)

# Plot the trajectories
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, sol[:, 0], sol[:, 1])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

plt.savefig('task_1.png')