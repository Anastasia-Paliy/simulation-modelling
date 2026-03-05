from monte_carlo import head_probability
from prng import LinearCongruentialPRNG
from numpy import mean
import matplotlib.pyplot as plt


iterations = [10**i for i in range(1, 6)]
maes = [mean([abs(head_probability(n, LinearCongruentialPRNG()) - 0.5)
              for _ in range(10)])
        for n in iterations]

plt.plot(iterations, maes)
plt.xscale('log')
plt.title('Зависимость MAE от числа итераций в методе статистических испытаний')
plt.xlabel('количество итераций')
plt.ylabel('MAE')
plt.show()
