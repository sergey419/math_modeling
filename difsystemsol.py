import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Определяем переменную величину
t = np.arange(0, 10, 0.01)

# Опредеояем функцию для системы диф.уравнений
def diff_func(z, t): # z - изменяемая величина для системы
    theta, omega = z # Указание изменяемых функций, через z

    # Первое уравнение системы
    dtheta_dt = omega

    # Второе уравнение системы
    domega_dt = - k * omega - c * np.sin(theta)

    return dtheta_dt, domega_dt

# Определяем начальное значение и параметры
# Входящие в сиситему
theta0 = np.pi - 0.1
omega0 = 0

# Начальное значение изменяемой величины системы
z0 = theta0, omega0

k = 0.25
c = 0.25

sol = odeint()




