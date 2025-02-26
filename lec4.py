	
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Определяем переменную величину
frames = 500
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)
 
# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    x, v_x, y, v_y = s
    
    dxdt = v_x
    dv_xdt = - G * M * x / (x**2 + y**2)**1.5
    dydt = v_y
    dv_ydt = - G * M * y / (x**2 + y**2)**1.5
    
    return dxdt, dv_xdt, dydt, dv_ydt
 
# Определяем начальные значения и параметры
G = 6.67 * 10**(-11)
M = 1.998 * 10**(30)
 
x0 = 149 * 10**9
v_x0 = 0
y0 = 0
v_y0 = 30000
 
s0 = (x0, v_x0, y0, v_y0)
 
sol = odeint(move_func, s0, t)

fig, ax = plt.subplots()
 
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
 
 
def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])
 
 
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
 
edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
	
ani.save('animation_2.gif', writer="pillow")
