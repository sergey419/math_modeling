import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m = 1.0  
F = 10.0 
gamma = 0.5  
a0 = F / m  
k = gamma / m  

def model(v, t):
    return a0 - k * v**2

t = np.linspace(0, 20, 100) 

v0 = 0.0  
v = odeint(model, v0, t)

plt.figure(figsize=(10, 6))
plt.plot(t, v, label='Скорость (м/с)', color='b')
plt.title('Закон изменения скорости со временем')
plt.xlabel('Время (с)')
plt.ylabel('Скорость (м/с)')
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()

plt.savefig('speed_time_graph.png', dpi=300)

plt.show()

