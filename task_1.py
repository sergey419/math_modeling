import numpy as np
import matplotlib.pyplot as plt

# Данные
m = 0.5  # кг
v0 = 20  # м/с
alpha = 60  # градусы
g = 9.8  # м/с²
mu = 0.1  # Н/(м/с)
kappa = 0.2  # Н/(кг·м²/с²)

# Начальные условия
vx0 = v0 * np.cos(np.radians(alpha))
vy0 = v0 * np.sin(np.radians(alpha))

# Время
t = np.linspace(0, 10, 1000)

# Модель с силой сопротивления, пропорциональной скорости
vx1 = vx0 * np.exp(-mu * t)
vy1 = vy0 * np.exp(-mu * t) - g * t

# Модель с силой сопротивления, пропорциональной квадрату скорости
vx2 = vx0 / (1 + kappa * vx0 * t)
vy2 = vy0 / (1 + kappa * vy0 * t) - g * t

# Построение графика
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.plot(vx1, vy1, label='Модель 1')
plt.plot(vx2, vy2, label='Модель 2')
plt.xlabel('x, м')
plt.ylabel('y, м')
plt.title('Траектория мяча')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, vx1, label='Модель 1')
plt.plot(t, vx2, label='Модель 2')
plt.xlabel('t, с')
plt.ylabel('vx, м/с')
plt.title('Скорость мяча по горизонтали')
plt.legend()

plt.tight_layout()
plt.show()

# Сохранение графика
plt.savefig('traektoria_mjacha.png')