import numpy as np
import matplotlib.pyplot as plt

# Параметры
days = np.arange(1, 366)  # дни в году
declination = 23.44 * np.sin(2 * np.pi * (days - 81) / 365)  # угловое отклонение Солнца

# Время в часах (от 0 до 24)
time = np.linspace(0, 24, 100)

# Вычисляем положение Солнца (азимут и высота)
azimuth = np.zeros((len(days), len(time)))
altitude = np.zeros((len(days), len(time)))

for i, day in enumerate(days):
    # Угол солнца в зависимости от времени и дня
    angle = (time - 12) * 15  # 15 градусов в час
    altitude[i] = np.maximum(0, np.sin(np.radians(declination[i])) * np.sin(np.radians(30)) + 
                                      np.cos(np.radians(declination[i])) * np.cos(np.radians(30)) * 
                                      np.cos(np.radians(angle)))
    azimuth[i] = angle

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(azimuth.flatten(), altitude.flatten(), 'b.', markersize=1)
plt.title('Аналемма Солнца')
plt.xlabel('Азимут (градусы)')
plt.ylabel('Высота (градусы)')
plt.xlim(-180, 180)
plt.ylim(0, 1)
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')

# Сохранение графика
plt.savefig('analemma.png', dpi=300)

# Показ графика
plt.show()