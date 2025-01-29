import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Пределы изменения переменной величины
# В данной задаче переменной величиной является время
t = np.arange(0, 10**6, 100)

# Запись диф. уравнения в виде функции
def radio_function(m, t):
    dmdt =  k * m
    return dmdt

# Определение начальных условий
m_0 = 10
k = 1.61 * 10**(-6) # постоянная распада для Висмута 210

'''
k_Ur_238 = 4.84*10**(-18) # Уран 238
k_Tl_210 = 8.76*10**(-3) # Талий 210
'''

# Решение дифферинциального уравнения функцией odeint
m_t = odeint(radio_function, m_0, t)


# Построение решения в виде графика
plt.plot(t, m_t[:,0], label='Распад Висмута 210')
plt.xlabel('Период увеличения, секунды')
plt.ylabel('Функция увеличения')
plt.title('Увеличение бактерий')
plt.legend()

plt.savefig('task_1.png')

