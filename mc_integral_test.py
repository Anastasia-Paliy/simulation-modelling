from monte_carlo import monte_carlo_integral
from prng import LinearCongruentialPRNG
from numpy import mean, sin, pi
import matplotlib.pyplot as plt


def f(x):
    return sin(pi*x)


# for f(x) = sin(pi*x)
ans = 2 / pi
iterations = [10**i for i in range(1, 6)]
maes = [mean(
    [abs(monte_carlo_integral(f, 0, 1, n, LinearCongruentialPRNG()) - ans)
     for _ in range(10)])
    for n in iterations]

plt.plot(iterations, maes)
plt.xscale('log')
plt.title('Зависимость MAE от числа итераций в методе Монте-Карло')
plt.xlabel('количество итераций')
plt.ylabel('MAE')
plt.show()

